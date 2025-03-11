#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	A simple mock implementation of python-ldap
Summary(pl.UTF-8):	Prosta implementacja atrapy python-ldap
Name:		python-mockldap
Version:	0.3.0.post1
Release:	3
License:	CC0 v1.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/mockldap/
Source0:	https://files.pythonhosted.org/packages/source/m/mockldap/mockldap-%{version}.tar.gz
# Source0-md5:	d48dc593c7afe9c7a97b561b869501b0
Patch0:		mockldap-requires.patch
URL:		https://pypi.org/project/mockldap/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:0.6c11
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools >= 1:0.6c11
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple mock implementation of python-ldap.

%description -l pl.UTF-8
Prosta implementacja atrapy python-ldap.

%package -n python3-mockldap
Summary:	A simple mock implementation of python-ldap
Summary(pl.UTF-8):	Prosta implementacja atrapy python-ldap
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-mockldap
A simple mock implementation of python-ldap.

%description -n python3-mockldap -l pl.UTF-8
Prosta implementacja atrapy python-ldap.

%package apidocs
Summary:	API documentation for Python mockldap module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona mockldap
Group:		Documentation

%description apidocs
API documentation for Python mockldap module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona mockldap.

%prep
%setup -q -n mockldap-%{version}
%patch -P 0 -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE.rst README.rst
%{py_sitescriptdir}/mockldap
%{py_sitescriptdir}/mockldap-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-mockldap
%defattr(644,root,root,755)
%doc CHANGES LICENSE.rst README.rst
%{py3_sitescriptdir}/mockldap
%{py3_sitescriptdir}/mockldap-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_modules,_static,*.html,*.js}
%endif
