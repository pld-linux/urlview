Summary:	A URL extractor/viewer for use with Mutt
Name:		urlview
Version:	0.9
Release:	3
License:	GPL
Group:		Applications/Internet
######		Unknown group!
Source0:	ftp://ftp.mutt.org/pub/mutt/contrib/%{name}-%{version}.tar.gz
Requires:	slang >= 0.99.38, webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
urlview extracts URLs from a given text file, and presents a menu of
URLs to view using a user specified command.

%prep
%setup -q

%build
%configure2_13 \
	--with-slang
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT/%{_mandir} \
	bindir=$RPM_BUILD_ROOT/%{_bindir}

install url_handler.sh $RPM_BUILD_ROOT%{_bindir}/


gzip -9nf AUTHORS ChangeLog README sample.urlview urlview.sgml



%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
