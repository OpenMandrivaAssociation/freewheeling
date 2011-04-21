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
Release:        %mkrel 1
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  alsa-lib-devel jackit-devel
BuildRequires:  SDL_ttf-devel SDL_gfx-devel freetype2-devel liblo-devel
BuildRequires:  libxml2-devel fluidsynth-devel sndfile-devel libvorbis-devel
BuildRequires:  gnutls-devel

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
%if %branch
autoreconf -i
%endif

%configure
%make

%install
rm -rf %{buildroot}
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS COPYING AUTHORS
%{_bindir}/fweelin
%{_datadir}/fweelin

%{_datadir}/applications/mandriva-%{name}.desktop

