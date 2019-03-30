/********************************************************************/
// First we include the libraries
#include <OneWire.h> 
#include <DallasTemperature.h>
/********************************************************************/
// Data wire is plugged into pin 2 on the Arduino 
#define ONE_WIRE_BUS 50 
/********************************************************************/
// Setup a oneWire instance to communicate with any OneWire devices  
// (not just Maxim/Dallas temperature ICs) 
OneWire oneWire(ONE_WIRE_BUS); 
/********************************************************************/
// Pass our oneWire reference to Dallas Temperature. 
DallasTemperature sensors(&oneWire);
/********************************************************************/ 
void setup(void) 
{ 
 // start serial port 
 Serial.begin(9600); 
 Serial.println("Dallas Temperature IC Control Library Demo"); 
 // Start up the library 
 sensors.begin(); 
} 
void loop(void) 
{ 
 // call sensors.requestTemperatures() to issue a global temperature 
 // request to all devices on the bus 
/********************************************************************/
 //Serial.print(" Requesting temperatures..."); 
 sensors.requestTemperatures(); // Send the command to get temperature readings 
 //Serial.println("DONE"); 
/********************************************************************/
 
 for (int i=0; i<10; i++){
     Serial.print(" Temp ")
     Serial.print(i);
     Serial.print(": ");
     Serial.print(sensors.getTempCByIndex(i));
 }
 Serial.println();
 
 /* Serial.print("Temp 0: "); 
 Serial.print(sensors.getTempCByIndex(0)); // Why "byIndex"? 
 Serial.print(" Temp 1: "); 
 Serial.print(sensors.getTempCByIndex(1));
 Serial.print(" Temp 2: "); 
 Serial.print(sensors.getTempCByIndex(2));
  Serial.print(" Temp 2: "); 
  Serial.print(sensors.getTempCByIndex(2));
  Serial.print(" Temp 2: "); 
 Serial.print(sensors.getTempCByIndex(2));
  Serial.print(" Temp 2: "); 
 Serial.print(sensors.getTempCByIndex(2));
 Serial.print(" Temp 3: ");
Serial.println(sensors.getTempCByIndex(3)); //Why "byIndex"?  */
   // You can have more than one DS18B20 on the same bus.  
   // 0 refers to the first IC on the wire 
   delay(1000); 
} 