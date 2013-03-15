Summary:	A GNU tool which simplifies the build process for users
Name:		make
Version:	3.82
Release:	6
Epoch:		1
Url:		http://www.gnu.org/directory/GNU/make.html
License:	GPLv2+
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/pub/gnu/make/%name-%version.tar.bz2
Patch1:		make-3.82-noclock_gettime.patch
Patch2:		make-3.82-j8k.patch
Patch3:		make-3.82-getcwd.patch
Patch4:		make-3.82-err-reporting.patch
Patch5:		make-3.81-memory.patch

# Upstream: https://savannah.gnu.org/bugs/?30748
Patch6:		make-3.82-weird-shell.patch

Patch7:		make-3.82-newlines.patch
Patch8:		make-3.82-jobserver.patch
Patch9:		make-3.82-bugfixes.patch
Patch10:	make-3.82-sort-blank.patch
Patch11:	make-3.82-copy-on-expand.patch

# Upstream: https://savannah.gnu.org/bugs/?33873
Patch12:	make-3.82-parallel-remake.patch

# http://savannah.gnu.org/bugs/?34335
Patch13:	make-3.82-warn_undefined_function.patch

# http://lists.gnu.org/archive/html/bug-make/2011-06/msg00032.html
Patch14:	make-3.82-trace.patch

# http://lists.gnu.org/archive/html/bug-make/2011-04/msg00002.html
Patch15:	make-3.82-expensive_glob.patch

# Upstream: https://savannah.gnu.org/bugs/?30653
Patch16:	make-3.82-dont-prune-intermediate.patch

# AArch64 patch
Patch17:	make-aarch64.patch
Patch18:	make-3.82-lib64.patch
Patch19:	make-3.80-gfortran.patch

BuildRequires:	gettext-devel

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files.  Make
allows users to build and install packages without any significant
knowledge about the details of the build process.  The details about how
the program should be built are provided for make in the program's
makefile.

The GNU make tool should be installed on your system because it is
commonly used to simplify the process of installing programs.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
#%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p0
%patch13 -p2
%patch14 -p1
%patch15 -p0
%patch16 -p0
%patch17 -p1
%patch18 -p1
%patch19 -p1

%build
%configure2_5x \
	--disable-rpath
%make

%check
# all tests must pass
make check

%install
%makeinstall_std

ln -sf make %{buildroot}%{_bindir}/gmake

%find_lang %{name}

%files -f %name.lang
%doc ABOUT-NLS AUTHORS ChangeLog README README.customs SCOPTIONS NEWS
%doc glob/COPYING.LIB glob/ChangeLog
%_bindir/make
%_bindir/gmake
%_mandir/man1/make.1*
%_infodir/make.info*


%changelog
* Mon Apr 18 2011 Antoine Ginies <aginies@mandriva.com> 1:3.82-3mdv2011.0
+ Revision: 655741
- use make-3.82-savannah-bugs-30612-30723.patch.bz2 patch

* Sun Aug 15 2010 Anssi Hannula <anssi@mandriva.org> 1:3.82-2mdv2011.0
+ Revision: 569887
- remove now unneeded make-pofiles.tar.bz2 (all translations are now
  provided by upstream)
- fix implicit re-executing of subdirs breaking variables provided in
  command line (upstream bug #30723, patch from upstream cvs)

* Sun Aug 01 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:3.82-1mdv2011.0
+ Revision: 564383
- update to new version 3.82
- drop patch0,
- rediff patch 1
- disable rpath
- spec file clean

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1:3.81-5mdv2010.1
+ Revision: 520152
- rebuilt for 2010.1

* Sun Dec 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1:3.81-4mdv2009.1
+ Revision: 317060
- rediffed some fuzzy patches

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1:3.81-3mdv2009.0
+ Revision: 223143
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 04 2007 Thierry Vignaud <tv@mandriva.org> 1:3.81-2mdv2008.1
+ Revision: 114962
- kill file require on info-install

* Wed Aug 22 2007 Adam Williamson <awilliamson@mandriva.org> 1:3.81-2mdv2008.0
+ Revision: 69242
- rebuild for 2008
- drop a 2006.0 conditional
- bunzip2 patches
- Import make



* Mon Aug 28 2006 Thierry Vignaud <tvignaud@mandriva.com> 3.81-1mdv2007.0
- new release (#24823)
- kill patch 2 (merged upstream)
- use %%mkrel
- fix make-check-outside-check-section, macro-in-%%changelog, ...

* Fri Sep  9 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.80-9mdk
- make gfortran the default fortran compiler (FC)

* Tue Mar 15 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.80-8mdk
- patch 2: fix memory exhausting (#14626)

* Fri Jan 21 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.80-7mdk
- linux32 fixes, aka. resolve -llib only in */lib when running under a
  32-bit personality

* Mon Oct 11 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.80-6mdk
- lib64 fixes

* Fri Jul 25 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.80-5mdk
- Patch0: Don't use high resolution timestamp to nuke librt dep

* Wed Jul 23 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 3.80-4mdk
- rebuild
- use %%make macro

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.80-3mdk
- build release

* Wed Nov 06 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.80-2mdk
- alter url for gnu site rather than source url (yura gusev)
- doc : add NEWS, remove glob/ChangeLog

* Tue Nov 05 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.80-1mdk
- new release
- fix url
- BuildRequires: autoconf2.5
- simplify
- drop patch 0 : there's no need to play with aclocal instead of using
  WANT_AUTOCONF_2_5
- drop patch 1 (better fix upstream)

* Sun Nov 03 2002 Stefan van der Eijk <stefan@eijk.nu> 3.79.1-12mdk
- BuildRequires: gettext-devel


* Thu Oct 10 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.79.1-11mdk
- patch 2: fix bad assertion triggered by xawtv

* Fri Jul  5 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.79.1-10mdk
- Costlessly make check in %%build stage

* Wed May 22 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.79.1-9mdk
- Automated rebuild with gcc 3.1-1mdk

* Mon May 06 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.79.1-8mdk
- Automated rebuild in gcc3.1 environment

* Tue Mar 26 2002 Frederic Lepied <flepied@mandrakesoft.com> 3.79.1-7mdk
- call libtoolize explicitly

* Fri Oct 26 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 3.79.1-6mdk
- Rebuild, fix rpmlint errors and warnings.
- Add patch #0, s/AC_PROG_RANLIB/AC_PROG_LIBTOOL/ in configure.in

* Thu Aug 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.79.1-5mdk
- corrected problem with %%preun script

* Thu Aug 03 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 3.79.1-4mdk
- integrated catalog files

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.79.1-3mdk
- BM

* Sun Jul  9 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.79.1-2mdk
- macroszifications.

* Sun Jun 25 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 3.79.1-1mdk
- 3.79.1

* Sat Jun 03 2000 David BAUDENS <baudens@mandrakesoft.com> 3.79-3mdk
- Fix %%doc
- Spec-helper

* Wed Apr 17 2000 Jeff Garzik <jgarzik@mandrakesoft.com> 3.79-2mdk
- more documentation in package

* Wed Apr 12 2000 Christopher Molnar <molnarc@mandrakesoft.com> 3.79-1mdk
- Update to 3.79

* Tue Apr 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 3.77-13mdk
- New Group

* Thu Jan 13 2000 Pixel <pixel@mandrakesoft.com>
- fix an rm

* Wed Oct 27 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with jeff package.

* Fri Aug 13 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- bzip2 info

* Tue Jul 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Bzip2 info pages, spec files tweaks.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Thu Apr 15 1999 Bill Nottingham <notting@redhat.com>
- added a serial tag so it upgrades right

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Wed Sep 16 1998 Cristian Gafton <gafton@redhat.com>
- added a patch for large file support in glob
 
* Tue Aug 18 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.77

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- udpated from 3.75 to 3.76
- various spec file cleanups
- added install-info support

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
