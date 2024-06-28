# Connexion TCP au challenge root me "TCP - Retour au collège"
import socket
import sys

HOST = "challenge01.root-me.org"
PORT = 52002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    data = s.recv(1024)
    print(data.decode('utf-8'))
    if data.decode('utf-8').find("Password") != -1:
        break
    else:   
        s.sendall(data)
        print(data.decode('utf-8'))
        s.sendall(b'\n')
        print("Envoi de la réponse")
        print("En attente de la réponse")
        data = s.recv(1024)
        print(data.decode('utf-8'))
        print("Réponse reçue")
        print("Envoi de la réponse")
        s.sendall(b'\n')
        print("En attente de la réponse")
        data = s.recv(1024)
        print(data.decode('utf-8'))
        