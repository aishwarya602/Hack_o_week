# Assembly Line Object Counter

## Overview
This project simulates an assembly line object counting system using Arduino. A push button (simulating an inductive proximity sensor) detects metal objects on a conveyor belt and increments a counter. The count is displayed on an LCD and logged via the Serial Monitor.


## Features
- Real-time object counting
- Sensor simulation using push button
- LCD display (16x2 I2C) for live count
- Serial monitoring for tracking production
- Debouncing logic to avoid false counts


## Components Used
- Arduino UNO
- Push Button (simulating inductive sensor)
- 16x2 LCD Display (I2C)
- Breadboard and jumper wires


## Circuit Connections

### Push Button (Sensor Simulation)
- 1.l → Pin 2
- 1.r → GND
- Uses `INPUT_PULLUP`

### LCD (I2C)
- VCC → 5V
- GND → GND
- SDA → A4
- SCL → A5


## Working Principle
1. The push button simulates detection of a metal object.
2. On each button press:
   - Counter value increments.
   - Updated count is displayed on LCD.
   - Count is logged in Serial Monitor.
3. Debounce delay ensures accurate counting.


## Code Highlights
- Edge detection prevents multiple counts per press
- `LiquidCrystal_I2C` library used for LCD interface
- Serial output helps in monitoring production data
- Clean and efficient counting logic


## How to Run (Wokwi Simulation)
1. Open Wokwi Arduino Simulator
2. Add components: Arduino, button, I2C LCD
3. Connect as per circuit diagram
4. Upload the code
5. Press button to simulate object detection

## Link to simulator
https://wokwi.com/projects/460998852482658305

## Output
- LCD:
  - Displays live object count
- Serial Monitor:
  - Logs count updates in real time


## Future Improvements
- Replace button with real inductive proximity sensor
- Add IoT dashboard for production tracking
- Implement conveyor belt motor control
- Add multiple sensors for multi-line counting
- Store count data in cloud/database


## Applications
- Industrial automation
- Manufacturing assembly lines
- Production monitoring systems
- Inventory tracking
