Summary:	A GNU tool which simplifies the build process for users
Name:		make
Epoch:		1
Version:	3.82
Release:	12
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnu.org/directory/GNU/make.html
Source0:	ftp://ftp.gnu.org/pub/gnu/make/%{name}-%{version}.tar.bz2
Patch1:		make-3.82-noclock_gettime.patch
Patch2:		make-3.82-j8k.patch
Patch3:		make-3.82-getcwd.patch
Patch4:		make-3.82-err-reporting.patch
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
Patch20:	make-texinfo5-item.patch

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
%apply_patches

%build
%configure2_5x
%make

%check
# all tests must pass
make check

%install
%makeinstall_std

ln -sf make %{buildroot}%{_bindir}/gmake

%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog README README.customs SCOPTIONS NEWS
%doc glob/COPYING.LIB glob/ChangeLog
%{_bindir}/make
%{_bindir}/gmake
%{_mandir}/man1/make.1*
%{_infodir}/make.info*

