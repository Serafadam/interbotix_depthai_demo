ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}-ros-base

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
   && apt-get -y install --no-install-recommends software-properties-common git libusb-1.0-0-dev wget zsh python3-colcon-common-extensions curl

RUN sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

RUN curl 'https://raw.githubusercontent.com/Interbotix/interbotix_ros_manipulators/main/interbotix_ros_xsarms/install/amd64/xsarm_amd64_install.sh' > xsarm_amd64_install.sh
RUN chmod +x xsarm_amd64_install.sh
ENV WS=/ws
RUN ./xsarm_amd64_install.sh -d humble -n -p $WS

RUN mkdir -p $WS/src
COPY ./ .$WS/src/interbotix_depthai_demo
RUN cd .$WS/ && rosdep install --from-paths src --ignore-src  -y

RUN cd .$WS/ && . /opt/ros/${ROS_DISTRO}/setup.sh && colcon build --symlink-install
RUN echo "if [ -f ${WS}/install/setup.zsh ]; then source ${WS}/install/setup.zsh; fi" >> $HOME/.zshrc
RUN echo 'eval "$(register-python-argcomplete3 ros2)"' >> $HOME/.zshrc
RUN echo 'eval "$(register-python-argcomplete3 colcon)"' >> $HOME/.zshrc
RUN echo "if [ -f ${WS}/install/setup.bash ]; then source ${WS}/install/setup.bash; fi" >> $HOME/.bashrc
ENTRYPOINT [ "/ws/src/interbotix_depthai_demo/entrypoint.sh" ]
CMD ["zsh"]