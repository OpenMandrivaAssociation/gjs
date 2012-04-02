%define api			1.0
%define major		0
%define girmajor	1.0
%define libname		%mklibname %{name} %major
%define develname	%mklibname -d %{name}
%define girname		%mklibname %{name}-gir %{girmajor}

Summary: JavaScript bindings based on gobject-introspection
Name: gjs
Version: 1.32.0
Release: 1
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch0:	gjs-1.31.0_g_constant_info_free_value.patch
License: BSD
Group: Development/Other
Url:  http://live.gnome.org/Gjs

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
Group: System/Libraries
Summary: JavaScript bindings based on gobject-introspection

%description -n %{libname}
This package contains JavaScript bindings based on gobject-introspection.

%package -n %{girname}
Summary: GObject Introspection interface description for %{name}
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Group: Development/C
Summary: JavaScript bindings based on gobject-introspection
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains JavaScript bindings based on gobject-introspection.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make LIBS='-lgio-2.0'

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc README COPYING NEWS
%{_bindir}/gjs
%{_bindir}/gjs-console
%{_datadir}/%{name}-%api
%{_libdir}/gjs-%api

%files -n %{libname}
%{_libdir}/libgjs-dbus.so.%{major}*
%{_libdir}/libgjs-gdbus.so.%{major}*
%{_libdir}/libgjs.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GjsDBus-1.0.typelib

%files -n %{develname}
%{_libdir}/libgjs-dbus.so
%{_libdir}/libgjs-gdbus.so
%{_libdir}/libgjs.so
%{_libdir}/pkgconfig/gjs-%api.pc
%{_libdir}/pkgconfig/gjs-dbus-%api.pc
%{_libdir}/pkgconfig/gjs-internals-%api.pc
%{_datadir}/gir-1.0/GjsDBus-%{girmajor}.gir
%{_includedir}/gjs-%api
