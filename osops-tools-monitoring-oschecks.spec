# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
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

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  git
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  openstack-macros
Requires: python%{pyver}-psutil >= 1.2.1
Requires: python%{pyver}-ceilometerclient
Requires: python%{pyver}-cinderclient
Requires: python%{pyver}-glanceclient
Requires: python%{pyver}-keystoneclient
Requires: python%{pyver}-neutronclient
Requires: python%{pyver}-novaclient
Requires: python%{pyver}-openstackclient >= 3.12.0
Requires: python%{pyver}-six >= 1.10.0


BuildArch: noarch

%description
%{summary}

%prep
%autosetup -v -n osops-tools-monitoring-oschecks-%{upstream_version}/monitoring-for-openstack -S git
%py_req_cleanup

rm -rf monitoring_for_openstack.egg-info


%build
%{pyver_build}

%install
%{pyver_install}
find %{buildroot}%{pyver_sitelib}/oschecks/*.py -not -name '__init__.py' -exec chmod +x {} \;

%files
%{_libexecdir}/openstack-monitoring/checks/oschecks-*
%{pyver_sitelib}/oschecks
%{pyver_sitelib}/monitoring_for_openstack*

%changelog
