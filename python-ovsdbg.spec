%global pkgname ovsdbg
%global pkgversion 0.0.13
%global pkgrelease CROC1

Name:python-%{pkgname}
Version:%{pkgversion}
Release:%{pkgrelease}%{?dist}
Summary:OVS Debug contains scripts and libraries that help debug OVS and OVN

Group:          Development/Python
License:        ASL 2.0
URL:            https://github.com/amorenoz/ovs-dbg
Source0:        python-%{pkgname}-%{pkgversion}.tar.gz
BuildArch:      noarch


BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%global _description\
OVS Debug contains scripts and libraries that help debug OVS and OVN.\
Full documentation here: https://ovs-dbg.readthedocs.io/en/latest.\

%description %_description


%package -n python%{python3_pkgversion}-%{pkgname}
Summary: %summary
%description -n python%{python3_pkgversion}-%{pkgname} %_description


%prep
%setup -c


%build
%{py3_build}


%install
%{py3_install}


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.md
%{_prefix}/etc/*
%{_prefix}/extras/*
%{_bindir}/*
%{python3_sitelib}/*


%changelog
* Thu Dec 30 2021 Evgenii Kovalev <evgkovalev@croc.ru>
- Build rpm package ovs-dbg.
