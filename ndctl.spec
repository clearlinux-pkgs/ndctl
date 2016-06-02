#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndctl
Version  : 53.1
Release  : 11
URL      : https://github.com/pmem/ndctl/archive/v53.1.tar.gz
Source0  : https://github.com/pmem/ndctl/archive/v53.1.tar.gz
Summary  : Manage "libnvdimm" subsystem devices (Non-volatile Memory)
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: ndctl-bin
Requires: ndctl-lib
Requires: ndctl-data
BuildRequires : asciidoc
BuildRequires : docbook-xml
BuildRequires : kmod-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(uuid)
BuildRequires : sed
BuildRequires : xmlto
Patch1: build.patch

%description
# ndctl
Utility library for managing the libnvdimm (non-volatile memory device)
sub-system in the Linux kernel

%package bin
Summary: bin components for the ndctl package.
Group: Binaries
Requires: ndctl-data

%description bin
bin components for the ndctl package.


%package data
Summary: data components for the ndctl package.
Group: Data

%description data
data components for the ndctl package.


%package dev
Summary: dev components for the ndctl package.
Group: Development
Requires: ndctl-lib
Requires: ndctl-bin
Requires: ndctl-data
Provides: ndctl-devel

%description dev
dev components for the ndctl package.


%package lib
Summary: lib components for the ndctl package.
Group: Libraries
Requires: ndctl-data

%description lib
lib components for the ndctl package.


%prep
%setup -q -n ndctl-53.1
%patch1 -p1

%build
%autogen --disable-static --disable-docs
make V=1  %{?_smp_mflags}

%check
export LANG=C
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

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/ndctl

%files dev
%defattr(-,root,root,-)
/usr/include/daxctl/libdaxctl.h
/usr/include/ndctl/libndctl.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
