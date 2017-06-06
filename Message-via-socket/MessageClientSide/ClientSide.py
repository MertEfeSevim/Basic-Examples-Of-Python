import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 1995))
print("Got a connection.")

'''
Estahblishes the connection and receives messages for printing.
If received message equals to "q" it should close the socket.
'''

while True :

    receivedMessage = s.recv(10)
    receivedMessage = receivedMessage.decode('UTF-8')

    if receivedMessage == "Search":
        print(">> Searching...")
        receivedQuestion = s.recv(10)
        print(">> Searching for",receivedQuestion.decode('UTF-8'))

    elif receivedMessage != 'q':
        print(">>", receivedMessage)

    else:
        s.close()

s.close()

print("Thanks")
