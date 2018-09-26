%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}
%define girname	%mklibname %{name}-gir %{api}

%define __noautoreq 'devel\\(libmozjs-52(.*)'
%define _disable_rebuild_configure 1

Summary:	JavaScript bindings based on gobject-introspection
Name:		gjs
Version:	1.54.1
Release:	1
License:	BSD
Group:		Development/Other
Url:		http://live.gnome.org/Gjs
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
#Patch0:		object-Define-GObject-properties-as-configurable.patch

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.18.0
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.29.16
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(mozjs-52)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	dbus

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
Requires:	pkgconfig(mozjs-52)
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains JavaScript bindings based on gobject-introspection.

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-static

%make

%install
%makeinstall_std

%files
%doc README COPYING NEWS
%{_bindir}/gjs
%{_bindir}/gjs-console

%files -n %{libname}
%{_libdir}/libgjs.so.%{major}*

%files -n %{girname}
%{_libdir}/gjs/girepository-1.0/GjsPrivate-%{api}.typelib

%files -n %{devname}
%{_libdir}/libgjs.so
%{_datadir}/gjs-%{api}/lsan/lsan.supp
%{_datadir}/gjs-%{api}/valgrind/gjs.supp
%{_libdir}/pkgconfig/gjs-%{api}.pc
#{_libdir}/pkgconfig/gjs-internals-%{api}.pc
%{_includedir}/gjs-%{api}
