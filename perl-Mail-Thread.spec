#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Thread
Summary:	Mail::Thread - Perl implementation of JWZ's mail threading algorithm
Summary(pl.UTF-8):	Mail::Thread - perlowa implementacja algorytmu wątkowania poczty JWZ
Name:		perl-Mail-Thread
Version:	2.5
Release:	2
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	37f291b44ea2055ba59228ee95402c39
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Mail::Internet)
BuildRequires:	perl-Email-Abstract
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements something relatively close to Jamie Zawinski's
mail threading algorithm, as described by
http://www.jwz.org/doc/threading.html. Any deviations from the
algorithm are accidental.

%description -l pl.UTF-8
Ten moduł jest implementacją czegoś w miarę bliskiego do algorytmu
wątkowania poczty autorstwa Jamie Zawinskiego, opisanego w
http://www.jwz.org/doc/threading.html. Wszelkie odchylenia od
algorytmu są przypadkowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Mail/*.pm
%{_mandir}/man3/*
