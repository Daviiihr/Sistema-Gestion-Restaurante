Crear un entorno virtual `.venv` y activar dependencias

Requisitos (Debian/Ubuntu):
- Tener privilegios para instalar paquetes del sistema (sudo).

Pasos:
1. Instale el paquete del sistema que provee venv (si falta):
   sudo apt update
   sudo apt install python3.12-venv

2. Cree el entorno virtual en el directorio del proyecto:
   python3 -m venv .venv

3. Active el entorno virtual:
   source .venv/bin/activate

4. Actualice pip y luego instale dependencias:
   pip install --upgrade pip
   pip install -r requirements.txt

Notas:
- En este entorno de ejecución automatizado la creación de `.venv` falló debido a que
  'ensurepip' no está disponible en la instalación de sistema de Python. Por eso las
  dependencias se instalaron en el entorno de usuario mediante pip (no en `.venv`).
- Si desea que le cree el `.venv` directamente aquí, se requiere instalar el paquete
  `python3.12-venv` en el sistema (acción que normalmente requiere sudo y privilegios).