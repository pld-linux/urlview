Name: urlview
%define version 0.7
Version: %{version}
Release: 3
Copyright: GPL
Group: Applications/Internet
Source: ftp://ftp.cs.hmc.edu/pub/me/urlview-0.7.tar.gz
Patch: urlview-default.patch
Requires: slang >= 0.99.38, webclient
Buildroot: /var/tmp/urlview-root
Summary: A URL extractor/viewer for use with Mutt.

%description
urlview extracts URLs from a given text file, and presents a menu
of URLs to view using a user specified command.

%prep
%setup -q
%patch -p1 -b .default

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr \
	--with-slang
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}
make prefix=$RPM_BUILD_ROOT/usr install
install -m755 url_handler.sh $RPM_BUILD_ROOT/usr/bin/url_handler.sh
strip $RPM_BUILD_ROOT/usr/bin/urlview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%doc INSTALL README sample.urlview 
%doc urlview.sgml
/usr/bin/urlview
/usr/bin/url_handler.sh
/usr/man/man1/urlview.1

%changelog
* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Thu Mar 18 1999 Bill Nottingham <notting@redhat.com>
- strip binary
- fix defaults some

* Sat Dec 12 1998 Bill Nottingham <notting@redhat.com>
- initial build
