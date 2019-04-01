/********************************************************************/
// First we include the libraries
#include <OneWire.h> 
#include <DallasTemperature.h>
/********************************************************************/
// Data wire is plugged into pin 50 on the Arduino 
#define ONE_WIRE_VERTICAL 50 

#define ONE_WIRE_HORIZONTAL 40
/********************************************************************/
// Setup a oneWire instance to communicate with any OneWire devices  
// (not just Maxim/Dallas temperature ICs) 
OneWire horizontalWire(ONE_WIRE_HORIZONTAL); 
OneWire verticalWire(ONE_WIRE_VERTICAL); 
/********************************************************************/
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature hSensors(&horizontalWire);
DallasTemperature vSensors(&verticalWire);
/********************************************************************/ 
void setup(void) 
{ 
 // start serial port 
 Serial.begin(9600); 
 Serial.println("Horizontal and vertical wire test"); 

 // H-wire is 30m long and has 10 sensors
 // V-wire is 4m long and has 4 sensors
 // Start up the library 
 vSensors.begin(); 
 hSensors.begin(); 
} 
void loop(void) 
{ 
 // call sensors.requestTemperatures() to issue a global temperature 
 // request to all devices on the bus 
 // request vertical wire temperatures
 vSensors.requestTemperatures(); // Send the command to get temperature readings 
 Serial.print("V: ");
 for (int i=0; i<4; i++){
     Serial.print(vSensors.getTempCByIndex(i));
     Serial.print(",");
 }
 Serial.println();
  // print csv temp readings. decode using order.txt reference

  // request horizontal wire temperatures
 hSensors.requestTemperatures(); // Send the command to get temperature readings 
 Serial.print("H: ");
 for (int i=0; i<10; i++){
     Serial.print(hSensors.getTempCByIndex(i));
     Serial.print(",");
 }
 Serial.println();
 
 delay(1000); 
} 
