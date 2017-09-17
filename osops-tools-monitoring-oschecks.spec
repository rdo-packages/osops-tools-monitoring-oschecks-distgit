%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global commit          23ee1b59533329b24f4b53a5eb49ba1a027de8ab
%global shortcommit     %(c=%{commit}; echo ${c:0:7})


Name:           osops-tools-monitoring-oschecks
Version:        XXX
Release:        XXX
Summary:        Scripts used to monitor an Openstack Installation

License:        ASL 2.0
URL:            https://github.com/openstack/osops-tools-monitoring
Source0:        https://github.com/openstack/osops-tools-monitoring/archive/%{commit}/osops-tools-monitoring-%{shortcommit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  git
BuildRequires:  python-setuptools
BuildRequires:  openstack-macros
Requires: python-psutil >= 1.2.1
Requires: python-ceilometerclient
Requires: python-cinderclient
Requires: python-glanceclient
Requires: python-keystoneclient
Requires: python-neutronclient
Requires: python-novaclient
Requires: python-openstackclient >= 3.2.0
Requires: python-six >= 1.9.0


BuildArch: noarch

%description
%{summary}

%prep
%autosetup -v -n osops-tools-monitoring-oschecks-%{upstream_version}/monitoring-for-openstack -S git
%py_req_cleanup

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
