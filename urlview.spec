Summary:	A URL extractor/viewer for use with Mutt
Summary(pl):	Program do wyci±gania/ogl±dania URL-i dla Mutta
Name:		urlview
Version:	0.9
Release:	4
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.mutt.org/pub/mutt/contrib/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slang-devel
Requires:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
urlview extracts URLs from a given text file, and presents a menu of
URLs to view using a user specified command.

%description -l pl
urlview wyci±ga URL-e z podanego pliku tekstowego i pokazuje menu
pozwalaj±ce je ogl±daæ podanym poleceniem.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure \
	--with-slang
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install url_handler.sh $RPM_BUILD_ROOT%{_bindir}/

gzip -9nf AUTHORS ChangeLog README sample.urlview urlview.sgml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
