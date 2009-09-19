%define shortname Murrine-Sky
Summary:	A light blue theme!
Name:		gtk2-theme-%{shortname}
Version:	1.0
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.cimitan.com/murrine/files/%{shortname}.tar.gz
# Source0-md5:	9b5e10156d2334b4466e6111999f3857
Requires:	gtk2-theme-engine-murrine >= 0.90.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A light blue theme!

%prep
%setup -q -n %{shortname}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/themes/%{shortname}
cp -R gtk* $RPM_BUILD_ROOT%{_datadir}/themes/%{shortname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/themes/%{shortname}
