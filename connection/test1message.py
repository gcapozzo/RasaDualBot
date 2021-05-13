import requests
import time

def send_message(port, message, sender):
    url = 'http://localhost:'+str(port)+'/webhooks/rest/webhook'
#    url = 'http://localhost:'+str(port)+'/domain'
    data = {"sender":"Chatbot 1","message":"hola"}

    x = requests.post(url, json = data)

    print(sender + ": " + x.text)

# Puertos donde tienen que estar corriendo los dos chatbots
port_c1 = 5006
port_c2 = 5005

# Tiempo de espera entre mensaje y mensaje para que no vaya a las chapas (en segundos)
delay = 0.5


# Mando el mensaje inicial simulando que soy el chatbot 1
print(send_message(port_c1, "hola", "Chatbot 1"))
