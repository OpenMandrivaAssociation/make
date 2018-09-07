%bcond_without guile

Summary:	A GNU tool which simplifies the build process for users
Name:		make
Epoch:		1
Version:	4.2.1
Release:	5
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnu.org/directory/GNU/make.html
Source0:	ftp://ftp.gnu.org/pub/gnu/make/%{name}-%{version}.tar.bz2
Patch1:		make-3.82-noclock_gettime.patch
Patch2:		make-4.2-j8k.patch
# Don't reimplement stuff that's already in glibc, musl and friends
Patch3:		make-4.1-less-bloat.patch
# Upstream: https://savannah.gnu.org/bugs/?30748
Patch4:		make-3.82-weird-shell.patch
# (tpg) patches form CLR
Patch5:		skip-tests-features-archive.patch
Patch6:		0002-Fix_tests.patch
# Upstream patch: https://git.savannah.gnu.org/cgit/make.git/patch/?id=193f1e81edd6b1b56b0eb0ff8aa4b41c7b4257b4
# Fixes wrong assumptions of glibc's glob internals.
Patch7:		make-4.2.1-glob-fix-2.patch
# Upstream patch: https://git.savannah.gnu.org/cgit/make.git/patch/?id=48c8a116a914a325a0497721f5d8b58d5bba34d4
# Fixes incorrect use of glibc 2.27 glob internals.
Patch8:		make-4.2.1-glob-fix.patch
# Fix build with guile 2.2 (as opposed to 1.8 and 2.0)
Patch9:		make-4.2.1-guile-2.2.patch

BuildRequires:	gettext-devel
BuildRequires:	gmp-devel
%if %{with guile}
BuildRequires:	pkgconfig(guile-2.2)
%endif
Suggests:   %{name}-doc

%description
A GNU tool for controlling the generation of executables and other
non-source files of a program from the program's source files.  Make
allows users to build and install packages without any significant
knowledge about the details of the build process.  The details about how
the program should be built are provided for make in the program's
makefile.

The GNU make tool should be installed on your system because it is
commonly used to simplify the process of installing programs.

%package doc
Summary:    Documentation for %{name}
Group:      Books/Computer books
BuildArch:	noarch
Requires:   %{name}

%description doc
Documentation, manuals and infos for %{make}.

%prep
%setup -q
%apply_patches

aclocal -I config
automake -a

%build
%configure \
%if %{with guile}
    --with-guile
%else
    --without-guile
%endif

./build.sh
cp make make-new
./make-new clean

./make-new %{?_smp_mflags}

%if ! %{cross_compiling}
%check
# all tests must pass
./make-new check
%endif

%install
./make install DESTDIR=%{buildroot}

ln -sf make %{buildroot}%{_bindir}/gmake

# We probably don't need this
rm -rf %{buildroot}%{_includedir}

%find_lang %{name} || touch %{name}.lang

%files -f %{name}.lang
%{_bindir}/make
%{_bindir}/gmake

%files doc
%doc ABOUT-NLS AUTHORS README README.customs SCOPTIONS NEWS
%doc glob/COPYING.LIB glob/ChangeLog
%{_mandir}/man1/make.1*
%{_infodir}/make.info*
