#define Tp 50 //digial tempurature data pin number

void setup() {

    Serial.begin(115200);
    pinmode(Tp, INPUT);
}



void loop() {

    Tdat = digialRead(Tp);
    Serial.println(Tdat);
    delay(100);
    }
}
