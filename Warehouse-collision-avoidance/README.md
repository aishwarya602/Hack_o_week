# Warehouse Collision Avoidance System

## Overview
This project simulates a collision avoidance system for warehouse automation using Arduino. An ultrasonic sensor continuously monitors the distance to obstacles, and a stepper motor (simulating an automated vehicle) stops when an object is detected within a safety threshold. An LED provides visual warning.


## Features
- Real-time obstacle detection using ultrasonic sensor
- Automated stop mechanism for moving system
- Stepper motor control for movement simulation
- LED-based visual alert system
- Serial monitoring for debugging and analysis


## Components Used
- Arduino UNO
- Ultrasonic Sensor (HC-SR04)
- Stepper Motor (with driver module)
- LED
- Breadboard and jumper wires


## Circuit Connections

### Ultrasonic Sensor (HC-SR04)
- VCC → 5V
- GND → GND
- TRIG → Pin 9
- ECHO → Pin 10

### Stepper Motor Driver
- STEP → Pin 5
- DIR → Pin 6
- VCC → External supply (or 5V depending on driver)
- GND → GND

### LED
- Anode → Pin 3
- Cathode → GND


## Working Principle
1. The ultrasonic sensor measures distance to nearby objects.
2. If distance is less than 30 cm:
   - System stops movement (no step pulses sent)
   - LED turns ON indicating danger
3. If path is clear:
   - Stepper motor continues moving (STEP pulses generated)
   - LED remains OFF
4. Distance readings are continuously printed to Serial Monitor.


## Code Highlights
- `pulseIn()` used for ultrasonic distance calculation
- Stepper motor controlled using STEP and DIR pins
- Threshold-based safety logic implemented
- Efficient delay-based pulse generation for motor control


## How to Run (Wokwi Simulation)
1. Open Wokwi Arduino Simulator
2. Add components: Arduino, HC-SR04, stepper motor + driver, LED
3. Connect as per circuit diagram
4. Upload the code
5. Adjust object distance to test collision detection

## Link to simulator
https://wokwi.com/projects/460168095432112129


## Output
- Serial Monitor:
  - Distance readings
  - STOP message when obstacle detected
- LED:
  - ON → Obstacle detected
  - OFF → Safe path
- Stepper Motor:
  - Moves when path is clear
  - Stops when obstacle is detected


## Future Improvements
- Add buzzer for audio alert
- Implement speed control instead of full stop
- Use multiple sensors for 360° coverage
- Integrate IoT dashboard for monitoring
- Add AI-based obstacle classification


## Applications
- Automated Guided Vehicles (AGVs)
- Warehouse automation
- Robotics navigation systems
- Industrial safety systems
