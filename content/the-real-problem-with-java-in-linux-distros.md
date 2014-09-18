Title: The real problem with Java in Linux distros
Date: 2010-09-24 10:13
Author: Thierry Carrez
Tags: Open source
Slug: the-real-problem-with-java-in-linux-distros

Java is not a first-class citizen in Linux distributions. We generally
have decent coverage for Java libraries, but lots of Java software is
not packaged at all, or packaged in alternate repositories. Some
consider that it's because Linux distribution developers dislike Java
and prefer other languages, like C or Python. The reality is slightly
different.

## Java is fine

There is nothing sufficiently wrong with Java that would cause it to
uniformly be a second-class citizen on every distro. It is a widely-used
language, especially in the corporate world. It has a vibrant open
source community. On servers, it generated very interesting stable
(Tomcat) and cutting-edge (Hadoop, Cassandra...) projects. So what
grudge do the distributions hold against Java ?

## Distributing distributions

The problem is that Java open source upstream projects do not really
release code. Their main artifact is a complete binary distribution, a
bundle including their compiled code and a set of third-party libraries
they rely on. If you take the Java project point of view, it makes
sense: you pick versions of libraries that work for you, test that
precise combination, and release the same bundle for all platforms. It
makes it easy to use everywhere, especially on operating systems that
don't enjoy the greatness of an unified package management system.

That doesn't play well with how Linux distributions package software. We
want to avoid code duplication (so that a security update in a library
package benefits all software that uses it), so we package libraries
separately. We keep those up to date, to benefit from bugfixes and new
features. We consider libraries to be part of the platform provided by
the Linux distribution.

The Java upstream project consider libraries to be part of the software
bundle they release. So they keep the libraries at a precise version
they tested, and only update them when they really need to. Essentially,
they maintain their own platform of libraries. **They do, at their
scale, the same work the Linux distributions do.** And that's where the
real problem lies.

## Solutions ?

### Force software to use your libraries

For simple Java software, stripping the upstream distribution and
forcing it to use your platform libraries can work. But that creates
friction with upstream projects (since you introduce an untested
difference). And that doesn't work with more complex software: swapping
libraries below it will just make it fail.

### Package all versions of libraries

The next obvious solution is to make separate packages for every version
of library that the software uses. The problem is that there is no real
convergence on "commonly-used" versions of libraries. There is no ABI
protection, nor general guidelines on versioning. You end up having to
package each and every minor version of a library that the software
happens to want. That doesn't scale well: it creates an explosion in the
number of packages, code duplication, security update nightmares, etc.
Furthermore, sometimes the Java project patches the libraries they ship
with to include a specific feature they need, so it doesn't even match
with a real library version anymore.

*Note: The distribution that is the closest to implementing this
approach is Gentoo, through the SLOT system that lets you have several
versions of the same package installed at the same time.*

### Bundle software with their libraries

At that point, you accept code duplication, so just shipping the precise
libraries together with the software doesn't sound that bad of an idea.
Unfortunately it's not that simple. Linux distributions must build
everything from source code. In most cases, the upstream Java project
doesn't ship the source code used in the libraries it bundles. And what
about the source code of the build dependencies of your libraries ? In
some corner cases, the library project is even abandoned, and its source
code lost...

## What can we do to fix it ?

So you could say that the biggest issue the Linux distributions have
with Java is not really about the language itself. It's about an
ecosystem that glorifies binary bundles and not source code. And there
is no easy solution around it, that's why you can often hear Java
packagers in Linux distributions explain how much they hate Java. That's
why there is only a minimal number of Java projects packaged in
distributions. Shall we abandon all hope ?

The utopia solution is to aim for a reference platform, reasonably
up-to-date libraries that are known to work well together, and encourage
all Java upstream developers to use that. That was one of JPackage's
goals, but it requires a lot more momentum to succeed. It's very
difficult, especially since Java developers often use Windows or OSX.

Another plan is to build a parallel distribution mechanism for Java
libraries inside your distro. A Java library wouldn't be shipped as a
package anymore. But I think unified package systems are the glory of
Linux distributions, so I don't really like that option.

## Other issues, for reference

There are a few other issues I didn't mention in this article, to
concentrate on the "distributing distributions" aspect. The tarball
distributions don't play nice with the FHS, forcing you to play with
symlinks to try to keep both worlds happy (and generally making both
unhappy). Maven encourages projects to pick precise versions of
libraries and stick to them, often resulting in multiple different
versions of the same library being used in a given project. Java code
tends to build-depend on hundreds of obscure libraries, transforming
seemingly-simple packaging work into a man-year exponential effort.
Finally, the same dependency inflation issue makes it a non-trivial
engagement to contractually support all the dependencies (and build
dependencies) of a given software (like Canonical does for software in
the Ubuntu main repository).
