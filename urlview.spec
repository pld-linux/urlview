Summary:	A URL extractor/viewer for use with Mutt
Name:		urlview
Version:	0.7
Release:	3
License:	GPL
Group:		Applications/Internet
######		Unknown group!
Source0:	ftp://ftp.cs.hmc.edu/pub/me/%{name}-%{version}.tar.gz
Patch0:		urlview-default.patch
Requires:	slang >= 0.99.38, webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
urlview extracts URLs from a given text file, and presents a menu of
URLs to view using a user specified command.

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-slang
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT/%{_mandir} \
	bindir=$RPM_BUILD_ROOT/%{_bindir}

install url_handler.sh $RPM_BUILD_ROOT%{_bindir}/url_handler

gzip -9nf AUTHORS ChangeLog README sample.urlview urlview.sgml \
	$RPM_BUILD_ROOT/%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
