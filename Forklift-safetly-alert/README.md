# Forklift Safety Alert System

## Overview
This project implements a real-time forklift safety system using an ultrasonic sensor. The system detects obstacles or pedestrians in front of the forklift and automatically stops movement while triggering alerts. This helps prevent accidents in industrial environments.


## Features
- Real-time obstacle detection using ultrasonic sensor
- Automatic forklift stop mechanism (servo motor simulation)
- Audible alert using buzzer
- Visual alert using LED
- Serial monitoring for debugging and tracking


## Components Used
- Arduino UNO
- Ultrasonic Sensor (HC-SR04)
- Servo Motor (used as forklift motor simulation)
- Buzzer
- LED
- Breadboard and jumper wires


## Circuit Connections

### Ultrasonic Sensor (HC-SR04)
- VCC → 5V
- GND → GND
- TRIG → Pin 3
- ECHO → Pin 4

### Servo Motor
- PWM → Pin 9
- VCC → 5V
- GND → GND

### Buzzer
- Red → Pin 8
- Black → GND

### LED
- Anode → Pin 13
- Cathode → GND


## Working Principle
1. The ultrasonic sensor continuously measures the distance to nearby objects.
2. If an object is detected within 20 cm:
   - The forklift stops (servo motor set to 0°).
   - Buzzer is activated.
   - LED turns ON.
3. If the path is clear:
   - Forklift continues moving (servo at 90°).
   - Buzzer and LED remain OFF.
4. Distance readings are displayed on the Serial Monitor.


## Code Highlights
- `pulseIn()` calculates echo duration from ultrasonic sensor
- Distance computed using speed of sound formula
- Conditional logic ensures safety actions are triggered instantly
- Servo motor simulates forklift motion control


## How to Run (Wokwi Simulation)
1. Open Wokwi Arduino Simulator
2. Add components: Arduino, HC-SR04, servo, buzzer, LED
3. Connect components as per circuit diagram
4. Upload the code
5. Change object distance in simulator to test behavior

## Link to simulator
https://wokwi.com/projects/460995252352665601

## Output
- Serial Monitor:
  - Distance readings in cm
  - Safety alerts when obstacle detected
- LED:
  - ON → Danger
  - OFF → Safe
- Buzzer:
  - ON → Alert
- Servo:
  - 90° → Moving
  - 0° → Stopped


## Future Improvements
- Add IoT alerts (send warnings to mobile)
- Integrate camera for vision-based detection
- Add speed control instead of full stop
- Use multiple sensors for 360° coverage
- Implement AI-based pedestrian detection


## Applications
- Industrial warehouses
- Smart factories
- Automated guided vehicles (AGVs)
- Construction site safety
