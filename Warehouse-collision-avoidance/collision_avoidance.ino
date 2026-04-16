#define TRIG_PIN 9
#define ECHO_PIN 10

#define STEP_PIN 5
#define DIR_PIN 6

#define LED_PIN 3

long duration;
int distance;

void setup() {
  Serial.begin(9600);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);

  pinMode(LED_PIN, OUTPUT);

  digitalWrite(DIR_PIN, HIGH); // direction
}

void loop() {

  // Ultrasonic trigger
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.println(distance);

  if (distance < 30) {
    // 🚨 Obstacle detected
    digitalWrite(LED_PIN, HIGH);
    Serial.println("STOP");

  } else {
    // ✅ Move motor
    digitalWrite(LED_PIN, LOW);

    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(800);
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(800);
  }

  delay(100);
}