# Modulo de inicializacion grafica GUI para la aplicación híbrida CLI/GUI con logica separada.
import sys

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