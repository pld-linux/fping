Summary:	fping - pings multiple hosts at once
Summary(pl.UTF-8):	fping - ping sprawdzający wiele hostów naraz
Summary(pt_BR.UTF-8):	Ferramenta para enviar pings para várias máquinas de uma só vez
Name:		fping
Version:	5.4
Release:	1
License:	distributable
Group:		Networking/Utilities
Source0:	http://fping.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	b19d8ef759befa3e1dcf44fcc529fcfd
URL:		http://fping.org/
BuildRequires:	autoconf >= 2.59
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

%description -l pl.UTF-8
fping to program podobny do ping(1), używającego żądania echo
(echo-request) protokołu ICMP do stwierdzenia, czy host działa. fping
różni się od ping tym, że można podać dowolną liczbę hostów z linii
poleceń lub podać plik zawierający listę hostów do sprawdzenia.
Zamiast sprawdzania pojedynczego hosta do upłynięcia limitu czasu lub
odpowiedzi, fping wysyła pakiet pinga i przesuwa się do następnego
hosta w trybie Round-Robin. Jeżeli host odpowiada, jest on zapisywany
i usuwany z listy do sprawdzenia. Jeżeli nie odpowiada przez pewien
czas lub pewną liczbę prób, jest traktowany jako niedostępny.

%description -l pt_BR.UTF-8
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

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-ipv4 \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	sbindir=%{_bindir} \
	DESTDIR=$RPM_BUILD_ROOT

ln -s %{_bindir}/fping $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md doc/{CHANGELOG.pre-v4,README.1992}
%attr(4754,root,icmp) %{_bindir}/fping
%attr(4754,root,icmp) %{_sbindir}/fping
%{_mandir}/man8/fping*.8*
