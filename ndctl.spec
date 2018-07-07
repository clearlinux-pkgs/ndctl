#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndctl
Version  : 61.2
Release  : 34
URL      : https://github.com/pmem/ndctl/archive/v61.2.tar.gz
Source0  : https://github.com/pmem/ndctl/archive/v61.2.tar.gz
Summary  : Manage "libnvdimm" subsystem devices (Non-volatile Memory)
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: ndctl-bin
Requires: ndctl-lib
Requires: ndctl-data
Requires: ndctl-license
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
Requires: ndctl-license

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


%package doc
Summary: doc components for the ndctl package.
Group: Documentation

%description doc
doc components for the ndctl package.


%package lib
Summary: lib components for the ndctl package.
Group: Libraries
Requires: ndctl-data
Requires: ndctl-license

%description lib
lib components for the ndctl package.


%package license
Summary: license components for the ndctl package.
Group: Default

%description license
license components for the ndctl package.


%prep
%setup -q -n ndctl-61.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530973306
%autogen --disable-static --disable-docs
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1530973306
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ndctl
cp COPYING %{buildroot}/usr/share/doc/ndctl/COPYING
cp util/COPYING %{buildroot}/usr/share/doc/ndctl/util_COPYING
cp ccan/str/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_str_LICENSE
cp ccan/short_types/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_short_types_LICENSE
cp ccan/minmax/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_minmax_LICENSE
cp ccan/list/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_list_LICENSE
cp ccan/endian/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_endian_LICENSE
cp ccan/container_of/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_container_of_LICENSE
cp ccan/check_type/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_check_type_LICENSE
cp ccan/build_assert/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_build_assert_LICENSE
cp ccan/array_size/LICENSE %{buildroot}/usr/share/doc/ndctl/ccan_array_size_LICENSE
cp Documentation/copyright.txt %{buildroot}/usr/share/doc/ndctl/Documentation_copyright.txt
cp Documentation/COPYING %{buildroot}/usr/share/doc/ndctl/Documentation_COPYING
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
/usr/include/ndctl/ndctl.h
/usr/lib64/libdaxctl.so
/usr/lib64/libndctl.so
/usr/lib64/pkgconfig/libdaxctl.pc
/usr/lib64/pkgconfig/libndctl.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ndctl/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdaxctl.so.1
/usr/lib64/libdaxctl.so.1.2.0
/usr/lib64/libndctl.so.6
/usr/lib64/libndctl.so.6.10.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/ndctl/COPYING
/usr/share/doc/ndctl/Documentation_COPYING
/usr/share/doc/ndctl/ccan_array_size_LICENSE
/usr/share/doc/ndctl/ccan_build_assert_LICENSE
/usr/share/doc/ndctl/ccan_check_type_LICENSE
/usr/share/doc/ndctl/ccan_container_of_LICENSE
/usr/share/doc/ndctl/ccan_endian_LICENSE
/usr/share/doc/ndctl/ccan_list_LICENSE
/usr/share/doc/ndctl/ccan_minmax_LICENSE
/usr/share/doc/ndctl/ccan_short_types_LICENSE
/usr/share/doc/ndctl/ccan_str_LICENSE
/usr/share/doc/ndctl/util_COPYING
