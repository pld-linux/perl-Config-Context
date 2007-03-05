#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	Context
Summary:	Config::Context - Add <Location> and <LocationMatch> style context matching to hierarchical configfile formats such as Config::General, XML::Simple and Config::Scoped
#Summary(pl):	
Name:		perl-Config-Context
Version:	0.10
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be34d48faef25c3236525cb092562918
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Clone)
BuildRequires:	perl(Config::General) >= 2.27
BuildRequires:	perl(Hash::Merge)
# builds without that, but skips some tests
BuildRequires:	perl(Config::Scoped)
# builds without that, but skips some tests
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(XML::SAX)
BuildRequires:	perl(XML::Filter::XInclude)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a consistent interface to many hierarchical
configuration file formats such as Config::General, XML::Simple
and Config::Scoped.

It also provides Apache-style context matching.  You can include blocks
of configuration that match or not based on run-time parameters.

For instance (using Config::General syntax):

    company_name      = ACME
    in_the_users_area = 0

    <Location /users>
        in_the_users_area = 1
    </Location>

At runtime, if Location is within /users, then the configuration
within the <Location> block is merged into the top level.
Otherwise, the block is ignored.



# %description -l pl
# TODO

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
