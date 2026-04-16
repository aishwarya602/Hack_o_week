#include <Servo.h>

#define TRIG_PIN 3
#define ECHO_PIN 4
#define BUZZER 8
#define LED 13

Servo motor;  // Using servo as forklift motor

long duration;
int distance;

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(LED, OUTPUT);

  Serial.begin(9600);

  motor.attach(9);
  motor.write(90); // moving state

  Serial.println("Forklift Safety System Initialized");
}

void loop() {
  // Trigger ultrasonic pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Read echo
  duration = pulseIn(ECHO_PIN, HIGH);

  // Convert to distance (cm)
  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance > 0 && distance < 20) {
    Serial.println("⚠️ Object Detected! STOPPING Forklift");

    digitalWrite(BUZZER, HIGH);
    digitalWrite(LED, HIGH);

    motor.write(0); // STOP
  } else {
    Serial.println("✅ Path Clear");

    digitalWrite(BUZZER, LOW);
    digitalWrite(LED, LOW);

    motor.write(90); // RUN
  }

  delay(500);
}
