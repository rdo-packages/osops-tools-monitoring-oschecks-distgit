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

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  git
BuildRequires:  python2-setuptools
BuildRequires:  openstack-macros
Requires: python2-psutil >= 1.2.1
Requires: python2-ceilometerclient
Requires: python2-cinderclient
Requires: python2-glanceclient
Requires: python2-keystoneclient
Requires: python2-neutronclient
Requires: python2-novaclient
Requires: python2-openstackclient >= 3.12.0
Requires: python2-six >= 1.10.0


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
