#Import socket module
import socket

def server_program():
    #Get host name and store in variable
    host = socket.gethostname()
    #Reserve port
    port = 6000 
    
    #Create socket instance
    server_socket = socket.socket() 
    #Bind the host IP and port to socket instance
    server_socket.bind((host, port))
    
    # Configure how many clients the server can listen to simultaneosly
    server_socket.listen(2)
    conn, address = server_socket.accept() # Accept new connection
    print("Connection from: " + str(address))
    
    while True:
        # Recieve data stream. (It won't accept data packets larger than 1024 bytes)
        data = conn.recv(1024).decode()
        
        if not data:
            # If data is not recieved break
            break
        
        print("From connected user: " + str(data))
        data = input(' --> ')
        conn.send(data.encode()) # Send data to the client
        
    conn.close() # Close the connection
    
if __name__ == '__main__':
    server_program()
        


