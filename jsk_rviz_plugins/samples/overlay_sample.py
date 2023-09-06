#!/usr/bin/env python
try:
  from jsk_rviz_plugins.msg import *
except:
  import roslib;roslib.load_manifest("jsk_rviz_plugins")
  from jsk_rviz_plugins.msg import *

from std_msgs.msg import ColorRGBA, Float32
import rospy
import math

density = 0.0;


rospy.init_node("overlay_sample")

text_pub = rospy.Publisher("text_sample", OverlayText, queue_size=1)
# value_pub = rospy.Publisher("value_sample", Float32, queue_size=1)

def callback(data):
    density = data.data
    text = OverlayText()
    theta = counter % 255 / 255.0
    text.width = 500
    text.height = 100
    #text.height = 600
    text.left = 10
    text.top = 10
    text.text_size = 25
    text.line_width = 2
    text.font = "DejaVu Sans Mono"
    text.text = """
  density is %0.1f people/m^2
    """ % (density)
    text.fg_color = ColorRGBA(25 / 255.0, 1.0, 240.0 / 255.0, 1.0)
    text.bg_color = ColorRGBA(0.0, 0.0, 0.0, 0.2)
    text_pub.publish(text)

rospy.Subscriber("/people_density", Float32, callback)


counter = 0
rate = 100
rospy.spin();
# r = rospy.Rate(rate)
# import random, math
# while not rospy.is_shutdown():
#   counter = counter + 1
#   text = OverlayText()
#   theta = counter % 255 / 255.0
#   text.width = 400
#   text.height = 60
#   #text.height = 600
#   text.left = 10
#   text.top = 10
#   text.text_size = 12
#   text.line_width = 2
#   text.font = "DejaVu Sans Mono"
#   text.text = """
# density is %0.1f people/m^2
#   """ % (density)
#   text.fg_color = ColorRGBA(25 / 255.0, 1.0, 240.0 / 255.0, 1.0)
#   text.bg_color = ColorRGBA(0.0, 0.0, 0.0, 0.2)
#   text_pub.publish(text)
#   # value_pub.publish(math.sin(counter * math.pi * 2 / 100))
#   # if int(counter % 500) == 0:
#   #   rospy.logdebug('This is ROS_DEBUG.')
#   # elif int(counter % 500) == 100:
#   #   rospy.loginfo('This is ROS_INFO.')
#   # elif int(counter % 500) == 200:
#   #   rospy.logwarn('This is ROS_WARN.')
#   # elif int(counter % 500) == 300:
#   #   rospy.logerr('This is ROS_ERROR.')
#   # elif int(counter % 500) == 400:
#   #   rospy.logfatal('This is ROS_FATAL.')
#   r.sleep()

