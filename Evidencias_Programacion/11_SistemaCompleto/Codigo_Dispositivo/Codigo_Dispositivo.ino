/*
Prototipo de dispositivo que controla la posicion de un deflector con un servo,
segun la temperatura sensada por un termistor.
se agrego un potenciometro para simular el estado de carga de la bateria.
*/

#include <Servo.h> //inxcluimos la libreria servo

Servo myservo;  // crear el objeto servo

const float BETA = 3950; // coeficiente del termistor
int term = 0;  // pin analogico donde se conecta el termistor
int val;    // variable para escribir la salida al servo
const double NOMINAL_RESISTANCE = 10000; // Nominal resistance at a known temperature (usually 25°C)
int potpin = 1;  // pin analogico para conectar el potenciometro simulador de bateria
int simbate;    // variable para escribir la simulacion de bateria desde el potenciometro

void setup() {
  myservo.attach(9);  // salida al servo en el pin 9
  Serial.begin(9600); // incia la comunicacion serial
}

void loop() {
  
  int analogValue = analogRead(term);
  double resistance = NOMINAL_RESISTANCE * ((1023.0 / analogValue) - 1.0);
  float celsius = 1.0 / (1.0 / 298.15 + 1.0 / BETA * log(resistance / NOMINAL_RESISTANCE)) - 273.15;

if (celsius > 30.0) {
    myservo.write(90); // Posiciona el servo en 90° si la temperatura supera los 30°C.
    val=90;
  } else if (celsius > 25.0) {
    myservo.write(50); // Posiciona el servo en 50° si la temperatura supera los 25°C.
    val=50;
  } else if (celsius > 22.0) {
    myservo.write(25); // Posiciona el servo en 25° si la temperatura supera los 22°C.
    val=25;
  } else {
    myservo.write(0); // Mantén el servo en 0° en otros casos.
    val=0;
  }
  
  myservo.write(val);   // posiciona el servo segun la variable
  
  simbate = analogRead(potpin); // lee el pin del potensiometro
  simbate = map(simbate, 0, 1023, 0, 100); // traduce la lactura del potenciometro a porcentaje

// presentacion de resultados por interface serial
//se comenta las salidas del proyecto original para hacer las pruebas con temperatura
/* 
  Serial.print("Temperatura: ");
  Serial.print(celsius);
  Serial.println(" ℃");
  Serial.print("Posicion deflector: ");
  Serial.print(val);
  Serial.println("°");
  Serial.print("Bateria: ");
  Serial.print(simbate);
  Serial.println(" %");
  */
Serial.println(celsius);
  

  delay(1001); // retraso del loop
}
