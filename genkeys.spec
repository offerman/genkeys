Name:           genkeys
Version:        0.2.0
Release:        1%{?dist}
Summary:        Generate, update, and prepublish ZSK and KSK key pairs for DNSSEC deployment
Group:          Applications/Internet

License:        GPLv3
URL:            https://github.com/offerman/genkeys
Source0:        genkeys-0.2.0.tgz
BuildArch:      noarch
Packager:       Adrian Offerman <http://www.offerman.com>

#BuildRequires:  
Requires:       bash coreutils fileutils findutils sed
Requires:       bind >= 9.8

%description
This bash script is a wrapper around the dnssec-keygen tool that comes with
BIND named. It allows you to generate, update, and prepublish ZSK and KSK key
pairs for DNSSEC deployment for all your existing zone files in a single run.
The default values should work out-of-the-box on CentOS 6.


%prep
%setup -c


%build


%check


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 gp-genkeys2 $RPM_BUILD_ROOT%{_bindir}/
(cd $RPM_BUILD_ROOT%{_bindir}/; ln -s gp-genkeys2 genkeys)


# only for EPEL
%clean
rm -rf $RPM_BUILD_ROOT


%files
%{_bindir}/gp-genkeys2
%{_bindir}/genkeys
%defattr(644, root, root, 755)
%doc ChangeLog COPYING LICENSE README README.md TODO


%changelog
* Sun Aug 25 2013 Adrian Offerman <http://www.offerman.com> - 0.2.0-1
- Initial RPM release


