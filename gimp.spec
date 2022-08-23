%define requires_file() %( readlink -f '%*' | LC_ALL=C xargs -r rpm -q --qf 'Requires: %%{name} >= %%{epoch}:%%{version}\\n' -f | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")

%bcond_without is_git_build
%bcond_without binreloc

%define alsa_version            1.0.0
%define appstream_glib_version  0.7.7
%define atk_version             2.4.0
%define babl_version            0.1.82
%define cairo_version           1.14.0
%define cairo_pdf_version       1.12.2
%define dbus_glib_version       0.70
%define gdk_pixbuf_version      2.30.8
%define fontconfig_version      2.12.4
%define freetype2_version       2.1.7
%define gdk_pixbuf_version      2.30.8
%define gegl04_version          0.4.26
%define gexiv2_version          0.10.6
%define glib_version            2.56.2
%define gtk3_version            3.22.29
%define gudev_version           167
%define harfbuzz_version        1.0.5
%define lcms2_version           2.8
%define libexif_version         0.6.15
%define libheif_version         1.5.2
%define liblzma_version         5.0.0
%define libmypaint_version      1.4.0
%define libopenjp2_version      2.1.0
%define libpng_version          1.6.25
%define librsvg_version         2.40.6
%define libunwind_version       1.1.0
%define libwebp_version         0.6.0
%define mypaint_brushes_version 1.3.0
%define OpenEXR_version         1.6.1
%define pango_version           1.44.0
%define poppler_data_version    0.4.9
%define poppler_glib_version    0.69.0
%define vapigen_version         0.40.0
%define libvala_version         0.40.0
%define webkit2gtk_version      2.20.3

%global abiver 5
%global apiver 3.0

Name:           gimp
Version:        2.99.6
Release:        3
Epoch:          2
Summary:        The GNU Image Manipulation Program
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://www.gimp.org/
Source:         https://download.gimp.org/mirror/pub/gimp/v2.99/%{name}-%{version}.tar.bz2
Source1:        macros.gimp
Source2:        autogen.sh
Source3:        MAINTAINERS
Source98:       gimp-rpmlintrc
Source99:       baselibs.conf
Patch0:         git_info_from_dirname.patch
BuildRequires:  autoconf glibc-all-langpacks
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  aalib-devel
BuildRequires:  babl-vala >= %{babl_version}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gegl04 >= %{gegl04_version}
BuildRequires:  ghostscript-devel
BuildRequires:  glib-networking
BuildRequires:  gtk-doc
BuildRequires:  intltool >= 0.40.1
BuildRequires:  libwmf-devel >= 0.2.8
BuildRequires:  pkgconfig
BuildRequires:  python3 >= 3.6.0
BuildRequires:  python3-gobject
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(OpenEXR) >= %{OpenEXR_version}
BuildRequires:  pkgconfig(alsa) >= %{alsa_version}
BuildRequires:  pkgconfig(appstream-glib) >= %{appstream_glib_version}
BuildRequires:  pkgconfig(atk) >= %{atk_version}
BuildRequires:  pkgconfig(babl) >= %{babl_version}
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= %{cairo_version}
BuildRequires:  pkgconfig(cairo-pdf) >= %{cairo_pdf_version}
BuildRequires:  pkgconfig(dbus-glib-1) >= %{dbus_glib_version}
BuildRequires:  pkgconfig(fontconfig) >= %{fontconfig_version}
BuildRequires:  pkgconfig(freetype2) >= %{freetype2_version}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= %{gdk_pixbuf_version}
BuildRequires:  pkgconfig(gegl-0.4) >= %{gegl04_version}
BuildRequires:  pkgconfig(gexiv2) >= %{gexiv2_version}
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(gudev-1.0) >= %{gudev_version}
BuildRequires:  pkgconfig(harfbuzz) >= %{harfbuzz_version}
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(lcms2) >= %{lcms2_version}
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libexif) >= %{libexif_version}
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblzma) >= %{liblzma_version}
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmypaint) >= %{libmypaint_version}
BuildRequires:  pkgconfig(libopenjp2) >= %{libopenjp2_version}
BuildRequires:  pkgconfig(libpng) >= %{libpng_version}
BuildRequires:  pkgconfig(librsvg-2.0) >= %{librsvg_version}
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libunwind) >= %{libunwind_version}
BuildRequires:  pkgconfig(libwebp) >= %{libwebp_version}
%ifnarch riscv64
BuildRequires:  pkgconfig(luajit)
%endif riscv64
BuildRequires:  pkgconfig(mypaint-brushes-1.0) >= %{mypaint_brushes_version}
BuildRequires:  pkgconfig(pango) >= %{pango_version}
BuildRequires:  pkgconfig(poppler-data) >= %{poppler_data_version}
BuildRequires:  pkgconfig(poppler-glib) >= %{poppler_glib_version}
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(vapigen) >= %{vapigen_version}
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= %{webkit2gtk_version}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
%requires_eq    gegl-0_4
Requires:       gjs
Requires:       libgimp-3_0-0 = %{epoch}:%{version}
Requires:       libgimpui-3_0-0 = %{epoch}:%{version}
%ifnarch riscv64
Requires:       luajit
%endif
Requires:       shared-mime-info
Requires:       xdg-utils
Recommends:     %{name}-plugins-python3 = %{epoch}:%{version}
Recommends:     iso-codes
Suggests:       AdobeICCProfiles
Provides:       gimp-2.0 = %{epoch}:%{version}
Provides:       gimp(abi) = %{abiver}
Provides:       gimp(api) = %{apiver}

%description
The GIMP is an image composition and editing program, which can be
used for creating logos and other graphics for Web pages. The GIMP
offers many tools and filters, and provides a large image
manipulation toolbox, including channel operations and layers,
effects, subpixel imaging and antialiasing, and conversions, together
with multilevel undo. The GIMP offers a scripting facility, but many
of the included scripts rely on fonts that we cannot distribute.

%package -n libgimp-3_0-0
Summary:        The GNU Image Manipulation Program - Libraries
Group:          System/Libraries

%requires_file %{_libdir}/libbabl-0.1.so
%requires_file %{_libdir}/libgegl-0.4.so
%requires_file %{_libdir}/libgexiv2.so

%description -n libgimp-3_0-0
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This package provides GIMP libraries.

%package -n libgimpui-3_0-0
Summary:        The GNU Image Manipulation Program - UI Libraries
Group:          System/Libraries

%description -n libgimpui-3_0-0
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This package provides GIMP UI libraries.

%package plugin-python3
Summary:        The GNU Image Manipulation Program - python3 goject introspection plugins
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name} = %{epoch}:%{version}
Requires:       python3 >= 3.6.0
Requires:       python3-gobject
Supplements:    %{name}
Provides:       gimp-plugins-python3 = %{epoch}:%{version}-%{release}
Obsoletes:      gimp-plugins-python3 < %{epoch}:%{version}-%{release}
%description plugin-python3
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.


%package vala
Summary:        The GNU Image Manipulation Program - Vala development files
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name}-devel = %{epoch}:%{version}
%description vala
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

%package plugin-aa
Summary:        The GNU Image Manipulation Program -- ASCII-Art output plugin
Group:          Productivity/Graphics/Bitmap Editors
Requires:       %{name} = %{epoch}:%{version}
Supplements:    (%{name} and libaa1)

%description plugin-aa
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

%package devel
Summary:        The GNU Image Manipulation Program
Group:          Development/Libraries/Other
Requires:       libgimp-3_0-0 = %{epoch}:%{version}
Requires:       libgimpui-3_0-0 = %{epoch}:%{version}
Provides:       gimp-devel = %{epoch}:%{version}
Provides:       gimp-doc = 2.6.4
Obsoletes:      gimp-doc < 2.6.4
Obsoletes:      gimp-unstable-devel < 2.6.0

%description devel
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This subpackage contains libraries and header files for developing
applications that want to make use of the GIMP libraries.

%package extension-goat-excercises
Summary:        The GNU Image Manipulation Program
Group:          Development/Libraries/Other
Requires:       libgimpui-3_0-0 = %{epoch}:%{version}
Requires:       gimp-vala = %{epoch}:%{version}
Requires:       gimp-devel = %{epoch}:%{version}
Requires:       gimp-plugin-python3 = %{epoch}:%{version}

%description extension-goat-excercises
The GIMP is an image composition and editing program. GIMP offers
many tools and filters, and provides a large image manipulation
toolbox and scripting.

This subpackage contains example the goat extension examples
that extend gimp.



%prep
%autosetup -p1
chmod 744 %{SOURCE2}
cp %{SOURCE2} .
cp %{SOURCE3} .

%build
%define _lto_cflags %{nil}
NOCONFIGURE=1 ./autogen.sh

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
test -x "$(type -p %{_bindir}/gcc-7)" && export CC="%{_bindir}/gcc-7"
test -x "$(type -p %{_bindir}/g++-7)" && export CXX="%{_bindir}/g++-7"
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
	--disable-silent-rules \
	--disable-static\
	--libexecdir=%{_prefix}/lib\
	--enable-default-binary\
    --enable-binreloc \
	--enable-mp

# Safety check for ABI version change.
vabi=$(printf "%%d" $(sed -n '/#define GIMP_MODULE_ABI_VERSION/{s/.* //;p}' libgimpmodule/gimpmodule.h))
if test "x${vabi}" != "x%{abiver}"; then
   : Error: Upstream ABI version is now ${vabi}, expecting %{abiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi
# Safety check for API version change.
vapi=$(sed -n '/#define GIMP_API_VERSION/{s/.* //;p}' libgimpbase/gimpversion.h | sed -e 's@"@@g')
if test "x${vapi}" != "x%{apiver}"; then
   : Error: Upstream API version is now ${vapi}, expecting %{apiver}.
   : Update the apiver macro and rebuild.
   exit 1
fi

%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/gimp/2.99/*/*.*a
touch gimp_all_parts.lang
for lang_part in gimp30 gimp30-libgimp gimp30-python gimp30-script-fu gimp30-std-plug-ins ; do
%find_lang ${lang_part} %{?no_lang_C} ${lang_part}.lang
cat ${lang_part}.lang >> gimp_all_parts.lang
done
echo "%%defattr(-,root,root)" >plugins.list
echo "%%defattr(-,root,root)" >plugins-python.list
for PLUGIN in %{buildroot}%{_libdir}/gimp/2.99/plug-ins/* ; do
    if grep -q '^#!.*python' ${PLUGIN}/* ; then
	echo "${PLUGIN#%{buildroot}}" >>plugins-python.list
    else
	echo "${PLUGIN#%{buildroot}}" >>plugins.list
    fi
done
cat gimp_all_parts.lang >> plugins.list
find %{buildroot} -type f -name "*.la" -delete -print
install -d %{buildroot}%{_sysconfdir}/rpm
sed -e "s/@GIMP_APIVER@/%{apiver}/;s/@GIMP_ABIVER@/%{abiver}/" \
    < $RPM_SOURCE_DIR/macros.gimp > macros.gimp
install -m 644 -c macros.gimp \
           %{buildroot}%{_sysconfdir}/rpm/macros.gimp
%fdupes %{buildroot}%{_datadir}/gtk-doc/
%fdupes %{buildroot}%{_libdir}/gimp/2.99/python/
%fdupes %{buildroot}%{_datadir}/gimp/2.99/

%post -n libgimp-3_0-0 -p /sbin/ldconfig
%postun -n libgimp-3_0-0 -p /sbin/ldconfig
%post -n libgimpui-3_0-0 -p /sbin/ldconfig
%postun -n libgimpui-3_0-0 -p /sbin/ldconfig

%files -f plugins.list
%license COPYING LICENSE
%doc AUTHORS NEWS* README MAINTAINERS HACKING
%{_bindir}/gimp
%{_bindir}/gimp-2.*
%{_bindir}/gimp-console
%{_bindir}/gimp-console-2.*
%{_bindir}/gimp-test-clipboard-2.99
%{_prefix}/lib/gimp-debug-tool-2.99
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/gimp-data-extras.metainfo.xml
%{_datadir}/metainfo/org.gimp.GIMP.appdata.xml
%{_datadir}/applications/gimp.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/gimp/
%{_libdir}/gimp/2.99/environ/default.env
%{_libdir}/gimp/2.99/interpreters/default.interp
%{_libdir}/gimp/2.99/modules/libcolor-selector-cmyk.so
%{_libdir}/gimp/2.99/modules/libcolor-selector-water.so
%{_libdir}/gimp/2.99/modules/libcolor-selector-wheel.so
%{_libdir}/gimp/2.99/modules/libcontroller-linux-input.so
%{_libdir}/gimp/2.99/modules/libcontroller-midi.so
%{_libdir}/gimp/2.99/modules/libdisplay-filter-aces-rrt.so
%{_libdir}/gimp/2.99/modules/libdisplay-filter-clip-warning.so
%{_libdir}/gimp/2.99/modules/libdisplay-filter-color-blind.so
%{_libdir}/gimp/2.99/modules/libdisplay-filter-gamma.so
%{_libdir}/gimp/2.99/modules/libdisplay-filter-high-contrast.so
%{_mandir}/man?/gimp.*
%{_mandir}/man?/gimp-2*
%{_mandir}/man?/gimp-console.*
%{_mandir}/man?/gimp-console-2*
%{_mandir}/man?/gimprc.*
%{_mandir}/man?/gimprc-2*
%{_mandir}/man?/gimptool-2*
%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/2.99
%config %{_sysconfdir}/gimp/2.99/*rc
%config %{_sysconfdir}/gimp/2.99/*css
%exclude %{_libdir}/gimp/2.99/plug-ins/file-aa

%files plugin-aa
%{_libdir}/gimp/2.99/plug-ins/file-aa

%files -n libgimp-3_0-0
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/2.99
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/2.99
%dir %{_libdir}/gimp/2.99/environ
%dir %{_libdir}/gimp/2.99/interpreters
%dir %{_libdir}/gimp/2.99/modules
%dir %{_libdir}/gimp/2.99/plug-ins
%dir %{_libdir}/gimp/2.99/extensions
%{_libdir}/libgimp-3.0.so.*
%{_libdir}/libgimpbase-3.0.so.*
%{_libdir}/libgimpcolor-3.0.so.*
%{_libdir}/libgimpconfig-3.0.so.*
%{_libdir}/libgimpmath-3.0.so.*
%{_libdir}/libgimpmodule-3.0.so.*

%files -n libgimpui-3_0-0
%{_libdir}/libgimpthumb-3.0.so.*
%{_libdir}/libgimpui-3.0.so.*
%{_libdir}/libgimpwidgets-3.0.so.*

%files plugin-python3 -f plugins-python.list
%{_libdir}/gimp/2.99/environ/python.env
%{_libdir}/gimp/2.99/interpreters/pygimp.interp
%{_libdir}/girepository-1.0/Gimp-3.0.typelib
%{_libdir}/girepository-1.0/GimpUi-3.0.typelib

%files vala
%{_datadir}/vala/vapi/gimp-3.deps
%{_datadir}/vala/vapi/gimp-3.vapi
%{_datadir}/vala/vapi/gimp-ui-3.deps
%{_datadir}/vala/vapi/gimp-ui-3.vapi

%files devel
%doc README.i18n
%{_bindir}/gimptool-2.99
%{_includedir}/gimp-3.0/
%{_libdir}/*.so
%{_datadir}/aclocal/gimp-3.0.m4
%{_libdir}/pkgconfig/gimp-3.0.pc
%{_libdir}/pkgconfig/gimpthumb-3.0.pc
%{_libdir}/pkgconfig/gimpui-3.0.pc
%dir %{_datadir}/gtk-doc
%{_datadir}/gtk-doc/html/*
%dir %{_datadir}/locale
%{_datadir}/locale/*/LC_MESSAGES/*
%config %{_sysconfdir}/rpm/macros.gimp
%{_datadir}/gir-1.0/Gimp-3.0.gir
%{_datadir}/gir-1.0/GimpUi-3.0.gir

%files extension-goat-excercises
%{_libdir}/gimp/2.99/extensions/org.gimp.extension.goat-exercises

%changelog
* Tue Aug 23 2022 jchzhou <jchzhou@outlook.com> - 2:2.99.6-3
- Excluding luajit deps for riscv64

* Mon Jun 13 2022 houyingchao <houyingchao@h-partners.com> - 2:2.99.6-2
- Fix compilation failed

* Wed Aug 25 2021 chenchen <chen_aka_jan@163.com> - 2:2.99.6-1
- update to 2.99.6

* Sat Mar 21 2020 hexiujun <hexiujun1@huawei.com> - 2:2.10.6-7
- Type:NA
- ID:NA
- SUG:NA
- DESC:add gdb build require

* Tue Mar 10 2020 songnannan <songnannan2@huawei.com> - 2:2.10.6-6
- delete the jasper

* Mon Feb 17 2020 hexiujun <hexiujun1@huawei.com> - 2:2.10.6-5
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:unpack libs subpackage

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 2:2.10.6-4
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Fri Dec 13 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:2.10.6-3
- Package init
