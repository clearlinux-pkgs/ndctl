#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndctl
Version  : 64.1
Release  : 39
URL      : https://github.com/pmem/ndctl/archive/v64.1.tar.gz
Source0  : https://github.com/pmem/ndctl/archive/v64.1.tar.gz
Summary  : Utility library for managing the libnvdimm (non-volatile memory device) sub-system in the Linux kernel
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: ndctl-bin = %{version}-%{release}
Requires: ndctl-data = %{version}-%{release}
Requires: ndctl-lib = %{version}-%{release}
Requires: ndctl-license = %{version}-%{release}
Requires: ndctl-services = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : docbook-xml
BuildRequires : keyutils-dev
BuildRequires : kmod-dev
BuildRequires : libxml2-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(libkmod)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(systemd)
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
Requires: ndctl-data = %{version}-%{release}
Requires: ndctl-license = %{version}-%{release}
Requires: ndctl-services = %{version}-%{release}

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
Requires: ndctl-lib = %{version}-%{release}
Requires: ndctl-bin = %{version}-%{release}
Requires: ndctl-data = %{version}-%{release}
Provides: ndctl-devel = %{version}-%{release}

%description dev
dev components for the ndctl package.


%package lib
Summary: lib components for the ndctl package.
Group: Libraries
Requires: ndctl-data = %{version}-%{release}
Requires: ndctl-license = %{version}-%{release}

%description lib
lib components for the ndctl package.


%package license
Summary: license components for the ndctl package.
Group: Default

%description license
license components for the ndctl package.


%package services
Summary: services components for the ndctl package.
Group: Systemd services

%description services
services components for the ndctl package.


%prep
%setup -q -n ndctl-64.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549464273
%autogen --disable-static --disable-docs
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1549464273
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ndctl
cp COPYING %{buildroot}/usr/share/package-licenses/ndctl/COPYING
cp Documentation/COPYING %{buildroot}/usr/share/package-licenses/ndctl/Documentation_COPYING
cp ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_array_size_LICENSE
cp ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_build_assert_LICENSE
cp ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_check_type_LICENSE
cp ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_container_of_LICENSE
cp ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_endian_LICENSE
cp ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_list_LICENSE
cp ccan/minmax/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_minmax_LICENSE
cp ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_short_types_LICENSE
cp ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/ccan_str_LICENSE
cp util/COPYING %{buildroot}/usr/share/package-licenses/ndctl/util_COPYING
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
/usr/share/daxctl/daxctl.conf

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdaxctl.so.1
/usr/lib64/libdaxctl.so.1.2.1
/usr/lib64/libndctl.so.6
/usr/lib64/libndctl.so.6.13.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ndctl/COPYING
/usr/share/package-licenses/ndctl/Documentation_COPYING
/usr/share/package-licenses/ndctl/ccan_array_size_LICENSE
/usr/share/package-licenses/ndctl/ccan_build_assert_LICENSE
/usr/share/package-licenses/ndctl/ccan_check_type_LICENSE
/usr/share/package-licenses/ndctl/ccan_container_of_LICENSE
/usr/share/package-licenses/ndctl/ccan_endian_LICENSE
/usr/share/package-licenses/ndctl/ccan_list_LICENSE
/usr/share/package-licenses/ndctl/ccan_minmax_LICENSE
/usr/share/package-licenses/ndctl/ccan_short_types_LICENSE
/usr/share/package-licenses/ndctl/ccan_str_LICENSE
/usr/share/package-licenses/ndctl/util_COPYING

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ndctl-monitor.service
