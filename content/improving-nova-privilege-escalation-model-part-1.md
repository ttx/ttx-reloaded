Title: Improving Nova privilege escalation model, part 1
Date: 2011-11-23 16:31
Author: Thierry Carrez
Tags: OpenStack
Slug: improving-nova-privilege-escalation-model-part-1

In this series, I'll discuss how to strengthen the privilege escalation
model for OpenStack Compute (Nova). Due to the way networking,
virtualization and volume management work, some Nova nodes need to be
able to run some commands as root. To reduce the effects of a potential
compromise (attacker being able to run arbitrary code as the Nova user),
we want to limit the commands that Nova can run as root on a given node
to the strict necessary. Today we'll explain how the current model
works, its limitations, and the groundwork already implemented during
the Diablo cycle to improve that.

#### Current model: sudo and sudoers

Currently, in a typical Nova deployment, the nodes run under an account
with limited rights (usually called "nova"). When Nova needs to run a
command as root, it prepends "sudo" to the command. The nova packages of
your distribution of choice are supposed to ship a **sudoers** file that
contains all the commands that nova is allowed to run as root without
providing a password. This is a privilege escalation security model
which is pretty well-known and easy to audit.

#### Limitations of the current model

That said, in the context of Nova, this model is very limited. The
sudoers file does not allow to efficiently filter arguments, so you can
basically pass any argument to the allowed command... and some of the
commands that nova wants to use are rather open-ended. As an example,
the current nova\_sudoers file contains commands like *chown*, *kill*,
*dd* or *tee*, which are more than enough to compromise a target system
completely.

There are a couple other limitations.  The sudoers file belongs to the
distributions packaging, so it's difficult to keep it in sync with the
rest of Nova code when someone wants to add a privileged command. Last
but not least, the same nova\_sudoers file is used for any type of Nova
node. A Nova API server, which does not *need* to run any command as
root, is still allowed to run all the commands that a compute node
requires, for example. Those other limitations could be fixed while
still using sudo and sudoers files, but the first limitation would
remain. Can we do better ?

#### Substitute a wrapper to sudo

To be able to propose alternative privilege escalation security models,
we first needed to be able to change all the "sudo" calls in the code
and make them potentially use something else. That's [what I worked
on](https://blueprints.launchpad.net/nova/+spec/refactor-privesc) late
during the Diablo timeframe: creating a *run\_as\_root* option in
nova.utils.execute that would use a configurable **root\_helper**
command (by default, "sudo"), and force all the existing calls to go
through that (rather than blindly calling "sudo" themselves).

Thanks to the default root\_helper, everything still behaves the same,
but now we have the possibility to use *something else*, if we can be
smarter than sudoers files. Like call a wrapper that will do advanced
filtering of the command that nova wants to use. In part 2 of this
series, we'll look into a proposed, alternative Python-based
root\_helper and open discussion on its security model.
