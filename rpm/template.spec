Name:           ros-indigo-concert-master
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS concert_master package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/concert_master
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-concert-conductor
Requires:       ros-indigo-concert-msgs
Requires:       ros-indigo-concert-schedulers
Requires:       ros-indigo-concert-service-manager
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-gateway
Requires:       ros-indigo-rocon-hub
Requires:       ros-indigo-rocon-icons
Requires:       ros-indigo-rocon-interactions
Requires:       ros-indigo-rocon-master-info
Requires:       ros-indigo-rocon-python-comms
Requires:       ros-indigo-rocon-python-utils
Requires:       ros-indigo-rocon-std-msgs
Requires:       ros-indigo-rosbridge-server
Requires:       ros-indigo-rospy
Requires:       ros-indigo-zeroconf-avahi
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-indigo-catkin

%description
General concert functionality.

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
* Mon Feb 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.4-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.3-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.1-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.0-0
- Autogenerated by Bloom

