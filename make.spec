%bcond_without guile

Summary:	A GNU tool which simplifies the build process for users
Name:		make
Epoch:		1
Version:	4.1
Release:	4
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnu.org/directory/GNU/make.html
Source0:	ftp://ftp.gnu.org/pub/gnu/make/%{name}-%{version}.tar.bz2
Patch1:		make-3.82-noclock_gettime.patch
# Don't reimplement stuff that's already in glibc, musl and friends
Patch2:		make-4.1-less-bloat.patch
# Upstream: https://savannah.gnu.org/bugs/?30748
Patch6:		make-3.82-weird-shell.patch

BuildRequires:	gettext-devel
%if %{with guile}
BuildRequires:	pkgconfig(guile-2.0)
%endif

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

aclocal -I config
automake -a

%build
%configure \
%if %{with guile}
	--with-guile
%else
	--without-guile
%endif

%make

%if ! %{cross_compiling}
%check
# all tests must pass
make check
%endif

%install
%makeinstall_std

ln -sf make %{buildroot}%{_bindir}/gmake

# We probably don't need this
rm -rf %{buildroot}%{_includedir}

%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS README README.customs SCOPTIONS NEWS
%doc glob/COPYING.LIB glob/ChangeLog
%{_bindir}/make
%{_bindir}/gmake
%{_mandir}/man1/make.1*
%{_infodir}/make.info*
