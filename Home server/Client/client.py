import socket
import tqdm
import os

SEPERATOR = "[SEPARATOR]"
BUFFER_SIZE = 4096 #How many data sent each step

#HomeServer ip adress
host = "192.168.1.5"

# port
port = 5001

filename = "Rabin.zip"

filesize = os.path.getsize(filename)

s= socket.socket()

print(f"[+] Connecting to {host}:{port}")
try:
	s.connect((host,port))
	print("[+] Connection Sucessfull!")
	pass
except Exception as e:	
	print(f"[!] Connection unsucessfull!")
	print(f"[!] error code: {e}")
	exit()


s.send(f"{filename}{SEPERATOR}{filesize}".encode("utf-8"))

progess = tqdm.tqdm(range(filesize), f"Sending{filename}", unit = "B", unit_scale = True, unit_divisor= 1024)

with open(filename, "rb") as f:
	while True:
		bytes_read = f.read(BUFFER_SIZE)
		if not bytes_read:
			break

		s.sendall(bytes_read)

		progess.update(len(bytes_read))	

s.close()		




