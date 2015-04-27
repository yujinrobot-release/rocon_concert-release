Name:           ros-indigo-rocon-concert
Version:        0.6.8
Release:        0%{?dist}
Summary:        ROS rocon_concert package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/rocon_concert
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-concert-conductor
Requires:       ros-indigo-concert-master
Requires:       ros-indigo-concert-schedulers
Requires:       ros-indigo-concert-service-link-graph
Requires:       ros-indigo-concert-service-manager
Requires:       ros-indigo-concert-service-utilities
Requires:       ros-indigo-concert-software-farmer
Requires:       ros-indigo-concert-utilities
Requires:       ros-indigo-rocon-tf-reconstructor
BuildRequires:  ros-indigo-catkin

%description
The concert framework modules.

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
* Mon Apr 27 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.8-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.7-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.6-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.5-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.4-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Daniel Stonier <d.stonier@gmail.com> - 0.6.3-0
- Autogenerated by Bloom

