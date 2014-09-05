Title: GTD with RTM
Date: 2010-01-25 19:51
Author: Thierry Carrez
Tags: Productivity
Slug: gtd-with-rtm

Following my colleague and friend
[Mathias](http://ubuntumathiaz.wordpress.com/)'s advice, I've been using
GTD (Getting Things Done) to keep myself organized for some time now. A
recurrent question is "what software are you using ?". I tried several
programs, but nothing could quite fit my system and decentralized use.

Lots of folks are now pushing GTG (Getting Things Gnome). While I see a
lot of potential in GTG, it's still a task manager (everything is a
task) rather than a flexible list manager. GTD uses lists of things that
are specifically *not* tasks (the inbox, the maybe lists, the project
list...).

Mathias recommended using [Remember the
Milk](http://www.rememberthemilk.com) (RTM), a highly flexible web
service with lots of APIs (and more). I originally set up something
along the lines of this [reference
post](http://blog.rememberthemilk.com/2008/05/guest-post-advanced-gtd-with-remember-the-milk/),
but it failed for me in several areas:

-   Parsing Inbox was painful (no shortcut key to move tasks to other
    lists)
-   No "tickler file" approach allowing you to forget about an item for
    some time
-   My projects are using work items in Ubuntu blueprints, keeping them
    in sync was also painful

So I changed it, here is my new setup:

-   New items are created in the "Inbox", without tags.
-   A @ToProcess smartlist, using "list:Inbox and (isTagged:false or
    (tag:hide and dueBefore:tomorrow))", contains the stuff I need to
    parse during next Process phase
-   Process phase: for each item in @ToProcess:
    -   If it's actionable and takes less than 2 minutes, do it, mark it
        as completed (\<c\> shortcut)
    -   If it's actionable but needs more time, use \<s\> shortcut to
        tag it with appropriate context ("me" if only me is required)
    -   If you don't want to process it now, but want to file it in your
        tickler file for it to reappear in two weeks: use \<d\> "two
        weeks" to set a Due Date, then use \<s\> and tag it "hide"
    -   Delegate tasks by using \<s\> and tag it "wait" + some context
        of who you're delegating to
    -   As soon as it's tagged, the item disappears from the @ToProcess
        list, which is good !
    -   If it needs to go to one of the Maybe lists, move it there
-   My @NextActions smartlist uses "isTagged:true and not (tag:wait or
    tag:hide)"
-   My @WaitingFor smartlist just uses "tag:wait"

I don't maintain anymore "one list per project", which was painful to
me. I just use a "Projects" list that is a regular GTD Projects list I
use during weekly reviews. I use multiple "Maybe" lists (one for ideas
needing incubating, one for technologies to look at, one for blog
article ideas, etc.).

A few remarks:

-   I use Google Calendar for actions occurring at a specific time
-   I use the priority shortcuts to give a sense of urgency that helps
    me quickly pick the right next action from the @NextActions list
-   I use context tags for everyone: for example, I mark "jib" all tasks
    that require jib to be completed. When I talk to that person, I use
    the RTM tag cloud to quickly bring up a "tag:jib" search to get a
    list of all subjects I need him for, but also a reminder of tasks I
    delegated to him.
-   I try to have my inbox at hand all the time, to be able to quickly
    drop there a quick idea that crosses my mind. I use RTM google
    calendar plugin, RTM netvibes module and also coded a "rtm" tool
    using their python API, for direct use when I'm hacking in a
    terminal. All create items in the default list (Inbox) and without
    tagging, so it just works.
-   I also use an ActivityReport smartlist (completedWithin:"1 week of
    today")

Hope it helps :)
