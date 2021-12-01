# Turtlesim Simulations

## A]Reactive-Navigation
#### 
* In Reactive Navigation the navigation is executed purely based on the processing of the current/recent sensor data.
#### 
* Reactive Navigation does not include a map and hence the position of the robot with respect to a global frame of reference is not known.
#### 
* Using Reactive Navigation a robot can navigate in completely unknown environments containing unpredictable moving obstacles.

### Implementations:
1. Follower application between two turtlesim robots:
    * One turtlesim robot is teleoperated and the other follows it. 
    * One frame of reference is attached to each turtlesim robot and the relative transformation between these two frames is calculated.
    * Then, control commands are given such that it follows the teleoperated robot using feedback control.
<p align="center">
  <img src="https://user-images.githubusercontent.com/64685403/142398934-4ee75385-6bc0-4a84-91c2-5b5d05654b6a.gif" width="300">
</p>

## B] Go to goal behaviour:
* The user enters the x coordinate and y coordinate of the desired goal position.
* Then, control commands are given such that the turtlesim robot reaches the goal position using feedback control.
<p align="center">
  <img src="https://user-images.githubusercontent.com/64685403/124230204-5372ab80-db2c-11eb-8226-f537f3a2864a.gif" width="600">
</p>
