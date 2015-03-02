Name:           ros-indigo-kobuki-dashboard
Version:        0.4.2
Release:        0%{?dist}
Summary:        ROS kobuki_dashboard package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/kobuki_dashboard
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-kobuki-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rqt-robot-dashboard
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-kobuki-msgs
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rqt-robot-dashboard

%description
The Kobuki dashboard is a RQT-based plug-in for visualising data from Kobuki and
giving easy access to basic functionalities.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Mar 02 2015 Marcus Liebhardt <marcus.liebhardt@yujinrobot.com> - 0.4.2-0
- Autogenerated by Bloom

