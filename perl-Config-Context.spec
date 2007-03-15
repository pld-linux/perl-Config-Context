#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Context
Summary:	Config::Context - Add <Location> and <LocationMatch> style context matching to hierarchical configfile formats such as Config::General, XML::Simple and Config::Scoped
Summary(pl.UTF-8):	Config::Context - dodawanie dopasowywania kontekstu w stylu <Location> i <LocationMatch> do hierarchicznych formatów takich jak Config::General, XML::Simple czy Config::Scoped
Name:		perl-Config-Context
Version:	0.10
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be34d48faef25c3236525cb092562918
URL:		http://search.cpan.org/dist/Config-Context/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Clone
BuildRequires:	perl-Config-General >= 2.27
BuildRequires:	perl-Hash-Merge
# builds without that, but skips some tests
BuildRequires:	perl-Config-Scoped
# builds without that, but skips some tests
BuildRequires:	perl-XML-Simple
BuildRequires:	perl-XML-SAX
BuildRequires:	perl-XML-Filter-XInclude
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a consistent interface to many hierarchical
configuration file formats such as Config::General, XML::Simple
and Config::Scoped.

It also provides Apache-style context matching. You can include blocks
of configuration that match or not based on run-time parameters.

%description -l pl.UTF-8
Ten moduł udostępnia spójny interfejs do wielu hierarchicznych
formatów plików konfiguracyjnych, takich jak Config::General,
XML::Simple czy Config::Scoped.

Udostępnia także dopasowywanie kontekstu w stylu Apache'a. Można
dołączać bloki konfiguracji pasujące lub nie pasujące do danych
parametrów w trakcie działania programu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/Config/*.pm
%{perl_vendorlib}/Config/Context
%{_mandir}/man3/*
