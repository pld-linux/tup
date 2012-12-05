Summary:	Tup - build system
Name:		tup
Version:	0.6
Release:	1
License:	GPL v2
Group:		Development/Building
# git repo fetch: git clone git://github.com/gittup/tup.git
Source0:	https://github.com/gittup/tup/archive/v0.6.tar.gz
# Source0-md5:	0e4d0a6ab524731d3153e015135be097
Patch0:		%{name}-upstream.patch
URL:		http://gittup.org/tup/
BuildRequires:	gcc
BuildRequires:	libfuse-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tup is a file-based build system for Linux, OSX, and Windows. It
inputs a list of file changes and a directed acyclic graph (DAG), then
processes the DAG to execute the appropriate commands required to
update dependent files. Updates are performed with very little
overhead since tup implements powerful build algorithms to avoid doing
unnecessary work. This means you can stay focused on your project
rather than on your build system

%prep
%setup -q -n tup-%{version}
%patch0 -p1

%build
./build.sh
#./bootstrap.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install build/tup $RPM_BUILD_ROOT%{_bindir}
install tup.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tup
%{_mandir}/man1/tup.1*
