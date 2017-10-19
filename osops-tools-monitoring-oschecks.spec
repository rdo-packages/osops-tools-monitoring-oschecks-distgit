%{!?upstream_version: %global upstream_version %{commit}}

%global commit          62160d10683023c8c9d96f616223d8def88b870d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git

Name:           osops-tools-monitoring-oschecks
Version:        0.1
# Latest build from Opstool SIG NVR:
# osops-tools-monitoring-oschecks-0.1-0.8.23ee1b5git.el7
Release:        0.9%{?alphatag}%{?dist}
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
%autosetup -v -n osops-tools-monitoring-%{upstream_version}/monitoring-for-openstack -S git
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
* Thu Oct 19 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.1-0.9.62160d106git
- Initial Pike release (62160d10683023c8c9d96f616223d8def88b870d)
