# import socket module
from socket import *

import chardet as chardet

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
hostname = "192.168.43.3"
serverPort = 4444
serverSocket.bind((hostname, serverPort))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    print("successful")
    # Fill in end
    try:
        # Fill in start
        message = connectionSocket.recv(1024)
        # Fill in end
        file_path = 'E:\Temp\\'
        filename = message.split()[1].decode("utf-8")
        file_file_path = file_path + filename[1:]
        f = open(file_file_path, 'r', encoding='UTF-8')
        # Fill in start

        outputdata = f.read()
        # Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        http_response = "HTTP/1.1 200 OK\r\n"
        http_response += "Content-Type: text/html\r\n"
        http_response += "\r\n"  # 响应头部和响应体之间有一个空行
        connectionSocket.send(http_response.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('utf-8'))
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        response = "404 Not Found"
        connectionSocket.send(response.encode('utf-8'))
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
    serverSocket.close()
