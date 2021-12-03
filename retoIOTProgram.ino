#include <WiFiNINA.h>
#include <ArduinoJson.h>

// Datos de la red a conectar
char ssid[] = "iPhone de Salva";
char password[] = "23568910";

int status = WL_IDLE_STATUS;

//Dirección de la api
char server[] = "c84e-148-241-109-145.ngrok.io";    //Always modify when re-run ngrok

WiFiClient client;

void setup(){
  Serial.begin(9600);
  
  //Conectarse a la red
  while (status != WL_CONNECTED) {
    Serial.println("Attempting to connect to Network: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid,password);
    delay (1000);
  }

  Serial.print("Connected to SSID: ");
  Serial.println(WiFi.SSID());
  IPAddress ip = WiFi.localIP();
  IPAddress gateway = WiFi.gatewayIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

}

void loop(){
  
  //Crear los json 
  DynamicJsonDocument doc1(1024);
  DynamicJsonDocument doc2(1024);
  DynamicJsonDocument doc3(1024);
  DynamicJsonDocument doc4(1024);
  
  //Datos para la lectura de gases
  float sensor1 = analogRead(A0);
  float voltaje = sensor1 * (5.0 /1023.0);
  float rs = 1000*( (5-voltaje) / voltaje);
  double co =-0.913*log(rs) + 9.6282;
  
  //Valores para la base de datos
  int cuarto1 = 15;
  int parametro1 = 5;
  int alumno1 = 55;
  
  //Toma del gas y escritura en el json
  Serial.print("  co: ");
  Serial.print(co);
  doc1["value"] = co;
  doc1["gasType"] = "co";
  doc1["idCuarto"] = cuarto1;
  doc1["idParametro"] = parametro1;
  doc1["idAlumno"] = alumno1;
  
  double metano =-0.567*log(rs) + 5.7419;
  Serial.print("  metano: ");
  Serial.print(metano);
  doc2["value"] = metano;
  doc2["gasType"] = "metano";
  doc2["idCuarto"] = cuarto1;
  doc2["idParametro"] = parametro1;
  doc2["idAlumno"] = alumno1;

  double lpg = -0.34*log(rs) + 3.2377;
  Serial.print("  lpg: ");
  Serial.print(lpg);
  doc3["value"] = lpg;
  doc3["gasType"] = "lpg";
  doc3["idCuarto"] = cuarto1;
  doc3["idParametro"] = parametro1;
  doc3["idAlumno"] = alumno1;

  double hidrox = -0.421*log(rs) + 4.0112;
  Serial.print("  hidrox: ");
  Serial.print(hidrox);
  doc4["value"] = hidrox;
  doc4["gasType"] = "hidrox";
  doc4["idCuarto"] = cuarto1;
  doc4["idParametro"] = parametro1;
  doc4["idAlumno"] = alumno1;

  String postData1;
  String postData2;
  String postData3;
  String postData4;

  serializeJson(doc1, postData1);
  serializeJson(doc2, postData2);
  serializeJson(doc3, postData3);
  serializeJson(doc4, postData4);
  
   //Mandar json a la api
   if (client.connect(server, 80)) {
    client.println("POST /agregarMedicion HTTP/1.1");
    client.println("Host: c84e-148-241-109-145.ngrok.io");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(postData1.length());
    client.println();
    client.print(postData1);
   }
   delay(500);

   
   if (client.connect(server, 80)) {
    client.println("POST /agregarMedicion HTTP/1.1");
    client.println("Host: c84e-148-241-109-145.ngrok.io");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(postData2.length());
    client.println();
    client.print(postData2);
   }
   delay(500);

   if (client.connect(server, 80)) {
    client.println("POST /agregarMedicion HTTP/1.1");
    client.println("Host: c84e-148-241-109-145.ngrok.io");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(postData3.length());
    client.println();
    client.print(postData3);
  }
  delay(500);

  if (client.connect(server, 80)) {
    client.println("POST /agregarMedicion HTTP/1.1");
    client.println("Host: c84e-148-241-109-145.ngrok.io");
    client.println("Content-Type: application/json");
    client.print("Content-Length: ");
    client.println(postData4.length());
    client.println();
    client.print(postData4);
  }
  delay(500);

  if (client.connected()) {
    client.stop();
  }
  Serial.println(" ");
  Serial.println(postData1);
  Serial.println(postData2);
  Serial.println(postData3);
  Serial.println(postData4);
  

  delay(2000);
  
}
