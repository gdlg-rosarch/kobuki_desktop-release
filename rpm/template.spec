Name:           ros-kinetic-kobuki-qtestsuite
Version:        0.5.6
Release:        0%{?dist}
Summary:        ROS kobuki_qtestsuite package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_qtestsuite
Source0:        %{name}-%{version}.tar.gz

Requires:       PyQt4-devel
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-kobuki-testsuite
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-qt-gui-py-common
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-rqt-gui
Requires:       ros-kinetic-rqt-gui-py
Requires:       ros-kinetic-rqt-plot
Requires:       ros-kinetic-rqt-py-common
BuildRequires:  python-qt5-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-kobuki-testsuite
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-qt-gui-py-common
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-rqt-gui
BuildRequires:  ros-kinetic-rqt-gui-py
BuildRequires:  ros-kinetic-rqt-plot
BuildRequires:  ros-kinetic-rqt-py-common

%description
An rqt plugin that provides a graphical, interactive testsuite for Kobuki.

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
* Sat Apr 01 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.5.6-0
- Autogenerated by Bloom

* Wed Mar 29 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.5.5-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Daniel Stonier <stonier@yujinrobot.com> - 0.5.3-0
- Autogenerated by Bloom

* Tue Sep 20 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.5.1-0
- Autogenerated by Bloom

* Thu Aug 11 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.5.0-0
- Autogenerated by Bloom

* Thu Aug 11 2016 Daniel Stonier <stonier@yujinrobot.com> - 0.4.2-0
- Autogenerated by Bloom

