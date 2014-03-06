Name:		log4cxx
Version:	0.10.0
Release:	0
Summary:	C++ logging framework modeled after log4j
License:	Apache-2.0
Group:		Application Framework/Libraries
URL:		http://logging.apache.org/log4cxx/
Source:		%name-%version.tar.xz
Source1001: 	log4cxx.manifest
BuildRequires:	autoconf >= 2.64, automake >= 1.11
BuildRequires:	libtool >= 2.2
BuildRequires:	pkgconfig(apr-1)
BuildRequires:	pkgconfig(apr-util-1)

%description
Apache log4cxx is a logging framework for C++ patterned after Apache
log4j, which uses Apache Portable Runtime for most platform-specific
code and should be usable on any platform supported by APR. Apache
log4cxx is licensed under the Apache License, an open source license
certified by the Open Source Initiative. 

%package devel
Summary:	Development files for the log4cxx library
Group:		Application Framework/Libraries
Requires:       %name = %version
Requires:       apr-devel
Requires:       apr-util-devel

%description devel
Development files, including headers, for the log4cxx library.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license LICENSE
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/log4cxx/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc