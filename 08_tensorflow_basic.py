# -*- coding: utf-8 -*-
#Example of using GPU and CPU to do some operations
import os
import sys
import tensorflow as tf
import numpy as np
from datetime import datetime
#command line nvidia-smi
#NVIDIA Management Library (NVML),



shape = (int(100),int(100))
#using GPU as default device
sel=0
#comment to use default GPU and uncomment to use CPU
#sel=1
if sel==0:
    device_name = "/GPU:0"
else:
    device_name = "/CPU:0"




with tf.device(device_name):
    random_matrix = tf.random_uniform(shape=shape, minval=0, maxval=1)
    dot_operation = tf.matmul(random_matrix, tf.transpose(random_matrix))
    sum_operation = tf.reduce_sum(dot_operation)


startTime = datetime.now()
with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as session:
        result = session.run(sum_operation)
        print(result)

# It can be hard to see the results on the terminal with lots of output -- add some newlines to improve readability.
print("\n" * 5)
print("Shape:", shape, "Device:", device_name)
print("Time taken:", datetime.now() - startTime)

print("\n" * 5)
