Name:           abbyylib
Version:        0.1
Release:        1%{?dist}
Summary:        This is a RPM package for the c++ library to call ABBYY. 

Group:          Development/Libraries
License:        Copyright (C) 2016 by Autodesk, Inc. All rights reserved.
URL:            http://www.autodesk.com
Source0:        abbyylib-0.1.tar.gz
AutoReqProv:    no

BuildRequires:  chrpath
Requires:      	glibc == 2.12

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
Prefix:         %{_prefix}

# OR Use following line to install into [/opt/abbyylib] dir
# %define abbyylib /opt/abbyylib
# Another way is install to /usr/lib64/abbyylib as followed
%define abbyylib %{_libdir}/abbyylib


%description
This package includes all binary files from ABBYY

%prep
%setup -q
chrpath --delete Bin/libDL100pdfl.so.10.1.0.51

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{abbyylib}
cp -R * $RPM_BUILD_ROOT%{abbyylib}

#Create symbol links if necessary
#ln -sf %{abbyylib}/Bin/libFREngine.so $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{abbyylib}/
# List your symbol link file below
#%{_bindir}/libFREngine.so

%doc

%changelog
