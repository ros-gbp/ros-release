Name:           ros-melodic-rosmake
Version:        1.14.7
Release:        1%{?dist}
Summary:        ROS rosmake package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rosmake
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-melodic-catkin
BuildRequires:  ros-melodic-catkin >= 0.5.68

%description
rosmake is a ros dependency aware build tool which can be used to build all
dependencies in the correct order.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Oct 03 2019 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.7-1
- Autogenerated by Bloom

* Mon Mar 18 2019 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.6-0
- Autogenerated by Bloom

* Mon Mar 04 2019 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.5-0
- Autogenerated by Bloom

* Tue May 01 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.4-0
- Autogenerated by Bloom

* Tue Jan 30 2018 Dirk Thomas <dthomas@osrfoundation.org> - 1.14.3-0
- Autogenerated by Bloom

