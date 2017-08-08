%global commit          23ee1b59533329b24f4b53a5eb49ba1a027de8ab
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           osops-tools-monitoring-oschecks
Version:        XXX
Release:        XXX
Summary:        Scripts used to monitor an Openstack Installation

License:        ASL 2.0
URL:            https://github.com/openstack/osops-tools-monitoring
Source0:        https://github.com/openstack/osops-tools-monitoring/archive/%{commit}/osops-tools-monitoring-%{shortcommit}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  git
BuildRequires:  python-setuptools
Requires: python-psutil
Requires: python-ceilometerclient
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-neutronclient
Requires: python-novaclient
Requires: python-openstackclient
Requires: python-six


BuildArch: noarch

%description
%{summary}

%prep
%autosetup -n osops-tools-monitoring-%{commit}/monitoring-for-openstack -S git
rm requirements.txt test-requirements.txt

rm -rf monitoring_for_openstack.egg-info


%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
find %{buildroot}%{python2_sitelib}/oschecks/*.py -not -name '__init__.py' -exec chmod +x {} \;

%files
%{_libexecdir}/openstack-monitoring/checks/oschecks-*
%{python2_sitelib}/oschecks
%{python2_sitelib}/monitoring_for_openstack*

%changelog
