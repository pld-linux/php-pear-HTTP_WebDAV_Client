%define		status		stable
%define		pearname	HTTP_WebDAV_Client
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - WebDAV stream wrapper class
Summary(pl.UTF-8):	%{pearname} - wrapper dla strumienia WebDAV
Name:		php-pear-%{pearname}
Version:	1.0.2
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	b5fd549a41d2f6ba06cb7010c9f15fab
URL:		http://pear.php.net/package/HTTP_WebDAV_Client/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 4.3
Requires:	php-pear >= 4:1.0-9.2
Requires:	php-pear-HTTP_Request >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC2518 compliant stream wrapper that allows to use WebDAV server
resources like a regular file system from within PHP.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Zgodny z RFC2518 wrapper dla strumieni umożliwiający obsługę zasobów
serwera WebDAV tak jak gdyby to był zwykły plik.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/HTTP_WebDAV_Client/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTTP/WebDAV/*.php
%{php_pear_dir}/HTTP/WebDAV/Client
%{php_pear_dir}/HTTP/WebDAV/Tools/*
