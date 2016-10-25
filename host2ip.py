import socket
reader=open("host.txt","r")
out=open("ip.txt","w")
for host in reader.read().split('\n'):
	try:
		ip=socket.gethostbyname(host)
	except:
		ip="N/A"
	out.write(ip)
	out.write("\n")
out.close()
reader.close()