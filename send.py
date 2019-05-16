'''Arnav Kumar - Naive approach to verify whether the data has been changed or not
(a very naive approach, just for demonstration purposes)'''

def main():
    import socket
    import hashlib, json
    # the template for the encapsulated data (just a naive representation)
    class secureData:
        def __init__(self):
            self.header='md5'
            self.data='this is the data'
            self.verify=''

    HOST = input()  # The server's hostname or IP address
    PORT = 8081        # The port used by the server

    p1=secureData() #creating an instance of the custom class
    hash_data=hashlib.md5(p1.data.encode()) #generating a md5 hash of the data
    p1.verify=hash_data.hexdigest() #storing the hash in the verify field of the instance
    jsonstring=json.dumps(p1.__dict__) #converting to json object to send over the network
    print(type(jsonstring)) 
    try:
        #opening a socket to send the data
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(jsonstring.encode()) #any data sent using the socket has to be converted to 'bytes' format (that's why encode())
            data = s.recv(1024) #receiving any data the server is sending
            print('Received', repr(data))
            return
    except ConnectionRefusedError: #so that the code keeps on trying to connect until it connects
        time.sleep(2) #to prevent recursion depth error
        main()

if __name__=='__main__':
    main()