Title: My desktop backup solution
Date: 2010-11-29 17:24
Author: Thierry Carrez
Tags: Productivity
Slug: my-desktop-backup-solution

I was inspired by a good [blogpost by Martin
Pitt](http://www.piware.de/2009/11/my-desktop-backup-solution/) to setup
my own desktop backup solution. I liked the idea of not requiring the
computer to be on all the time, and having the backup pushed from the
client rather than pulled from the server. However, my needs were
slightly different from his, so I adapted it.

His solution uses rsnapshot locally, then pushes the resulting
directories to a remote server. I didn't want to use local disk space
(SSD ain't cheap), but I had a local server with 2Tb available. So in my
solution, the client rsyncs to the server, then the server triggers
rsnapshot locally if the rsync was successful. This is done over SSH and
the server has no right whatsoever on the client.

### Prerequisites

In the examples the client to back up will be called *mycli* and the
server on which the backup will live is named *mysrv*. As a
prerequisite, mycli will need rsync and openssh-client installed. mysrv
will need rsnapshot and openssh-server installed. OpenSSH needs to have
public-key authentication enabled.

### SSH setup

<span style="text-decoration:underline;">On the client side</span>,
generate a specific passwordless SSH key for the backup connection:

    mkdir ~/.backup
    ssh-keygen -f ~/.backup/id_backup

<span style="text-decoration:underline;">On the server side</span>,
we'll assume you want to put backups into /srv/backup. First of all,
create an rbackup user that will be used to run the backup serverside:

    sudo mkdir /srv/backup
    sudo adduser --home /srv/backup --no-create-home --disabled-password rbackup

Next, add your backup public key (the contents of mycli:\~/
.backup/id\_backup.pub) to mysrv:/srv/backup/.ssh/authorized\_keys. The
trick is to prefix it (same line, one space separator) with the only
command you want the rbackup user to perform via that SSH connection:

    command="rsync --config /srv/backup/rsyncd-mycli.conf --server
    --daemon ." ssh-rsa AAAAB3NzaLwm0ckRdzotb3...5Mbiw== ttx@mycli

Finally, you need to let rbackup read those .ssh files:

    sudo chgrp -R rbackup /srv/backup/.ssh
    sudo chmod -R g+r /srv/backup/.ssh

### rsync setup (server-side)

Now we need to set up the rsync configuration that will be used on those
connections:

    # /srv/backup/rsyncd-mycli.conf
    max connections = 1
    lock file = /srv/backup/mycli/rsync.lock
    log file = /srv/backup/mycli/rsync.log
    use chroot = false
    max verbosity = 3
    read only = false
    write only = true

    [mycli]
     path = /srv/backup/mycli/incoming
     post-xfer exec = /srv/backup/kick-rsnapshot /srv/backup/mycli/rsnapshot.conf

The *post-xfer* exec command is executed on successful transfers to
/srv/backup/client/incoming. In our case, we want rsync to trigger the
/srv/backup/kick-rsnapshot script:

    #!/bin/bash
    if [ "$RSYNC_EXIT_STATUS" == "0" ]; then
       rsnapshot -c $1 daily
    fi

Don't forget to make that one executable :)

### rsnapshot setup (server-side)

rsnapshot itself is configured in the /srv/backup/mycli/rsnapshot.conf
file. This is where you specify how many pseudo-weekly copies you want
to keep (read rsnapshot documentation to understand the *interval*
concept):

    # /srv/backup/mycli/rsnapshot.conf
    config_version    1.2
    snapshot_root    /srv/backup/mycli
    cmd_rm      /bin/rm
    cmd_rsync   /usr/bin/rsync
    cmd_logger  /usr/bin/logger
    interval    daily    6
    interval    weekly    6   
    verbose     2
    loglevel    3
    lockfile    /srv/backup/mycli/rsnapshot.pid
    rsync_long_args    --delete --numeric-ids --delete-excluded
    link_dest   1
    backup      /srv/backup/mycli/incoming/    ./

Now you just have to create the backup directory hierarchy with
appropriate permissions:

    mkdir -p /srv/backup/mycli/incoming
    chown -R rbackup:rbackup /srv/backup/mycli

### The backup (client-side)

The client will rsync periodically to the server, using the following
script:

    #!/bin/bash
    set -e
    TOUCHFILE=$HOME/.backup/last_backup

    # Check if last backup was more than a day before
    now=`date +%s`
    if [ -e $TOUCHFILE ]; then
       age=$(($now - `stat -c %Y $TOUCHFILE`))
    else
       unset age
    fi
    [ -n "$age" ] && [ $age -lt 86300 ] && exit 0

    nice -n 10 rsync -e "ssh -i $HOME/.backup/id_backup" -avzF   
        --delete --safe-links $HOME rbackup@mysrv::mycli
    touch $TOUCHFILE

That script ensures that at most once per day, you will sync to the
server. You can run it (as your user) as often as you'd like (I suggest
hourly via cron). On successful syncs, the server will trigger rsnapshot
to do its magic backup rotation ! Using the same model, you can easily
set up multiple directories or multiple clients.

Like with Martin's solution, you should set up various *.rsync-filter*
files to exclude the directories and files you don't want copied to the
backup server.

The drawback of this approach is that the server keeps an extra copy of
your backup (in the incoming directory). But in my case, since the
server has plenty of space, I can afford it. It also does not work when
you are away from your backup server.

I hope you find that setup useful, it served me well so far.
