#
# Conditional build:
%bcond_with	tests	# unit tests (failing?)

Summary:	Sphinx extension which outputs "serialized" HTML files
Summary(pl.UTF-8):	Rozszerzenie Sphinksa zapisujące "zserializowane" pliki HTML
Name:		python3-sphinxcontrib-serializinghtml
Version:	1.1.5
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-serializinghtml/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-serializinghtml/sphinxcontrib-serializinghtml-%{version}.tar.gz
# Source0-md5:	d99d2edc7b26988dc5fa92163857bfbf
URL:		https://pypi.org/project/sphinxcontrib-serializinghtml/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
%setup -q -n sphinxcontrib-serializinghtml-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/serializinghtml
%{py3_sitescriptdir}/sphinxcontrib_serializinghtml-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_serializinghtml-%{version}-py*-nspkg.pth
