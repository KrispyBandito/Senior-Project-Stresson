long randomNumber;


void setup() {
  
  //setup serial communications through the USB
  Serial.begin(9600);

  //Let's make it more random
  randomSeed(42);   
      
}//close setup

void loop() {
  
  //generate a random number
  randomNumber = random(80,90);
  
  //display the random number on the serial monitor
  Serial.print("The HRV (IBI) is = ");
  Serial.println(randomNumber);
  delay(70);
  
}