# integrador-ayso-cornejo-dantur-
# Explicacion paso a paso del desarollo del codigo

---------------------------------------------------------------------------------

Importar módulos necesarios:

import subprocess
import socket
Se importan dos librerías de Python:

subprocess permite ejecutar comandos del sistema operativo (en este caso, el comando ping).

socket se usa para trabajar con conexiones de red, como obtener direcciones IP o nombres de host.

Definir la función ping:

def ping(host):
    response = subprocess.call(['ping', '-c', '3', host])
    return response == 0
Esta función usa el comando ping para intentar contactar a una dirección (puede ser IP o dominio).

-c 3 significa que se hacen 3 intentos de ping.

Si el ping tiene éxito, devuelve True; si falla, devuelve False.

Definir la función obtener_ip:


def obtener_ip(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return None
Esta función recibe un dominio (como google.com) y trata de obtener su IP.

Si lo logra, devuelve la IP.

Si no puede (por ejemplo, si el dominio no existe), devuelve None.

Definir la función obtener_host:



def obtener_host(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return None
Esta función hace lo contrario de la anterior: recibe una IP y trata de obtener el nombre del host (dominio).

Si puede resolverla, devuelve el nombre.

Si no, devuelve None.

Inicio del programa principal:

if __name__ == "__main__":
Esto indica que lo que sigue se va a ejecutar solo si el archivo se corre directamente (no si se importa en otro código).

Ingreso de direcciones por el usuario:

hosts = []
print("Ingrese direcciones IP o dominios (deje el campo vacio para terminar):")

while True:
    host = input("Dirección IP o dominio: ")
    if not host.strip():
        break
    hosts.append(host.strip())
Acá se le pide al usuario que escriba varias direcciones IP o dominios. Cuando deja el campo vacío, el programa termina la entrada de datos. Todas las direcciones se guardan en una lista llamada hosts.

Proceso para cada dirección ingresada:

for host in hosts:
    ip = obtener_ip(host)
    if ip:
        ...
Por cada dirección:

Intenta obtener la IP.

Si la IP existe:

Muestra la IP y trata de obtener el nombre del host.

Hace ping a la IP y muestra si responde o no.

Si no pudo obtener la IP, muestra un mensaje de error.

Mensajes de salida:

Dependiendo de si el host responde al ping o si no se puede resolver, el programa muestra mensajes claros:

Ping exitoso: ✅

Ping fallido o error de resolución: ❌

Mensaje final:

print("Finalizado el monitoreo de estado de red. 👋")
Al terminar con todas las direcciones, se muestra un mensaje que indica que el monitoreo ha finalizado.


