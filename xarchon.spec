%define name xarchon
%define version 0.50
%define release %mkrel 14

Name: %{name}
Summary: X ARCHON is a strange game of chess
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Patch0:	xarchon-fonts.patch.bz2
Patch1: xarchon-0.50-gcc34.patch.bz2
Patch2: xarchon-gcc-fix.patch
Group: Games/Boards
URL: http://xarchon.seul.org/
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
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

(cd $RPM_BUILD_ROOT
mkdir -p ./usr/lib/menu
cat > ./usr/lib/menu/%{name} <<EOF
?package(%{name}): \
command="/usr/games/xarchon" \
title="Xarchon" \
longtitle="Clone of ARCHON game" \
icon="boards_section.png" \
needs="x11" \
section="More applications/Games/Boards" \
xdg="true"
EOF
)

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=%{title}
Comment=Clone of ARCHON game
Exec=%{_bindir}/%{name} 
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Boards
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
%_menudir/*
%{_datadir}/applications/mandriva-%{name}.desktop
