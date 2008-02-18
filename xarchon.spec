%define name xarchon
%define version 0.50
%define release %mkrel 16

Name: %{name}
Summary: Strange game of chess
Version: %{version}
Release: %{release}
Source: http://xarchon.seul.org/%{name}-%{version}.tar.bz2
Patch0:	xarchon-fonts.patch
Patch1: xarchon-0.50-gcc34.patch
Patch2: xarchon-gcc-fix.patch
Group: Games/Boards
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xarchon.seul.org/
License: GPLv2+
BuildRequires: esound-devel
BuildRequires: gtk-devel
BuildRequires: xpm-devel

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
 
%post
%{update_menus}
 
%postun
%{clean_menus}
                   
%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr (-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog
%_gamesbindir/*
%_mandir/man6/*
%dir %_gamesdatadir/xarchon/
%_gamesdatadir/xarchon/*
%{_datadir}/applications/mandriva-%{name}.desktop
