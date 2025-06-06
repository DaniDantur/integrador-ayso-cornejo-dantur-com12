# Monitor de Red en Entorno Virtualizado


## 📌 Descripción del Proyecto


Este proyecto consiste en un **monitor de red básico desarrollado en Python**, diseñado y ejecutado dentro de un entorno virtualizado. A través del uso de comandos como `ping` y funciones de resolución de nombres/IP, el programa permite verificar el estado de conectividad de diferentes direcciones IP o dominios.


El objetivo principal es demostrar cómo un entorno virtual (usando herramientas como **VirtualBox** y **Debian** Linux) puede ser utilizado como un espacio de pruebas seguro, replicable y aislado para desarrollar y ejecutar aplicaciones de red sin comprometer el sistema anfitrión.


## 🧪 Tecnologías Utilizadas


- 💻 **VirtualBox** – para crear la máquina virtual.
- 🐧 **Debian** – sistema operativo instalado en la VM.
- 🐍 **Python 3** – lenguaje de programación utilizado.
- 🧠 **VS Code con Remote SSH** – para trabajar desde la máquina anfitriona directamente sobre la VM.


## ⚙️ ¿Cómo funciona el script?


El programa realiza las siguientes acciones:


1. **Solicita al usuario direcciones IP o dominios**.
2. **Resuelve el dominio a su dirección IP**.
3. **Resuelve el nombre de host a partir de la IP**.
4. **Envía un ping para comprobar conectividad**.
5. **Muestra los resultados de forma clara y ordenada**.


Ejemplo de salida:


Resolviendo: google.com
IP: 142.250.78.206
Host: mad02s27-in-f14.1e100.net
Ping a google.com (142.250.78.206) exitoso. ✅


## 🧭 Objetivo Educativo


Este proyecto forma parte de un trabajo práctico orientado a:


- Aprender los fundamentos de la virtualización.
- Implementar scripts de red simples.
- Familiarizarse con entornos Linux y herramientas de desarrollo remoto.
- Utilizar máquinas virtuales para realizar pruebas sin afectar el entorno principal.


## ✅ Ventajas de usar virtualización


- Aislamiento del entorno de pruebas.
- Mayor seguridad para experimentar.
- Reproducibilidad: se puede reinstalar o compartir la VM fácilmente.
- Ideal para prácticas de administración de sistemas y redes.


## 🚀 Requisitos para ejecutar el proyecto


- Máquina virtual Debian con Python 3 instalado.
- Acceso a red desde la VM.
- Terminal o entorno como VS Code conectado vía SSH.


## 🔚 Conclusión


Este proyecto muestra cómo la virtualización permite un desarrollo más seguro, flexible y profesional. Además, ejemplifica cómo se pueden realizar pequeñas herramientas útiles para tareas de diagnóstico de red desde un entorno totalmente controlado.
