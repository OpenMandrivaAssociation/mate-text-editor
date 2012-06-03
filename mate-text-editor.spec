%define _disable_ld_no_undefined 1
%define build_python 1

Summary:	Small but powerful text editor for MATE
Name:		mate-text-editor
Version:	1.2.0
Release:	1
License:	GPLv2+
Group:		Editors 
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	mate-conf
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(enchant)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gtksourceview-2.0)
BuildRequires:	pkgconfig(iso-codes)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
%if %{build_python}
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(pygtksourceview-2.0)
%endif

%description
Pluma is a small but powerful text editor designed expressly
for MATE.

It includes such features as split-screen mode, a plugin
API, which allows Pluma to be extended to support many
features while remaining small at its core, multiple
document editing through the use of a 'tabbed' notebook and
many more functions.

%package devel
Group:		Development/C
Summary:	Headers for writing Pluma plugins

%description devel
Install this if you want to build plugins that use Pluma's API.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--enable-gtk-doc \
%if %{build_python}
	--enable-python \
%else
	--disable-python \
%endif
	--disable-updater \
	--enable-gvfs-metadata

%make LIBS='-lm -lgmodule-2.0'

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang pluma --with-gnome

%files -f pluma.lang
%doc README AUTHORS NEWS
%{_sysconfdir}/mateconf/schemas/pluma-file-browser.schemas
%{_sysconfdir}/mateconf/schemas/pluma.schemas
%{_bindir}/*
%{_datadir}/applications/pluma.desktop
%{_datadir}/pluma
%{_mandir}/man1/pluma.1*
# mate help files
%{_datadir}/mate/help/*

%dir %{_libdir}/pluma
%{_libdir}/pluma/pluma-bugreport.sh
%dir %{_libdir}/pluma/plugin-loaders
%{_libdir}/pluma/plugin-loaders/libcloader.so
%{_libdir}/pluma/plugin-loaders/libpythonloader.so
%dir %{_libdir}/pluma/plugins
%{_libdir}/pluma/plugins/changecase.pluma-plugin
%{_libdir}/pluma/plugins/docinfo.pluma-plugin
%{_libdir}/pluma/plugins/filebrowser.pluma-plugin
%{_libdir}/pluma/plugins/libtaglist.so
%{_libdir}/pluma/plugins/modelines.pluma-plugin
%{_libdir}/pluma/plugins/sort.pluma-plugin
%{_libdir}/pluma/plugins/spell.pluma-plugin
%{_libdir}/pluma/plugins/taglist.pluma-plugin
%{_libdir}/pluma/plugins/time.pluma-plugin
%{_libdir}/pluma/plugins/libchangecase.so
%{_libdir}/pluma/plugins/libdocinfo.so
%{_libdir}/pluma/plugins/libfilebrowser.so
%{_libdir}/pluma/plugins/libmodelines.so
%{_libdir}/pluma/plugins/libsort.so
%{_libdir}/pluma/plugins/libspell.so
%{_libdir}/pluma/plugins/libtime.so
%if %{build_python}
%{_libdir}/pluma/plugins/externaltools.pluma-plugin
%{_libdir}/pluma/plugins/pythonconsole.pluma-plugin
%{_libdir}/pluma/plugins/quickopen.pluma-plugin
%{_libdir}/pluma/plugins/snippets.pluma-plugin
%{_libdir}/pluma/plugins/externaltools/*
%{_libdir}/pluma/plugins/pythonconsole/*
%{_libdir}/pluma/plugins/quickopen/*
%{_libdir}/pluma/plugins/snippets/*
%endif

%files devel
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/pkgconfig/*

