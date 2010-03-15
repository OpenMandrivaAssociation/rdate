Summary:	Retrieving the date and time from another machine on your network
Name:		rdate
Version:	1.4
Release:	%mkrel 10
License:	GPL
Group:		System/Configuration/Other
URL:		ftp://people.redhat.com/sopwith
Source0:	ftp://people.redhat.com/sopwith/%{name}-%{version}.tar.bz2
Patch0:		rdate-1.4-udp.patch
Patch1:		rdate-1.4-format_not_a_string_literal_and_no_format_arguments.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The rdate utility retrieves the date and time from another machine on your
network, using the protocol described in RFC 868. If you run rdate as root, it
will set your machine's local time to the time of the machine that you queried.
Note that rdate isn't scrupulously accurate. If you are worried about
milliseconds, get the xntpd program instead.

%prep
%setup -q
%patch0 -p1 -b .udp
%patch1 -p0 -b .format_not_a_string_literal_and_no_format_arguments

%build
%make CFLAGS="%{optflags} -Wall -DINET6" CC="gcc" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
