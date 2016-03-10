#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndctl
Version  : 51
Release  : 6
URL      : https://github.com/pmem/ndctl/archive/v51.tar.gz
Source0  : https://github.com/pmem/ndctl/archive/v51.tar.gz
Summary  : Device discovery and manipulation for the "nd" subsystem
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: ndctl-bin
Requires: ndctl-lib
Requires: ndctl-doc
BuildRequires : asciidoc
BuildRequires : docbook-xml
BuildRequires : kmod-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(uuid)
BuildRequires : sed
BuildRequires : xmlto

%description
# ndctl
Utility library for managing the libnvdimm (non-volatile memory device)
sub-system in the Linux kernel

%package bin
Summary: bin components for the ndctl package.
Group: Binaries

%description bin
bin components for the ndctl package.


%package dev
Summary: dev components for the ndctl package.
Group: Development
Requires: ndctl-lib
Requires: ndctl-bin
Provides: ndctl-devel

%description dev
dev components for the ndctl package.


%package doc
Summary: doc components for the ndctl package.
Group: Documentation

%description doc
doc components for the ndctl package.


%package lib
Summary: lib components for the ndctl package.
Group: Libraries

%description lib
lib components for the ndctl package.


%prep
%setup -q -n ndctl-51

%build
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ndctl

%files dev
%defattr(-,root,root,-)
/usr/include/ndctl/libndctl.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
