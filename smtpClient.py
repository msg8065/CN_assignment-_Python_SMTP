Import socket

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message.\r\n"
    endmsg = "\r\n.\r\n"

    server_hostname = "smtp.gmail.com"
    server_port = 1025
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((mailserver, port))

    recv = clientsocket.recv(1024).decode()
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    
    heloCommand = 'HELO Alice\r\n'
    clientsocket.send(heloCommand.encode())
    recv = clientsocket.recv(1024).decode()
    #print(recv)

    
    clientsocket.send('STARTTLS\r\n'.encode())
    recv = clientsocket.recv(1024).decode()
    #print(recv)

    
    mailFromCommand = 'MAIL FROM: <msg8065@nyu.edu>\r\n'
    clientsocket.send(mailFromCommand.encode())
    recv = clientsocket.recv(1024).decode()
    #print(recv)

    
    rcptToCommand = 'RCPT TO: <manjit.msg@gmail.com>\r\n'
    clientsocket.send(rcptToCommand.encode())
    recv = clientsocket.recv(1024).decode()
    #print(recv)

    
    dataCommand = 'DATA\r\n'
    clientsocket.send(dataCommand.encode())
    recv = clientsocket.recv(1024).decode()
    #print(recv)

    
    clientsocket.send(msg.encode())
    clientsocket.send(endmsg.encode())
    recv = clientsocket.recv(1024).decode()
    #print(recv)

    
    quitCommand = 'QUIT\r\n'
    clientsocket.send(quitCommand.encode())
    recv = clientsocket.recv(1024).decode()
    #print(recv)

    clientsocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
