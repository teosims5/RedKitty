import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT_NUMBER = 65432  # Port to listen on (non-privileged ports are > 1023)

# Initialize a server socket with the following parameters:
# AF_INET: specifying to use an IPv4 address
# SOCK_STREAM: spacifying to use a stream socket, e.g. TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allow the socket to quickly restart
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Use the host and port (defined above) to bind the server socket to the server
server_socket.bind((HOST, PORT_NUMBER))
# Start listening for incoming connections
server_socket.listen()

print(f"\nServer started at address {HOST}:{PORT_NUMBER}\n")

# Wait for a connection from a client
connection, address = server_socket.accept()

print(f"Client connected from: {address}\n")

# Use an infinite loop to keep the server running
while True:
  # Wait to receive a message from the client
  data = connection.recv(1024)
  # If no data is received, the client has disconnected
  if not data:
    break

  # Print the received data
  print("----- Received Message from client: -----\n")
  print(data.decode())
  print("----- End of received message -----\n")

  # Create a HTTP response message
  http_response = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
  <head>
    <title>My great website</title>
  </head>
  <body>
    <h1>Hello World!</h1>
  </body>
</html>
"""

  # Send the response to the client
  connection.send((http_response).encode())

  # Print the sent message
  print("----- Response sent from the server: -----\n")
  print(http_response)
  print("----- End of server response -----\n")

  # Closing all connections:
  connection.close()
  server_socket.close()

  # Stop the infinite server loop
  break
