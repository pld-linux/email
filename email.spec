Summary:	Email can send email using remote SMTP
Summary(pl):	Email potrafi wysy³aæ pocztê u¿ywaj±c zdalnych SMTP
Name:		email
Version:	2.3.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://email.cleancode.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	46aefdf1e8ef23b168712b3fa30631d2
URL:		http://email.cleancode.org/
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email is a program for the Unix environment that sends messages.
It can send email from the command line using your SMTP server 
instead of sendmail.

%description -l pl
Email jest programem przeznaczonym do wysy³ania wiadomo¶ci w 
¶rodowisku UNIX. Jest uruchamiany z wiersza poleceñ. Potrafi wysy³aæ
pocztê u¿ywaj±c zdalnych serwerów SMTP.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man1}
install email.conf $RPM_BUILD_ROOT%{_sysconfdir}
install src/email $RPM_BUILD_ROOT%{_bindir}
install email.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README RFC821 email.help email.address.template
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/email.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
