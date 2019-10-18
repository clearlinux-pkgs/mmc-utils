#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mmc-utils
Version  : 73d6c59af8d1bcedf5de4aa1f5d5b7f765f545f5
Release  : 1
URL      : https://git.kernel.org/pub/scm/linux/kernel/git/cjb/mmc-utils.git/snapshot/mmc-utils-73d6c59af8d1bcedf5de4aa1f5d5b7f765f545f5.tar.gz
Source0  : https://git.kernel.org/pub/scm/linux/kernel/git/cjb/mmc-utils.git/snapshot/mmc-utils-73d6c59af8d1bcedf5de4aa1f5d5b7f765f545f5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: mmc-utils-bin = %{version}-%{release}
Requires: mmc-utils-man = %{version}-%{release}

%description
No detailed description available

%package bin
Summary: bin components for the mmc-utils package.
Group: Binaries

%description bin
bin components for the mmc-utils package.


%package man
Summary: man components for the mmc-utils package.
Group: Default

%description man
man components for the mmc-utils package.


%prep
%setup -q -n mmc-utils-73d6c59af8d1bcedf5de4aa1f5d5b7f765f545f5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571378869
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1571378869
rm -rf %{buildroot}
%make_install
## install_append content
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/man/man1
install mmc %{buildroot}/usr/bin/
install man/mmc.1 %{buildroot}/usr/share/man/man1/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mmc

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mmc.1
