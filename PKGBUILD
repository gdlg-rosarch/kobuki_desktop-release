# Script generated with Bloom
pkgdesc="ROS - Visualisation and simulation tools for Kobuki"
url='http://ros.org/wiki/kobuki_desktop'

pkgname='ros-kinetic-kobuki-desktop'
pkgver='0.5.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-kobuki-dashboard'
'ros-kinetic-kobuki-gazebo'
'ros-kinetic-kobuki-gazebo-plugins'
'ros-kinetic-kobuki-qtestsuite'
'ros-kinetic-kobuki-rviz-launchers'
)

conflicts=()
replaces=()

_dir=kobuki_desktop
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_desktop $srcdir/kobuki_desktop
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

