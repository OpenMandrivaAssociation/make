%bcond_without guile

Summary:	A GNU tool which simplifies the build process for users
Name:		make
Epoch:		1
Version:	4.3
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnu.org/directory/GNU/make.html
Source0:	ftp://ftp.gnu.org/pub/gnu/make/%{name}-%{version}.tar.lz
Patch1:		make-3.82-noclock_gettime.patch
Patch2:		make-4.3-clang.patch
# Don't reimplement stuff that's already in glibc, musl and friends
Patch3:		make-4.1-less-bloat.patch
# Upstream: https://savannah.gnu.org/bugs/?30748
Patch4:		make-3.82-weird-shell.patch
# (tpg) patches form CLR
Patch5:		skip-tests-features-archive.patch
# Fix armv7hnl build
Patch6:		make-4.3-arm-buildfix.patch
BuildRequires:	lzip
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
Summary:	Documentation for %{name}
Group:		Books/Computer books
BuildArch:	noarch
Requires:	%{name}

%description doc
Documentation, manuals and infos for %{make}.

%prep
%autosetup -p1

aclocal -I m4
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
# FIXME at some point all tests should pass on non-x86 as well
# but let's not delay the ports for now
%ifarch %{ix86} %{x86_64}
%check
# all tests must pass
./make-new check
%endif
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
%{_mandir}/man1/make.1*
%{_infodir}/make.info*
