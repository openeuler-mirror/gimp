Name:     gimp
Version:  2.10.6
Release:  3
Epoch:    2
Summary:  A versatile graphics manipulation package
License:  GPLv3+ and GPLv3 and LGPLv3+
URL:      http://www.gimp.org/

Source0:        http://download.gimp.org/pub/gimp/v2.10/gimp-2.10.6.tar.bz2
Patch1:         gimp-2.10.0-cm-system-monitor-profile-by-default.patch
Patch2:         gimp-2.10.0-external-help-browser.patch
Patch6000:      backport-CVE-2018-12713.patch

%global apiversion 2.0
%global textversion 20
%global allversion 2.10

BuildRequires:  alsa-lib-devel >= 1.0.0 libgudev1-devel >= 167 libgexiv2-devel >= 0.10.6 librsvg2-devel >= 2.40.6 libpng-devel >= 1.6.25 libtiff-devel
BuildRequires:  lcms2-devel >= 2.8 harfbuzz-devel >= 0.9.19 glib2-devel >= 2.54.2 gtk2-devel >= 2.24.10 gegl04-devel >= 0.4.6 gdk-pixbuf2-devel >= 2.30.8
BuildRequires:  atk-devel >= 2.2.0 babl-devel >= 0.1.56 cairo-devel >= 1.12.2 bzip2-devel fontconfig-devel >= 2.12.4 freetype-devel >= 2.1.7 libX11-devel
BuildRequires:  libgs-devel iso-codes-devel jasper-devel libjpeg-devel libmng-devel libwebp-devel >= 0.6.0 pango-devel >= 1.29.4 poppler-glib-devel >= 0.44.0
BuildRequires:  libwmf-devel >= 0.2.8 libmypaint-devel >= 1.3.0 mypaint-brushes-devel >= 1.3.0 OpenEXR-devel >= 1.6.1 openjpeg2-devel >= 2.1.0
BuildRequires:  poppler-data-devel >= 0.4.7 pycairo-devel >= 1.0.2 pygtk2-devel >= 2.10.4 pygobject2-devel python2-devel >= 2.5.0 xz-devel >= 5.0.0
BuildRequires:  perl >= 5.10.0 libappstream-glib gtk-doc >= 1.0 gegl04-tools libXpm-devel pkgconfig zlib-devel
BuildRequires:  libXmu-devel gettext >= 0.19 chrpath >= 0.13-5 intltool >= 0.40.1

Requires:       babl%{?_isa} >= 0.1.56 fontconfig >= 2.12.4 freetype >= 2.1.7 pango >= 1.29.4 xdg-utils gimp-libs%{?_isa} = 2:2.10.6-2.h1
Requires:       gegl04%{?_isa} >= 0.4.6 glib2 >= 2.54.0 gtk2 >= 2.24.10 pygtk2 >= 2.10.4 hicolor-icon-theme

Obsoletes:      gimp-help-browser < 2:2.10.6-2.h1
Conflicts:      gimp-help-browser < 2:2.10.6-2.h1
Obsoletes:      gimp-unstable < 2:2.10
Conflicts:      gimp-unstable < 2:2.10
Provides:       %{name}-libs%{?_isa} %{name}-libs
Obsoletes:      %{name}-libs
Obsoletes:      gimp-unstable-libs < 2:2.10
Conflicts:      gimp-unstable-libs < 2:2.10

%description
GIMP is a cross-platform image editor available for GNU/Linux, OS X, Windows and more operating systems.
It is free software, you can change its source code and distribute your changes.
Whether you are a graphic designer, photographer, illustrator, or scientist,
GIMP provides you with sophisticated tools to get your job done. You can further enhance
your productivity with GIMP thanks to many customization options and 3rd party plugins.


%package devel
Summary:        GIMP development kit
License:        LGPLv3+
Requires:       gimp-libs%{?_isa} = 2:2.10.6-2.h1 glib2-devel rpm >= 4.11.0
Requires:       gimp-devel-tools = 2:2.10.6-2.h1 gtk2-devel pkgconfig

Provides:       %{name}-devel-tools%{?_isa} %{name}-devel-tools
Obsoletes:      %{name}-devel-tools
Obsoletes:      gimp-unstable-devel < 2:2.10
Conflicts:      gimp-unstable-devel < 2:2.10
Obsoletes:      gimp-unstable-devel-tools < 2:2.10
Conflicts:      gimp-unstable-devel-tools < 2:2.10

%description devel
GIMP development kit


%package        help
Summary:        Including man files for gimp
Requires:       man

%description    help
This contains man files for the using of gimp.


%prep

%autosetup -n %{name}-%{version} -p1

%build


%configure \
    --enable-mp \
    --enable-python \
    --disable-static \
    --with-print \
    --with-poppler \
    --with-gudev --without-hal \
    --without-webkit \
    --with-lcms=lcms2 \
    --enable-gimp-console \
    --enable-default-binary=yes \
    --without-aa \
    --with-linux-input \
    --with-webp \
    --with-gvfs \
    --with-alsa \
    --with-dbus \
    --with-script-fu \
    --with-cairo-pdf \
    --without-appdata-test \
    --with-libtiff \
    --with-libjpeg \
    --with-libpng \
    --with-libmng \
    --with-libjasper \
    --with-libexif \
    --with-librsvg \
    --with-libxpm

%make_build


gimp_pc_extract_normalize() {
    PKG_CONFIG_PATH="$PWD" \
        pkg-config --variable="$1" gimp-2.0 | \
    sed \
        -e 's|^/usr/share/man|%{_mandir}|' \
        -e 's|^/usr/share/info|%{_infodir}|' \
        -e 's|^/usr/include|%{_includedir}|' \
        -e 's|^/usr/lib64|%{_libdir}|' \
        -e 's|^/usr/bin|%{_bindir}|' \
        -e 's|^/usr|%{_exec_prefix}|' \
        -e 's|^/var|%{_localstatedir}|' \
        -e 's|^/usr/share|%{_datadir}|' \
        -e 's|^/var/lib|%{_sharedstatedir}|' \
        -e 's|^/etc|%{_sysconfdir}|' \
        -e 's|^/usr/libexec|%{_libexecdir}|' \
        -e 's|^/usr/sbin|%{_sbindir}|' \
        -e 's|^/usr|%{_prefix}|'
}

_gimp_sysconfdir="$(gimp_pc_extract_normalize gimpsysconfdir)"
_gimp_localedir="$(gimp_pc_extract_normalize gimplocaledir)"
_gimp_datadir="$(gimp_pc_extract_normalize gimpdatadir)"
_gimp_libdir="$(gimp_pc_extract_normalize gimplibdir)"
_gimp_scriptdir="${_gimp_datadir}/scripts"
_gimp_plugindir="${_gimp_libdir}/plug-ins"

cat << EOF > macros.gimp
#RPM macros for GIMP

%%_gimp_sysconfdir ${_gimp_sysconfdir}
%%_gimp_localedir ${_gimp_localedir}
%%_gimp_datadir ${_gimp_datadir}
%%_gimp_libdir ${_gimp_libdir}
%%_gimp_scriptdir ${_gimp_scriptdir}
%%_gimp_plugindir ${_gimp_plugindir}
EOF



%install

%make_install
install -D -m0644 macros.gimp %{buildroot}%{_rpmconfigdir}/macros.d/macros.gimp
find %buildroot -type f -print0 | xargs -0 -L 20 chrpath --delete --keepgoing 2>/dev/null || :


%delete_la

find %{buildroot}%{_libdir}/gimp/%{apiversion}/* -type d | sed "s@^%{buildroot}@%%dir @g" >> gimp-plugin-files
find %{buildroot}%{_libdir}/gimp/%{apiversion} -type f | sed "s@^%{buildroot}@@g" | grep -v '\.a$' > gimp-plugin-files


grep "\.py$" gimp-plugin-files > gimp-plugin-files-py
for file in $(cat gimp-plugin-files-py); do
    for newfile in ${file}c ${file}o; do
        grep -F -q -x "$newfile" gimp-plugin-files || echo "$newfile"
    done
done >> gimp-plugin-files


%py_byte_compile %{__python2} %{buildroot}%{_libdir}/gimp/%{apiversion}




%find_lang gimp%{textversion}
%find_lang gimp%{textversion}-libgimp
%find_lang gimp%{textversion}-tips
%find_lang gimp%{textversion}-python
%find_lang gimp%{textversion}-std-plug-ins
%find_lang gimp%{textversion}-script-fu


cat gimp%{textversion}.lang \
    gimp%{textversion}-std-plug-ins.lang \
    gimp%{textversion}-script-fu.lang \
    gimp%{textversion}-libgimp.lang \
    gimp%{textversion}-tips.lang \
    gimp%{textversion}-python.lang > gimp-all.lang


cat gimp-plugin-files gimp-all.lang > gimp.files



ln -snf gimp-%{allversion} %{buildroot}%{_bindir}/gimp
ln -snf gimp-%{allversion}.1 %{buildroot}%{_mandir}/man1/gimp.1
ln -snf gimp-console-%{allversion} %{buildroot}/%{_bindir}/gimp-console
ln -snf gimptool-%{apiversion} %{buildroot}%{_bindir}/gimptool
ln -snf gimptool-%{apiversion}.1 %{buildroot}%{_mandir}/man1/gimptool.1
ln -snf gimprc-%{allversion}.5 %{buildroot}/%{_mandir}/man5/gimprc.5
ln -snf gimp-console-%{allversion}.1 %{buildroot}/%{_mandir}/man1/gimp-console.1


grep -E -rl '^#!\s*%{_bindir}/env\s+python' --include=\*.py "%{buildroot}" |
    while read file; do
        sed -r '1s,^#!\s*%{_bindir}/env\s+python,#!%{__python},' -i "$file"
    done



%check

make check %{?_smp_mflags}

%ldconfig_scriptlets


%files -f gimp.files
%license COPYING
%doc AUTHORS README
%doc docs/*.xcf*
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/2.0
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/2.0
%dir %{_libdir}/gimp/2.0/environ
%dir %{_libdir}/gimp/2.0/interpreters
%dir %{_libdir}/gimp/2.0/modules
%dir %{_libdir}/gimp/2.0/plug-ins
%dir %{_libdir}/gimp/2.0/python

%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/gimp/2.0/*


%dir /etc/gimp
%dir /etc/gimp/2.0
%config(noreplace) /etc/gimp/2.0/controllerrc
%config(noreplace) /etc/gimp/2.0/gimprc
%config(noreplace) /etc/gimp/2.0/gtkrc
%config(noreplace) /etc/gimp/2.0/unitrc
%config(noreplace) /etc/gimp/2.0/sessionrc
%config(noreplace) /etc/gimp/2.0/templaterc
%config(noreplace) /etc/gimp/2.0/menurc

/usr/bin/gimp-2.10
/usr/bin/gimp-console-2.10
/usr/bin/gimp
/usr/bin/gimp-console
/usr/bin/gimp-test-clipboard-2.0
/usr/libexec/gimp-debug-tool-2.0
/usr/share/icons/hicolor/*/apps/gimp.png

%{_libdir}/libgimp*so.*


%files devel
%doc HACKING README.i18n
%doc /usr/share/gtk-doc
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/2.0
%dir %{_libdir}/gimp/2.0/modules
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
/usr/share/aclocal/*.m4
/usr/include/gimp-2.0
/usr/lib/rpm/macros.d/macros.gimp
/usr/bin/gimptool-2.0
/usr/bin/gimptool


%files help
%{_mandir}/man*/*

%changelog
* Fri Dec 13 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:2.10.6-3
- Package init
