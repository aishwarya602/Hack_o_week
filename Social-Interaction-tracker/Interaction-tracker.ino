#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define RSSI_PIN A0

LiquidCrystal_I2C lcd(0x27, 16, 2);

int rssiValue;

void setup() {
  Serial.begin(9600);

  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Social Tracker");
  delay(1500);
  lcd.clear();
}

void loop() {
  rssiValue = analogRead(RSSI_PIN);

  String interaction;

  if (rssiValue > 700) {
    interaction = "Strong";
  } 
  else if (rssiValue > 400) {
    interaction = "Medium";
  } 
  else {
    interaction = "Weak";
  }

  // Display on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("RSSI:");
  lcd.print(rssiValue);

  lcd.setCursor(0, 1);
  lcd.print(interaction);

  // Serial Output
  Serial.print("RSSI: ");
  Serial.print(rssiValue);
  Serial.print(" -> ");
  Serial.println(interaction);

  delay(500);
}