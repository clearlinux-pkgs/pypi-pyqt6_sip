#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyqt6_sip
Version  : 13.4.0
Release  : 26
URL      : https://files.pythonhosted.org/packages/39/fc/f889254efda90418e367df28da9d14ac64ca19a9d93f44355d21ac562b0f/PyQt6_sip-13.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/39/fc/f889254efda90418e367df28da9d14ac64ca19a9d93f44355d21ac562b0f/PyQt6_sip-13.4.0.tar.gz
Summary  : The sip module support for PyQt6
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: pypi-pyqt6_sip-filemap = %{version}-%{release}
Requires: pypi-pyqt6_sip-lib = %{version}-%{release}
Requires: pypi-pyqt6_sip-license = %{version}-%{release}
Requires: pypi-pyqt6_sip-python = %{version}-%{release}
Requires: pypi-pyqt6_sip-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
sip Extension Module
====================
The sip extension module provides support for the PyQt6
package.

%package filemap
Summary: filemap components for the pypi-pyqt6_sip package.
Group: Default

%description filemap
filemap components for the pypi-pyqt6_sip package.


%package lib
Summary: lib components for the pypi-pyqt6_sip package.
Group: Libraries
Requires: pypi-pyqt6_sip-license = %{version}-%{release}
Requires: pypi-pyqt6_sip-filemap = %{version}-%{release}

%description lib
lib components for the pypi-pyqt6_sip package.


%package license
Summary: license components for the pypi-pyqt6_sip package.
Group: Default

%description license
license components for the pypi-pyqt6_sip package.


%package python
Summary: python components for the pypi-pyqt6_sip package.
Group: Default
Requires: pypi-pyqt6_sip-python3 = %{version}-%{release}

%description python
python components for the pypi-pyqt6_sip package.


%package python3
Summary: python3 components for the pypi-pyqt6_sip package.
Group: Default
Requires: pypi-pyqt6_sip-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(pyqt6_sip)

%description python3
python3 components for the pypi-pyqt6_sip package.


%prep
%setup -q -n PyQt6_sip-13.4.0
cd %{_builddir}/PyQt6_sip-13.4.0
pushd ..
cp -a PyQt6_sip-13.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665605178
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyqt6_sip
cp %{_builddir}/PyQt6_sip-%{version}/LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/pypi-pyqt6_sip/2136dbc93e95a70deae070e44ff6b2702ec1599c || :
cp %{_builddir}/PyQt6_sip-%{version}/LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/pypi-pyqt6_sip/34e9b06e7f12eaed676f57481de931ec91c6ce0a || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-pyqt6_sip

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyqt6_sip/2136dbc93e95a70deae070e44ff6b2702ec1599c
/usr/share/package-licenses/pypi-pyqt6_sip/34e9b06e7f12eaed676f57481de931ec91c6ce0a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
