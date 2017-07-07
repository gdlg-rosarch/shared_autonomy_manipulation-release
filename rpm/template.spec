Name:           ros-indigo-safe-teleop-pr2
Version:        0.0.1
Release:        0%{?dist}
Summary:        ROS safe_teleop_pr2 package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/safe_teleop_pr2
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-joy
Requires:       ros-indigo-pr2-teleop
Requires:       ros-indigo-safe-teleop-base
BuildRequires:  ros-indigo-catkin

%description
Launch files for running safe_teleop_base on pr2

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
        -DCMAKE_INSTALL_LIBDIR="lib" \
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
* Fri Jul 07 2017 Charles DuHadway (maintained by Benjamin Pitzer) <foo@foo.com> - 0.0.1-0
- Autogenerated by Bloom

