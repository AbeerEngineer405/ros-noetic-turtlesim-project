# ROS Noetic TurtleSim Project 🐢

This project demonstrates basic ROS Noetic concepts using TurtleSim, including Publisher/Subscriber communication and autonomous turtle movement.

## Project Features

- ROS Noetic running on Ubuntu 20.04 using WSL.
- Publisher node for sending messages.
- Subscriber node for receiving messages.
- Publisher and Subscriber communication using ROS topics.
- Autonomous TurtleSim movement.
- Turtle movement in a square pattern.

## Files

### `publisher.py`
Publishes the message:

`Smart Methods Robotics`

to a ROS topic.

### `subscriber.py`
Subscribes to the ROS topic and receives the published message.

Example output:

`Received: Smart Methods Robotics`

### `square.py`
Controls the TurtleSim turtle using velocity commands and makes it move automatically in a square pattern.

## Running the Project

Start ROS:

```bash
roscore
```

Start TurtleSim:

```bash
rosrun turtlesim turtlesim_node
```

Run the Publisher:

```bash
python publisher.py
```

Run the Subscriber:

```bash
python subscriber.py
```

Run the autonomous square movement:

```bash
python square.py
```

## Result

The Publisher and Subscriber successfully communicated through ROS topics.

The TurtleSim turtle was also successfully controlled programmatically and moved in a square pattern.

## Technologies

- ROS Noetic
- Ubuntu 20.04
- WSL
- Python
- TurtleSim

## Project Status

✅ Publisher completed  
✅ Subscriber completed  
✅ ROS topic communication tested  
✅ TurtleSim movement completed  
✅ Autonomous square movement completed
