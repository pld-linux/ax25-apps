Summary:	ax25 tools for hamradio
Summary(pl):	Narzêdzia ax25 dla hamradio
Name:		ax25-apps
Version:	0.0.6
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://prdownloads.sourceforge.net/ax25/%{name}-%{version}.tar.gz
BuildRequires:	libax25-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Requires:	libax25 >= 0.0.9
Requires:	ax25-tools >= 0.0.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kernel <= 2.2.0

%description
Applications to test our AX25 connects.

%description -l pl
Aplikacje testuj±ce sprawno¶æ po³±czeñ protoko³u AX25.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
AM_CFLAGS="-I%{_includedir}/ncurses"; export AM_CFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install installconf \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README \
	*/{COPYING,HISTORY,README}*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz */*.gz
%{_sysconfdir}/ax25/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man[158]/*
