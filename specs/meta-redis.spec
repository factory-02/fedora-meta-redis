Name:                           meta-redis
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install and configure Redis
License:                        GPLv3

Source10:                       redis.local.conf

Requires:                       redis

%description
META-package for install and configure Redis.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/redis.local.conf

%files
%config %{_sysconfdir}/redis.local.conf

%changelog
* Wed Feb 13 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
