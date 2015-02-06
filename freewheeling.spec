%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define svn_snapshot svn20110421
%endif

Name:           freewheeling
Summary:        Live Audio Looper
Version:        0.6
%if %branch
Release:        %mkrel -c %svn_snapshot 1
%else
Release:        2
%endif
%if %branch
Source:         http://freewheeling.svn.sourceforge.net/viewvc/freewheeling/%{name}.tar.gz
%else
Source:         http://dl.sf.net/%{name}/%{version}/%{name}-%{version}.tar.bz2
%endif
Patch0:         freewheeling-0.6-strfmt.patch
URL:            http://%{name}.sourceforge.net/
License:        GPLv2
Group:          Sound

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(SDL_ttf) 
BuildRequires:  pkgconfig(SDL_gfx)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(fluidsynth) 
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(gnutls)

%description
FreeWheeling is an audio tool for live looping. It provides a highly
configurable, fluid user interface for instrumentalists to capture
loops in real-time.

%prep
%if %branch
%setup -q -n %{name}
%patch0 -p0 -b .strfmt
%else
%setup -q
%endif

%build
export LDFLAGS="${LDFLAGS} -logg -lSDL" 
%if %branch
autoreconf -i
%endif

%configure
%make

%install
%makeinstall_std

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Freewheeling
Comment=Live Looper
Exec=%{_bindir}/fweelin
Icon=sound_section
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
Encoding=UTF-8
EOF

%files
%doc README NEWS COPYING AUTHORS
%{_bindir}/fweelin
%{_datadir}/fweelin
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Thu Apr 21 2011 Frank Kober <emuse@mandriva.org> 0.6-0.svn20110421.1mdv2011.0
+ Revision: 656495
- import freewheeling

