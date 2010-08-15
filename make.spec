Summary:	A GNU tool which simplifies the build process for users
Name:		make
Version:	3.82
Release:	%mkrel 2
Epoch:		1
Url:		http://www.gnu.org/directory/GNU/make.html
License:	GPLv2+
Group:		Development/Other
Source:		ftp://ftp.gnu.org/pub/gnu/make/%name-%version.tar.bz2
Patch1:		make-3.82-lib64.patch
Patch3:		make-3.80-gfortran.patch
# https://savannah.gnu.org/bugs/?30723
Patch4:		make-bug-30723.patch
BuildRequires:	gettext-devel
Requires(pre):		info-install
Requires(post):		info-install
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot

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
%patch3 -p1 -b .gfortran
%patch4 -p1

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

%clean
rm -rf %{buildroot}

%post
%_install_info make.info

%preun
%_remove_install_info make.info

%files -f %name.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog README README.customs SCOPTIONS NEWS
%doc glob/COPYING.LIB glob/ChangeLog
%_bindir/make
%_bindir/gmake
%_mandir/man1/make.1*
%_infodir/make.info*
