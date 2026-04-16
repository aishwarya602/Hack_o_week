# Smart Parking Slot Occupancy System

## Overview
This project simulates a smart parking management system using Arduino. A PIR motion sensor detects vehicle movement and updates parking slot occupancy dynamically. The system tracks available slots using an array-based approach and displays real-time status on an LCD.


## Features
- Real-time parking slot tracking
- PIR sensor-based vehicle detection
- Entry and exit mode handling (state-based logic)
- LCD display for live occupancy status
- Serial monitor logging for debugging
- Efficient slot allocation using array structure


## Components Used
- Arduino UNO
- PIR Motion Sensor
- 16x2 LCD Display (I2C)
- Breadboard and jumper wires


## Circuit Connections

### PIR Motion Sensor
- VCC → 5V
- GND → GND
- OUT → Pin 2

### LCD (I2C)
- VCC → 5V
- GND → GND
- SDA → A4
- SCL → A5


## Working Principle
1. The PIR sensor detects motion (vehicle entry/exit).
2. System uses two modes:
   - ENTRY MODE → fills empty slots
   - EXIT MODE → frees occupied slots
3. When motion is detected:
   - Slot array is updated accordingly
   - Occupied count is adjusted
4. If parking is full:
   - System switches to EXIT mode
5. If parking becomes empty:
   - System switches back to ENTRY mode
6. LCD displays current occupancy and mode


## Code Highlights
- Array (`slots[]`) used for slot management
- Edge detection prevents repeated triggering
- Mode-based logic simulates real parking flow
- LCD integration for user-friendly output
- Serial logging for debugging and monitoring


## How to Run (Wokwi Simulation)
1. Open Wokwi Arduino Simulator
2. Add components: Arduino, PIR sensor, I2C LCD
3. Connect as per circuit diagram
4. Upload the code
5. Trigger PIR sensor to simulate motion

## Link to simulator
https://wokwi.com/projects/460999614616161281

## Output
- LCD:
  - Displays number of occupied slots
  - Shows current mode (ENTRY / EXIT)
- Serial Monitor:
  - Logs vehicle entry/exit
  - Displays slot array status


## Future Improvements
- Add ultrasonic sensors for individual slot detection
- Integrate mobile app via Bluetooth/WiFi
- Add LED indicators per slot
- Implement payment and reservation system
- Use camera-based AI detection for accuracy


## Applications
- Smart parking systems
- Malls and commercial complexes
- Office parking automation
- Smart city infrastructure
