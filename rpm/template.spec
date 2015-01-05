Name:           ros-indigo-concert-schedulers
Version:        0.6.3
Release:        0%{?dist}
Summary:        ROS concert_schedulers package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/concert_schedulers
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-concert-msgs
Requires:       ros-indigo-concert-scheduler-requests
Requires:       ros-indigo-rocon-app-manager-msgs
Requires:       ros-indigo-rocon-console
Requires:       ros-indigo-rocon-uri
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-rospy
Requires:       ros-indigo-scheduler-msgs
Requires:       ros-indigo-unique-id
Requires:       ros-indigo-uuid-msgs
BuildRequires:  ros-indigo-catkin

%description
Various schedulers for the concert

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
* Mon Jan 05 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.3-0
- Autogenerated by Bloom

* Tue Dec 02 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.2-0
- Autogenerated by Bloom

* Fri Nov 21 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.1-0
- Autogenerated by Bloom

* Mon Aug 25 2014 Daniel Stonier <d.stonier@gmail.com> - 0.6.0-0
- Autogenerated by Bloom

