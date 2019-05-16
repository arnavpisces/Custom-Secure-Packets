'''
Arnav Kumar - A naive approach to verify whether the data received from a json
is tampered with or not
'''
import socket #for socket api
import json #for interpreting the custom format of the data
import hashlib #for hash and digest functions
HOST = "0.0.0.0" #listen on all interfaces
PORT = 8081	#which port to listen to
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind ((HOST,PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('connected by', addr)
		while True:
			#the try except block is for ending packets which are sent by the sockets and don't have json data
			try:
				data=conn.recv(1024)
				decoded_data=data.decode() #convert from bytes to string
				json_data=json.loads(decoded_data) #convert the string to json format
				md5_present=json_data['verify'] #store the hash present in the json data
				#json_data['data']="this is the new data" #uncomment this line after which the hash present in the json and the calculated hash will be different and therefore the breach will be reported
				md5_calculated=(hashlib.md5(json_data['data'].encode()).hexdigest()) #from the data value in json, calculate the md5 hash again and store it
				if md5_present==md5_calculated:
					newdata="The data is not tampered"
					print(newdata)
					conn.sendall(newdata.encode())
				else:
					newdata="There has been a breach"
					print(newdata)
					conn.sendall(newdata.encode())
			except ValueError: #for handling the packets that don't have json data
				print("\nNot json packet, so no processing")
			print("data received : ",data)
			if not data:
				break
			conn.sendall(data)
