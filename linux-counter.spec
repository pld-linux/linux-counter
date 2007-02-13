%include	/usr/lib/rpm/macros.perl
Summary:	The Linux Counter Client Script
Summary(pl.UTF-8):	Skrypt kliencki serwisu Linux Counter
Name:		linux-counter
Version:	0.25
Release:	0.2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://counter.li.org/scripts/machine-update
# Source0-md5:	81d92853841c78721ffff2f63d0f0c7b
URL:		http://counter.li.org/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a script that can be run on a Linux box to ease
the task of registering with the Linux Counter, and of keeping a
registration up to date.

%description -l pl.UTF-8
Ten pakiet zawiera skrypt, który można uruchomić na maszynie z
Linuksem, aby ułatwić proces rejestracji w serwisie Linux Counter oraz
uaktualnianie rejestracji.

%prep
%setup -qcT
install %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install machine-update $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
