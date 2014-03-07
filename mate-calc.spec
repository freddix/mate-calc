Summary:	MATE calculator
Name:		mate-calc
Version:	1.8.0
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	8a22d9a65599163fa94d240fab5c15f2
URL:		http://mate-desktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MATE-calc is a simple calculator that performs a variety of functions.

%prep
%setup -q

# kill gnome common deps
%{__sed} -i -e 's/MATE_COMPILE_WARNINGS.*//g'	\
    -i -e 's/MATE_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/MATE_COMMON_INIT//g'		\
    -i -e 's/MATE_CXX_WARNINGS.*//g'		\
    -i -e 's/MATE_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules		\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mate-calc
%attr(755,root,root) %{_bindir}/mate-calc-cmd
%attr(755,root,root) %{_bindir}/mate-calculator
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_datadir}/mate-calc
%{_desktopdir}/mate-calc.desktop
%{_mandir}/man1/mate-calc-cmd.1*
%{_mandir}/man1/mate-calc.1*

