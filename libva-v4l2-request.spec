Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version lead=1.0 follow=0 }}}
Release:        1%{?dist}
Summary:        LibVA implementation for the Linux Video4Linux2 Request API

License:        LGPLv2.1, MIT
URL:            https://github.com/Leuca/libva-v4l2-request
VCS:            {{{ git_dir_vcs }}}

Source:         {{{ git_dir_pack }}}

Patch0:         libva-v4l2-request-fix-kernel-5.14.patch
Patch1:         libva-v4l2-request-fix-paths-and-flags.patch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  m4
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  kernel-devel
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libdrm)

%description
This libVA backend is designed to work with the Linux Video4Linux2 Request API that is used by a number of video codecs drivers, including the Video Engine found in most Allwinner SoCs.

The v4l2-request libVA backend currently supports the following formats:
    - MPEG2 (Simple and Main profiles)
    - H264 (Baseline, Main and High profiles)
    - H265 (Main profile)

%package devel
Summary:        Development headers for %{name}
Requires:       %{name}%{?isa} = %{version}-%{release}

%description devel
This package contains development headers for %{name} and a libtool archive file (.la) meant for compiling software that uses this shared library.

%prep
{{{ git_dir_setup_macro }}}
%autopatch -p1

%build
autoreconf -vi
%configure
%make_build

%install
%make_install

%files
%license COPYING COPYING.LGPL COPYING.MIT
%doc README.md CREDITS AUTHORS
%{_libdir}/dri/*.so

%files devel
%{_libdir}/dri/*.la
%{_includedir}/*.h

%changelog
{{{ git_dir_changelog }}}
