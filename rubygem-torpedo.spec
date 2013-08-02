%global gem_name torpedo
%global rubyabi 1.8
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}

Summary: Fire when ready. Fast Ruby integration tests for OpenStack
Name: rubygem-%{gem_name}
Version: 1.0.19
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/dprince/torpedo
Source0: %{gem_name}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
Requires: ruby 
Requires: rubygem(thor) => 0.14.6
Requires: rubygem(fog)
Requires: rubygem(net-ssh) >= 2.2.0
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Fast integration tests OpenStack.


%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
gem install --no-rdoc --no-ri --local --install-dir .%{gem_dir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

sed -e 's|.*s\.add.*dependency.*||g' -i %{buildroot}%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec


%files
%dir %{gem_instdir}
%{_bindir}/torpedo
%{gem_instdir}/bin
%{gem_instdir}/README.md
%{gem_instdir}/LICENSE.txt
%{gem_instdir}/VERSION
%{gem_instdir}/CHANGELOG
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/test/helper.rb
%exclude %{gem_instdir}/torpedo.gemspec
%{gem_libdir}
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%changelog
* Fri Aug 02 2013 Dan Prince - 2.1.0-1
- Add support for volumes.

* Wed May 01 2013 Dan Prince - 1.0.19-1
- Initial package
