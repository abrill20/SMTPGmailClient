from socket import *
import base64, ssl

# Choose a mail server (e.g. Google mail server) and call it mail server
mailserver = "smtp.gmail.com"
# Create socket called client Socket and establish a TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = ssl.wrap_socket(clientSocket)
print('====================================')
print('Establishing connection...')
clientSocket.connect((mailserver,465))
recv = clientSocket.recv(1024).decode()
print("Server: ", recv)
if recv[:3] != '220':
  print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO smtp.gmail.com \r\n'
print('====================================')
print('Client: ', heloCommand)
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print("Server: ", recv)
if recv[:3] != '250':
  print('250 reply not received from server.')


################################
# Authentication
################################

username = input("Enter gmail username: ")
password = input("Enter gmail password: ")

authCommand = 'AUTH LOGIN\r\n'
print('====================================')
print('Client: ', authCommand)
clientSocket.send(authCommand.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)
username64 = base64.b64encode(username.encode())
password64 = base64.b64encode(password.encode())
print('Client: username (b64 encoded)\r\n')
clientSocket.send(username64)
clientSocket.send('\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)
print('Client: password (b64 encoded)\r\n')
clientSocket.send(password64)
clientSocket.send('\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)

################################
# Send MAIL FROM command and print server response.
################################
mailFrom = 'baronbrill@gmail.com'

mailFromCommand = 'MAIL FROM:<' + mailFrom + '>\r\n'
print('====================================')
print('Client: ', mailFromCommand)
clientSocket.send(mailFromCommand.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)

################################
# Send RCPT TO command and print server response.
################################
rcptTo = 'baronbrill@gmail.com'

rcptToCommand = 'RCPT TO:<' + rcptTo + '>\r\n'
print('====================================')
print('Client: ', rcptToCommand)
clientSocket.send(rcptToCommand.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)

################################
# Send DATA command and print server response.
################################

dataCommand = 'DATA\r\n'
print('====================================')
print('Client: ', dataCommand)
clientSocket.send(dataCommand.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)

################################
# Send message data.
################################

message = input("Enter a message: ")

message = message + '\r\n\r\n.\r\n'

print('====================================')
print('Client: ', message)
clientSocket.send(message.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)

################################
# Send QUIT command and get server response.
################################

quitCommand = 'QUIT\r\n'
print('====================================')
print('Client: ', quitCommand)
clientSocket.send(quitCommand.encode())
recv = clientSocket.recv(1024).decode()
print('Server: ', recv)

clientSocket.close()