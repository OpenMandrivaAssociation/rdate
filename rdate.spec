Summary:	Retrieving the date and time from another machine on your network
Name:		rdate
Version:	1.5
Release:	2
License:	GPLv2
Group:		System/Configuration/Other
Url:		https://www.aelius.com/njh/rdate
Source0:	https://fossies.org/linux/misc/old/%{name}-%{version}.tar.gz
Patch0:		rdate-1.4-format_not_a_string_literal_and_no_format_arguments.diff

%description
The rdate utility retrieves the date and time from another machine on your
network, using the protocol described in RFC 868. If you run rdate as root, it
will set your machine's local time to the time of the machine that you queried.
Note that rdate isn't scrupulously accurate. If you are worried about
milliseconds, get the xntpd program instead.

%prep
%autosetup -p1

%build
sh autogen.sh
%configure
%make_build CFLAGS="%{optflags} -Wall -DINET6" CC="%{__cc}" LDFLAGS="%{ldflags}"

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

