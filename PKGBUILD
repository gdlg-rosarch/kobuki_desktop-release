# Script generated with Bloom
pkgdesc="ROS - Kobuki simulation for Gazebo"
url='http://ros.org/wiki/kobuki_gazebo'

pkgname='ros-kinetic-kobuki-gazebo'
pkgver='0.5.7_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-gazebo-plugins'
'ros-kinetic-gazebo-ros'
'ros-kinetic-kobuki-description'
'ros-kinetic-kobuki-gazebo-plugins'
'ros-kinetic-kobuki-random-walker'
'ros-kinetic-kobuki-safety-controller'
'ros-kinetic-robot-state-publisher'
'ros-kinetic-yocs-cmd-vel-mux'
)

conflicts=()
replaces=()

_dir=kobuki_gazebo
source=()
md5sums=()

prepare() {
    cp -R $startdir/kobuki_gazebo $srcdir/kobuki_gazebo
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

