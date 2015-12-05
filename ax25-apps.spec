Summary:	ax25 tools for hamradio
Summary(pl.UTF-8):	Narzędzia ax25 dla hamradio
Name:		ax25-apps
Version:	0.0.6
Release:	5
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/ax25/%{name}-%{version}.tar.gz
# Source0-md5:	47d9a775890f3694cf47659423a69ae5
URL:		http://ax25.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libax25-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Requires:	ax25-tools >= 0.0.8
Requires:	libax25 >= 0.0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kernel <= 2.2.0

%description
Applications to test our AX25 connects.

%description -l pl.UTF-8
Aplikacje testujące sprawność połączeń protokołu AX25.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
AM_CFLAGS="-I/usr/include/ncurses"; export AM_CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install installconf \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# note: ax25ipd/COPYING.ax25ipd contains notes other than GPL
%doc AUTHORS ChangeLog NEWS README ax25*/{COPYING,HISTORY,README}.ax25*
%{_sysconfdir}/ax25/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*
