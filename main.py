# Aplicación de Python con interface hibrida que puede ejecutarse en modo CLI o GUI con la lógica unificada en un solo archivo.

import argparse
import sys

# Logica de ejecucion para CLI
def run_cli():
    print("Modo CLI activado")
    # Aquí va tu lógica de línea de comandos
    nombre = input("¿Cuál es tu nombre? ")
    print(f"Hola, {nombre} (desde CLI)")

# Logica de ejecucion para GUI
def run_gui():
    print("Modo GUI activado")
    # Aquí tu código para la interfaz gráfica (ej. PySide6, Tkinter, NiceGUI, etc.)
    from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QLabel("Hola desde la interfaz gráfica"))
    window.setLayout(layout)
    window.setWindowTitle("App GUI")
    window.show()
    sys.exit(app.exec())

def main():
    parser = argparse.ArgumentParser(description="App con GUI y CLI en Python")
    parser.add_argument("--cli", action="store_true", help="Iniciar la app en modo CLI en lugar de GUI")
    args = parser.parse_args()

    if args.cli:
        run_cli()
    else:
        run_gui()

if __name__ == "__main__":
    main()
