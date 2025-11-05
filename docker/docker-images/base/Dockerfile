

FROM moveit/moveit:noetic-source
LABEL maintainer="Gido Dielemans <gido.dielemans@tum.de>"

SHELL ["/bin/bash","-c"]

# All apt-get commands start with an update, then install
# and finally, a cache cleanup to keep the image size small.

# Install packages
RUN apt-get update \
    && apt-get install -y \
    # Basic utilities
    git \
    net-tools \ 
    iputils-ping \
    dnsutils \
    # ROS bridge server and related packages
    ros-${ROS_DISTRO}-rosbridge-server \
    # ros-${ROS_DISTRO}-tf2-web-republisher   # NOT yet published?   \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Create local catkin workspace
ENV CATKIN_WS=/root/catkin_ws
RUN mkdir -p $CATKIN_WS/src
WORKDIR $CATKIN_WS/src

# Initialize local catkin workspace
RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
    && apt-get update \
    # ROS File Server
    && git clone https://github.com/gramaziokohler/ros_file_server.git \
    # Install dependencies
    && cd $CATKIN_WS \
    && rosdep install -y --from-paths . --ignore-src --rosdistro ${ROS_DISTRO} \
    # Build catkin workspace
    && catkin_make

# Always source ros_catkin_entrypoint.sh when launching bash (e.g. when attaching to container)
RUN echo "source /usr/local/bin/ros_catkin_entrypoint.sh" >> /root/.bashrc

COPY roscore_check.py /usr/local/bin/roscore_check.py
COPY ros_catkin_entrypoint.sh /usr/local/bin/ros_catkin_entrypoint.sh

RUN chmod +x /usr/local/bin/roscore_check.py
RUN chmod +x /usr/local/bin/ros_catkin_entrypoint.sh

ENTRYPOINT ["/usr/local/bin/ros_catkin_entrypoint.sh"]
CMD ["bash"]

# Add robot packages to local catkin workspace
RUN echo "Building common MoveIt Planners" \
    && source /opt/ros/${ROS_DISTRO}/setup.bash \
    && apt-get update && apt-get -y upgrade \
    # ABB packages (abb_driver only included because some other packages reference it, but we don't use it)
    && git clone https://github.com/gidodielemans/abb.git \
    && git clone https://github.com/ros-industrial/abb_driver.git \
    && git clone https://github.com/ros-industrial/abb_experimental.git \
    && git clone https://github.com/gramaziokohler/abb_crb15000_5_95_moveit_config.git \
    # RRC packages
    && git clone https://github.com/compas-rrc/compas_rrc_ros.git \
    # Install dependencies
    && cd $CATKIN_WS \
    && rosdep install -y --from-paths . --ignore-src --skip-keys="abb_driver gazebo" --rosdistro ${ROS_DISTRO} \
    # Build catkin workspace
    && catkin_make \
    && rm -rf /var/lib/apt/lists/*