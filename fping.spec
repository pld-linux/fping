Summary:	fping
Summary(pl):	fping
Name:		fping
Version:	2.4b2
Release:	1
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administracyjne
License:	GPL (?)
Source0:	http://www.fping.com/download/%{name}-%{version}.tar.gz
URL:		http://www.fping.com
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fping is a ping(1) like program which uses the Internet Control
Message Protocol (ICMP) echo request to determine if a host is up.
fping is different from ping in that you can specify any number of
hosts on the command line, or specify a file containing the lists of
hosts to ping. Instead of trying one host until it timeouts or
replies, fping will send out a ping packet and move on to the next
host in a round-robin fashion. If a host replies, it is noted and
removed from the list of hosts to check. If a host does not respond
within a certain time limit and/or retry limit it will be considered
unreachable.


%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(4750,root,adm) %{_sbindir}/*
%{_mandir}/man*/*
