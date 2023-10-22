# Please keep this package in sync with FC

# "fix" underlinking:
%define _disable_ld_no_undefined 1

%global optflags %{optflags} -Wno-embedded-directive

%global major 1
%define libname %mklibname virglrenderer %major
%define devname %mklibname -d virglrenderer
%global gitdate %{nil}
%global gitversion %{nil}

Name:		virglrenderer
Version:	1.0.0
Release:	1
Summary:	Virgl Rendering library
Group:		Emulators
License:	MIT
#VCS: git:git://anongit.freedesktop.org/git/virglrenderer
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
#Source0:	https://github.com/freedesktop/virglrenderer/archive/%{name}-%{version}.tar.gz
Source0:  https://gitlab.freedesktop.org/virgl/virglrenderer/-/archive/%{version}/virglrenderer-%{version}.tar.bz2

BuildRequires:	meson
BuildRequires:	x11-util-macros
BuildRequires:	pkgconfig(epoxy)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libdrm)

%description
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package -n %{libname}
Summary:	Virgl Rendering library
Group:		Emulators
Obsoletes:		%{mklibname virglrenderer 0} < 0.8.1

%description -n %{libname}
The virgil3d rendering library is a library used by
qemu to implement 3D GPU support for the virtio GPU.

%package -n %{devname}
Summary:	Virgil3D renderer development files
Group:		Emulators
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Virgil3D renderer development files, used by
qemu to build against.

%package test-server
Summary:	Virgil3D renderer testing server
Group:		Emulators
Requires:	%{libname} = %{EVRD}

%description test-server
Virgil3D renderer testing server is a server
that can be used along with the mesa virgl
driver to test virgl rendering without GL.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%license COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/virgl/
%{_includedir}/virgl/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files test-server
%{_bindir}/virgl_test_server
