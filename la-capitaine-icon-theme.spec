%global commit0 d3d93f31606ba0c935576cfa5dffd77289b3cbd8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:		la-capitaine-icon-theme
Version:	0.6.2
Release:	1%{gver}%{?dist}
Summary:	An icon pack designed to integrate with most desktop environments

Source:		https://github.com/keeferrourke/la-capitaine-icon-theme/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

Group:		User Interface/Desktops
License:	GPLv3
URL:		https://krourke.org/projects/art/la-capitaine-icon-theme

BuildArch:	noarch
Requires:	filesystem
Requires:	hicolor-icon-theme

%description
La Capitaine is an icon pack, designed to integrate with most desktop 
environments. The set of icons takes inspiration from the latest 
iterations of macOS and Google's Material Design.

%prep
%autosetup -n %{name}-%{commit0}

%build
find -type f -executable -exec chmod -x {} \;

%install
install -d %{buildroot}%{_datadir}/icons/%{name}/
cp -rf * %{buildroot}%{_datadir}/icons/%{name}/

%post
/bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/%{name} &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%files
%license LICENSE
%doc README.md COPYING Thanks.md
%{_datadir}/icons/%{name}/

%changelog

* Sat May 22 2021 David Va <davidva AT tuta DOT io> 0.6.2-1.git36b9768
- Updated to current commit

* Sun Apr 26 2020 David Va <davidva AT tuta DOT io> 0.6.1-2.git36b9768
- Updated to current commit

* Thu Nov 15 2018 David Va <davidva AT tuta DOT io> 0.6.1-1.git1717f4d
- Updated to 0.6.1-1.git1717f4d

* Wed Aug 01 2018 David Va <davidva AT tuta DOT io> 0.6.0-1.gita3ac190
- Updated to 0.6.0-1.gita3ac190

* Wed Jun 27 2018 David Vásquez <davidva AT tutanota DOT com> - 0.5.0-5.gitfad3f22
- Updated to current commit

* Thu Mar 15 2018 David Vásquez <davidva AT tutanota DOT com> - 0.5.0-4.gita733e77
- Updated to current commit 

* Wed Nov 22 2017 David Vásquez <davidva AT tutanota DOT com> - 0.5.0-3.git6540a5f
- Updated to 0.5.0-3.git6540a5f

* Thu Oct 26 2017 David Vásquez <davidva AT tutanota DOT com> - 0.5.0-2.git1d21a65
- Updated to 0.5.0-2.git1d21a65

* Tue Sep 26 2017 David Vásquez <davidva AT tutanota DOT com> - 0.5.0-1.gitcd47483
- Updated to 0.5.0-1.gitcd47483

* Fri Aug 18 2017 David Vásquez <davidva AT tutanota DOT com> - 0.4.0-1.git635f2e8
- Initial build
