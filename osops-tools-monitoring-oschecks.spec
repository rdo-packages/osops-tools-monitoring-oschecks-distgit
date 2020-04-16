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
Obsoletes:      osops-tools-monitoring-oschecks < %{version}-%{release}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  git
BuildRequires:  python3-setuptools
BuildRequires:  openstack-macros
BuildRequires:  /usr/bin/pathfix.py
Requires: python3-psutil >= 1.2.1
Requires: python3-ceilometerclient
Requires: python3-cinderclient
Requires: python3-glanceclient
Requires: python3-keystoneclient
Requires: python3-neutronclient
Requires: python3-novaclient
Requires: python3-openstackclient >= 3.12.0
Requires: python3-six >= 1.10.0

BuildArch: noarch

%description
%{summary}

%prep
%autosetup -v -n osops-tools-monitoring-oschecks-%{upstream_version}/monitoring-for-openstack -S git
%py_req_cleanup

rm -rf monitoring_for_openstack.egg-info


%build
%{py3_build}

%install
%{py3_install}
find %{buildroot}%{python3_sitelib}/oschecks/*.py -not -name '__init__.py' -exec chmod +x {} \;

pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitelib}/oschecks/

%files
%{_libexecdir}/openstack-monitoring/checks/oschecks-*
%{python3_sitelib}/oschecks
%{python3_sitelib}/monitoring_for_openstack*

%changelog
