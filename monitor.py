import subprocess
import socket

def ping(host):
    response = subprocess.call(['ping', '-c', '3', host])
    return response == 0

def obtener_ip(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None
    
def obtener_host(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None

if __name__ == "__main__":
    hosts = []
    print("Ingrese direcciones IP o dominios (deje el campo vacio para terminar):")

    while True:
        host = input("Dirección IP o dominio: ")
        if not host.strip():
            break
        hosts.append(host.strip())
    
    for host in hosts:
        ip = obtener_ip(host)
        if ip:
            print("Resolviendo:", host)
            print("IP:", ip)
            print("Host:", obtener_host(ip))
            if ping(ip):
                print("-" * 40)
                print(f"Ping a {host} ({ip}) exitoso. ✅")
            else:
                print("-" * 40)
                print(f"Ping a {host} ({ip}) fallido. ❌")
        else:
            print(f"No se pudo resolver el host: {host} ❌")
        print("-" * 40)
    print("Finalizado el monitoreo de estado de red. 👋")