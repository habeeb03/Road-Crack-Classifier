# import tensorflow as tf
from predict import predict
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import os
import time
import shutil


start = time.time()

test_dir = input("Enter directory name to check: ")

try:
    basepath = os.getcwd()
    dir_path = basepath + '/data/train/{}'.format(test_dir)
    if not os.path.exists(dir_path):
        print("No such directory")
        raise Exception
    
    # Walk though all testing images one by one
    for root, dirs, files in os.walk(dir_path):
        for name in files:

            print("")
            image_path = name
            filename = dir_path +'/' +image_path
            print(filename)
            class_name = predict(filename)
            
            if class_name == test_dir:
                print("Herererere", basepath + '/data/test_ok/{}'.format(test_dir))
                shutil.copy(filename, basepath + '/data/test_ok/{}'.format(test_dir))
            #     print(basepath + '/data/test_ok/{}'.format(test_dir))
            
except Exception as e:
    print(e)