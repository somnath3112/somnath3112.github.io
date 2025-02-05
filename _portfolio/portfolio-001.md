---
title: "[Active] Navigation and SLAM."
excerpt: "Extending the ORB-SLAM2 for robotics application.<br/><img src='/images/Video_snaps/orb_slam2_test.gif' style='width:640px;height:360px;'>"
collection: portfolio
---

<img src='/images/Video_snaps/pangolin_test.gif' style='width:640px;height:360px;'>

# Topics 
1. Setup 
2. Preliminary results 

## 1. Setup 

Before working with ORB-SLAM2 and its forks, you need to set up the following dependencies: **Pangolin** for real-time 3D visualization and debugging, **OpenCV** for computer vision tasks like feature detection, image preprocessing, pose estimation, and visualization, and **Eigen** for efficient linear algebra operations essential for SLAM algorithms. These dependencies ensure efficient and accurate performance of your SLAM system. 

### Pangolin 

Pangolin is a lightweight and efficient library for managing OpenGL display and interaction. It is particularly useful in SLAM (Simultaneous Localization and Mapping) applications for visualizing the 3D environment and the trajectory of the robot in real-time. By providing an intuitive interface for rendering graphics, Pangolin helps developers to debug and analyze the performance of their SLAM algorithms effectively.

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/pangolin_test.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/pangolin_test2.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

### OpenCV 3.2

OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It contains more than 2500 optimized algorithms, which can be used for a wide range of applications, including object detection, image segmentation, and face recognition.

In the context of SLAM (Simultaneous Localization and Mapping), OpenCV is particularly useful for processing and analyzing the visual data captured by the robot's cameras. Some of the key applications of OpenCV in SLAM include:

- **Feature Detection and Matching**: OpenCV provides various algorithms for detecting and matching features (e.g., ORB, SIFT, SURF) in images. These features are essential for tracking the robot's movement and building a map of the environment.
- **Image Preprocessing**: OpenCV offers tools for preprocessing images, such as filtering, edge detection, and histogram equalization. These preprocessing steps can enhance the quality of the visual data and improve the accuracy of the SLAM algorithms.
- **Pose Estimation**: OpenCV includes functions for estimating the pose of the robot by analyzing the visual data. This involves calculating the position and orientation of the robot relative to its surroundings.
- **Visualization**: OpenCV can be used to visualize the results of the SLAM process, such as the trajectory of the robot and the 3D map of the environment.

By utilizing OpenCV, developers can enhance the performance and accuracy of their SLAM systems, enabling robots to navigate and map their surroundings more effectively.

**Video Description:** In the video-test to show open CV and Pangolin working together, we demonstrate the process of loading a test image, applying edge detection, and then displaying the result in a rotation animation. The edge detection algorithm highlights the boundaries within the image, making it easier to identify distinct features. The rotation animation provides a dynamic view of the processed image, showcasing the effectiveness of the edge detection technique.

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/dual_cv_pangolin_test.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

### Eigen 

Eigen is a C++ template library for linear algebra, including matrices, vectors, numerical solvers, and related algorithms. It is highly efficient and versatile, making it a popular choice for many scientific computing projects.

In the context of SLAM (Simultaneous Localization and Mapping), Eigen is used extensively for matrix and vector operations, which are fundamental to the algorithms involved. For instance, Eigen is used for transformations, optimizations, and solving systems of linear equations, all of which are critical for accurately mapping the environment and determining the robot's position within it.

By leveraging Eigen, developers can ensure that their SLAM implementations are both fast and reliable, enabling real-time performance and accurate results in robotics applications.

## 2. Preliminary results 

### ORB-SLAM2 

ORB-SLAM2 is a versatile and highly efficient SLAM (Simultaneous Localization and Mapping) system that can operate in real-time. It is capable of processing monocular, stereo, and RGB-D camera inputs, making it suitable for a wide range of applications in robotics and computer vision.

Key features of ORB-SLAM2 include:

- **Feature Extraction and Matching**: ORB-SLAM2 uses ORB (Oriented FAST and Rotated BRIEF) features for tracking and mapping. These features are robust to changes in lighting and viewpoint, making them ideal for SLAM applications.
- **Local Mapping**: The system maintains a local map of the environment, which is continuously updated as the robot moves. This local map is used to optimize the robot's trajectory and improve the accuracy of the SLAM process.
- **Loop Closing**: ORB-SLAM2 includes a loop closing mechanism that detects when the robot revisits a previously mapped area. This allows the system to correct any drift in the robot's trajectory and improve the overall consistency of the map.
- **Relocalization**: If the robot loses track of its position, ORB-SLAM2 can relocalize itself by matching the current view with the existing map. This ensures that the system can recover from tracking failures and continue operating effectively.

The preliminary results of our experiments with ORB-SLAM2 demonstrate its ability to accurately track the robot's movement and build a detailed map of the environment. The system performs well in various scenarios, including indoor and outdoor environments, and can handle challenging conditions such as dynamic objects and changes in lighting.

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/orb_slam2_test.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
