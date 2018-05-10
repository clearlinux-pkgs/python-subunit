#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : python-subunit
Version  : 1.2.0
Release  : 32
URL      : http://pypi.debian.net/python-subunit/python-subunit-1.2.0.tar.gz
Source0  : http://pypi.debian.net/python-subunit/python-subunit-1.2.0.tar.gz
Source99 : http://pypi.debian.net/python-subunit/python-subunit-1.2.0.tar.gz.asc
Summary  : Python implementation of subunit test streaming protocol
Group    : Development/Tools
License  : Apache-2.0
Requires: python-subunit-bin
Requires: python-subunit-python3
Requires: python-subunit-python
Requires: docutils
Requires: extras
Requires: fixtures
Requires: hypothesis
Requires: testscenarios
Requires: testtools
BuildRequires : extras
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : testtools

%description
subunit: A streaming protocol for test results
Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
license at the users choice. A copy of both licenses are available in the
project source as Apache-2.0 and BSD. You may not use this file except in
compliance with one of these two licences.

%package bin
Summary: bin components for the python-subunit package.
Group: Binaries

%description bin
bin components for the python-subunit package.


%package python
Summary: python components for the python-subunit package.
Group: Default
Requires: python-subunit-python3

%description python
python components for the python-subunit package.


%package python3
Summary: python3 components for the python-subunit package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-subunit package.


%prep
%setup -q -n python-subunit-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523299791
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
