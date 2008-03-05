Summary:	Retrieving the date and time from another machine on your network
Name:		rdate
Version:	1.4
Release:	%mkrel 5
License:	GPL
Group:		System/Configuration/Other
URL:		ftp://people.redhat.com/sopwith
Source0:	ftp://people.redhat.com/sopwith/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The rdate utility retrieves the date and time from another machine on your
network, using the protocol described in RFC 868. If you run rdate as root, it
will set your machine's local time to the time of the machine that you queried.
Note that rdate isn't scrupulously accurate. If you are worried about
milliseconds, get the xntpd program instead.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS -Wall" CC="gcc"

%install
rm -rf %{buildroot}
install -m755 -s %{name} -D %{buildroot}%{_bindir}/%{name}
install -m644 %{name}.1 -D %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


