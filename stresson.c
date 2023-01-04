//Temp libraries
#include <Adafruit_MLX90614.h>
#include <Wire.h>
#include "MAX30105.h"
#include "heartRate.h"


//TEMP variables
#define MLX90614_I2CADDR 0x0E
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
double tempO = 0.0;

//GSR variables
const int GSR=A0;
int sensorValue=0;
int gsr_average=0;


//HEARTRATE libraries
#define USE_ARDUINO_INTERRUPTS true    
#include <PulseSensorPlayground.h>      

//HEARTRATE variables
const int PulseWire = 1;       
const int LED13 = 13;          
int Threshold = 550;                                        
PulseSensorPlayground pulseSensor; 



//SPO2 variables

 
void setup(){
  Serial.begin(9600);
  //temp initialization
  mlx.begin();       
  //pulse initialization
  particleSensor.setup(); //Configure sensor with default settings
  particleSensor.setPulseAmplitudeRed(0x0A); //Turn Red LED to low to indicate sensor is running
  particleSensor.setPulseAmplitudeGreen(0); //Turn off Green LED
}

void loop() {
    Serial.print(gsr());
    Serial.print(",");
    Serial.print(temp());
    Serial.print(",");
    Serial.print(bpm());
}

//function to get temp
double temp() {
    tempO = mlx.readObjectTempF();
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
   Serial.println(gsr_average);
}

//function to get bpm
void setup() {   

  Serial.begin(9600);          

  pulseSensor.analogInput(PulseWire);   
  pulseSensor.setThreshold(Threshold);   

 
   if (pulseSensor.begin()) {
    Serial.println("We created a pulseSensor Object !");  
  }
}



void loop() {

 int myBPM = pulseSensor.getBeatsPerMinute();
                                               

if (pulseSensor.sawStartOfBeat()) {            
 Serial.println("♥  A HeartBeat Happened ! "); 
 Serial.print("BPM: ");                        
 Serial.println(myBPM);                        
}

  delay(20);                   

}

//function to get spo2


//function to get hrv

