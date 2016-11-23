%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}
%define devstat	%mklibname -s %{name}

Summary:	Library for accessing USB devices
Name:		bctoolbox
Version:	0.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/BelledonneCommunications/
Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	mbedtls-devel
BuildRequires:	pkgconfig(bcunit)

%description
Utilities library used by Belledonne Communications
softwares like belle-sip, mediastreamer2 and linphone.

#--------------------------------------------------------------------

%package -n	%{libname}
Summary:	Library for accessing USB devices
Group:		System/Libraries

%description -n	%{libname}
Library used by Belledonne Communications
softwares like belle-sip, mediastreamer2 and linphone.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*
%{_libdir}/lib%{name}-tester.so.%{major}*

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel-doc < 1.0.15-2

%description -n	%{devname}
This package includes the development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-tester.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-tester.pc
%{_datadir}/%{name}/cmake/

#--------------------------------------------------------------------

%package -n	%{devstat}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%files -n %{devstat}
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}-tester.a

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=Debug \
	-DENABLE_SHARED:BOOL=ON \
	-DENABLE_STATIC:BOOL=OFF \
	-DENABLE_POLARSSL:BOOL=OFF \
	-DENABLE_MBEDTLS:BOOL=ON \
	-DENABLE_TESTS:BOOL=ON
%make

%install
%makeinstall_std -C build

