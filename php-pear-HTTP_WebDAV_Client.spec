%include	/usr/lib/rpm/macros.php
%define         _class          HTTP
%define         _subclass       WebDAV
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}_Client

Summary:	%{_pearname} - WebDAV stream wrapper class
Summary(pl):	%{_pearname} - Wrapper dla strumienia WebDAV
Name:		php-pear-%{_pearname}
Version:	0.9.6
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d76666313be0a632746fcff382cb4b9a
URL:		http://pear.php.net/package/HTTP_WebDAV_Client/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC2518 compliant stream wrapper that allows to use WebDAV server
resources like a regular file system from within PHP.

This class has in PEAR status: %{_status}.

%description -l pl
Zgodny z RFC2518 wrapper dla strumieni umo¿liwiaj±cy obs³ugê zasobów
serwera WebDAV tak jak gdyby to by³ zwyk³y plik.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/{Client,Tools}

install %{_pearname}-%{version}/*.php 		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Client/*.php 	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Client
install %{_pearname}-%{version}/Tools/*.php 	$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Tools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Client
%{php_pear_dir}/%{_class}/%{_subclass}/Tools
