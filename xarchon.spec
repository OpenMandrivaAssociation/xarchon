%define name xarchon
%define version 0.50
%define release %mkrel 20

Name: %{name}
Summary: Strange game of chess
Version: %{version}
Release: %{release}
Source: http://xarchon.seul.org/%{name}-%{version}.tar.bz2
Patch0:	xarchon-fonts.patch
Patch1: xarchon-0.50-gcc34.patch
Patch2: xarchon-gcc-fix.patch
Patch3: xarchon-0.50-gcc43.patch
Group: Games/Boards
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xarchon.seul.org/
License: GPLv2+
BuildRequires: esound-devel
BuildRequires: gtk-devel
BuildRequires: xpm-devel
Buildrequires: imagemagick

%description 
X ARCHON is a clone of the golden oldie ARCHON game created by Freewall
Associates and distributed by Electronic Arts. ARCHON, in its simplest form,
resembles a strange game of chess. But no one ever said that Archon was a
simple game. When a piece is challenged a duel ensued between the two pieces
until one of the pieces is dead. Combine with spells and fantastic units, an
you have a very small taste of Archon.

%prep
%setup -q
%patch0 -p1
%patch1 -p0 -b .gcc34-fix
%patch2 -p0 -b .gcc-fix
%patch3 -p1 -b .gcc43

%build
%configure --bindir=%{_gamesbindir} \
           --datadir=%{_gamesdatadir} \
           --disable-rpath
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall bindir=$RPM_BUILD_ROOT%{_gamesbindir} datadir=$RPM_BUILD_ROOT%{_gamesdatadir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=XArchon
Comment=Clone of ARCHON game
Exec=%{_gamesbindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=BoardGame;Game;GTK;
EOF

mkdir -p %buildroot%_iconsdir
convert data/icon.xpm %buildroot%_iconsdir/%name.png
 
%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus}
%endif
                   
%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr (-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog
%_gamesbindir/*
%_mandir/man6/*
%dir %_gamesdatadir/xarchon/
%_gamesdatadir/xarchon/*
%_iconsdir/%name.png
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.50-20mdv2010.0
+ Revision: 445868
- rebuild

* Mon Apr 06 2009 Funda Wang <fundawang@mandriva.org> 0.50-19mdv2009.1
+ Revision: 364348
- add gcc 43 patch

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Feb 18 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.50-16mdv2008.1
+ Revision: 171181
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag

* Thu Feb 07 2008 Funda Wang <fundawang@mandriva.org> 0.50-15mdv2008.1
+ Revision: 163379
- bunzip patches

  + Thierry Vignaud <tvignaud@mandriva.com>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 0.50-14mdv2008.0
+ Revision: 23244
- path2: more gcc fix
- xdg menu
- Import xarchon



* Sun Jul 18 2004 Michael Scherer <misc@mandrake.org> 0.50-13mdk 
- rebuild for new gcc, patch 0

* Tue Dec 16 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.50-12mdk
- fix paths

* Thu Jul 31 2003 Götz Waschk <waschk@linux-mandrake.com> 0.50-11mdk
- add buildrequires

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.50-10mdk
- rebuild

* Thu Sep 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.50-9mdk
- patch0: fix call to missing fonts in board.c and field.c

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.50-8mdk
- rebuild

* Fri May 31 2002  Lenny Cartier <lenny@mandrakesoft.com> 0.50-7mdk
- rebuild against new libstdc++

* Tue Dec 25 2001 David BAUDENS <baudens@mandrakesoft.com> 0.50-6mdk
- Use standard icon for menu

* Fri Aug 24 2001 Etienne Faure <etienne@mandrakesoft.com> 0.50-5mdk
- rebuild

* Thu Feb 15 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.50-4mdk
- rebuild

* Wed Sep 20 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.50-3mdk
- fix install that was sooo crappy
- menu && bm && macros

* Thu May 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.50-2mdk
- fix group

* Mon Dec 06 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Upgrade to 0.50 version.

* Tue Oct 19 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Upgrade to 0.42 version.

* Thu Oct 07 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Little adaptations of the specfile

* Sun Sep 26 1999 Sean P. Kane <spkane@home.com>
- Created First Xarchon RPM

* Fri Aug 06 1999 Stefan Siegel <siegel@informatik.uni-kl.de>
- Added "config" tag for files containing /etc or /config
- Added compression for perl- and localized man-pages

* Sat Jun 26 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- create (more or less) generic spec file...
