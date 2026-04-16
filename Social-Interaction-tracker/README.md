# Social Interaction Tracker (BLE RSSI Simulation)

## Overview
This project simulates a social interaction tracking system using Arduino. In real-world scenarios, BLE (Bluetooth Low Energy) devices measure proximity using RSSI (Received Signal Strength Indicator). Since BLE is not supported in the simulator, this project uses a potentiometer to simulate RSSI values and classify interaction strength.


## Features
- Simulated RSSI-based proximity detection
- Interaction classification (Strong, Medium, Weak)
- Real-time display using LCD (16x2 I2C)
- Serial monitoring for interaction logs
- Simple and scalable logic for wearable systems


## Components Used
- Arduino UNO
- Potentiometer (RSSI simulation)
- 16x2 LCD Display (I2C)
- Breadboard and jumper wires


## Circuit Connections

### Potentiometer (RSSI Simulation)
- Left Pin → GND
- Right Pin → 5V
- Middle Pin → A0

### LCD (I2C)
- VCC → 5V
- GND → GND
- SDA → A4
- SCL → A5


## Working Principle
1. Potentiometer simulates RSSI values (signal strength).
2. Arduino reads analog value from A0.
3. Based on value:
   - High → Strong interaction
   - Medium → Moderate interaction
   - Low → Weak interaction
4. Results are displayed on LCD and printed in Serial Monitor.


## Code Highlights
- `analogRead()` used to simulate RSSI values
- Conditional logic for interaction classification
- LCD integration for user-friendly output
- Serial logging for debugging and analysis


## How to Run (Wokwi Simulation)
1. Open Wokwi Arduino Simulator
2. Add components: Arduino, potentiometer, I2C LCD
3. Connect as per circuit diagram
4. Upload the code
5. Rotate potentiometer to simulate proximity

## Link to simulator
https://wokwi.com/projects/461435237429722113

## Output
- LCD:
  - Displays RSSI value
  - Shows interaction level (Strong/Medium/Weak)
- Serial Monitor:
  - Logs RSSI and interaction classification


## Future Improvements
- Implement real BLE using ESP32
- Store interaction history in EEPROM or cloud
- Add mobile app for visualization
- Use multiple devices for network-based interaction tracking
- Apply ML for social behavior analysis


## Applications
- Wearable social interaction tracking
- Contact tracing systems
- Behavioral analytics
- Smart healthcare monitoring
