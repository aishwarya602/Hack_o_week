#include <Servo.h>
#include <EEPROM.h>

#define BUTTON 2
#define RELAY 7

Servo dispenser;

int inventory;
int eepromAddr = 0;

bool lastState = HIGH;

void setup() {
  pinMode(BUTTON, INPUT_PULLUP);
  pinMode(RELAY, OUTPUT);

  Serial.begin(9600);

  dispenser.attach(9);
  dispenser.write(0);

  inventory = EEPROM.read(eepromAddr);

  if (inventory == 255) {
    inventory = 10;
    EEPROM.write(eepromAddr, inventory);
  }

  Serial.print("Initial Inventory: ");
  Serial.println(inventory);
}

void loop() {
  int currentState = digitalRead(BUTTON);

  // Trigger ONLY on press (HIGH → LOW)
  if (lastState == HIGH && currentState == LOW) {

    if (inventory > 0) {
      Serial.println("🖐 Dispensing Item");

      digitalWrite(RELAY, HIGH);

      // Servo motion
      for (int pos = 0; pos <= 90; pos++) {
        dispenser.write(pos);
        delay(10);
      }

      delay(1000);

      for (int pos = 90; pos >= 0; pos--) {
        dispenser.write(pos);
        delay(10);
      }

      digitalWrite(RELAY, LOW);

      inventory--;
      EEPROM.write(eepromAddr, inventory);

      Serial.print("Remaining: ");
      Serial.println(inventory);
    } 
    else {
      Serial.println("❌ Out of Stock!");
    }

    delay(300); // debounce
  }

  lastState = currentState;
}