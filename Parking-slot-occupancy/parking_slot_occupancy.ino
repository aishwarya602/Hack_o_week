#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define PIR 2

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int totalSlots = 4;
int slots[4] = {0, 0, 0, 0};

int occupied = 0;
bool lastState = LOW;

// 0 = ENTRY MODE, 1 = EXIT MODE
int mode = 0;

void setup() {
  pinMode(PIR, INPUT);

  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Parking System");

  delay(1000);
  lcd.clear();
}

void loop() {
  int motion = digitalRead(PIR);

  // Detect motion edge (LOW → HIGH)
  if (motion == HIGH && lastState == LOW) {

    if (mode == 0) {
      // ENTRY MODE
      if (occupied < totalSlots) {

        // Fill first empty slot
        for (int i = 0; i < totalSlots; i++) {
          if (slots[i] == 0) {
            slots[i] = 1;
            occupied++;
            break;
          }
        }

        Serial.println("🚗 Vehicle Entered");

      } else {
        Serial.println("🚫 Parking Full!");
        mode = 1; // switch to exit mode
      }
    } 
    else {
      // EXIT MODE
      if (occupied > 0) {

        for (int i = totalSlots - 1; i >= 0; i--) {
          if (slots[i] == 1) {
            slots[i] = 0;
            occupied--;
            break;
          }
        }

        Serial.println("🚙 Vehicle Exited");

      } else {
        Serial.println("✅ Parking Empty!");
        mode = 0; // switch back to entry mode
      }
    }

    updateLCD();
    delay(500);
  }

  lastState = motion;
}

void updateLCD() {
  lcd.clear();

  lcd.setCursor(0, 0);
  lcd.print("Occupied:");
  lcd.print(occupied);

  lcd.setCursor(0, 1);
  lcd.print("Mode:");
  lcd.print(mode == 0 ? "ENTRY" : "EXIT");

  Serial.print("Slots: ");
  for (int i = 0; i < totalSlots; i++) {
    Serial.print(slots[i]);
    Serial.print(" ");
  }
  Serial.println();
}