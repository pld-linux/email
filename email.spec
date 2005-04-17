Summary:	Email can send email using remote SMTP
Summary(pl):	Email potrafi wysy³aæ pocztê u¿ywaj±c zdalnych SMTP
Name:		email
Version:	2.3.4
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://email.cleancode.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	6ced0bebeb6897e9bb975bb02b66b5ae
URL:		http://email.cleancode.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/email,%{_mandir}/man1}

install email.conf email.sig $RPM_BUILD_ROOT%{_sysconfdir}/email
install src/email $RPM_BUILD_ROOT%{_bindir}
install email.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README RFC821 email.help email.address.template TODO
%dir %{_sysconfdir}/email
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/email/email*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
