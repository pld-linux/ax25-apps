Summary:	ax25 tools for hamradio
Summary(pl.UTF-8):	Narzędzia ax25 dla hamradio
Name:		ax25-apps
Version:	0.0.6
Release:	6
License:	GPL v2+
Group:		Applications/Communications
Source0:	https://downloads.sourceforge.net/ax25/%{name}-%{version}.tar.gz
# Source0-md5:	47d9a775890f3694cf47659423a69ae5
Patch0:		%{name}-optflags.patch
URL:		https://ax25.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libax25-devel >= 0.0.8
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Requires:	ax25-tools >= 0.0.8
Requires:	libax25 >= 0.0.9
Conflicts:	kernel <= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Applications to test our AX25 connects.

%description -l pl.UTF-8
Aplikacje testujące sprawność połączeń protokołu AX25.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install installconf \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ax25-apps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# note: ax25ipd/COPYING.ax25ipd contains notes other than GPL
%doc AUTHORS ChangeLog NEWS README ax25ipd/{COPYING,HISTORY,README}.ax25ipd ax25rtd/{README,TODO}.ax25rtd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/ax25ipd.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/ax25mond.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ax25/ax25rtd.conf
%attr(755,root,root) %{_bindir}/call
%attr(755,root,root) %{_bindir}/listen
%attr(755,root,root) %{_sbindir}/ax25ipd
%attr(755,root,root) %{_sbindir}/ax25mond
%attr(755,root,root) %{_sbindir}/ax25rtctl
%attr(755,root,root) %{_sbindir}/ax25rtd
%{_mandir}/man1/call.1*
%{_mandir}/man1/listen.1*
%{_mandir}/man5/ax25ipd.conf.5*
%{_mandir}/man5/ax25mond.conf.5*
%{_mandir}/man8/ax25ipd.8*
%{_mandir}/man8/ax25mond.8*
