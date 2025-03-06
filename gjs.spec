%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}
%define girname	%mklibname %{name}-gir %{api}

%define __noautoreq 'devel\\(libmozjs-78(.*)'
%define _disable_rebuild_configure 1

Summary:	JavaScript bindings based on gobject-introspection
Name:		gjs
Version:	1.82.1
Release:	6
License:	BSD
Group:		Development/Other
Url:		https://live.gnome.org/Gjs
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.18.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.29.16
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(mozjs-128)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  cmake
BuildRequires:	dbus
BuildRequires:	dbus-daemon
BuildRequires:	meson
BuildRequires:  mozjs128
Provides: %{_bindir}/gjs

Requires:  mozjs128

# Filter requires for tests:
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}/usr/libexec/installed-tests|/usr/libexec/gjs/installed-tests|/usr/share/installed-tests/gjs

%description
This package contains JavaScript bindings based on gobject-introspection.

%package -n %{libname}
Summary:	JavaScript bindings based on gobject-introspection
Group:		System/Libraries

%description -n %{libname}
This package contains JavaScript bindings based on gobject-introspection.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	JavaScript bindings based on gobject-introspection
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Requires:	pkgconfig(mozjs-128)
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains JavaScript bindings based on gobject-introspection.

%package tests
Summary: Tests for the gjs package
Group: Development/Tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The gjs-tests package contains tests that can be used to verify
the functionality of the installed gjs package.

%prep
%autosetup -p1
%meson

%build
%meson_build

%install
%meson_install

%files
%doc README.md COPYING NEWS
%{_bindir}/gjs
%{_bindir}/gjs-console
#{_datadir}/glib-2.0/schemas/org.gnome.GjsTest.gschema.xml

%files -n %{libname}
%{_libdir}/libgjs.so.%{major}*

%files -n %{girname}
%{_libdir}/gjs/girepository-1.0/GjsPrivate-%{api}.typelib

%files -n %{devname}
%{_libdir}/libgjs.so
%{_datadir}/gjs-%{api}/lsan/lsan.supp
%{_datadir}/gjs-%{api}/valgrind/gjs.supp
%{_libdir}/pkgconfig/gjs-%{api}.pc
%{_includedir}/gjs-%{api}

%files tests
%{_libexecdir}/installed-tests/gjs
%{_datadir}/glib-2.0/schemas/org.gnome.GjsTest.gschema.xml
%{_datadir}/installed-tests
