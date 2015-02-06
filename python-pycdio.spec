%define srcname pycdio
Name:		python-pycdio
Version:	0.20
Release:	2
Summary:	A Python interface to the CD Input and Control library
Group:		Development/Python 
License:	GPLv3+
URL:		http://www.gnu.org/software/libcdio/
Source0:	ftp://ftp.gnu.org:21/pub/gnu/libcdio/pycdio-%{version}.tar.gz

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

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*
%doc README.txt


%changelog
* Thu Oct 27 2011 Götz Waschk <waschk@mandriva.org> 0.17-2mdv2012.0
+ Revision: 707551
- rebuild for new libcdio

* Wed May 11 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.17-1
+ Revision: 673578
- new version 0.17
- remove definition of buildroot
- remove clean at %%install

* Thu Nov 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.16-1mdv2011.0
+ Revision: 465315
- Update to new version 0.16
- Remove patch integrated upstream

* Sat Sep 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15-1mdv2010.0
+ Revision: 449616
- Create package based on Fedora package
- create python-pycdio



