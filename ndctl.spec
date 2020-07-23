#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ndctl
Version  : 69
Release  : 43
URL      : https://github.com/pmem/ndctl/archive/v69/ndctl-69.tar.gz
Source0  : https://github.com/pmem/ndctl/archive/v69/ndctl-69.tar.gz
Summary  : Manage "libnvdimm" subsystem devices (Non-volatile Memory)
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.1 MIT
Requires: ndctl-bin = %{version}-%{release}
Requires: ndctl-data = %{version}-%{release}
Requires: ndctl-lib = %{version}-%{release}
Requires: ndctl-license = %{version}-%{release}
Requires: ndctl-man = %{version}-%{release}
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
[![Build Status](https://travis-ci.org/pmem/ndctl.svg?branch=master)](https://travis-ci.org/pmem/ndctl)

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
Requires: ndctl = %{version}-%{release}

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


%package man
Summary: man components for the ndctl package.
Group: Default

%description man
man components for the ndctl package.


%package services
Summary: services components for the ndctl package.
Group: Systemd services

%description services
services components for the ndctl package.


%prep
%setup -q -n ndctl-69
cd %{_builddir}/ndctl-69
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595530521
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static --disable-asciidoctor
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1595530521
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ndctl
cp %{_builddir}/ndctl-69/COPYING %{buildroot}/usr/share/package-licenses/ndctl/5885edf2f275ae8fdcbbc22191d87064fbfa2516
cp %{_builddir}/ndctl-69/Documentation/COPYING %{buildroot}/usr/share/package-licenses/ndctl/cac5aabfbd6b7df58097e0f2efc0021152a31247
cp %{_builddir}/ndctl-69/Documentation/copyright.txt %{buildroot}/usr/share/package-licenses/ndctl/286b18774f60cb7349670ad94a0614927f9a83e2
cp %{_builddir}/ndctl-69/ccan/array_size/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/ccan/build_assert/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/ccan/check_type/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/ccan/container_of/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
cp %{_builddir}/ndctl-69/ccan/minmax/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/ccan/short_types/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/ccan/str/LICENSE %{buildroot}/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
cp %{_builddir}/ndctl-69/util/COPYING %{buildroot}/usr/share/package-licenses/ndctl/b47456e2c1f38c40346ff00db976a2badf36b5e3
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
/usr/lib64/libdaxctl.so.1.4.0
/usr/lib64/libndctl.so.6
/usr/lib64/libndctl.so.6.18.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ndctl/2807f3f1c4cb33b214defc4c7ab72f7e4e70a305
/usr/share/package-licenses/ndctl/286b18774f60cb7349670ad94a0614927f9a83e2
/usr/share/package-licenses/ndctl/3e8117303a7ac9ce341dc761b8a4f5ac3696e0a3
/usr/share/package-licenses/ndctl/5885edf2f275ae8fdcbbc22191d87064fbfa2516
/usr/share/package-licenses/ndctl/b47456e2c1f38c40346ff00db976a2badf36b5e3
/usr/share/package-licenses/ndctl/cac5aabfbd6b7df58097e0f2efc0021152a31247

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/daxctl-list.1
/usr/share/man/man1/daxctl-migrate-device-model.1
/usr/share/man/man1/daxctl-offline-memory.1
/usr/share/man/man1/daxctl-online-memory.1
/usr/share/man/man1/daxctl-reconfigure-device.1
/usr/share/man/man1/daxctl.1
/usr/share/man/man1/ndctl-check-labels.1
/usr/share/man/man1/ndctl-check-namespace.1
/usr/share/man/man1/ndctl-clear-errors.1
/usr/share/man/man1/ndctl-create-namespace.1
/usr/share/man/man1/ndctl-destroy-namespace.1
/usr/share/man/man1/ndctl-disable-dimm.1
/usr/share/man/man1/ndctl-disable-namespace.1
/usr/share/man/man1/ndctl-disable-region.1
/usr/share/man/man1/ndctl-enable-dimm.1
/usr/share/man/man1/ndctl-enable-namespace.1
/usr/share/man/man1/ndctl-enable-region.1
/usr/share/man/man1/ndctl-freeze-security.1
/usr/share/man/man1/ndctl-init-labels.1
/usr/share/man/man1/ndctl-inject-error.1
/usr/share/man/man1/ndctl-inject-smart.1
/usr/share/man/man1/ndctl-list.1
/usr/share/man/man1/ndctl-load-keys.1
/usr/share/man/man1/ndctl-monitor.1
/usr/share/man/man1/ndctl-read-infoblock.1
/usr/share/man/man1/ndctl-read-labels.1
/usr/share/man/man1/ndctl-remove-passphrase.1
/usr/share/man/man1/ndctl-sanitize-dimm.1
/usr/share/man/man1/ndctl-setup-passphrase.1
/usr/share/man/man1/ndctl-start-scrub.1
/usr/share/man/man1/ndctl-update-firmware.1
/usr/share/man/man1/ndctl-update-passphrase.1
/usr/share/man/man1/ndctl-wait-overwrite.1
/usr/share/man/man1/ndctl-wait-scrub.1
/usr/share/man/man1/ndctl-write-infoblock.1
/usr/share/man/man1/ndctl-write-labels.1
/usr/share/man/man1/ndctl-zero-labels.1
/usr/share/man/man1/ndctl.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ndctl-monitor.service
