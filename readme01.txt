
To install tensorflow

1. Install nvidia drivers
2. Install nvidia cuda from rpm
nvidia cuda muste be 9.0 and cuDNN 7.0 for tensorflow_gpu-1.5.0

add to the .bashrc or .profile file
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64\ {LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

or instead
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=/usr/local/cuda/include:$LD_LIBRARY_PATH
LD_LIBRARY_PATH=/usr/local/cuda:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH


2. Install cuDNN
nvidia cuda muste be 9.0 and cuDNN 7.0 for tensorflow_gpu-1.5.0

cudnn-9.1-linux-x64-v7 is for cuda 9.1
cudnn-9.0-linux-x64-v7 is for cuda 9.0

tar xvzf cudnn-9.0-linux-x64-v7.tgz
sudo cp -P cuda/include/cudnn.h /usr/local/cuda/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
3. Install libcupti-dev for nvidia<=7.x
4. Download tensorflow with cuda support (check the version of python )
5. Make a directory for tensorflow
6. sudo apt-get install python-pip python-dev
7. Run
   check pip --version and python version
   pip2.7 is used in opensuse 42.3

   sudo pip2.7 install tensorflow-gpu
   sudo pip2.7 install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.5.0-cp27-none-linux_x86_64.whl

8. Install pandas library for csv support
  sudo pip2.7 install pandas

9. Optional Install pytest
  sudo pip2.7 install pytest
  test panda
  import pandas as pd
  pd.test()

More info in:
https://www.tensorflow.org/versions/r0.12/get_started/os_setup
non cuda tensorflow
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-linux_x86_64.whl
