Summary:	A GNU tool which simplifies the build process for users
Name:		make
Version:	3.82
Release:	5
Epoch:		1
Url:		http://www.gnu.org/directory/GNU/make.html
License:	GPLv2+
Group:		Development/Other
Source0:	ftp://ftp.gnu.org/pub/gnu/make/%{name}-%{version}.tar.bz2
Patch1:		make-3.82-lib64.patch
Patch2:		make-fix_whitespace_tokenization.diff
Patch3:		make-3.80-gfortran.patch
# https://savannah.gnu.org/bugs/?30723
# https://savannah.gnu.org/bugs/?30612
Patch4:		make-3.82-savannah-bugs-30612-30723.patch.bz2
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
%patch1 -p1 -b .lib64
%patch2 -p1 -b .bug33125
%patch3 -p1 -b .gfortran
%patch4 -p1 -b .bugs30612-30723

%build
%configure2_5x \
	--disable-rpath
%make

%check
# all tests must pass
make check

%install
rm -rf %{buildroot}
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
