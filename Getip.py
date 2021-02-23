import sys, socket

def getip(hostname):
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]

hostname = socket.gethostname()
print ("Host name:", hostname)

print (socket.getfqdn(hostname))
try:
    print (", ".join(getip(hostname)))
except (socket.gaierror, e):
    print ("Couldn't not get IP addresses:", e)
