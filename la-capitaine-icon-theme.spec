%global commit0 cd4748301fde6c9cd74b68284fa42c7f159eceb5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:		la-capitaine-icon-theme
Version:	0.5.0
Release:	1.git%{shortcommit0}%{?dist}
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

* Tue Sep 26 2017 David Vásquez <davidva AT tutanota DOT com> - 0.5.0-1.gitcd47483
- Updated to 0.5.0-1.gitcd47483

* Fri Aug 18 2017 David Vásquez <davidva AT tutanota DOT com> - 0.4.0-1.git635f2e8
- Initial build
