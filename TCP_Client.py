# TCP CLIENT SIDE
import socket

def client_program():
    host = socket.gethostname() # Because both programs are running on same PC
    port = 5000 # Socket server port number
    
    client_socket = socket.socket() # Instantiate
    client_socket.connect((host, port)) # Connect to server
    
    message = input(" --> ") # Take input
    
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) # Send message
        data = client_socket.recv(1024).decode() # Recieve response
        
        print(f"Recieved from server: {data}") # Print in terminal
        
        message = input(" --> ") # Take another input
        
    client_socket.close() # Close connection


if __name__ == '__main__':
    client_program()
    

