#include <Adafruit_MLX90614.h>
#include <Wire.h>
Adafruit_MLX90614 mlx = Adafruit_MLX90614();
double tempO = 0.0;
#define MLX90614_I2CADDR 0x0E

void setup() {
  Serial.begin(9600);
  mlx.begin();
}

void loop() {
  tempO = mlx.readObjectTempF();
  delay(500);
  Serial.println(tempO);
}