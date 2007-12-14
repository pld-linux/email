Summary:	Email can send email using remote SMTP
Summary(pl.UTF-8):	Email potrafi wysyłać pocztę używając zdalnych SMTP
Name:		email
Version:	2.5.0
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	http://www.cleancode.org/downloads/email/%{name}-%{version}.tar.bz2
# Source0-md5:	d6e5f5764e3655226b5a6f9a07622836
Patch0:		%{name}-conf.patch
URL:		http://email.cleancode.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# configure fails to check strftime() otherwise
%undefine	with_ccache

%description
Email is a program for the Unix environment that sends messages. It
can send email from the command line using your SMTP server instead of
sendmail.

%description -l pl.UTF-8
Email jest programem przeznaczonym do wysyłania wiadomości w
środowisku UNIX. Jest uruchamiany z wiersza poleceń. Potrafi wysyłać
pocztę używając zdalnych serwerów SMTP.

%prep
%setup -q
%patch0 -p1

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
