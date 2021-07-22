%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-ros
Version:        1.15.8
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ros package

License:        BSD
URL:            http://www.ros.org/wiki/ROS
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-catkin
Requires:       ros-noetic-mk
Requires:       ros-noetic-rosbash
Requires:       ros-noetic-rosboost-cfg
Requires:       ros-noetic-rosbuild
Requires:       ros-noetic-rosclean
Requires:       ros-noetic-roscreate
Requires:       ros-noetic-roslang
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rosmake
Requires:       ros-noetic-rosunit
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
ROS packaging system

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Jul 21 2021 Michel Hidalgo <michel@ekumenlabs.com> - 1.15.8-1
- Autogenerated by Bloom

* Mon Sep 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.7-1
- Autogenerated by Bloom

* Mon Jul 20 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.6-1
- Autogenerated by Bloom

* Mon Jul 06 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.5-1
- Autogenerated by Bloom

* Thu May 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.4-1
- Autogenerated by Bloom

* Thu May 14 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.3-1
- Autogenerated by Bloom

* Tue Apr 07 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.2-1
- Autogenerated by Bloom

* Tue Mar 17 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.1-1
- Autogenerated by Bloom

* Tue Feb 11 2020 Dirk Thomas <dthomas@osrfoundation.org> - 1.15.0-1
- Autogenerated by Bloom

