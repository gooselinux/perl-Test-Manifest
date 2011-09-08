Name:           perl-Test-Manifest
Version:        1.22
Release:        5%{?dist}
Summary:        Test case module for Perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Manifest/
Source0:        http://www.cpan.org/authors/id/B/BD/BDFOY/Test-Manifest-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(ExtUtils::MakeMaker), perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
MakeMaker assumes that you want to run all of the .t files in the t/
directory in ascii-betical order during make test unless you say
otherwise. This leads to some interesting naming schemes for test
files to get them in the desired order.
You can specify any order or any files that you like, though, with the
test directive to WriteMakefile.
Test::Manifest looks in the t/test_manifest file to find out which
tests you want to run and the order in which you want to run them. It
constructs the right value for MakeMaker to do the right thing.


%prep
%setup -q -n Test-Manifest-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3*


%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-3
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-2
- rebuild for new perl

* Wed Dec 19 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.22-1
- 1.22
- license fix

* Fri Feb 23 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.17-1
- Update to 1.17.

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-5
- Rebuild for FC6.

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-4
- Rebuild for FC5 (perl 5.8.8).

* Thu May 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-3
- Add dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.14-2
- rebuilt

* Tue Mar 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Wed Mar 23 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.13-1
- Update to 1.13.

* Sat Oct 30 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.11-1
- Update to 1.11.

* Sun Jun 13 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:0.93-0.fdr.2
- Bring up to date with current fedora.us perl spec template.
- Require perl >= 2:5.8.0 for vendor install dir support
  (also resolves the ExtUtils::MakeMaker version problem).

* Sun Mar 14 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:0.93-0.fdr.1
- Update to 0.93.
- Reduce directory ownership bloat.

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:0.92-0.fdr.1
- First build.
