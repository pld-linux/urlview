Name: urlview
%define version 0.7
Version: %{version}
Release: 3
Copyright: GPL
Group: Applications/Internet
Source: ftp://ftp.cs.hmc.edu/pub/me/urlview-0.7.tar.gz
Patch: urlview-default.patch
Requires: slang >= 0.99.38, webclient
BuildRoot:	/tmp/%{name}-%{version}-root
Summary: A URL extractor/viewer for use with Mutt.

%description
urlview extracts URLs from a given text file, and presents a menu
of URLs to view using a user specified command.

%prep
%setup -q
%patch -p1 -b .default

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=/usr \
	--with-slang
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}
make prefix=$RPM_BUILD_ROOT/usr install
install -m755 url_handler.sh $RPM_BUILD_ROOT%{_bindir}/url_handler.sh
strip $RPM_BUILD_ROOT%{_bindir}/urlview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%doc INSTALL README sample.urlview 
%doc urlview.sgml
%{_bindir}/urlview
%{_bindir}/url_handler.sh
%{_mandir}/man1/urlview.1
