#include <Servo.h>

Servo door;

int irPin = 2;     // IR receiver output
int ledPin = 13;   // LED indicator

void setup() {
  pinMode(irPin, INPUT);
  pinMode(ledPin, OUTPUT);
  
  Serial.begin(9600);

  door.attach(9);     // Servo PWM pin
  door.write(0);      // Door initially closed

  Serial.println("Smart Door System Initialized");
}

void loop() {
  int irState = digitalRead(irPin);

  if (irState == HIGH) {   // Signal detected
    Serial.println("🚶 Person Detected -> Opening Door");

    digitalWrite(ledPin, HIGH);  // LED ON
    door.write(90);              // Open door
    delay(3000);                // Keep door open

    Serial.println("⏳ Waiting...");

    door.write(0);              // Close door
    digitalWrite(ledPin, LOW);  // LED OFF

    Serial.println("🚪 Door Closed\n");
    delay(2000);                // Prevent repeated triggering
  } 
  else {
    Serial.println("No Movement");
    delay(500);
  }
}