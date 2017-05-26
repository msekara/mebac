%define _topdir %(pwd)

Name:      mebac
Version:   1.0
Release:   0
Summary:   Media Backup
License:   GPL
Group:     Multimedia
Buildarch: noarch
Requires:  perl-Image-ExifTool
Source0:   mebac
Source1:   mebac-config
Source2:   mebac.conf

%description
Media Backup.

%prep
rm -rf %{buildroot}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/var/lib/%{name}
cp -r %{SOURCE0} %{SOURCE1} %{buildroot}/%{_bindir}
cp -r %{SOURCE2} %{buildroot}/var/lib/%{name}/

%files
%defattr(-,root,root)
/usr/bin/mebac
/usr/bin/mebac-config
%config /var/lib/%{name}/mebac.conf

%changelog
* Thu Feb 26 2015 Mladen Sekara <mladen.sekara@emefes.com> 1.0-0
- Initial release.
