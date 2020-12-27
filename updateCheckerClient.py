import socket
import os
VERSION = 'V0.01'
checked = 'false'
HOST = "Ip Here"
PORT = 25565
connected = 'true'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print(f'Connected to server on ip {HOST} and port {PORT}')
while connected == 'true': 
   

    serverVersion = client.recv(1024).decode('utf-8')
    if serverVersion.startswith('V'):  
        if checked == 'false':
        
        
            if VERSION != serverVersion:
                print("This vesion is outdated please upgrade to the latest version of AppName")
                client.send('COutDated'.encode('utf-8'))
                checked = 'true'
            else:
                if VERSION == serverVersion:
                    print('You are running the latest version of AppName')
                    client.send("!dis".encode('utf-8'))
                    connected = 'false'
                    
    #Doesn't start with V so isn't checking version
    if serverVersion.startswith('[link]'):
        print( 'Your version is outdated please download the latest version here: '+serverVersion)
        client.send("!dis".encode('utf-8'))
        connected = 'false'
    #print(command)
    #output = os.popen(command).read()
    #client.send(f"{command} was successfully executed \n Output: \n {output}".encode('utf-8'))
    #client.send(output.encode('utf-8'))
    
