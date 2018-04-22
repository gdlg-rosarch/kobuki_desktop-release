# Script generated with Bloom
pkgdesc="ROS - An rqt plugin that provides a graphical, interactive testsuite for Kobuki."
url='http://ros.org/wiki/kobuki_qtestsuite'

pkgname='ros-kinetic-kobuki-qtestsuite'
pkgver='0.5.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('python2-pyqt5'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-testsuite'
'ros-kinetic-nav-msgs'
'ros-kinetic-qt-gui-py-common'
'ros-kinetic-rospy'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-plot'
'ros-kinetic-rqt-py-common'
)

depends=('python2-pyqt5'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kobuki-testsuite'
'ros-kinetic-nav-msgs'
'ros-kinetic-qt-gui-py-common'
'ros-kinetic-rospy'
'ros-kinetic-rqt-gui'
'ros-kinetic-rqt-gui-py'
'ros-kinetic-rqt-plot'
'ros-kinetic-rqt-py-common'
)

conflicts=()
replaces=()

_dir=kobuki_qtestsuite
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_qtestsuite $srcdir/kobuki_qtestsuite
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

