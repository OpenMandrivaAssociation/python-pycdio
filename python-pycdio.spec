%define srcname pycdio
Name:		python-pycdio
Version:	0.17
Release:	%mkrel 2
Summary:	A Python interface to the CD Input and Control library
Group:		Development/Python 
License:	GPLv3+
URL:		http://www.gnu.org/software/libcdio/
Source0:	ftp://ftp.gnu.org/pub/gnu/libcdio/%{srcname}-%{version}.tar.gz

BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	libcdio-devel
BuildRequires:	swig

%description
The pycdio (and libcdio) libraries encapsulate CD-ROM reading and
control. Python programs wishing to be oblivious of the OS- and
device-dependent properties of a CD-ROM can use this library.

%prep
%setup -q -n %{srcname}-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root %{buildroot}
chmod 755 %{buildroot}/%{py_platsitedir}/*.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*
%doc README.txt
