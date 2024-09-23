from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    
    # Create a socket called clientSocket and establish a TCP connection with the mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    
    # Receive and decode the server's response to the connection
    recv = clientSocket.recv(1024).decode()
    print("Connection Response: " + recv)
    
    # Send HELO command to the server
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    
    # Receive and decode the server's response to the HELO command
    recv1 = clientSocket.recv(1024).decode()
    print("HELO Response: " + recv1)
    
    # Send MAIL FROM command to the server
    mailCommand = 'MAIL FROM:<from@local.host>\r\n'
    clientSocket.send(mailCommand.encode())
    
    # Receive and decode the server's response to the MAIL FROM command
    recv2 = clientSocket.recv(1024).decode()
    print("MAIL FROM Response: " + recv2)
    
    # Send RCPT TO command to the server
    rcptCommand = 'RCPT TO:<rcpt@local.host>\r\n'
    clientSocket.send(rcptCommand.encode())
    
    # Receive and decode the server's response to the RCPT TO command
    recv3 = clientSocket.recv(1024).decode()
    print("RCPT TO Response: " + recv3)
    
    # Send DATA command to the server
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    
    # Receive and decode the server's response to the DATA command
    recv4 = clientSocket.recv(1024).decode()
    print("DATA Response: " + recv4)
    
    # Send the email data
    emailData = "Subject: TEST EMAIL\r\n" + "From: from@local.host\r\n" + "To: rcpt@local.host" + msg
    clientSocket.send(emailData.encode())
    
    # Send the end of the message data
    clientSocket.send(endmsg.encode())
    
    # Receive and decode the server's response to the end of the message
    recv5 = clientSocket.recv(1024).decode()
    print("End of Message Response: " + recv5)
    
    # Send QUIT command to the server
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    
    # Receive and decode the server's response to the QUIT command
    recv6 = clientSocket.recv(1024).decode()
    print("QUIT Response: " + recv6)
    
    # Close the socket
    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
