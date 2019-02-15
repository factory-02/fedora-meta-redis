Name:                           meta-redis
Version:                        1.0.1
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
%{__mkdir} -p %{buildroot}%{_sysconfdir}
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/redis.local.conf

%files
%config %{_sysconfdir}/redis.local.conf

%changelog
* Fri Feb 15 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.1-1
- New version: 1.0.1.

* Wed Feb 13 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
