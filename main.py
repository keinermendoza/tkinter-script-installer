import json
import sys
import os
import shutil
import zipfile
import tarfile
from tkinter import filedialog
import importlib.util
from pathlib import Path
import tkinter as tk

def load_packages(root_dir: Path):
    packages = []
    package_dir = root_dir / "packages"
    
    if package_dir.is_dir():
        for dir in package_dir.iterdir():
            if dir.is_dir():
                config_path = dir / "config.json"
                if config_path.exists():
                    try:
                        with open(config_path, "r", encoding="utf-8") as f:
                            metadata = json.load(f)
                      
                        packages.append({
                            "name": metadata.get("name", "Desconocido"),
                            "script": str(dir / metadata.get("script", "")),
                            "data": metadata,
                            "path": dir,
                            "root_dir":root_dir
                        })
                    except Exception as e:
                        print(f"Error en {config_path}: {e}")
    return packages

def abrir_ventana_detalle(paquete):
    module_name = "module.name"
    spec = importlib.util.spec_from_file_location(module_name, paquete["script"])
    script = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = script
    spec.loader.exec_module(script)
    ventana = tk.Toplevel()
    script.run_app(ventana, paquete)

# This function will now be responsible for rendering/re-rendering the package buttons
def render_package_buttons(parent_frame, packages_list):
    # Clear existing buttons (if any)
    for widget in parent_frame.winfo_children():
        # Make sure not to delete the "Cargar nuevo paquete" button
        if isinstance(widget, tk.Button) and widget["text"] != "📦 Cargar nuevo paquete":
            widget.destroy()

    for i, paquete in enumerate(packages_list, 1):
        btn = tk.Button(parent_frame, text=paquete["name"], command=lambda p=paquete: abrir_ventana_detalle(p))
        # We need to adjust the row index because the "Cargar nuevo paquete" button is at row 0
        btn.grid(row=i, column=0, sticky="ew", padx=10, pady=5)


def main():
    root = tk.Tk()
    root.title("Lista de Paquetes")
    root.columnconfigure(0, weight=1, minsize=400)

    # Use a lambda to pass the root window to the function
    btn_cargar = tk.Button(root, text="📦 Cargar nuevo paquete", command=lambda: seleccionar_y_extraer_paquete(root))
    btn_cargar.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

    # Initial rendering of packages
    current_packages = load_packages(Path.cwd())
    render_package_buttons(root, current_packages)
    root.mainloop()




# Modified to accept the root window
def seleccionar_y_extraer_paquete(root_window):
    packages_dir = os.path.join(Path.cwd(), "packages")
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo comprimido",
        filetypes=[("ZIP files", "*.zip"), ("TAR.GZ files", "*.tar.gz *.tgz")]
    )

    if not archivo:
        print("No se seleccionó ningún archivo.")
        return

    nombre_archivo = os.path.basename(archivo)
    nombre_paquete = os.path.splitext(nombre_archivo)[0]
    destino = os.path.join(packages_dir, nombre_paquete)

    if os.path.exists(destino):
        print(f"El paquete '{nombre_paquete}' ya existe.")
        return

    os.makedirs(destino, exist_ok=True)

    try:
        if archivo.endswith(".zip"):
            with zipfile.ZipFile(archivo, 'r') as zip_ref:
                for member in zip_ref.namelist():
                    filename = os.path.basename(member)
                    if not filename:
                        continue  # omitimos carpetas vacías
                    source = zip_ref.open(member)
                    target_path = os.path.join(destino, filename)
                    with open(target_path, "wb") as target:
                        shutil.copyfileobj(source, target)

        elif archivo.endswith((".tar.gz", ".tgz")):
            with tarfile.open(archivo, "r:gz") as tar_ref:
                # Ensure extraction is into the 'destino' directory
                tar_ref.extractall(destino)
        else:
            print("Formato de archivo no soportado.")
            return

        print(f"✅ Paquete '{nombre_paquete}' extraído en: {destino}")
        
        # --- Crucial change: Re-render the package list ---
        updated_packages = load_packages(Path.cwd())
        render_package_buttons(root_window, updated_packages)
        # --- End crucial change ---

    except Exception as e:
        print(f"❌ Error: {e}")
        # Clean up if extraction fails
        if os.path.exists(destino):
            shutil.rmtree(destino)


if __name__ == "__main__":
    # Ensure the 'packages' directory exists at the root_dir
    os.makedirs(Path.cwd() / "packages", exist_ok=True)
    main()
