Title: Elite committers vs. Gated trunk
Date: 2011-08-12 15:26
Author: Thierry Carrez
Tags: Open source, OpenStack
Slug: gated-trunk

How to control what gets into your open source project code ? The
classic model, inherited from pre-DVCS days, is to have a set of
"committers" that are trusted with direct access while the vast majority
of project "contributors" must kindly ask them to sponsor their patches.
You can find that model in a lot of projects, including most Linux
distributions. This model doesn't scale that well -- even trusted
individuals are error-prone, nobody should escape peer review. But the
main issue is the binary nature of the committer power: it divides your
community (us vs. them) and does not really encourage contribution.

### Gated trunk

The solution to this is to implement a gated trunk with a code review
system like GitHub pull requests or Launchpad branch merge proposals.
Your "committers" become "core developers" that have a casting vote on
whether the proposal should be merged. Everyone goes through the peer
review process, and the peer review process is open for everyone: your
"contributors" become "developers" that can comment too. You reduce the
risk of human error and the community is much healthier, but some issues
remain: your core developers can still (wittingly or unwittingly) evade
peer review, and the final merge process is human and error-prone.

### Automation ftw

The solution is to add more automation, and not trust humans with direct
repository access anymore. An "automated gated trunk" bot can watch for
reviews and when a set of pre-defined rules are met (human approvals,
testsuites passed, etc.), trigger the trunk merge automatically. This
removes human error from the process, and effectively turns your "core
developers" into "reviewers". This last aspect makes for a very healthy
development community: there is no elite group anymore, just a developer
subgroup with additional review duties.

### Gerrit

In OpenStack, we used Tarmac in conjunction with Launchpad/bzr code
review in our first attempt to implement this. As we considered
migration to git, the lack of support for tracking formal approvals in
GitHub code review prevented the implementation of a complex automated
gated trunk on top of GitHub, so we deployed Gerrit. I was a bit
resisting the addition of a new tool to our toolset mix, but the
incredible Monty Taylor and Jim Blair did a great integration job, and I
realize now that this gives us a lot more flexibility and room for
future evolution. For example I like that some tests can be run when the
change is proposed, rather than only after the change is approved (which
results in superfluous review roundtrips).

At the end of the day, gated trunk automation helps in having a
welcoming, non-elitist (and lazy) developer community. I wish more
projects, especially distributions, would adopt it.
