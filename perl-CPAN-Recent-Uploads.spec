%define upstream_name    CPAN-Recent-Uploads
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Retrieves recentfiles from a CPAN mirror
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Spec::Unix)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(URI)
BuildRequires:	perl(YAML::Syck)
BuildArch:	noarch

%description
CPAN::Recent::Uploads provides a mechanism for obtaining a list of the
RECENT uploads to 'CPAN' as determined from the files produced by the
File::Rsync::Mirror::Recentfile manpage that exist in the 'authors/'
directory on 'CPAN'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 688742
- update to new version 0.06

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2
+ Revision: 654241
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 625007
- import perl-CPAN-Recent-Uploads

