import pandas as pd
import time
import paho.mqtt.client as mqttClient
import os
import json

dataframe=pd.read_csv("DatosPruebaMQTT.csv",index_col=0)
dataframe.head()
dataframe.describe(include="all")
df=dataframe.dropna()
print(df)
temp=df.Temperature.tolist()
hum=df.Humidity.tolist()
light=df.Light.tolist()
co=df.CO2.tolist()

#name = input("Your name: ")


Connected = False

def on_connect(client, userdata, flags, rc):
    """ Funcion que establece la conexion
    """
    
    if rc==0:
        print("Conectado al broker")
        global Connected
        Connected = True
    else:
        print("Falla de la conexion")
    return

broker_address="broker.hivemq.com" #public broker
#broker_address="IP"
port=1883 #defecto de MQTT

tag = "IoT/EquipoX/MQTT"




client = mqttClient.Client("IoT Equipo x") #Instanciacion
client.on_connect = on_connect  #Agregando funcion
client.connect(broker_address, port)
client.loop_start()

print(str(Connected) + " status")
i=0
time.sleep(1)
while Connected != False:
    time.sleep(0.1)
    try:
        publicar = {"Cliente": "Astro"}
        print(publicar)
        publicar = json.dumps(publicar)
        client.publish(tag, publicar,qos=2)
        time.sleep(1)
        i+=1
    except KeyboardInterrupt:
        print("Sesion interrumpida del usuario : {}".name)
        client.disconnect()
        Connected = False
