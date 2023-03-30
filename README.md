# Setup
``` bash
mkdir -p ws/src && cd ws/src
git clone https://github.com/Serafadam/interbotix_depthai_demo.git
cd interbotix_depthai_demo
sudo cp 99-interbotix-udev.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
docker buildx build --platform amd64 --build-arg ROS_DISTRO=humble --load -t interbotix_depthai_demo .
xhost +local:docker
docker run -it -v /dev/:/dev/ --network host --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix interbotix_depthai_demo
```
