%define api			1.0
%define major		0
%define girmajor	1.0
%define libname		%mklibname %{name} %major
%define develname	%mklibname -d %{name}
%define girname		%mklibname %{name}-gir %{girmajor}

Summary:	JavaScript bindings based on gobject-introspection
Name:		gjs
Version:	1.34.0
Release:	2
License:	BSD
Group:		Development/Other
Url:		http://live.gnome.org/Gjs
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.34/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.18.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.29.16
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(mozjs185)

%description
This package contains JavaScript bindings based on gobject-introspection.

%package -n %{libname}
Group:		System/Libraries
Summary:	JavaScript bindings based on gobject-introspection

%description -n %{libname}
This package contains JavaScript bindings based on gobject-introspection.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Group:		Development/C
Summary:	JavaScript bindings based on gobject-introspection
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains JavaScript bindings based on gobject-introspection.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make V=1

%install
%makeinstall_std

%files
%doc README COPYING NEWS
%{_bindir}/gjs
%{_bindir}/gjs-console
%{_datadir}/%{name}-%{api}
%{_libdir}/gjs-%{api}

%files -n %{libname}
%{_libdir}/libgjs-dbus.so.%{major}*
%{_libdir}/libgjs.so.%{major}*

%files -n %{girname}
%{_libdir}/gjs/girepository-1.0/GjsPrivate-1.0.typelib

%files -n %{develname}
%{_libdir}/libgjs-dbus.so
%{_libdir}/libgjs.so
%{_libdir}/pkgconfig/gjs-%{api}.pc
%{_libdir}/pkgconfig/gjs-dbus-%{api}.pc
%{_libdir}/pkgconfig/gjs-internals-%{api}.pc
%{_includedir}/gjs-%{api}


%changelog
* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 1.34.0-1
- update to 1.34.0

* Mon Apr 30 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.32.0-2
+ Revision: 794594
- rebuild for typelib

* Mon Apr 02 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.32.0-1
+ Revision: 788778
- version update 1.32

* Mon Nov 21 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.31.0-1
+ Revision: 732246
- new version 1.31.0
- removed defattr
- fixed file lists
- separated out gir pkg
- plugins/modules to main pkg
- removed clean section
- removed .la files
- disabled static build
- switched to apply_patches macro
- dropped building with xulrunner (now deprecated in mdv) for mozjs185
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot
- dropped old build p0
- added p0 for g_constant_info_free_value has been added to gobject-introspection
- cleaned up spec

* Thu Apr 28 2011 Funda Wang <fwang@mandriva.org> 0.7.14-2
+ Revision: 660126
- rebuild for new xulrunner

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 0.7.14-1
+ Revision: 650269
- new version

* Tue Mar 22 2011 Funda Wang <fwang@mandriva.org> 0.7.13-1
+ Revision: 647527
- BR readline
- new version 0.7.13
- fix linkage

* Mon Nov 15 2010 Götz Waschk <waschk@mandriva.org> 0.7.7-1mdv2011.0
+ Revision: 597754
- update to new version 0.7.7
- update to new version 0.7.6

* Thu Oct 28 2010 Götz Waschk <waschk@mandriva.org> 0.7.5-1mdv2011.0
+ Revision: 589698
- new version
- update file list

* Tue Oct 05 2010 Götz Waschk <waschk@mandriva.org> 0.7.4-1mdv2011.0
+ Revision: 583086
- update to new version 0.7.4

* Fri Oct 01 2010 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 582395
- new version
- drop patch 1

  + Funda Wang <fwang@mandriva.org>
    - partial patch to build with xulrunner 2.0

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 563574
- new version

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 0.6-5mdv2011.0
+ Revision: 561173
- rebuild for xulrunner 1.9.2.8

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 0.6-4mdv2010.1
+ Revision: 549369
- rebuild with latest xulrunner

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 0.6-3mdv2010.1
+ Revision: 531047
- rebuild for new xulrunner

* Wed Mar 24 2010 Götz Waschk <waschk@mandriva.org> 0.6-2mdv2010.1
+ Revision: 527072
- rebuild for new xulrunner

* Thu Mar 18 2010 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2010.1
+ Revision: 525126
- update to new version 0.6

* Tue Feb 16 2010 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2010.1
+ Revision: 506437
- new version
- drop patch 1

* Sun Jan 10 2010 Götz Waschk <waschk@mandriva.org> 0.4-6mdv2010.1
+ Revision: 488680
- rebuild for new xulrunner

* Fri Jan 01 2010 Götz Waschk <waschk@mandriva.org> 0.4-5mdv2010.1
+ Revision: 484664
- fix build with new xulrunner

* Wed Dec 16 2009 Götz Waschk <waschk@mandriva.org> 0.4-4mdv2010.1
+ Revision: 479218
- rebuild for new xulrunner

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 0.4-3mdv2010.1
+ Revision: 460639
- rebuild for new xulrunner

* Wed Sep 16 2009 Götz Waschk <waschk@mandriva.org> 0.4-2mdv2010.0
+ Revision: 443445
- add explicit versioned xulrunner dep
- rebuild for new xulrunner

* Wed Aug 26 2009 Götz Waschk <waschk@mandriva.org> 0.4-1mdv2010.0
+ Revision: 421331
- new version
- update file list

* Sun Jul 05 2009 Götz Waschk <waschk@mandriva.org> 0.3-1mdv2010.0
+ Revision: 392671
- fix format string
- new version
- fix source URL
- add dbus binding
- drop patch

* Thu Jan 22 2009 Götz Waschk <waschk@mandriva.org> 0.2-2mdv2009.1
+ Revision: 332448
- rebuild

* Wed Nov 12 2008 Götz Waschk <waschk@mandriva.org> 0.2-1mdv2009.1
+ Revision: 302494
- import gjs


