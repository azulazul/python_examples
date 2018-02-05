
To install tensorflow in opensuse 42.3

1. Install nvidia drivers
2. Install nvidia cuda https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=OpenSUSE&target_version=Leap423&target_type=rpmlocal
3. Install libcupti-dev
4. Download tensorflow with cuda support (check the version of python )
5. Make a directory for tensorflow
6. Run
   sudo pip install tensorflow-gpu


More info in:
https://www.tensorflow.org/versions/r0.12/get_started/os_setup
