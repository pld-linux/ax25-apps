Summary:	ax25 tools for hamradio
Summary(pl):	Narzêdzia ax25 dla hamradio
Name:		ax25-apps
Version:	0.0.5
Release:	1
License:	LGPL
Group:		Applications/Communications
Group(de):	Applikationen/Kommunikation
Group(pl):	Aplikacje/Komunikacja
Source0:	http://prdownloads.sourceforge.net/ax25/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}
Requires:	glibc >= 2.2
Requires:	kernel >= 2.2.0
Requires:	libtool >= 1.4.2
Requires:	libax25 >= 0.0.9
Requires:	zlib >= 1.1.3
Requires:	ax25-tools >= 0.0.8

BuildRequires:	libax25-devel
BuildRequires:	zlib-devel

%description
Applications to test our AX25 connects.

%description -l pl
Aplikacje testuj±ce sprawno¶æ po³±czeñ protoko³u AX25.

%prep
%setup -q

%build
CPPFLAGS="-I%{_includedir}/ncurses"; export CPPFLAGS
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install installconf
gzip -9nf $RPM_BUILD_ROOT%{_datadir}/doc/ax25-apps/*
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man5/*
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/*

%clean                                                                          
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_sysconfdir}/ax25/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%docdir %{_docdir}/ax25-apps
%dir %{_docdir}/ax25-apps
%{_docdir}/ax25-apps/*.gz
%{_mandir}/man[158]/*.gz
