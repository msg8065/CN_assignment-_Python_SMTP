import socket

def smtp_client(port=587, mailserver='smtp.gmail.com'):
    msg = "\r\n My message.\r\n"
    endmsg = "\r\n.\r\n"
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((mailserver, port))
    
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '220':
        print('220 reply not received from server.')
        return
    
    heloCommand = 'HELO Alice\r\n'
    clientsocket.send(heloCommand.encode())
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '250':
        print('250 reply not received from server after HELO.')
        return
    
    clientsocket.send('STARTTLS\r\n'.encode())
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '220':
        print('220 reply not received from server after STARTTLS.')
        return
    
    # Here you would typically upgrade the connection to TLS
    # This requires additional libraries such as ssl to wrap the socket.
    
    mailFromCommand = 'MAIL FROM: <msg8065@nyu.edu>\r\n'
    clientsocket.send(mailFromCommand.encode())
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '250':
        print('250 reply not received from server after MAIL FROM.')
        return
    
    rcptToCommand = 'RCPT TO: <manjit.msg@gmail.com>\r\n'
    clientsocket.send(rcptToCommand.encode())
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '250':
        print('250 reply not received from server after RCPT TO.')
        return
    
    dataCommand = 'DATA\r\n'
    clientsocket.send(dataCommand.encode())
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '354':
        print('354 reply not received from server after DATA.')
        return
    
    clientsocket.send(msg.encode())
    clientsocket.send(endmsg.encode())
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '250':
        print('250 reply not received from server after message data.')
        return
    
    quitCommand = 'QUIT\r\n'
    clientsocket.send(quitCommand.encode())
    recv = clientsocket.recv(1024).decode()
    if recv[:3] != '221':
        print('221 reply not received from server after QUIT.')
    
    clientsocket.close()

if __name__ == '__main__':
    smtp_client(587, 'smtp.gmail.com')
