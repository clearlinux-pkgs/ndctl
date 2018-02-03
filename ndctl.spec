#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndctl
Version  : 58.4
Release  : 23
URL      : https://github.com/pmem/ndctl/archive/v58.4.tar.gz
Source0  : https://github.com/pmem/ndctl/archive/v58.4.tar.gz
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
BuildRequires : pkgconfig(libpmem)
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
%setup -q -n ndctl-58.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517701455
%autogen --disable-static --disable-docs
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1517701455
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/daxctl
/usr/bin/ndctl

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/ndctl

%files dev
%defattr(-,root,root,-)
/usr/include/daxctl/libdaxctl.h
/usr/include/ndctl/libdaxctl.h
/usr/include/ndctl/libndctl.h
/usr/lib64/libdaxctl.so
/usr/lib64/libndctl.so
/usr/lib64/pkgconfig/libdaxctl.pc
/usr/lib64/pkgconfig/libndctl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdaxctl.so.1
/usr/lib64/libdaxctl.so.1.2.0
/usr/lib64/libndctl.so.6
/usr/lib64/libndctl.so.6.7.0
