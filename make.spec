Summary:	A GNU tool which simplifies the build process for users
Name:		make
Epoch:		1
Version:	4.0
Release:	2
License:	GPLv2+
Group:		Development/Other
Url:		http://www.gnu.org/directory/GNU/make.html
Source0:	ftp://ftp.gnu.org/pub/gnu/make/%{name}-%{version}.tar.bz2
Patch1:		make-3.82-noclock_gettime.patch
# Upstream: https://savannah.gnu.org/bugs/?30748
Patch6:		make-3.82-weird-shell.patch

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

# We probably don't need this
rm -rf %{buildroot}%{_includedir}

%find_lang %{name}

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog README README.customs SCOPTIONS NEWS
%doc glob/COPYING.LIB glob/ChangeLog
%{_bindir}/make
%{_bindir}/gmake
%{_mandir}/man1/make.1*
%{_infodir}/make.info*

