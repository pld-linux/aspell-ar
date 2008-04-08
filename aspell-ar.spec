Summary:	Arabic dictionary for aspell
Summary(pl.UTF-8):	Słownik arabski dla aspella
Name:		aspell-ar
Version:	1.2
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/ar/aspell6-ar-%{version}-%{subv}.tar.bz2
# Source0-md5:	154cf762bafdd02db419b62191138738
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arabic dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik arabski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-ar-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
