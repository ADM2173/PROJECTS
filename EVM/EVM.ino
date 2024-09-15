#include <LiquidCrystal.h>

LiquidCrystal lcd(13, 12, 11, 10, 9, 8);

#define S1 7       // Button for KSC
#define S2 6       // Button for BCR
#define S3 5       // Button for RKK
#define S4 4       // Button for OTH
#define ADMIN_BTN 3 // Admin reset button

int vote1 = 0; // Votes for KSC
int vote2 = 0; // Votes for BCR
int vote3 = 0; // Votes for RKK
int vote4 = 0; // Votes for OTH
bool ready_to_vote = false;

void setup() {
  pinMode(S1, INPUT_PULLUP);
  pinMode(S2, INPUT_PULLUP);
  pinMode(S3, INPUT_PULLUP);
  pinMode(S4, INPUT_PULLUP);
  pinMode(ADMIN_BTN, INPUT_PULLUP);
  pinMode(LED_BUILTIN, OUTPUT);

  lcd.begin(16, 2);
  lcd.print("Electronic");
  lcd.setCursor(0, 1);
  lcd.print("Voting Machine");
  delay(3000);
  lcd.clear();

  // Initialize voting machine as not ready
  ready_to_vote = false;
}

void loop() {
  // Check if admin button is pressed
  if (digitalRead(ADMIN_BTN) == LOW) {
    // Toggle ready_to_vote state when admin button is pressed
    ready_to_vote = !ready_to_vote;
    delay(500); // Debounce delay
  }

  if (ready_to_vote) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Ready to Vote");

    // Check votes
    if (digitalRead(S1) == LOW) {
      digitalWrite(LED_BUILTIN, HIGH);
      vote1++;
      while (digitalRead(S1) == LOW); // Wait until button is released
      digitalWrite(LED_BUILTIN, LOW);
      delay(500); // Debounce delay
    }

    if (digitalRead(S2) == LOW) {
      digitalWrite(LED_BUILTIN, HIGH);
      vote2++;
      while (digitalRead(S2) == LOW); // Wait until button is released
      digitalWrite(LED_BUILTIN, LOW);
      delay(500); // Debounce delay
    }

    if (digitalRead(S3) == LOW) {
      digitalWrite(LED_BUILTIN, HIGH);
      vote3++;
      while (digitalRead(S3) == LOW); // Wait until button is released
      digitalWrite(LED_BUILTIN, LOW);
      delay(500); // Debounce delay
    }

    if (digitalRead(S4) == LOW) {
      digitalWrite(LED_BUILTIN, HIGH);
      vote4++;
      while (digitalRead(S4) == LOW); // Wait until button is released
      digitalWrite(LED_BUILTIN, LOW);
      delay(500); // Debounce delay
    }

    // Display results
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("KSC:");
    lcd.setCursor(4, 0);
    lcd.print(vote1);
    lcd.setCursor(8, 0);
    lcd.print("#");

    lcd.setCursor(0, 1);
    lcd.print("BCR:");
    lcd.setCursor(4, 1);
    lcd.print(vote2);
    lcd.setCursor(8, 1);
    lcd.print("&");

    delay(2000); // Show results for 2 seconds
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("RKK:");
    lcd.setCursor(4, 0);
    lcd.print(vote3);
    lcd.setCursor(8, 0);
    lcd.print("$");

    lcd.setCursor(0, 1);
    lcd.print("OTH:");
    lcd.setCursor(4, 1);
    lcd.print(vote4);
    lcd.setCursor(8, 1);
    lcd.print("%");

    delay(2000); // Show results for another 2 seconds
  } else {
    // Display message if not ready to vote
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Admin Button");
    lcd.setCursor(0, 1);
    lcd.print("Not Ready");
  }
}
