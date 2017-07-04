# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 14:19:22 2017

@author: naveendivakaran
"""

# Python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))