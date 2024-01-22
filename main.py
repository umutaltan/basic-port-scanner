from socket import *

def scanTcpPort(targethost, targetports):
    sock = socket(AF_INET,SOCK_STREAM)

    ip = gethostbyname(targethost)

    print("************")
    print("Ip         :",ip)

    try:
        host = gethostbyaddr(targethost)
        print("Reverse DNS:",host[0])
    except:
        host = "Unknown"
        print("Reverse DNS:",host)

    print("************")

    if targetports.find("-") != -1:
        ports = targetports.split("-")

        for port in range(int(ports[0]),int(ports[1])+1):
            try:
                sock.connect((targethost,port))
                print("%d open"%(port))
            except:
                print("%d close"%(port))

    else:
        ports = targetports.split()

        for port in ports:
            port = int(port)
            try:
                sock.connect((targethost,port))
                print("%d open"%(port))
            except:
                print("%d close"%(port))

host = input("Domain/Ip:")
port = input("Port(a b or a-b):")

scanTcpPort(host,port)



    