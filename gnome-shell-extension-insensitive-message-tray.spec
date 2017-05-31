%global uuid insensitivetray@tovotu.de
%global gitdate 20170531
# Minimum GNOME Shell version supported
%global min_gs_version 3.6

Name:           gnome-shell-extension-insensitive-message-tray
Version:        %{gitdate}
Release:        1%{?dist}
Summary:        A gnome-shell extension to make the bottom message tray insensitive
Group:          User Interface/Desktops
License:        Unknown
URL:            https://github.com/fennm/insensitive-message-tray
Source0:        https://github.com/fennm/insensitive-message-tray/archive/master/%{name}-%{gitdate}.tar.gz

BuildArch:      noarch
Requires:       gnome-shell-extension-common >= %{min_gs_version}

%description
Renders Gnome's bottom message tray insensitive. It will no longer steal the
focus and move the screen when your mouse hits the bottom of the screen.

%prep
tar -tf %{SOURCE0}
%autosetup -p1 -n %{name}-master

%build


%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json} \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
* Wed May 31 2017 Michael Fenn <michaelfenn87@gmail.com> - 20170531-1
- initial spec file
