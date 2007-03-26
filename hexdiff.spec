Summary:	Visual diff for binary files
Summary(pl.UTF-8):	Odpowiednik diffa dla plików binarnych
Name:		hexdiff
Version:	0.0.48
Release:	1
License:	distributable
Group:		Applications/Text
Source0:	http://tboudet.free.fr/hexdiff/%{name}.tar.gz
# Source0-md5:	f606d3a6af616b53395102a2cb1a243c
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
	COPT="%{rpmcflags} -I/usr/include/ncurses -DVERSION=\\\"%{version}\\\" -DTRACE=0 -ansi"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
