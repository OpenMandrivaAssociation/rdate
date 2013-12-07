Summary:	Retrieving the date and time from another machine on your network
Name:		rdate
Version:	1.4
Release:	18
License:	GPL
Group:		System/Configuration/Other
URL:		ftp://people.redhat.com/sopwith
Source0:	ftp://people.redhat.com/sopwith/%{name}-%{version}.tar.bz2
Patch0:		rdate-1.4-udp.patch
Patch1:		rdate-1.4-format_not_a_string_literal_and_no_format_arguments.diff

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
%make CFLAGS="%{optflags} -Wall -DINET6" CC="%{__cc}" LDFLAGS="%{ldflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-12mdv2011.0
+ Revision: 669411
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-11mdv2011.0
+ Revision: 607324
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4-10mdv2010.1
+ Revision: 520208
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4-9mdv2010.0
+ Revision: 426878
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-8mdv2009.1
+ Revision: 317567
- fix build with -Werror=format-security (P1)
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4-7mdv2009.0
+ Revision: 225313
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-6mdv2008.1
+ Revision: 180901
- added P0 from fedora, fixes #35342

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4-5mdv2008.1
+ Revision: 179418
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-4mdv2007.1
+ Revision: 145463
- Import rdate

* Sat Mar 17 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4-4mdv2007.1
- use the %%mrel macro

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.4-3mdk
- Rebuild

* Sun Dec 05 2004 Abel Cheung <deaddog@mandrake.org> 1.4-2mdk
- manpage is an ELF binary!?
- adjust group

* Thu Jun 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.4-1mdk
- 1.4
- cosmetics

