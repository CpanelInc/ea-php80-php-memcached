OBS_PROJECT := EA4
OBS_PACKAGE := ea-php80-php-memcached
DISABLE_BUILD := arch=i586 repository=CentOS_6.5_standard repository=Almalinux_10 repository=xUbuntu_22.04 repository=xUbuntu_24.04
include $(EATOOLS_BUILD_DIR)obs.mk
