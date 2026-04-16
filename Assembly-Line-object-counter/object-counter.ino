#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define BUTTON 2

LiquidCrystal_I2C lcd(0x27, 16, 2);

int count = 0;
bool lastState = HIGH;

void setup() {
  pinMode(BUTTON, INPUT_PULLUP);

  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Object Counter");
  
  Serial.println("Assembly Line Started");
}

void loop() {
  int currentState = digitalRead(BUTTON);

  // Detect press (object detected)
  if (lastState == HIGH && currentState == LOW) {
    count++;

    Serial.print("Metal Object Count: ");
    Serial.println(count);

    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Count:");
    lcd.setCursor(0, 1);
    lcd.print(count);

    delay(300); // debounce
  }

  lastState = currentState;
}