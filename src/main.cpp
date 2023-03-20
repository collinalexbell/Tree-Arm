/**
 * TA1-1
 * 
 * Tree Cybernetics
 *  Arm
 *   1st Model
 *     1st Iteration
 */

#include "Arduino.h"
#include <Servo.h>
#include "BorgServo.h"

#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif

int main_lever_pin = 2;
Servo servo;

void setup()
{
  // initialize LED digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  servo.attach(main_lever_pin);
}

int i = 0;
int delta = 1;
void loop()
{
  i = i + delta;
  if(i>180 || i < 0) {
    delta = delta * -1;
  }
  servo.write(i);
}
