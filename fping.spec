Summary:	fping - pings multiple hosts at once
Summary(pl):	fping - ping sprawdzaj±cy wiele hostów naraz
Summary(pt_BR):	Ferramenta para enviar pings para várias máquinas de uma só vez
Name:		fping
Version:	2.4b2
Release:	6
License:	distributable
Group:		Networking/Admin
Source0:	http://www.fping.com/download/%{name}-%{version}.tar.gz
# Source0-md5:	d3c4a12119a04893d744137f861e1ecd
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-ipv6.patch
Patch2:		%{name}-ipv6-ac.patch
URL:		http://www.fping.com/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl
fping to program podobny do ping(1), u¿ywaj±cego ¿±dania echo
(echo-request) protoko³u ICMP do stwierdzenia, czy host dzia³a. fping
ró¿ni siê od ping tym, ¿e mo¿na podaæ dowoln± liczbê hostów z linii
poleceñ lub podaæ plik zawieraj±cy listê hostów do sprawdzenia.
Zamiast sprawdzania pojedynczego hosta do up³yniêcia limitu czasu lub
odpowiedzi, fping wysy³a pakiet pinga i przesuwa siê do nastêpnego
hosta w trybie Round-Robin. Je¿eli host odpowiada, jest on zapisywany
i usuwany z listy do sprawdzenia. Je¿eli nie odpowiada przez pewien
czas lub pewn± liczbê prób, jest traktowany jako niedostêpny.

%description -l pt_BR
O fping é um programa que utiliza a requisição de eco do Internet
Control Message Protocol (ICMP) para determinar se uma máquina alvo
está respondendo. O fping difere do ping na medida que se pode
especificar qualquer número de alvos na linha de comando, ou
especificar um arquivo contendo as listas de alvos a enviar ping. Ao
invés de enviar para um alvo até que expire o tempo máximo ou ele
responda, o fping enviará um pacote de ping para cada alvo ao mesmo
tempo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
mv fping fping6

%configure \
	--disable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install fping6 $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README COPYING
%attr(4750,root,adm) %{_sbindir}/*
%{_mandir}/man*/*
