Summary:	A GNU tool which simplifies the build process for users
Name:		make
Version:	3.81
Release:	%mkrel 3
Epoch:		1
Url:		http://www.gnu.org/directory/GNU/make.html
License:	GPLv2+
Group:		Development/Other
Source:		ftp://ftp.gnu.org/pub/gnu/make/%name-%version.tar.bz2
# to remove once those po files are included in standard sources
Source1:	%{name}-pofiles.tar.bz2
Patch0:		make-3.80-no-hires-timestamp.patch
Patch1:		make-3.80-lib64.patch
Patch3:		make-3.80-gfortran.patch
BuildRequires:	gettext-devel
Requires(pre):		info-install
Requires(post):		info-install
Buildroot:	%_tmppath/%name-root

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
%setup -q -a1
# WARNING: only configure script is patched
%patch0 -p1 -b .no-hires-timestamp
%patch1 -p1 -b .lib64
%patch3 -p1 -b .gfortran

%build
%configure2_5x
%make

%check
# all tests must pass
make check

%install
rm -rf $RPM_BUILD_ROOT/

%makeinstall

ln -sf make $RPM_BUILD_ROOT%_bindir/gmake

# some hand dealing; to remove when the %{name}-pofiles.tar.bz2 is removed
for i in i18n/*.po ; do
  mkdir -p $RPM_BUILD_ROOT/%{_datadir}/locale/`basename $i .po`/LC_MESSAGES
  msgfmt -v -o $RPM_BUILD_ROOT/%{_datadir}/locale/`basename $i .po`/LC_MESSAGES/%{name}.mo $i
done

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

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
