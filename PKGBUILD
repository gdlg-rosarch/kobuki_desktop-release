# Script generated with Bloom
pkgdesc="ROS - The Kobuki dashboard is a RQT-based plug-in for visualising data from Kobuki and giving easy access to basic functionalities."
url='http://ros.org/wiki/kobuki_dashboard'

pkgname='ros-kinetic-kobuki-dashboard'
pkgver='0.5.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-kobuki-msgs'
'ros-kinetic-rospy'
'ros-kinetic-rqt-robot-dashboard'
)

depends=('ros-kinetic-kobuki-msgs'
'ros-kinetic-rospy'
'ros-kinetic-rqt-robot-dashboard'
)

conflicts=()
replaces=()

_dir=kobuki_dashboard
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_dashboard $srcdir/kobuki_dashboard
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

