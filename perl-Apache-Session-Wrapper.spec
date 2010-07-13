%define upstream_name    Apache-Session-Wrapper
%define upstream_version 0.34

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        A simple wrapper around Apache::Session
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(Apache::Test)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"

%check
./Build test </dev/null

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
