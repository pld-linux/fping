Summary:	fping - pings multiple hosts at once
Summary(pl):	fping - ping sprawdzaj�cy wiele host�w naraz
Summary(pt_BR):	Ferramenta para enviar pings para v�rias m�quinas de uma s� vez
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
fping to program podobny do ping(1), u�ywaj�cego ��dania echo
(echo-request) protoko�u ICMP do stwierdzenia, czy host dzia�a. fping
r�ni si� od ping tym, �e mo�na poda� dowoln� liczb� host�w z linii
polece� lub poda� plik zawieraj�cy list� host�w do sprawdzenia.
Zamiast sprawdzania pojedynczego hosta do up�yni�cia limitu czasu lub
odpowiedzi, fping wysy�a pakiet pinga i przesuwa si� do nast�pnego
hosta w trybie Round-Robin. Je�eli host odpowiada, jest on zapisywany
i usuwany z listy do sprawdzenia. Je�eli nie odpowiada przez pewien
czas lub pewn� liczb� pr�b, jest traktowany jako niedost�pny.

%description -l pt_BR
O fping � um programa que utiliza a requisi��o de eco do Internet
Control Message Protocol (ICMP) para determinar se uma m�quina alvo
est� respondendo. O fping difere do ping na medida que se pode
especificar qualquer n�mero de alvos na linha de comando, ou
especificar um arquivo contendo as listas de alvos a enviar ping. Ao
inv�s de enviar para um alvo at� que expire o tempo m�ximo ou ele
responda, o fping enviar� um pacote de ping para cada alvo ao mesmo
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
