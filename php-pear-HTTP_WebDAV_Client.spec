%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	WebDAV
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Client

Summary:	%{_pearname} - WebDAV stream wrapper class
Summary(pl):	%{_pearname} - wrapper dla strumienia WebDAV
Name:		php-pear-%{_pearname}
Version:	0.9.7
Release:	2
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	cbeaaaf935de86fc036d51fa29e437bc
URL:		http://pear.php.net/package/HTTP_WebDAV_Client/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC2518 compliant stream wrapper that allows to use WebDAV server
resources like a regular file system from within PHP.

In PEAR status of this package is: %{_status}.

%description -l pl
Zgodny z RFC2518 wrapper dla strumieni umo�liwiaj�cy obs�ug� zasob�w
serwera WebDAV tak jak gdyby to by� zwyk�y plik.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Client
%{php_pear_dir}/%{_class}/%{_subclass}/Tools
