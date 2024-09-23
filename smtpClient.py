from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Message"
    endmsg = "\r\n.\r\n"
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    clientSocket.recv(1024).decode()
    # Send HELO command
    heloCommand = 'HELO Mike\r\n'
    clientSocket.send(heloCommand.encode())
    clientSocket.recv(1024).decode()
    # Send MAIL FROM command
    mailCommand = 'MAIL FROM:<from@local.host\r\n'
    clientSocket.send(mailCommand.encode())
    clientSocket.recv(1024).decode()
    # Send RCPT TO command
    rcptCommand = 'RCPT TO:<rcpt@local.host\r\n'
    clientSocket.send(rcptCommand.encode())
    clientSocket.recv(1024).decode()
    # Send DATA command
    dataCommand = 'DATA\r\n\r\n'
    clientSocket.send(dataCommand.encode())
    clientSocket.recv(1024).decode()
    # Send message data
    emailData = "Subject: Sample mail\r\n" + "From: from@local.host\r\n" + "To: rcpt@local.host" + msg
    clientSocket.send(emailData.encode())
    # Message ends with a single period, send message end
    clientSocket.send(endmsg.encode())
    clientSocket.recv(1024).decode()
    # Send QUIT command
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    clientSocket.recv(1024).decode()
    # Close socket
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
