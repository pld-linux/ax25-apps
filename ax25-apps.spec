Summary: ax25 toolls for hamradio.
Name: ax25-apps
Version: 0.0.5
Release: 1
License: LGPL
Group: Applications/Communications
Group(pl): Aplikacje/Komunikacja
Source0: http://prdownloads.sourceforge.net/ax25/ax25-apps-%{version}.tar.gz
Patch0: http://zolw.eu.org/~djrzulf/PLD/patch/%{name}-call.patch
Patch1: http://zolw.eu.org/~djrzulf/PLD/patch/%{name}-menu.patch
Patch2: http://zolw.eu.org/~djrzulf/PLD/patch/%{name}-listen.patch
Patch3: http://zolw.eu.org/~djrzulf/PLD/patch/%{name}-utils.patch
BuildRoot: /tmp/%{name}-%{version}-root
ExclusiveArch: %{ix86}
Requires: glibc >= 2.2
Requires: kernel >= 2.2.0
Requires: libtool >= 1.4.2
Requires: libax25 >= 0.0.9
Requires: zlib >= 1.1.3
Requires: ax25-tools >= 0.0.8

BuildRequires: libax25-devel
BuildRequires: zlib-devel

%description

Applications to test our AX25 connects.

%description -l pl

Aplikacje testuj±ce sprawno¶æ po³±czeñ protoko³u AX25.

%prep
%setup -q

cd call
%patch0 -p0
%patch1 -p0
cd ../listen
%patch2 -p0
%patch3 -p0

%build

%configure2_13
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=${RPM_BUILD_ROOT} install installconf
gzip -9nf ${RPM_BUILD_ROOT}/usr/share/doc/ax25-apps/*
gzip -9nf ${RPM_BUILD_ROOT}/usr/share/man/man1/*
gzip -9nf ${RPM_BUILD_ROOT}/usr/share/man/man5/*
gzip -9nf ${RPM_BUILD_ROOT}/usr/share/man/man8/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

#%clean                                                                          
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/%{_sysconfdir}/ax25/*
/%{_bindir}/*
/%{_sbindir}/*
/%{_docdir}/ax25-apps/*.gz
/%{_mandir}/man[158]/*.gz
