const int ledPin = 2; 
int incomingByte;    
//char incomingByte;  

void setup() {

  Serial.begin(9600);

  pinMode(ledPin, OUTPUT);
}

void loop() {

  if (Serial.available() > 0) {

    incomingByte = Serial.read();
    //incomingByte = 'R';
    

    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    } 

    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }

    if(incomingByte == 'R'){
      float vol; 
      int sensorValue = analogRead(A0); 
      vol=(float)sensorValue/1024*5.0; 
      Serial.println(vol,1); 
      delay(2000);
    }

    if(incomingByte == 'G'){
      int sensorValue1 = analogRead(A1); 
      if(sensorValue1 < 1000){
        Serial.println("Yes");
      }
      if(sensorValue1 == 1023){
        Serial.println("No");
      }
      delay(1000);
    }
  }
}

