%define module  Apache-Session-Wrapper
%define name    perl-%{module}
%define version 0.31
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A simple wrapper around Apache::Session
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Apache/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(Apache::Test)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module is a simple wrapper around Apache::Session which
provides some methods to simplify getting and setting the session
id. It can uses cookies to store the session id, or it can look in
a provided object for a specific parameter. Alternately, you can
simply provide the session id yourself in the call to the
"session()" method. If you're using Mason, you should probably 
take a look at "MasonX::Request::WithApacheSession" first,  which
integrates this module directly into Mason.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}
%files
%defattr(-,root,root)
%doc Changes LICENSE README SIGNATURE
%{perl_vendorlib}/Apache
%{_mandir}/man3/*

