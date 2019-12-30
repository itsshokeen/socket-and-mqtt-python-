import socket
import paho.mqtt.client as mqtt 
from configuration import config

def on_connect(client, obj, flags, rc):
    if rc == 0:
        print("MQTT connected successfully " + str(rc))
    else:
        print("Bad connection returned code = ", rc)

def mqtt_message(client, obj, msg):
    # print(msg.payload)
    print("CLients connected now : ")
    print(len(webclients))

    for wc in webclients:
        print(wc)
        print(wc.send(msg.payload))


client = mqtt.Client()
client.username_pw_set("pds",password="Pds@orahi123")
client.on_connect = on_connect

client.on_message = mqtt_message

client.connect("mqtt.orahi.com", 1883, 60)
client.subscribe("#")
client.loop_start()

# create the socket
# AF_INET == ipv4
# SOCK_STREAM == TCP
webclients = set()

host = config['host']
port = config['port']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host , port))
s.listen(5)
while True:
    clientsocket, address = s.accept()
    webclients.add(clientsocket)

    # now our endpoint knows about the OTHER endpoint.
    print(f"Connection from {address} has been established.")
    # clientsocket.send(message.encode('utf-8'))

    
    
