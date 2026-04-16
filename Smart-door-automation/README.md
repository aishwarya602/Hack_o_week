# Smart Door Automation System

## Overview
This project implements a smart door automation system using an IR sensor and a servo motor. The system detects the presence of a person and automatically opens the door, then closes it after a short delay. An LED indicator and serial logging are used for monitoring system activity.

## Features
- Automatic door opening on person detection
- Servo motor-controlled door mechanism
- LED indication for door status
- Serial monitor logging for real-time tracking
- Simple and efficient embedded system design


## Components Used
- Arduino UNO
- IR Sensor (Proximity/Receiver)
- Servo Motor (SG90)
- LED
- Breadboard and jumper wires


## Circuit Connections

### IR Sensor
- VCC → 5V
- GND → GND
- OUT → Pin 2

### Servo Motor
- PWM → Pin 9
- VCC → 5V
- GND → GND

### LED
- Anode → Pin 13
- Cathode → GND


## Working Principle
1. The IR sensor detects the presence of a person.
2. When detection occurs (HIGH signal):
   - The LED turns ON.
   - The servo motor rotates to 90° to open the door.
3. After a delay, the system:
   - Closes the door (servo returns to 0°).
   - Turns OFF the LED.
4. The system continuously monitors for movement.


## Code Explanation
- `digitalRead(irPin)` reads the sensor input.
- `Servo.write()` controls door position.
- Serial messages provide real-time feedback.
- Delays ensure proper timing for door operation.


## How to Run (Wokwi Simulation)
1. Open Wokwi Arduino Simulator
2. Add components: Arduino, IR sensor, servo, LED
3. Connect components as per circuit diagram
4. Upload the code
5. Trigger the IR sensor to simulate detection

## Link to simulator 
https://wokwi.com/projects/460994552115608577

## Output
- Serial Monitor displays:
  - "Person Detected"
  - "Door Opening"
  - "Door Closed"
- LED indicates door status
- Servo simulates door movement


## Future Improvements
- Add PIR sensor for better motion detection
- Integrate IoT for remote monitoring
- Add buzzer for alert system
- Use face recognition for smart access control


## Applications
- Smart homes
- Office automation
- Security systems
- Touchless entry systems
