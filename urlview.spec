Summary:	A URL extractor/viewer for use with Mutt
Summary(pl.UTF-8):	Program do wyciągania/oglądania URL-i dla Mutta
Name:		urlview
Version:	0.9
Release:	11
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.mutt.org/mutt/contrib/%{name}-%{version}.tar.gz
# Source0-md5:	67731f73e69297ffd106b65c8aebb2ab
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-regexp.patch
Patch2:		%{name}-links.patch
Patch3:		%{name}-home_etc.patch
Patch4:		%{name}-linking.patch
Patch5:		%{name}-include.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
Requires:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
urlview extracts URLs from a given text file, and presents a menu of
URLs to view using a user specified command.

%description -l pl.UTF-8
urlview wyciąga URL-e z podanego pliku tekstowego i pokazuje menu
pozwalające je oglądać podanym poleceniem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4
%patch5

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install url_handler.sh $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README sample.urlview urlview.sgml
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
