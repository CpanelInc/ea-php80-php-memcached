%global scl_version ea-php80
%global ext_prefix opt/cpanel/%{scl_version}/root
%global ext_dir usr/%{_lib}/php/modules
%global conf_dir etc/php.d

Name: %{scl_version}-php-memcached
Version: 3.3.0
Summary: php-memcached extension for %{scl_version}
%define release_prefix 2
Release: %{release_prefix}%{?dist}.cpanel
License: MIT
Group: Programming/Languages
URL: https://pecl.php.net/package/memcached
Source: v%{version}.tar.gz
Source1: memcached.ini

# should be no requires for building this package
#Requires: memcached
Requires: ea-libmemcached
BuildRequires: cyrus-sasl-devel
BuildRequires: autotools-latest-autoconf
BuildRequires: ea-libmemcached ea-libmemcached-devel
BuildRequires: %{scl_version}
Requires: %{scl_version}-php-common
Requires: %{scl_version}-php-cli

%description
This is the PECL memcached extension, using the libmemcached library to connect
to memcached servers.


%prep
%setup -n php-memcached-%{version}

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
* Wed Apr 02 2025 Julian Brown <julian.brown@webpros.com> - 3.3.0-2
- ZC-12156: Automate creation of *.conffiles

* Tue Oct 29 2024 Cory McIntire <cory@cpanel.net> - 3.3.0-1
- EA-12493: Update ea-php80-php-memcached from v3.2.0 to v3.3.0

* Mon Oct 28 2024 Julian Brown <julian.brown@cpanel.net> - 3.2.0-4
- ZC-12246: Correct conffiles for Ubuntu

* Thu Sep 21 2023 Dan Muey <dan@cpanel.net> - 3.2.0-3
- ZC-11194: Remove unnecessary `BuildRequires` of php-cli

* Tue May 02 2023 Julian Brown <julian.brown@cpanel.net> - 3.2.0-2
- ZC-10320: Do not build on Ubuntu 22

* Wed Apr 26 2023 Travis Holloway <t.holloway@cpanel.net> - 3.2.0-1
- EA-11384: Update ea-php80-php-memcached from v3.1.5 to v3.2.0

* Tue Dec 28 2021 Dan Muey <dan@cpanel.net> - 3.1.5-3
- ZC-9589: Update DISABLE_BUILD to match OBS

* Tue Jul 13 2021 Julian Brown <julian.brown@webpros.com> - 3.1.5-2
- Rename the tarball

* Tue Aug 11 2020 Julian Brown <julian.brown@cpanel.net> - 3.1.3-1
- Created ea-php80-php-memcached

