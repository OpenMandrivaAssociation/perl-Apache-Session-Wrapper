%define upstream_name    Apache-Session-Wrapper
%define upstream_version 0.34

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        4

Summary:        A simple wrapper around Apache::Session
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            https://search.cpan.org/dist/%{upstream_name}
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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.340.0-2mdv2011.0
+ Revision: 680459
- mass rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.340.0-1mdv2011.0
+ Revision: 552251
- update to 0.34

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.330.0-1mdv2010.0
+ Revision: 402093
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.33-3mdv2009.0
+ Revision: 241148
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.33-1mdv2008.0
+ Revision: 19181
-New version


* Wed Aug 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdv2007.0
- New version 0.31
- Module::Build-based build
- fix directory ownership

* Thu Jun 15 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.29-1mdv2007.0
- New version 0.29

* Tue May 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.28-1mdv2007.0
- New release 0.28

* Thu Apr 27 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.26-2mdk
- Fix SPEC according to Perl Policy
    - Source URL
    - BuildRequires

* Fri Jan 27 2006 Oden Eriksson <oeriksson@mandriva.com> 0.26-1mdk
- initial Mandriva package

