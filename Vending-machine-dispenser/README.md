# Smart Vending Machine Dispenser

## Overview
This project simulates a smart vending machine using Arduino. A user interaction (push button simulating a capacitive sensor) triggers the dispensing mechanism. The system tracks inventory using EEPROM, ensuring data persistence even after power reset.


## Features
- Touchless interaction simulation using push button
- Automated dispensing using servo motor
- Relay-based control mechanism
- Persistent inventory tracking using EEPROM
- Serial monitoring for system logs
- Out-of-stock detection and alert


## Components Used
- Arduino UNO
- Push Button (simulating capacitive proximity sensor)
- Servo Motor (dispenser mechanism)
- Relay Module
- Breadboard and jumper wires


## Circuit Connections

### Push Button (Sensor Simulation)
- 1.l → Pin 2
- 1.r → GND
- Configured using `INPUT_PULLUP`

### Relay Module
- VCC → 5V
- GND → GND
- IN → Pin 7

### Servo Motor
- PWM → Pin 9
- VCC → 5V
- GND → GND


## Working Principle
1. User input is simulated via a push button.
2. On button press:
   - System checks inventory from EEPROM.
3. If stock is available:
   - Relay is activated.
   - Servo rotates to dispense item.
   - Inventory count is reduced and updated in EEPROM.
4. If stock is empty:
   - System displays "Out of Stock" message.
5. Inventory persists even after reset due to EEPROM storage.


## Code Highlights
- `EEPROM.read()` and `EEPROM.write()` used for persistent storage
- Edge detection implemented to avoid repeated triggering
- Servo motor simulates physical dispensing
- Relay represents actual vending mechanism control


## How to Run (Wokwi Simulation)
1. Open Wokwi Arduino Simulator
2. Add components: Arduino, button, servo, relay
3. Connect components as per diagram
4. Upload the code
5. Press button to simulate item dispensing

## Link to simulator
https://wokwi.com/projects/460996815420078081 


## Output
- Serial Monitor:
  - Initial inventory display
  - Dispensing logs
  - Remaining stock
  - Out-of-stock alert
- Servo:
  - Rotates to simulate dispensing
- Relay:
  - Activates during dispensing


## Future Improvements
- Add LCD display for real-time inventory
- Integrate payment system (RFID/QR)
- Add IoT dashboard for stock monitoring
- Implement multiple product selection
- Add restocking mechanism


## Applications
- Smart vending machines
- Retail automation
- Inventory management systems
- Contactless product dispensing
