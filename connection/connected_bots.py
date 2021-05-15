import requests
import time

def send_message(port, message, sender):
    url = 'http://localhost:'+str(port)+'/webhooks/rest/webhook'
    data = {'message': message, "sender": sender}

    x = requests.post(url, json = data)

    print(sender + ": " + x.text)
    
    if(x.status_code == 200):
    	return x.text
    else:
    	print(x.raw)
    	return None

# Puertos donde tienen que estar corriendo los dos chatbots
# 5006 developer
port_c1 = 5006 
# 5005 developer
port_c2 = 5005

# Tiempo de espera entre mensaje y mensaje para que no vaya a las chapas (en segundos)
delay = 1.0

# Mando el mensaje inicial simulando que soy el chatbot 1
message_c1 = send_message(port_c1, "hola", "Developer")
message_c2 = ""

# Loop infinito de los chatbots mandandose mensajes entre si, la conversacion se imprime en consola desde la funcion send_message
while message_c1.find("Chau") == -1:
    message_c2 = send_message(port_c2, message_c1, "Scrum Master")
    time.sleep(delay)
    message_c1 = send_message(port_c1, message_c2, "Developer")
    time.sleep(delay)
