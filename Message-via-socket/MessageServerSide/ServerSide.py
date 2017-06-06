import socket
import wolframalpha
import wikipedia
import _thread
import tweepy
from textblob import TextBlob

def grabMessage():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1995))

    while True:

        receivedMessage = s.recv(10)
        receivedMessage = receivedMessage.decode('UTF-8')

        if receivedMessage != 'q':
            print(">>", receivedMessage)
        else:
            s.close()
            break

def sendMessage(message):

    '''
    Sends message to socket by encoding. If message equals to "Search" then program asks for source
    to look up. There are three API's, Twitter's, Wikipedia's and Wolframalpha's.
    Then sends answer to the other side and prints here also.

    Wikipedi's API searches for topics from www.wikipedia.com
    Wolframalpha's API searches for calculations etc. from www.wolframalpha.com
    Twitter's API searches for tweets that are posted currently about entered topic
    and analysis by textblob. (for now)

    If message equals to "q", then program closes the socket.(!)

    Each API's works correct by now.
    '''
    while True:

        message = input(">>")

        if message == "Search":
            clientSocket.send(message.encode('UTF-8'))


            sourceOf = int(input("Wikipedi - 1\nWolframaplha - 2\nTwitter - 3\n"))

            usersQuestion = input("Your question : ")

            clientSocket.send(usersQuestion.encode('UTF-8'))

            if sourceOf == 1:

                print("wikipedia")
                # Wikipedia
                wikipedia.set_lang("tr")
                answer = wikipedia.summary(quit(usersQuestion))
                clientSocket.send(answer.encode('UTF-8'))
                print(answer)

            elif sourceOf == 2:

                print("wolfram")
                # Wolframalpha
                app_id = "9TQPJR-425Q5GU6Q3"
                client = wolframalpha.Client(app_id)

                res = client.query(usersQuestion)
                answer = next(res.results).text
                clientSocket.send(answer.encode('UTF-8'))

                print(answer)

            elif sourceOf == 3:

                print("twitter")
                # Twitter
                twitter_consumer_key = 'Rs0czbhC4Rchd1BoU3yWKJH1C'
                twitter_consumer_secret = 'ar8udzr8PuluiG6yzloajWFGmMRp55to8JYr2qt5eZJ3w50Fwh'

                twitter_access_token = '792811803852038144-3v1tEVPbQTL9oINacZ94pDH62QONm9n'
                twitter_access_secret = 'XfRnWeb1u2kCYcwQCgq2RhzBZ0yjQa0SHJevIkr98UyDk'

                auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
                auth.set_access_token(twitter_access_token, twitter_access_secret)

                api = tweepy.API(auth)

                public_tweets = api.search(usersQuestion)

                for tweet in public_tweets:
                    print(tweet.text)
                    clientSocket.send(tweet.text.encode('UTF-8'))
                    analysis = TextBlob(tweet.text)
                    print(analysis.sentiment)
                    print("")
                    clientSocket.send(analysis.sentiment.encode('UTF-8'))
            else :
                print("You have entered wrong.")

        elif message != 'q':
            clientSocket.send(message.encode('UTF-8'))

        else:
            clientSocket.send(message.encode('UTF-8'))
            clientSocket.close()
            exit(sendMessage(message))

def connectTo():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serverSocket.bind(('127.0.0.1', 1995))
    serverSocket.listen(1)
    clientSocket, addr = serverSocket.accept()

    # Estahblishes the connection , listens and accepts socket

    print("Got a connection from %s" % str(addr))

if __name__ == '__main__':

    while True:
        _thread.start_new_thread(connectTo(),())
        _thread.start_new_thread(sendMessage, (message,))
        _thread.start_new_thread(grabMessage)

clientSocket.close()

print("Thanks for using the program. Quitted...")