#include <LowPower.h>

void setup() {
  // put your setup code here, to run once:
  
  
}

void loop() {
  delay(5000);
  // put your main code here, to run repeatedly:
  LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);  
}
