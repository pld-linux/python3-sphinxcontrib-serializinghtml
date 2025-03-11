#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs "serialized" HTML files
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące "zserializowane" pliki HTML
Name:		python3-sphinxcontrib-serializinghtml
Version:	2.0.0
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-serializinghtml/
Source0:	https://pypi.debian.net/sphinxcontrib-serializinghtml/sphinxcontrib_serializinghtml-%{version}.tar.gz
# Source0-md5:	b536ce248d5ca134a30018692a17c6ca
URL:		https://pypi.org/project/sphinxcontrib-serializinghtml/
BuildRequires:	python3-build
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-installer
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs
"serialized" HTML files (json and pickle).

%description -l pl.UTF-8
sphinxcontrib-serializinghtml to rozszerzenie Sphinksa, zapisujące
"zserializowane" pliki HTML (w oparciu o json i pickle).

%prep
%setup -q -n sphinxcontrib_serializinghtml-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENCE.rst README.rst
%{py3_sitescriptdir}/sphinxcontrib/serializinghtml
%{py3_sitescriptdir}/sphinxcontrib_serializinghtml-%{version}.dist-info
