%define upstream_name    CPAN-Recent-Uploads
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Retrieves recentfiles from a CPAN mirror
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Spec::Unix)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(URI)
BuildRequires: perl(YAML::Syck)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
CPAN::Recent::Uploads provides a mechanism for obtaining a list of the
RECENT uploads to 'CPAN' as determined from the files produced by the
File::Rsync::Mirror::Recentfile manpage that exist in the 'authors/'
directory on 'CPAN'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


