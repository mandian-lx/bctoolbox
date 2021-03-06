%define major	0
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname -d %{name}

Summary:	Library for accessing USB devices
Name:		bctoolbox
Version:	0.4.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/BelledonneCommunications/%{name}
Source0:	https://github.com/BelledonneCommunications/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#Source0:	https://download-mirror.savannah.gnu.org/releases/linphone/%{name}/%{name}-%{version}.tar.gz
#Source1:	https://download-mirror.savannah.gnu.org/releases/linphone/%{name}/%{name}-%{version}.tar.gz.sig
Patch0:		%{name}-0.4.0-pkgconfig.patch

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
%doc COPYING

#--------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package includes the development files for %{name}.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-tester.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-tester.pc
%{_datadir}/%{name}/cmake/
%doc README
%doc NEWS
%doc AUTHORS
%doc ChangeLog
%doc COPYING

#--------------------------------------------------------------------

%prep
%setup -q

# Apply all patches
%patch0 -p1 -b .orig

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

