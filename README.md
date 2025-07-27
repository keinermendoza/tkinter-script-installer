# 📦 Instalador de Scripts

Este programa crea una interfaz gráfica que te permite instalar y ejecutar scripts de Python a través de una ventana interactiva.

## 🚀 Inicio Rápido
Crea un entorno virtual
```bash
python -m venv venv
```
Activa el entorno
```bash
source venv/bin/activate
```
- - -
> Si usas Windows sigue estas instrucciones para activar el ambiente virtual
<details>
 <summary>Activar ambiente virtual en <strong>Windows</strong></summary>

Abre PowerShell como administrador y ejecuta el siguiente comnado

```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Confirma la policy cuando te lo pregunte con **S**

Ahora puedes activar el ambiente con este comando

```shell
.\venv\Scripts\Activate.ps1
```
</details>

- - -
Instala las dependencias
```bash
pip install -r requirements.txt
```

Ejecuta el programa
```bash
python main.py
```



### Instalar Paquetes

Puedes cargar scripts creados por otras personas usando el botón **Cargar nuevo paquete** en la interfaz principal.

<img width="411" height="85" alt="step2" src="https://github.com/user-attachments/assets/17e4bc49-af93-4c3c-825c-b4110bd53f32" />

Esto abrirá el explorador de archivos de tkinter

> Si usas Windows la interfaz de las ventanas será la de costumbre

<img width="419" height="287" alt="step3" src="https://github.com/user-attachments/assets/cb3e9bfe-05fb-45a3-9a6b-e116ed70a775" />

Navega hasta donde se encuentra el archivador **.zip** del paquete que quieres instalar

<img width="420" height="286" alt="step4" src="https://github.com/user-attachments/assets/c8e29dcc-3879-46c4-8554-460077ef8955" />

Seleccionalo y haz click en **Abir**

<img width="406" height="120" alt="step5" src="https://github.com/user-attachments/assets/6f23f6ae-f886-470d-a441-f180330779cd" />

Ya está inslado!

---

### 🛠️ Crear tu Propio Paquete

Para crear tu propio paquete, debes crear una carpeta que contenga un archivo llamado `config.json` con los siguientes campos obligatorios:

- `name`: Nombre del paquete que se mostrará en el menú.
- `script`: Archivo `.py` que contiene la lógica principal del paquete.

También puedes agregar campos adicionales con información extra sobre tu paquete.

📄 **Ejemplo de `config.json`:**

```json
{
  "name": "Example",
  "script": "script.py"
}
```
### 🧩 Estructura del Script
En el archivo Python indicado en script, debes definir una función llamada run_app. Esta función será ejecutada por el programa principal y debe recibir dos argumentos posicionales:

1. ventana: Es la ventana principal de Tkinter. Puedes utilizarla para agregar widgets y permitir interacción con el usuario.

2. contexto: Es un diccionario que contiene información útil sobre el paquete y el entorno de ejecución. Incluye:

```python
{
  "name": str,       # Nombre del paquete
  "script": Path,    # Ruta del script
  "data": dict,      # Contenido completo de config.json
  "path": Path,      # Ruta de la carpeta del paquete
  "root_dir": Path   # Ruta del directorio raíz del programa principal
}
```

Esto te permite cargar recursos relativos al paquete o generar salidas en la carpeta output.


📄 **Ejemplo de `script.py`:**

```python
from tkinter import ttk

def show_package_info(context):
    print("The name of this package is:", context["name"])
    print("You can get the data defined in your config.json using the variable *data* inside context:", context["data"])
    print("The path of your package is:", context["path"])
    print("The path of the main program is:", context["root_dir"])

def run_app(window, context):
    window.title("Example script")
    window.geometry("300x200")
    button = ttk.Button(window, text="Show Info in Console", command=lambda:show_package_info(context))
    button.pack(pady=10)
```

### 📁 Estructura del Proyecto
Coloca cada paquete dentro de la carpeta packages/.

```
├── main.py
├── output/
├── packages/
│   └── example/
│       ├── config.json
│       └── script.py
├── README.md
└── requirements.txt
```

### 🌍 Compartir tus Paquetes
Para compartir un paquete, simplemente comprime la carpeta del paquete (la que contiene config.json y script.py) en un archivo .zip y súbelo a internet.

Otros usuarios podrán instalarlo usando el botón **Cargar nuevo paquete**, como se describe en la sección [Instalar Paquetes](#instalar-paquetes).
