//FOR READING CONTENT OF ARDUINO EEPROM

#include <EEPROM.h>
#include <string.h>


//A=display bytes human form
//B=potentially send byte data to python
//C=send bit data to python
//D=write to eeprom


// bool operationStart = false;
bool STARTreadEepromHuman = false;
bool STARTreadBytesDEC = false;
bool STARTreadEEpromBits = false;
bool STARTsaveToEeprom=false;
const int ledPin = 13;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void signalOperationEnd(){
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
}


//read all bytes from eeprom, for humans
void readEepromHuman() {
  for (int address = 0; address < EEPROM.length(); address++) {
    byte value = EEPROM.read(address);

    Serial.print(address);
    Serial.print("\t");
    Serial.print(value, HEX);
    Serial.print("\t");
    Serial.print(value, DEC);
    Serial.println();
  }
  signalOperationEnd();
}

//read bytes from eeprom
void readBytesDEC() {
  for (int address = 0; address < EEPROM.length(); address++) {
    byte value = EEPROM.read(address);
    Serial.println(value, DEC);
  }
  Serial.println("DONE");
  signalOperationEnd();
}

//read bits from eeprom, used for saving eeprom data
void readEEpromBits() {
  for (int address = 0; address < EEPROM.length(); address++) {
    byte value = EEPROM.read(address);
    // Serial.print("Address ");
    // Serial.print(address);
    // Serial.print(": ");
    
    for (int bit = 7; bit >= 0; bit--) { // Print bits from MSB to LSB
      Serial.println((value >> bit) & 0x01);
    }
    //Serial.println();
  }
   Serial.println("DONE");
   signalOperationEnd();
}

void saveToEeprom() {
  int address = 0;
  while (true) {
    if (Serial.available() > 0) {
      String command = Serial.readStringUntil('\n');
      command.trim(); // Remove any trailing whitespace

      if (command == "DONE") {
        // Signal operation end but do not save 'DONE' to EEPROM
        signalOperationEnd();
        return;
      } else {
        int value = command.toInt();
        if (address < EEPROM.length()) {
          EEPROM.update(address, value);
          address++;
        }
      }
    }
  }
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    Serial.println(command);

    if(command=='A'){
      STARTreadEepromHuman=true;
    }
    if (command == 'B') {
      STARTreadBytesDEC = true;
    }
    if(command=='C'){
      STARTreadEEpromBits=true;
    }
    if(command=='D'){
      STARTsaveToEeprom=true;
    }
  }

  if(STARTreadEepromHuman){
    readEepromHuman();
    STARTreadEepromHuman=false;
  }
  if(STARTreadBytesDEC){
    readBytesDEC();
    STARTreadBytesDEC=false;
  }
  if(STARTreadEEpromBits){
    readEEpromBits();
    STARTreadEEpromBits=false;
  }
  if(STARTsaveToEeprom){
    saveToEeprom();
    STARTsaveToEeprom=false;
  }
}

