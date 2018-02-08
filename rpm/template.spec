Name:           ros-kinetic-rosmake
Version:        1.14.3
Release:        0%{?dist}
Summary:        ROS rosmake package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosmake
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-kinetic-catkin
BuildRequires:  ros-kinetic-catkin >= 0.5.68

%description
rosmake is a ros dependency aware build tool which can be used to build all
dependencies in the correct order.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Feb 08 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.3-0
- Autogenerated by Bloom

* Thu Nov 02 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.6-0
- Autogenerated by Bloom

* Tue Feb 14 2017 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.5-0
- Autogenerated by Bloom

* Mon Sep 19 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.4-0
- Autogenerated by Bloom

* Fri Sep 16 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.3-0
- Autogenerated by Bloom

* Fri Sep 02 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.2-0
- Autogenerated by Bloom

* Sun Mar 13 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.1-0
- Autogenerated by Bloom

* Thu Mar 10 2016 Dirk Thomas <dthomas@osrfoundation.org> - 1.13.0-0
- Autogenerated by Bloom

