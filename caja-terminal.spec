%define debug_package %{nil}

Summary:	An embedded terminal in caja
Name:		caja-terminal
Version:	0.10
Release:	1
Group:		File tools
License:	GPLv3+
URL:		https://github.com/yselkowitz/%{name}
Source0:	https://github.com/yselkowitz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python2)

Requires:	python2-caja
Requires:	python2-gobject
Requires:	python2-xdg
Requires:	vte2.91

%description
Caja Terminal is an embedded terminal in caja, the MATE's file browser.
It is always open in the current folder, and follows the navigation.

%files -f %{name}.lang
%doc COPYING AUTHORS README
%{_datadir}/%{name}/
%{_datadir}/caja-python/extensions/%{name}.*

#---------------------------------------------------------------------------
%prep
%setup -q

# force to python2
sed -i -e 's|#!/usr/bin/python|#!/usr/bin/env python2|' code/caja-terminal.py

%build
# nothin to do here

%install
%makeinstall_std

bash install.sh --package %{buildroot}

# locales
%find_lang %{name} --with-gnome --all-name

