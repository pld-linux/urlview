Summary:	A URL extractor/viewer for use with Mutt.
Name:		urlview
Version:	0.7
Release:	3
Copyright:	GPL
Group:		Applications/Internet
Source:		ftp://ftp.cs.hmc.edu/pub/me/urlview-0.7.tar.gz
Patch:		urlview-default.patch
Requires:	slang >= 0.99.38, webclient
BuildRoot:	/tmp/%{name}-%{version}-root

%description
urlview extracts URLs from a given text file, and presents a menu
of URLs to view using a user specified command.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
%configure \
	--with-slang
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	mandir=$RPM_BUILD_ROOT/%{_mandir} \
	bindir=$RPM_BUILD_ROOT/%{_bindir}

install url_handler.sh $RPM_BUILD_ROOT%{_bindir}/url_handler
strip $RPM_BUILD_ROOT%{_bindir}/urlview

gzip -9nf AUTHORS ChangeLog README sample.urlview urlview.sgml \
	$RPM_BUILD_ROOT/%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,sample.urlview,urlview.sgml}.gz
%attr(755,root,root) %{_bindir}/urlview
%attr(755,root,root) %{_bindir}/url_handler
%{_mandir}/man1/urlview.1.gz
