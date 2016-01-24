Summary:	Visual diff for binary files
Summary(pl.UTF-8):	Odpowiednik diffa dla plików binarnych
Name:		hexdiff
Version:	0.0.50
Release:	4
License:	distributable
Group:		Applications/Text
Source0:	http://tboudet.free.fr/hexdiff/%{name}.tar.gz
# Source0-md5:	68dbf4c610f4fd1817401bcf6c671b71
Source1:	http://manpages.ubuntu.com/manpages.gz/vivid/man1/hexdiff.1.gz
# Source1-md5:	33bc4cc881971bd3f5d59ae42f9ab415
URL:		http://tboudet.free.fr/hexdiff/
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visuel Hexdiff displays binary files differences in hex and ASCII.

%description -l pl.UTF-8
Visuel Hexdiff pokazuje szesnastkowo oraz tekstowo różnice pomiędzy
plikami.

%prep
%setup -q -n HexDiff

%build
%{__make} \
	COMP="%{__cc}" \
	COPT="%{rpmcppflags} %{rpmcflags} -I/usr/include/ncurses -DVERSION=\\\"%{version}\\\" -DTRACE=0 -ansi"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{,fr}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
zcat %{SOURCE1} >  $RPM_BUILD_ROOT%{_mandir}/man1/hexdiff.1
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/fr/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%attr(755,root,root) %{_bindir}/hexdiff
%{_mandir}/man1/hexdiff.1*
%{_mandir}/fr/man1/hexdiff.1*
