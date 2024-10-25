---
title: "IMU interface - 3D visualization."
excerpt: "IMU interface and visualization in Matlab.<br/><img src='/images/qped_thumbnail.png'>"
collection: portfolio
---

A hobby project from my masters showing IMU interface to update the orientation of a virtual cuboid. [Youtube link](https://www.youtube.com/watch?v=GLnzKuQvPm8). 

The setup utilizes Atmega128 microcontroller to interface with the MPU-6050 IMU device using I2C protocol. The gyroscope data is ternsmitted to matlab via USB2UART converter for serial communication. The simulink model integrates the angular rate information and feed to the angles to the Virtual Reality Toolbox. 
 
