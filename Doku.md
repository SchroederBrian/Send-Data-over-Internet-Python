
# Serverseitiges Programm – Dokumentation

## Überblick

Diese Dokumentation beschreibt die Implementierung eines grundlegenden Servers mit der Socket-Programmierung in Python. Der Server ist darauf ausgelegt, Verbindungen für einzelne und mehrere Benutzer zu handhaben.

## Anforderungen

-   Python 3.x
-   `socket` Modul

## Verbindung für einzelne Benutzer

### Beschreibung

Dieses Skript richtet einen Server ein, der auf eingehende Verbindungen am Port 5000 lauscht. Es akzeptiert Verbindungen von einem Client, empfängt Daten und sendet eine Antwort zurück.

### Implementierung

    import socket
    
    # Erstelle ein Socket-Objekt
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definiere die Serveradresse und den Port
    server_address = ('0.0.0.0', 5000)
    
    # Binde das Socket an die Serveradresse und den Port
    server_socket.bind(server_address)
    
    # Lausche auf eingehende Verbindungen
    
        server_socket.listen(1)
        print('Server lauscht auf eingehende Verbindungen...')
        
        while True:
            # Akzeptiere eine Clientverbindung
            client_socket, client_address = server_socket.accept()
            print(f'Verbunden mit Client: {client_address}')
            try:
                while True:
                    # Empfange Daten vom Client
                    data = client_socket.recv(1024).decode()
                    if not data:
                        break
                    print(f'Empfangene Daten vom Client: {data}')
        
                    # Sende eine Antwort zurück an den Client
                    response = "Daten erfolgreich empfangen!"
                    client_socket.send(response.encode())
            finally:
                # Schließe das Client-Socket
                client_socket.close()
                print(f'Verbindung zum Client {client_address} wurde geschlossen.')

### Details

Der Server bindet an alle verfügbaren Netzwerkschnittstellen und hört auf eingehende Verbindungen. Empfangene Daten vom Client werden gedruckt und bestätigt. Die Verbindung wird geschlossen, wenn keine Daten empfangen werden, was darauf hindeutet, dass der Client die Verbindung getrennt hat.

## Verbindung für mehrere Benutzer

### Beschreibung

Der Server wurde erweitert, um mehrere Clients gleichzeitig mithilfe von Threads zu handhaben.

### Implementierung
    import socket
    import threading
    
    def handle_client(client_socket, client_address):
        print(f"Client {client_address} verbunden.")
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    print(f"Keine Daten empfangen, schließe Verbindung zu {client_address}.")
                    break
                print(f'Empfangene Daten von {client_address}: {data}')
                response = "Daten erfolgreich empfangen!"
                client_socket.send(response.encode())
        except ConnectionResetError:
            print(f"Verbindung verloren mit {client_address}.")
        finally:
            client_socket.close()
            print(f'Verbindung zu {client_address} wurde geschlossen.')
    
    def start_server():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('0.0.0.0', 5000)
        server_socket.bind(server_address)
        server_socket.listen(5)  # Lausche auf bis zu 5 Clients
        print("Server lauscht auf Port 5000...")
        
        try:
            while True:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()
        except KeyboardInterrupt:
            print("Server wird heruntergefahren...")
            server_socket.close()
    
    start_server()

### Details

Threads ermöglichen es dem Server, mehrere Verbindungen gleichzeitig zu verwalten. Jede Verbindung wird in einem separaten Thread behandelt.

----------

# Clientseitiges Programm – Dokumentation

## Überblick

Diese Dokumentation beschreibt ein einfaches Client-Programm, das über Sockets eine Verbindung zu einem Server aufbaut, um Daten zu senden und Antworten zu erhalten.

## Anforderungen

-   Python 3.x
-   `socket` Modul

## Implementierung
    import socket
    
    def connect_to_server(ip, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try {
            client_socket.connect((ip, port))
            return client_socket
        except socket.error as e {
            print(f"Fehler bei der Verbindung zum Server: {e}")
            return None
    
    def send_data(client_socket):
        try {
            while True {
                message = input("Bitte geben Sie Daten zum Senden ein oder tippen Sie 'exit' zum Beenden: ")
                if message.lower() == 'exit':
                    break
                client_socket.send(message.encode())
                response = client_socket.recv(1024).decode()
                print(f"Serverantwort: {response}")
        except socket.error as e {
            print(f"Fehler während der Kommunikation: {e}")
        finally {
            client_socket.close()
    
    ip = "85.215.76.149"
    port = 5000
    client_socket = connect_to_server(ip, port)
    if client_socket {
        send_data(client_socket)

### Details

Dieser Client stellt eine Verbindung zum Server her und bietet eine Schnittstelle zum Senden von Daten. Antworten vom Server werden auf der Konsole gedruckt. Die Verbindung wird bei Beendigung oder Fehler geschlossen.# Serverseitiges Programm – Dokumentation

## Überblick

Diese Dokumentation beschreibt die Implementierung eines grundlegenden Servers mit der Socket-Programmierung in Python. Der Server ist darauf ausgelegt, Verbindungen für einzelne und mehrere Benutzer zu handhaben.

## Anforderungen

-   Python 3.x
-   `socket` Modul

## Verbindung für einzelne Benutzer

### Beschreibung

Dieses Skript richtet einen Server ein, der auf eingehende Verbindungen am Port 5000 lauscht. Es akzeptiert Verbindungen von einem Client, empfängt Daten und sendet eine Antwort zurück.

### Implementierung

    import socket
    
    # Erstelle ein Socket-Objekt
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Definiere die Serveradresse und den Port
    server_address = ('0.0.0.0', 5000)
    
    # Binde das Socket an die Serveradresse und den Port
    server_socket.bind(server_address)
    
    # Lausche auf eingehende Verbindungen
    server_socket.listen(1)
    print('Server lauscht auf eingehende Verbindungen...')
    
    while True:
        # Akzeptiere eine Clientverbindung
        client_socket, client_address = server_socket.accept()
        print(f'Verbunden mit Client: {client_address}')
        try:
            while True:
                # Empfange Daten vom Client
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(f'Empfangene Daten vom Client: {data}')
    
                # Sende eine Antwort zurück an den Client
                response = "Daten erfolgreich empfangen!"
                client_socket.send(response.encode())
        finally:
            # Schließe das Client-Socket
            client_socket.close()
            print(f'Verbindung zum Client {client_address} wurde geschlossen.')
            
### Details

Der Server bindet an alle verfügbaren Netzwerkschnittstellen und hört auf eingehende Verbindungen. Empfangene Daten vom Client werden gedruckt und bestätigt. Die Verbindung wird geschlossen, wenn keine Daten empfangen werden, was darauf hindeutet, dass der Client die Verbindung getrennt hat.

## Verbindung für mehrere Benutzer

### Beschreibung

Der Server wurde erweitert, um mehrere Clients gleichzeitig mithilfe von Threads zu handhaben.

### Implementierung

    import socket
    import threading
    
    def handle_client(client_socket, client_address):
        print(f"Client {client_address} verbunden.")
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    print(f"Keine Daten empfangen, schließe Verbindung zu {client_address}.")
                    break
                print(f'Empfangene Daten von {client_address}: {data}')
                response = "Daten erfolgreich empfangen!"
                client_socket.send(response.encode())
        except ConnectionResetError:
            print(f"Verbindung verloren mit {client_address}.")
        finally:
            client_socket.close()
            print(f'Verbindung zu {client_address} wurde geschlossen.')
    
    def start_server():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('0.0.0.0', 5000)
        server_socket.bind(server_address)
        server_socket.listen(5)  # Lausche auf bis zu 5 Clients
        print("Server lauscht auf Port 5000...")
        
        try:
            while True:
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()
        except KeyboardInterrupt:
            print("Server wird heruntergefahren...")
            server_socket.close()
    
    start_server()

### Details

Threads ermöglichen es dem Server, mehrere Verbindungen gleichzeitig zu verwalten. Jede Verbindung wird in einem separaten Thread behandelt.

----------

# Clientseitiges Programm – Dokumentation

## Überblick

Diese Dokumentation beschreibt ein einfaches Client-Programm, das über Sockets eine Verbindung zu einem Server aufbaut, um Daten zu senden und Antworten zu erhalten.

## Anforderungen

-   Python 3.x
-   `socket` Modul

## Implementierung

    import socket
    
    def connect_to_server(ip, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try {
            client_socket.connect((ip, port))
            return client_socket
        except socket.error as e {
            print(f"Fehler bei der Verbindung zum Server: {e}")
            return None
    
    def send_data(client_socket):
        try {
            while True {
                message = input("Bitte geben Sie Daten zum Senden ein oder tippen Sie 'exit' zum Beenden: ")
                if message.lower() == 'exit':
                    break
                client_socket.send(message.encode())
                response = client_socket.recv(1024).decode()
                print(f"Serverantwort: {response}")
        except socket.error as e {
            print(f"Fehler während der Kommunikation: {e}")
        finally {
            client_socket.close()
    
    ip = "85.215.76.149"
    port = 5000
    client_socket = connect_to_server(ip, port)
    if client_socket {
        send_data(client_socket) 

### Details

Dieser Client stellt eine Verbindung zum Server her und bietet eine Schnittstelle zum Senden von Daten. Antworten vom Server werden auf der Konsole gedruckt. Die Verbindung wird bei Beendigung oder Fehler geschlossen.
