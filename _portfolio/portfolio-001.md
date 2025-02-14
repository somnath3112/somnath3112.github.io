---
title: "[Active] Navigation and SLAM."
excerpt: "Extending ORB-SLAM2 & 3 for robotics application.<br/><img src='/images/Video_snaps/orb_slam2_test.gif' style='width:640px;height:360px;'>"
collection: portfolio
---

_Collaborators: Vivek Yogi_
# Topics 
1. Setup 
2. Preliminary results 

## 1. Setup 

Before working with ORB-SLAM2 and ORB-SLAM3 and their forks, you need to set up the following dependencies: **Pangolin** for real-time 3D visualization and debugging, **OpenCV** for computer vision tasks like feature detection, image preprocessing, pose estimation, and visualization, and **Eigen** for efficient linear algebra operations essential for SLAM algorithms. These dependencies ensure efficient and accurate performance of your SLAM system. 

### Pangolin 

Pangolin is a lightweight and efficient library for managing OpenGL display and interaction. It is particularly useful in SLAM (Simultaneous Localization and Mapping) applications for visualizing the 3D environment and the trajectory of the robot in real-time. By providing an intuitive interface for rendering graphics, Pangolin helps developers to debug and analyze the performance of their SLAM algorithms effectively.

<img src='/images/Video_snaps/pangolin_test.gif' style='width:640px;height:360px;'>

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

### ORB-SLAM2, VI-ORB-SLAM2, and ORB-SLAM3

ORB-SLAM2 and ORB-SLAM3 are versatile and highly efficient SLAM (Simultaneous Localization and Mapping) systems that can operate in real-time. They are capable of processing monocular, stereo, and RGB-D camera inputs, making them suitable for a wide range of applications in robotics and computer vision.

Key features of ORB-SLAM2 and ORB-SLAM3 include:

- **Feature Extraction and Matching**: Both systems use ORB (Oriented FAST and Rotated BRIEF) features for tracking and mapping. These features are robust to changes in lighting and viewpoint, making them ideal for SLAM applications.
- **Local Mapping**: The systems maintain a local map of the environment, which is continuously updated as the robot moves. This local map is used to optimize the robot's trajectory and improve the accuracy of the SLAM process.
- **Loop Closing**: ORB-SLAM2 and ORB-SLAM3 include a loop closing mechanism that detects when the robot revisits a previously mapped area. This allows the systems to correct any drift in the robot's trajectory and improve the overall consistency of the map.
- **Relocalization**: If the robot loses track of its position, both systems can relocalize themselves by matching the current view with the existing map. This ensures that the systems can recover from tracking failures and continue operating effectively.

The preliminary results of our experiments with ORB-SLAM2 demonstrate their ability to accurately track the robot's movement and build a detailed map of the environment. The systems perform well in various scenarios, including indoor and outdoor environments, and can handle challenging conditions such as dynamic objects and changes in lighting.

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/orb_slam2_test.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/res1_slam2.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

The preliminary results of our experiments with VI-ORB-SLAM2 show its capability to handle visual-inertial data effectively. VI-ORB-SLAM2 integrates visual information from cameras with inertial measurements from IMUs (Inertial Measurement Units), providing more robust and accurate SLAM performance, especially in challenging environments.

Key observations from our experiments include:

- **Improved Robustness**: The integration of inertial data helps in maintaining accurate tracking even in scenarios with rapid motion or temporary visual occlusions. This results in a more stable and reliable SLAM system.
- **Enhanced Accuracy**: By combining visual and inertial data, VI-ORB-SLAM2 can achieve higher accuracy in both trajectory estimation and map building. This is particularly beneficial in environments with poor lighting or repetitive textures where visual-only SLAM might struggle.
- **Better Loop Closure**: The inertial data aids in detecting loop closures more reliably, reducing drift and improving the overall consistency of the map.

The results demonstrate that VI-ORB-SLAM2 is well-suited for applications requiring high precision and robustness, such as autonomous navigation in complex and dynamic environments.

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/vi_orb_slam2_test.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<!-- <video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/res1_vislam2.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video> -->

The preliminary results of our experiments with ORB-SLAM3 highlight its advanced capabilities in handling various SLAM tasks. ORB-SLAM3 extends the functionalities of ORB-SLAM2 by supporting monocular, stereo, and RGB-D cameras, as well as visual-inertial systems. This makes it a versatile solution for a wide range of applications in robotics and computer vision.

Key observations from our experiments with ORB-SLAM3 include:

- **Enhanced Feature Tracking**: ORB-SLAM3 improves upon the feature tracking capabilities of its predecessor by incorporating more robust algorithms for feature extraction and matching. This results in more accurate and reliable tracking, even in challenging environments with dynamic objects and varying lighting conditions.
- **Improved Map Management**: The system includes advanced map management techniques that allow for more efficient handling of large-scale environments. This includes better data association, map pruning, and optimization strategies that enhance the overall performance of the SLAM process.
- **Visual-Inertial Integration**: ORB-SLAM3 seamlessly integrates visual and inertial data, providing more robust and accurate SLAM performance. This integration helps in maintaining accurate tracking and mapping in scenarios with rapid motion or temporary visual occlusions.
- **Loop Closure and Relocalization**: The system includes improved loop closure and relocalization mechanisms that enhance the consistency and accuracy of the generated maps. This is particularly beneficial in large and complex environments where revisiting previously mapped areas is common.

The preliminary results demonstrate that ORB-SLAM3 is capable of delivering high-precision and reliable SLAM performance in a variety of scenarios. Its ability to handle different types of camera inputs and integrate visual-inertial data makes it a powerful tool for autonomous navigation and mapping applications.

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/orb_slam3_test.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/orb_slam3_extra_test.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>

<video width="640" height="360" controls>
    <source src="https://somnath3112.github.io/files/videos/res1_slam3.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
