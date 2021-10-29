#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x579C160D4C9E23E8 (jelmer@fsfe.org)
#
Name     : python-subunit
Version  : 1.4.0
Release  : 63
URL      : https://files.pythonhosted.org/packages/e4/57/c9d1130411945fee7de701366f238a6568d4e3a5ef8dda94cbdc63937c8d/python-subunit-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/57/c9d1130411945fee7de701366f238a6568d4e3a5ef8dda94cbdc63937c8d/python-subunit-1.4.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/e4/57/c9d1130411945fee7de701366f238a6568d4e3a5ef8dda94cbdc63937c8d/python-subunit-1.4.0.tar.gz.asc
Summary  : Python implementation of subunit test streaming protocol
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: python-subunit-bin = %{version}-%{release}
Requires: python-subunit-license = %{version}-%{release}
Requires: python-subunit-python = %{version}-%{release}
Requires: python-subunit-python3 = %{version}-%{release}
Requires: extras
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : extras
BuildRequires : testtools

%description
A simple package to deal with ISO 8601 date time formats.
ISO 8601 defines a neutral, unambiguous date string format, which also
has the property of sorting naturally.

%package bin
Summary: bin components for the python-subunit package.
Group: Binaries
Requires: python-subunit-license = %{version}-%{release}

%description bin
bin components for the python-subunit package.


%package license
Summary: license components for the python-subunit package.
Group: Default

%description license
license components for the python-subunit package.


%package python
Summary: python components for the python-subunit package.
Group: Default
Requires: python-subunit-python3 = %{version}-%{release}

%description python
python components for the python-subunit package.


%package python3
Summary: python3 components for the python-subunit package.
Group: Default
Requires: python3-core
Provides: pypi(python_subunit)
Requires: pypi(extras)
Requires: pypi(testtools)

%description python3
python3 components for the python-subunit package.


%prep
%setup -q -n python-subunit-1.4.0
cd %{_builddir}/python-subunit-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1596051733
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-subunit
cp %{_builddir}/python-subunit-1.4.0/Apache-2.0 %{buildroot}/usr/share/package-licenses/python-subunit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/python-subunit-1.4.0/python/iso8601/LICENSE %{buildroot}/usr/share/package-licenses/python-subunit/e7da7157e8398cab6dffd7f689d3f1dc7676f871
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/bin/subunit2disk

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/subunit-1to2
/usr/bin/subunit-2to1
/usr/bin/subunit-filter
/usr/bin/subunit-ls
/usr/bin/subunit-notify
/usr/bin/subunit-output
/usr/bin/subunit-stats
/usr/bin/subunit-tags
/usr/bin/subunit2csv
/usr/bin/subunit2gtk
/usr/bin/subunit2junitxml
/usr/bin/subunit2pyunit
/usr/bin/tap2subunit

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-subunit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/python-subunit/e7da7157e8398cab6dffd7f689d3f1dc7676f871

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
