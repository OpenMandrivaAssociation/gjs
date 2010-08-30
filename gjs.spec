%define name gjs
%define version 0.7.1
%define release %mkrel 1
%define api 1.0
%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name

%if %{?xulrunner_libname:0}%{?!xulrunner_libname:1}
%define xulrunner_libname libxulrunner
%define xulrunner_version 1.9
%endif

Summary: JavaScript bindings based on gobject-introspection
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch: gjs-0.3-format-strings.patch
Patch1: gjs-0.7.1-xulrunner-2.0.patch
License: BSD
Group: Development/Other
Url:  http://live.gnome.org/Gjs
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: xulrunner-devel >= 1.9
BuildRequires: gobject-introspection-devel >= 0.6
BuildRequires: dbus-glib-devel

%description
This package contains JavaScript bindings based on gobject-introspection.

%package -n %libname
Group:System/Libraries
Summary:JavaScript bindings based on gobject-introspection
Requires: %xulrunner_libname

%description -n %libname
This package contains JavaScript bindings based on gobject-introspection.

%package -n %develname
Group:Development/C
Summary:JavaScript bindings based on gobject-introspection
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release
Requires: xulrunner-devel = %xulrunner_version

%description -n %develname
This package contains JavaScript bindings based on gobject-introspection.

%prep
%setup -q
%patch -p1
%patch1 -p0 -b .xul

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING NEWS
%_bindir/gjs
%_bindir/gjs-console
%_datadir/%name-%api

%files -n %libname
%defattr(-,root,root)
%_libdir/libgjs-dbus.so.%{major}*
%_libdir/libgjs-gi.so.%{major}*
%_libdir/libgjs.so.%{major}*
%_libdir/gjs-%api

%files -n %develname
%defattr(-,root,root)
%_libdir/libgjs-dbus.so
%_libdir/libgjs-gi.so
%_libdir/libgjs.so
%_libdir/libgjs*.la
%_libdir/pkgconfig/gjs-dbus-%api.pc
%_libdir/pkgconfig/gjs-%api.pc
%_libdir/pkgconfig/gjs-gi-%api.pc
%_includedir/gjs-%api
