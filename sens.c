//Temp libraries
#include <Adafruit_MLX90614.h>
#include <Wire.h>
#define MLX90614_I2CADDR 0x0E
//HR libraries
//#include "MAX30105.h"
//#include "heartRate.h"
#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>     // Includes the PulseSensorPlayground Library.   

//TEMP variables
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
double tempO = 0.0;

//GSR variables
const int GSR=A0;
int sensorValue=0;
int gsr_average=0;

//HEARTRATE variables
/*
MAX30105 particleSensor;
const byte RATE_SIZE = 4; //Increase this for more averaging. 4 is good.
byte rates[RATE_SIZE]; //Array of heart rates
byte rateSpot = 0;
long lastBeat = 0; //Time at which the last beat occurred
float beatsPerMinute;
int beatAvg;*/
const int PulseWire = 1;       // PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED13 = 13;          // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;
PulseSensorPlayground pulseSensor;

//SPO2 variables

void setup(){
  Serial.begin(9600);
  mlx.begin();
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.setThreshold(Threshold); 
  pulseSensor.begin();
  /*particleSensor.setup(); //Configure sensor with default settings
  particleSensor.setPulseAmplitudeRed(0x0A); //Turn Red LED to low to indicate sensor is running
  particleSensor.setPulseAmplitudeGreen(0); //Turn off Green LED*/
  //Serial.flush();
}

void loop() {
    Serial.print(gsr());
    Serial.print(" ");
    Serial.print(temp());
    Serial.print(" ");
    Serial.println(getBPM());
    delay(100);
    //exit(0);
}

//function to get temp
double temp() {
    tempO = mlx.readObjectTempF();
    delay(5);
    return tempO;
}

//function to get gsr
int gsr(){
  long sum=0;
  for(int i=0;i<10;i++)           //Average the 10 measurements to remove the glitch
      {
      sensorValue=analogRead(GSR);
      sum += sensorValue;
      delay(5);
      }
   gsr_average = sum/10;
   //Serial.println(gsr_average);
   return gsr_average;
}

//function to get bpm NO
/*
int bpm() {
  long irValue = particleSensor.getIR();
  if (checkForBeat(irValue) == true) {
    long delta = millis() - lastBeat;
    lastBeat = millis();
    beatsPerMinute = 60 / (delta / 1000.0);
    if (beatsPerMinute < 255 && beatsPerMinute > 20) {
      rates[rateSpot++] = (byte)beatsPerMinute; //Store this reading in the array
      rateSpot %= RATE_SIZE; //Wrap variable
      //Take average of readings
      beatAvg = 0;
      for (byte x = 0 ; x < RATE_SIZE ; x++)
        beatAvg += rates[x];
      beatAvg /= RATE_SIZE;
    }
  }
  return beatAvg;
}*/

int getBPM() {
  int myBPM = pulseSensor.getBeatsPerMinute();  // Calls function on our pulseSensor object that returns BPM as an "int".
  //delay(10);
  return myBPM;
}