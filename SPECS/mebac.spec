%define _topdir %(pwd)

Name:      mebac
Version:   1.0
Release:   9
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
* Wed Oct 31 2018 Mladen Sekara <mladen.sekara@emefes.com> 1.0-9
- Added support for multilevel source directory.

* Thu May 25 2017 Mladen Sekara <mladen.sekara@emefes.com> 1.0-8
- Added brackets around each var for consistency.

* Sun May 21 2017 Mladen Sekara <mladen.sekara@emefes.com> 1.0-7
- Simplified the date extraction and changed logging to optional.

* Mon May 17 2017 Mladen Sekara <mladen.sekara@emefes.com> 1.0-6
- Fixed issue with date detection

* Mon May 15 2017 Mladen Sekara <mladen.sekara@emefes.com> 1.0-5
- Added Date/Time Original to complement createDate and GPSDateStamp

* Wed Nov 03 2016 Mladen Sekara <mladen.sekara@emefes.com> 1.0-4
- If createDate is empty, source date from GPS

* Thu Oct 06 2016 Mladen Sekara <mladen.sekara@emefes.com> 1.0-3
- Added double quotes around $pic.

* Thu Jun 05 2014 Mladen Sekara <mladen.sekara@emefes.com> 1.0-2
- Added copy check.

* Fri Apr 04 2014 Mladen Sekara <mladen.sekara@emefes.com> 1.0-1
- Initial release.
