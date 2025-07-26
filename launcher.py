# Aplicación de Python con interface hibrida que puede ejecutarse en modo CLI o GUI con la lógica separada en archivos individuales.

import argparse
import sys
from ui.gui.gui_app import run_gui
from ui.cli.cli_app import run_cli

def main():
    parser = argparse.ArgumentParser(description="App híbrida CLI/GUI")
    parser.add_argument("--cli", action="store_true", help="Ejecutar la app en modo CLI")
    args = parser.parse_args()

    if args.cli:
        run_cli()
    else:
        run_gui()

if __name__ == "__main__":
    main()
