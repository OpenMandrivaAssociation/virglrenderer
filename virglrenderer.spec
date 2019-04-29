# Please keep this package in sync with FC

# "fix" underlinking:
%define _disable_ld_no_undefined 1

%global major 0
%define libname %mklibname virglrenderer %major
%define devname %mklibname -d virglrenderer
%global gitdate 20190424
%global gitversion d1758cc09

Name:		virglrenderer
Version:	0.7.0
Release:	%mkrel 1.%{gitdate}git%{gitversion}

Summary:	Virgl Rendering library
Group:		Emulators
License:	MIT

#VCS: git:git://anongit.freedesktop.org/git/virglrenderer
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
Source0:	virglrenderer-%{gitdate}.tar.xz

BuildRequires:	autoconf
BuildRequires:	autoconf-archive
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	x11-util-macros
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(egl)
BuildRequires:	python3
BuildRequires:	pkgconfig(libdrm)

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package -n %libname
Summary: Virgl Rendering library
Group:	Emulators

%description -n %libname
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package -n %devname
Summary: Virgil3D renderer development files
Group:	Emulators
Provides: %{name}-devel
Requires: %{libname} = %{version}-%{release}

%description -n %devname
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary: Virgil3D renderer testing server
Group:	Emulators

Requires: %{libname} = %{version}-%{release}

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
%setup -q -n %{name}-%{gitdate}
%build
autoreconf -vif
%configure --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.la' | xargs rm -f -- || :

%files -n %libname
%license COPYING
%{_libdir}/lib*.so.*

%files -n %devname
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files test-server
%{_bindir}/virgl_test_server
