#include <Wire.h>

//temp libraries
#include <Adafruit_MLX90614.h>
//#define MLX90614_I2CADDR 0x0E

//hr libraries
#define USE_ARDUINO_INTERRUPTS true    // Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h>

//spo2 libraries
#include "MAX30105.h"
#include "spo2_algorithm.h"

//spo2 variables
MAX30105 particleSensor;
#define MAX_BRIGHTNESS 255
#if defined(__AVR_ATmega328P__) || defined(__AVR_ATmega168__)
uint16_t irBuffer[50]; //infrared LED sensor data
uint16_t redBuffer[50];  //red LED sensor data
#else
uint32_t irBuffer[50]; //infrared LED sensor data
uint32_t redBuffer[50];  //red LED sensor data
#endif
int32_t bufferLength; //data length
int32_t spo2; //SPO2 value
int8_t validSPO2; //indicator to show if the SPO2 calculation is valid
int32_t heartRate; //heart rate value
int8_t validHeartRate; //indicator to show if the heart rate calculation is valid

//temp variables
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
double tempO = 0.0;

//hr vriables
const int PulseWire = 1;       // PulseSensor PURPLE WIRE connected to ANALOG PIN 1
const int LED13 = 13;          // The on-board Arduino LED, close to PIN 13.
int Threshold = 550;  
int done = 0;
int myBPM = 0;
PulseSensorPlayground pulseSensor; 

//hrv variables
int hrv = 0;

//GSR variables
const int GSR=A0;
int sensorValue=0;
int gsr_average=0;

void setup()
{
  Serial.begin(9600);
  //spo2 sensor setup
  particleSensor.begin(Wire, I2C_SPEED_FAST); //{}
  byte ledBrightness = 60; //Options: 0=Off to 255=50mA
  byte sampleAverage = 1; //Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 3; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  byte sampleRate = 50; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 69; //Options: 69, 118, 215, 411
  int adcRange = 16384; //Options: 2048, 4096, 8192, 16384
  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange); //Configure sensor with these settings
  //hr setup
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED13);
  pulseSensor.setThreshold(Threshold); 
  pulseSensor.begin();
  //temp setup
  mlx.begin();
}

void loop() {
  bufferLength = 50; 
  for (byte i = 0 ; i < bufferLength; i++)
  {
    while (particleSensor.available() == false) 
      particleSensor.check(); 
    redBuffer[i] = particleSensor.getRed();
    irBuffer[i] = particleSensor.getIR();
    particleSensor.nextSample(); 
  }
  maxim_heart_rate_and_oxygen_saturation(irBuffer, bufferLength, redBuffer, &spo2, &validSPO2, &heartRate, &validHeartRate);
  temp();
  delay(10);
  gsr();
  delay(10);
  getbpm();
  delay(10);
  gethrv();
  int good = 0;
  while(!good) {
  if(validSPO2) {
    if(spo2 >= 95 && spo2 <= 100) {
      good = 1;
    }
  }
  else;
  }
  Serial.print(spo2, DEC);
  Serial.print(" ");
  Serial.print(tempO);
  Serial.print(" ");
  Serial.print(gsr_average);
  Serial.print(" ");
  Serial.print(myBPM);
  Serial.print(" ");
  Serial.print(hrv);
  delay(30);
  exit(1);
  }


//function to get temp
void temp() {
      tempO = mlx.readObjectTempF();
}

//function to get gsr
void gsr(){
  long sum=0;
  for(int i=0;i<10;i++)           
      {
      sensorValue=analogRead(GSR);
      sum += sensorValue;
      delay(5);
      }
   gsr_average = sum/10;
}

//function to get bpm
void getbpm() {
  myBPM = pulseSensor.getBeatsPerMinute(); 
  delay(10);
} 

//function to get hrv
void gethrv() {
  hrv = pulseSensor.getInterBeatIntervalMs(); 
  delay(10);
}