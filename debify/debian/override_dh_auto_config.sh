#!/bin/bash

source debian/vars.sh

set -x

ls -ld /opt/cpanel/*
ls -ld /opt/cpanel/ea-php80/root/usr/bin/*
ls -ld /opt/cpanel/ea-php80/root/usr/bin/phpize
pwd
ls -ld *

cd memcached-*
/opt/cpanel/ea-php80/root/usr/bin/phpize

./configure \
    --with-php-config=/opt/cpanel/ea-php80/root/usr/bin/php-config \
    --with-libdir=lib64

make
cd ..

