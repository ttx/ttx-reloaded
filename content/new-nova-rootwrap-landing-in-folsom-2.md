Title: New nova-rootwrap landing in folsom-2
Date: 2012-07-02 11:52
Author: Thierry Carrez
Tags: OpenStack
Slug: new-nova-rootwrap-landing-in-folsom-2

This Thursday we will publish our second milestone of the Folsom cycle
for Nova. It will include [a number of new
features](https://launchpad.net/nova/+milestone/folsom-2), including the
one I worked on: a new, more configurable and extensible nova-rootwrap
implementation. Here is what you should know about it, depending on
whether you're a Nova user, packager or developer !

#### Architecture

##### Purpose {#Purpose}

The goal of the root wrapper is to allow the *nova* unprivileged user to
run a number of actions as the *root* user, in the safest manner
possible. Historically, Nova used a specific *sudoers* file listing
every command that the *nova* user was allowed to run, and just used
**sudo** to run that command as *root*. However this was difficult to
maintain (the *sudoers* file was in packaging), and did not allow for
complex filtering of parameters (advanced filters). The rootwrap was
[designed]({filename}/improving-nova-privilege-escalation-model-part-1.md)
to solve those issues.

##### How rootwrap works {#How_rootwrap_works}

Instead of just calling **sudo make me a sandwich**, Nova calls **sudo
nova-rootwrap /etc/nova/rootwrap.conf make me a sandwich**. A generic
*sudoers* entry lets the *nova* user run **nova-rootwrap** as *root*.
nova-rootwrap looks for filter definition directories in its
configuration file, and loads **command filters** from them. Then it
checks if the command requested by Nova matches one of those filters, in
which case it executes the command (as *root*). If no filter matches, it
denies the request.

##### Security model {#Security_model}

The escalation path is fully controlled by the *root* user. A *sudoers*
entry (owned by *root*) allows *nova* to run (as *root*) a specific
rootwrap executable, and only with a specific configuration file (which
should be owned by *root*). nova-rootwrap imports the Python modules it
needs from a cleaned (and system-default) PYTHONPATH. The configuration
file (also *root*-owned) points to *root*-owned filter definition
directories, which contain *root*-owned filters definition files. This
chain ensures that the *nova* user itself is not in control of the
configuration or modules used by the nova-rootwrap executable.

#### Rootwrap for users: Nova configuration {#Rootwrap_for_users}

Nova must be configured to use nova-rootwrap as its *root\_helper*. You
need to set the following in **nova.conf**:

    root_helper=sudo nova-rootwrap /etc/nova/rootwrap.conf

The configuration file (and executable) used here must match the one
defined in the *sudoers* entry (see below), otherwise the commands will
be rejected !

#### Rootwrap for packagers {#Rootwrap_for_packagers}

##### Sudoers entry {#Sudoers_entry}

Packagers need to make sure that Nova nodes contain a *sudoers* entry
that lets the *nova* user run nova-rootwrap as *root*, pointing to the
*root*-owned rootwrap.conf configuration file and allowing any parameter
after that:

    nova ALL = (root) NOPASSWD: /usr/bin/nova-rootwrap /etc/nova/rootwrap.conf *

##### Filters path {#Filters_path}

Nova looks for a *filters\_path* in **rootwrap.conf**, which contains
the directories it should load filter definition files from. It is
recommended that Nova-provided filters files are loaded from
**/usr/share/nova/rootwrap** and extra user filters files are loaded
from **/etc/nova/rootwrap.d**.

    [DEFAULT]
    filters_path=/etc/nova/rootwrap.d,/usr/share/nova/rootwrap

Directories defined on this line should all exist, be owned and
writeable only by the *root* user.

##### Filter definitions {#Filter_definitions}

Finally, packaging needs to install, for each node, the filters
definition file that corresponds to it. You should **not** install any
other filters file on that node, otherwise you would allow extra
unneeded commands to be run by *nova* as *root*.

The filter file corresponding to the node must be installed in one of
the *filters\_path* directories (preferably /usr/share/nova/rootwrap).
For example, on compute nodes, you should only have
/usr/share/nova/rootwrap/compute.filters. The file should be owned and
writeable only by the *root* user.

All filter definition files can be found in Nova source code under
etc/nova/rootwrap.d.

#### Rootwrap for plug-in writers: adding new run-as-root commands {#Rootwrap_for_plug-in_writers}

Plug-in writers may need to have the *nova* user run additional commands
as *root*. They should use nova.utils.execute(run\_as\_root=True) to
achieve that. They should create their own filter definition file and
install it (owned and writeable only by the *root* user !) into one of
the *filters\_path* directories (preferably /etc/nova/rootwrap.d). For
example the foobar plugin could define its extra filters in a
/etc/nova/rootwrap.d/foobar.filters file.

The format of the filter file is defined
[here](http://wiki.openstack.org/Nova/Rootwrap#Reference).

#### Rootwrap for core developers {#Rootwrap_for_core_developers}

##### Adding new run-as-root commands {#Adding_new_run-as-root_commands-1}

Core developers may need to have the *nova* user run additional commands
as *root*. They should use nova.utils.execute(run\_as\_root=True) to
achieve that, and add a filter for the command they need in the
corresponding etc/nova/rootwrap.d/ .filters file in Nova's source code.
For example, to add a command that needs to be tun by network nodes,
they should modify the etc/nova/rootwrap.d/network.filters file.

The format of the filter file is defined
[here](http://wiki.openstack.org/Nova/Rootwrap#Reference).

##### Adding your own filter types {#Adding_your_own_filter_types}

The default filter type, CommandFilter, is pretty basic. It only checks
that the command name matches, it does not perform advanced checks on
the command arguments. A number of other more command-specific filter
types are available, see
[here](http://wiki.openstack.org/Nova/Rootwrap#Reference).

That said, you can easily define new filter types to further control
what exact command you actually allow the *nova* user to run as *root*.
See nova/rootwrap/filters.py for details.

This documentation, together with a reference section detailing the file
formats, is available [on the
wiki](http://wiki.openstack.org/Nova/Rootwrap).
