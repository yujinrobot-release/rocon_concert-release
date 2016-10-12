Name:           ros-indigo-rocon-tf-reconstructor
Version:        0.6.11
Release:        1%{?dist}
Summary:        ROS rocon_tf_reconstructor package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-concert-msgs
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-tf
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-concert-msgs
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-tf

%description
The rocon_tf_reconstructor package

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
* Wed Oct 12 2016 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.11-1
- Autogenerated by Bloom

* Fri Aug 28 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.11-0
- Autogenerated by Bloom

* Thu Jul 09 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.9-0
- Autogenerated by Bloom

* Mon Apr 27 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.8-0
- Autogenerated by Bloom

* Mon Apr 06 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.7-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.6-0
- Autogenerated by Bloom

* Fri Feb 27 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.5-0
- Autogenerated by Bloom

* Mon Feb 09 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.4-0
- Autogenerated by Bloom

* Mon Jan 05 2015 Jihoon Lee <jihoonlee.in@gmail.com> - 0.6.3-0
- Autogenerated by Bloom

