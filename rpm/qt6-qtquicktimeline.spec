%global  qt_version 6.7.2

Summary: Qt6 - QuickTimeline plugin
Name:    qt6-qtquicktimeline
Version: 6.7.2
Release: 2%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
Source0: %{name}-%{version}.tar.bz2

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja
BuildRequires: qt6-rpm-macros >= %{qt_version}
BuildRequires: qt6-qtbase-static >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel


%description
The Qt Quick Timeline plugin provides QML types to use timelines and keyframes
to animate Qt Quick user interfaces.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_qt6

%cmake_build


%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/GPL*
%dir %{_qt6_qmldir}/QtQuick
%{_qt6_libdir}/libQt6QuickTimeline.so.6*
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.so.6*
%{_qt6_qmldir}/QtQuick/Timeline/

%files devel
%{_qt6_includedir}/QtQuickTimeline/
%{_qt6_includedir}/QtQuickTimelineBlendTrees/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6QuickTimeline/
%{_qt6_libdir}/cmake/Qt6QuickTimeline/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTrees/
%{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTrees/*.cmake
%{_qt6_libdir}/libQt6QuickTimeline.prl
%{_qt6_libdir}/libQt6QuickTimeline.so
%{_qt6_libdir}/libQt6QuickTimeline.prl
%{_qt6_libdir}/libQt6QuickTimeline.so
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.prl
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.so
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

