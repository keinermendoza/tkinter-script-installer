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

Instala las dependencias
```bash
pip install -r requirements.txt
```

Ejecuta el programa
```bash
python main.py
```


### Instalar Paquetes

Puedes cargar scripts creados por otras personas usando el botón **Cargar Paquetes** en la interfaz principal.

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

Otros usuarios podrán instalarlo usando el botón **Cargar Paquetes**, como se describe en la sección [Instalar Paquetes](#instalar-paquetes).
