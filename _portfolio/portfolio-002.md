---
title: "[Active] Quadruped"
excerpt: "Quadruped in Matlab-Python-ROS-Gazebo and MuJoCo-SBL3.<br/><img src='/images/qped_thumbnail.png'>"
collection: portfolio
---

## Planning Quadruped

_Source: [Channel for Quadrupedal Planning](https://www.youtube.com/playlist?list=PLeSCFB3ScayliH88QdEOWEA-8GdDj-G6t)_

Assuming the Center of Mass (CoM) coincides with the Zero Moment Point (ZMP), the CoM must remain within the foot support polygon to prevent falling. The algorithm concurrently plans for both the CoM and foot positions. This approach is based on A. Winkler's 2017 paper.

<iframe width="600" height="480" src="https://www.youtube.com/embed/IQ50ZoWJ0eo?list=PLeSCFB3ScayliH88QdEOWEA-8GdDj-G6t" title="Implemented simplified simulation from A. Winkler&#39;s planning algorithm" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Control Quadruped

_Source: [Channel for Quadrupedal Control](https://www.youtube.com/playlist?list=PLeSCFB3Scayl5d13Q9SgN08hZuESpzMK3)_

Developing an interface to MATLAB, ROS, and Gazebo involves creating a seamless communication bridge between these platforms. This integration allows for efficient simulation, control, and analysis of the quadruped robot, leveraging the strengths of each tool to enhance the overall development process.

<iframe width="600" height="480" src="https://www.youtube.com/embed/HqfPNuIz6WE?list=PLeSCFB3Scayl5d13Q9SgN08hZuESpzMK3" title="quadruped jumping" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Learning Quadruped

_Source: [Channel for Quadrupedal Learning](https://www.youtube.com/playlist?list=PLeSCFB3ScayksgDsXM790253w18kFyePm)_

MuJoCo in Colab with a codebase for training deep reinforcement learning (RL). The training process will commence with setting up the environment, followed by defining the RL algorithms and training the quadruped model. This setup allows for efficient experimentation and fine-tuning of the model using the computational resources available in Colab.


<iframe width="600" height="480" src="https://www.youtube.com/embed/ciEWys6NA8U?list=PLeSCFB3ScayksgDsXM790253w18kFyePm" title="anymal OL" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>