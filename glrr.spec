%define name glrr
%define version 0
%define date 20050529
%define rel 2
%define release %mkrel 0.%{date}.%{rel}
%define distname %{name}-%{date}
%define common_description glrr is a set of utility functions for glib, gobject, and gtk+.

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary: Utility functions for glib, gobject, and gtk+
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
Patch0: glrr-20050529-underlinking.patch
License: BSD
Group: System/Libraries
Url: http://sourceforge.net/projects/grift/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel

%description
%{common_description}

%package -n %{libname}
Summary: Main library for %{name}
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
%{common_description}

This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary: Headers for developing programs that will use %{name}
Group: Development/GNOME and GTK+
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
%{common_description}

This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q -n %{distname}
%patch0 -p1 -b .underlinking
autoreconf

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/lib%{name}-*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib%{name}-*.so
%{_libdir}/lib%{name}-*.la
%{_libdir}/pkgconfig/%{name}-*.pc
%dir %{_includedir}/%{name}-glib
%{_includedir}/%{name}-glib/*.h
%dir %{_includedir}/%{name}-gobject
%{_includedir}/%{name}-gobject/*.h
%dir %{_includedir}/%{name}-gtk
%{_includedir}/%{name}-gtk/*.h
