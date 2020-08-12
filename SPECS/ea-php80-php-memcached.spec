%global scl_version ea-php80
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcached
Version: 3.1.5
Summary: php-memcached extension for %{scl_version}
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
License: MIT
Group: Programming/Languages
URL: https://pecl.php.net/package/memcached
Source: memcached-3.1.5.tgz
Source1: memcached.ini

# should be no requires for building this package
#Requires: memcached
Requires: ea-libmemcached
BuildRequires: cyrus-sasl-devel
BuildRequires: autotools-latest-autoconf
BuildRequires: ea-libmemcached ea-libmemcached-devel
BuildRequires: %{scl_version} %{scl_version}-php-cli
Requires: %{scl_version}-php-common
Requires: %{scl_version}-php-cli

%description
This is the PECL memcached extension, using the libmemcached library to connect
to memcached servers.


%prep
%setup -n memcached-%{version}

%build

%if 0%{rhel} < 7
export PHP_AUTOCONF=/usr/bin/autoconf
%endif

scl enable %{scl_version} phpize
scl enable %{scl_version} './configure --with-libmemcached-dir=/opt/cpanel/libmemcached --with-libdir=lib64'
make

%install
make install INSTALL_ROOT=%{buildroot}
install -m 755 -d %{buildroot}/%{ext_prefix}/%{conf_dir}
install -m 644 %{SOURCE1} %{buildroot}/%{ext_prefix}/%{conf_dir}/

%clean
%{__rm} -rf %{buildroot}

%files
/%{ext_prefix}/%{ext_dir}/memcached.so
%config /%{ext_prefix}/%{conf_dir}/memcached.ini

%changelog
* Tue Aug 11 2020 Julian Brown <julian.brown@cpanel.net> - 3.1.3-1
- Created ea-php80-php-memcached

