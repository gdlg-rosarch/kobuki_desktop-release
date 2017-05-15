Name:           ros-kinetic-kobuki-gazebo
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS kobuki_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-gazebo-plugins
Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-kobuki-description
Requires:       ros-kinetic-kobuki-gazebo-plugins
Requires:       ros-kinetic-kobuki-random-walker
Requires:       ros-kinetic-kobuki-safety-controller
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-yocs-cmd-vel-mux
BuildRequires:  ros-kinetic-catkin

%description
Kobuki simulation for Gazebo

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
* Sun May 14 2017 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.5.7-0
- Autogenerated by Bloom

* Sat Apr 01 2017 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.5.6-0
- Autogenerated by Bloom

* Wed Mar 29 2017 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.5.5-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.5.3-0
- Autogenerated by Bloom

* Tue Sep 20 2016 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.5.1-0
- Autogenerated by Bloom

* Thu Aug 11 2016 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.5.0-0
- Autogenerated by Bloom

* Thu Aug 11 2016 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.4.2-0
- Autogenerated by Bloom

