#!/usr/bin/env python3
"""
🎯 Script de Configuración Inicial del Template Python Hybrid
==============================================================

Este script interactivo guía al usuario para configurar el template según sus necesidades:
1. Selección del tipo de lógica (Unificada vs Separada)
2. Selección del tipo de interfaz (Híbrida, Solo GUI, Solo CLI)
3. Limpieza automática de archivos y código no utilizados

Autor: Party-Templates
Licencia: MIT
"""

import os
import sys
import shutil
from pathlib import Path


class Colors:
    """Códigos de colores ANSI para terminal"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(text):
    """Imprime un encabezado destacado"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'=' * 70}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text.center(70)}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'=' * 70}{Colors.ENDC}\n")


def print_section(text):
    """Imprime una sección"""
    print(f"\n{Colors.CYAN}{Colors.BOLD}{text}{Colors.ENDC}")
    print(f"{Colors.CYAN}{'-' * len(text)}{Colors.ENDC}")


def print_info(text):
    """Imprime información general"""
    print(f"{Colors.BLUE}{text}{Colors.ENDC}")


def print_success(text):
    """Imprime un mensaje de éxito"""
    print(f"{Colors.GREEN}✓ {text}{Colors.ENDC}")


def print_warning(text):
    """Imprime una advertencia"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.ENDC}")


def print_error(text):
    """Imprime un error"""
    print(f"{Colors.RED}✗ {text}{Colors.ENDC}")


def print_option(number, title, description):
    """Imprime una opción de selección"""
    print(f"\n{Colors.BOLD}{number}. {title}{Colors.ENDC}")
    print(f"   {description}")


def get_user_choice(prompt, valid_options):
    """
    Solicita al usuario una elección y valida la entrada
    
    Args:
        prompt: Texto del prompt
        valid_options: Lista de opciones válidas (como strings)
    
    Returns:
        La opción seleccionada (como string)
    """
    while True:
        print(f"\n{Colors.BOLD}{prompt}{Colors.ENDC}", end=" ")
        choice = input().strip()
        
        if choice in valid_options:
            return choice
        else:
            print_error(f"Opción inválida. Por favor, elige entre: {', '.join(valid_options)}")


def show_welcome():
    """Muestra el mensaje de bienvenida"""
    print_header("🐍 CONFIGURADOR INTERACTIVO - Python Hybrid Template")
    
    print(f"{Colors.BOLD}¡Bienvenido!{Colors.ENDC}")
    print()
    print("Este asistente te ayudará a configurar tu template Python Hybrid")
    print("según tus necesidades específicas del proyecto.")
    print()
    print(f"{Colors.YELLOW}📋 Pasos del proceso:{Colors.ENDC}")
    print("  1️⃣  Selección del tipo de lógica (Unificada o Separada)")
    print("  2️⃣  Selección del tipo de interfaz (Híbrida, GUI o CLI)")
    print("  3️⃣  Limpieza automática de archivos no necesarios")
    print()
    print_warning("Este proceso eliminará archivos. Asegúrate de tener un backup si es necesario.")
    print()
    
    input(f"{Colors.BOLD}Presiona ENTER para continuar...{Colors.ENDC}")


def explain_logic_types():
    """Explica los tipos de lógica disponibles"""
    print_header("📚 PASO 1: Selección del Tipo de Lógica")
    
    print_section("¿Qué es el Tipo de Lógica?")
    print_info(
        "El tipo de lógica determina cómo está organizado el código de tu aplicación.\n"
        "Hay DOS enfoques disponibles:"
    )
    
    # OPCIÓN 1: Lógica Unificada
    print_option(
        "1",
        "LÓGICA UNIFICADA (main.py)",
        "Todo el código en un solo archivo - Enfoque simple y directo"
    )
    
    print(f"\n   {Colors.BOLD}📄 Características:{Colors.ENDC}")
    print("   • Un solo archivo: main.py contiene toda la lógica")
    print("   • CLI y GUI implementadas en el mismo archivo")
    print("   • Ideal para prototipos y proyectos pequeños")
    print("   • Fácil de entender de un vistazo")
    
    print(f"\n   {Colors.BOLD}✅ Ventajas:{Colors.ENDC}")
    print("   • Arranque ultra-rápido (5 minutos)")
    print("   • Simple y fácil de entender")
    print("   • Todo el código en un lugar")
    print("   • Perfecto para aprender el concepto")
    
    print(f"\n   {Colors.BOLD}❌ Limitaciones:{Colors.ENDC}")
    print("   • Difícil de escalar a proyectos grandes")
    print("   • Testing más complicado")
    print("   • Menos organizado para equipos")
    
    print(f"\n   {Colors.BOLD}🎯 Casos de uso ideales:{Colors.ENDC}")
    print("   • Prototipos rápidos")
    print("   • Proyectos personales/escolares")
    print("   • Aplicaciones < 500 líneas")
    print("   • Scripts de un solo uso")
    print("   • Aprendizaje y experimentación")
    
    # OPCIÓN 2: Lógica Separada
    print_option(
        "2",
        "LÓGICA SEPARADA (launcher.py)",
        "Código modularizado en archivos separados - Enfoque profesional"
    )
    
    print(f"\n   {Colors.BOLD}📦 Características:{Colors.ENDC}")
    print("   • Arquitectura modular organizada")
    print("   • CLI en ui/cli/cli_app.py")
    print("   • GUI en ui/gui/gui_app.py")
    print("   • Lógica compartida en core/")
    print("   • Fácil de mantener y testear")
    
    print(f"\n   {Colors.BOLD}✅ Ventajas:{Colors.ENDC}")
    print("   • Altamente escalable")
    print("   • Código organizado y limpio")
    print("   • Fácil de testear (unit tests)")
    print("   • Colaboración eficiente en equipos")
    print("   • Separación clara de responsabilidades")
    
    print(f"\n   {Colors.BOLD}❌ Limitaciones:{Colors.ENDC}")
    print("   • Setup inicial más complejo")
    print("   • Más archivos que gestionar")
    print("   • Curva de aprendizaje ligeramente mayor")
    
    print(f"\n   {Colors.BOLD}🎯 Casos de uso ideales:{Colors.ENDC}")
    print("   • Proyectos profesionales/comerciales")
    print("   • Aplicaciones de producción")
    print("   • Trabajo en equipo")
    print("   • Proyectos > 500 líneas")
    print("   • Mantenimiento a largo plazo")
    print("   • Integración con CI/CD")
    
    # Comparación
    print_section("📊 Comparación Rápida")
    print(f"""
    {'Característica':<25} {'Unificada':<20} {'Separada':<20}
    {'-' * 65}
    {'Archivos principales':<25} {'1 (main.py)':<20} {'3+ archivos':<20}
    {'Complejidad inicial':<25} {'⭐ Baja':<20} {'⭐⭐⭐ Media':<20}
    {'Escalabilidad':<25} {'⭐⭐':<20} {'⭐⭐⭐⭐⭐':<20}
    {'Mantenibilidad':<25} {'⭐⭐':<20} {'⭐⭐⭐⭐⭐':<20}
    {'Testing':<25} {'⭐⭐':<20} {'⭐⭐⭐⭐⭐':<20}
    {'Tiempo de setup':<25} {'5 minutos':<20} {'15 minutos':<20}
    """)
    
    print_section("💡 Recomendación")
    print_info(
        "• Si estás empezando o haciendo un prototipo → Elige LÓGICA UNIFICADA (1)\n"
        "• Si es un proyecto serio o de equipo → Elige LÓGICA SEPARADA (2)"
    )


def select_logic_type():
    """Solicita al usuario que seleccione el tipo de lógica"""
    choice = get_user_choice(
        "Selecciona el tipo de lógica [1 o 2]:",
        ["1", "2"]
    )
    
    if choice == "1":
        print_success("Has seleccionado: LÓGICA UNIFICADA (main.py)")
        return "unified"
    else:
        print_success("Has seleccionado: LÓGICA SEPARADA (launcher.py)")
        return "separated"


def explain_interface_types():
    """Explica los tipos de interfaz disponibles"""
    print_header("🎨 PASO 2: Selección del Tipo de Interfaz")
    
    print_section("¿Qué es el Tipo de Interfaz?")
    print_info(
        "El tipo de interfaz determina cómo los usuarios interactuarán con tu aplicación.\n"
        "Hay TRES opciones disponibles:"
    )
    
    # OPCIÓN 1: Híbrida
    print_option(
        "1",
        "HÍBRIDA (CLI + GUI)",
        "Soporta ambas interfaces - Máxima flexibilidad"
    )
    
    print(f"\n   {Colors.BOLD}🔄 Características:{Colors.ENDC}")
    print("   • Puede ejecutarse en modo terminal (CLI)")
    print("   • Puede ejecutarse en modo ventana (GUI)")
    print("   • El usuario elige con el flag --cli")
    print("   • Sin flag: abre GUI | Con --cli: usa terminal")
    
    print(f"\n   {Colors.BOLD}✅ Ventajas:{Colors.ENDC}")
    print("   • Máxima flexibilidad de uso")
    print("   • Automatizable (CLI) e interactivo (GUI)")
    print("   • Perfecto para diferentes contextos")
    print("   • Usuarios técnicos y no técnicos")
    
    print(f"\n   {Colors.BOLD}❌ Consideraciones:{Colors.ENDC}")
    print("   • Mantener dos interfaces requiere más trabajo")
    print("   • Dependencias de GUI necesarias (PySide6, etc.)")
    print("   • Código más completo")
    
    print(f"\n   {Colors.BOLD}🎯 Casos de uso ideales:{Colors.ENDC}")
    print("   • Herramientas de desarrollo (CLI para scripts, GUI para config)")
    print("   • Aplicaciones de datos (CLI para batch, GUI para visualización)")
    print("   • Utilidades del sistema (CLI para remoto, GUI para local)")
    print("   • Aplicaciones empresariales versátiles")
    
    # OPCIÓN 2: Solo GUI
    print_option(
        "2",
        "SOLO GUI (Interfaz Gráfica)",
        "Solo interfaz gráfica de ventanas - Para usuarios finales"
    )
    
    print(f"\n   {Colors.BOLD}🎨 Características:{Colors.ENDC}")
    print("   • Solo interfaz gráfica con ventanas")
    print("   • Elimina todo el código CLI")
    print("   • No requiere argparse")
    print("   • Ejecutable directo sin argumentos")
    
    print(f"\n   {Colors.BOLD}✅ Ventajas:{Colors.ENDC}")
    print("   • Interfaz visual intuitiva")
    print("   • Perfecto para usuarios no técnicos")
    print("   • Código más simple (sin CLI)")
    print("   • Experiencia de usuario amigable")
    
    print(f"\n   {Colors.BOLD}❌ Consideraciones:{Colors.ENDC}")
    print("   • No automatizable desde terminal")
    print("   • Requiere display gráfico")
    print("   • No funciona en servidores sin GUI")
    
    print(f"\n   {Colors.BOLD}🎯 Casos de uso ideales:{Colors.ENDC}")
    print("   • Aplicaciones de escritorio para usuarios finales")
    print("   • Herramientas visuales de diseño o edición")
    print("   • Dashboards y paneles de control")
    print("   • Aplicaciones multimedia")
    
    # OPCIÓN 3: Solo CLI
    print_option(
        "3",
        "SOLO CLI (Línea de Comandos)",
        "Solo interfaz de terminal - Para automatización"
    )
    
    print(f"\n   {Colors.BOLD}⌨️  Características:{Colors.ENDC}")
    print("   • Solo interfaz de línea de comandos")
    print("   • Elimina todo el código GUI")
    print("   • No requiere dependencias gráficas")
    print("   • Ligero y rápido")
    
    print(f"\n   {Colors.BOLD}✅ Ventajas:{Colors.ENDC}")
    print("   • Ultraligero (sin deps de GUI)")
    print("   • Fácil de automatizar")
    print("   • Perfecto para servidores y scripts")
    print("   • Rápido de ejecutar")
    print("   • SSH y acceso remoto friendly")
    
    print(f"\n   {Colors.BOLD}❌ Consideraciones:{Colors.ENDC}")
    print("   • Solo para usuarios técnicos")
    print("   • No hay interfaz visual")
    print("   • Curva de aprendizaje para usuarios finales")
    
    print(f"\n   {Colors.BOLD}🎯 Casos de uso ideales:{Colors.ENDC}")
    print("   • Scripts de automatización")
    print("   • Herramientas de servidor")
    print("   • Procesamiento batch")
    print("   • Integración con CI/CD")
    print("   • Herramientas de administración")
    
    # Comparación
    print_section("📊 Comparación Rápida")
    print(f"""
    {'Característica':<25} {'Híbrida':<15} {'Solo GUI':<15} {'Solo CLI':<15}
    {'-' * 70}
    {'Flexibilidad':<25} {'⭐⭐⭐⭐⭐':<15} {'⭐⭐⭐':<15} {'⭐⭐⭐':<15}
    {'Facilidad de uso':<25} {'⭐⭐⭐⭐':<15} {'⭐⭐⭐⭐⭐':<15} {'⭐⭐':<15}
    {'Automatizable':<25} {'Sí':<15} {'No':<15} {'Sí':<15}
    {'Peso (deps)':<25} {'Medio':<15} {'Medio':<15} {'Ligero':<15}
    {'Usuario objetivo':<25} {'Todos':<15} {'No técnico':<15} {'Técnico':<15}
    """)
    
    print_section("💡 Recomendación")
    print_info(
        "• Si necesitas flexibilidad máxima → Elige HÍBRIDA (1)\n"
        "• Si es una app para usuarios finales → Elige SOLO GUI (2)\n"
        "• Si es una herramienta de automatización → Elige SOLO CLI (3)"
    )


def select_interface_type():
    """Solicita al usuario que seleccione el tipo de interfaz"""
    choice = get_user_choice(
        "Selecciona el tipo de interfaz [1, 2 o 3]:",
        ["1", "2", "3"]
    )
    
    if choice == "1":
        print_success("Has seleccionado: HÍBRIDA (CLI + GUI)")
        return "hybrid"
    elif choice == "2":
        print_success("Has seleccionado: SOLO GUI")
        return "gui_only"
    else:
        print_success("Has seleccionado: SOLO CLI")
        return "cli_only"


def confirm_selection(logic_type, interface_type):
    """Confirma la selección del usuario antes de proceder"""
    print_header("📋 Confirmación de Selección")
    
    logic_name = "LÓGICA UNIFICADA (main.py)" if logic_type == "unified" else "LÓGICA SEPARADA (launcher.py)"
    
    interface_names = {
        "hybrid": "HÍBRIDA (CLI + GUI)",
        "gui_only": "SOLO GUI",
        "cli_only": "SOLO CLI"
    }
    interface_name = interface_names[interface_type]
    
    print(f"\n{Colors.BOLD}Tu configuración seleccionada:{Colors.ENDC}\n")
    print(f"  {Colors.CYAN}🔧 Tipo de Lógica:{Colors.ENDC}    {Colors.BOLD}{logic_name}{Colors.ENDC}")
    print(f"  {Colors.CYAN}🎨 Tipo de Interfaz:{Colors.ENDC}  {Colors.BOLD}{interface_name}{Colors.ENDC}")
    
    print(f"\n{Colors.YELLOW}⚠️  ADVERTENCIA:{Colors.ENDC}")
    print("  El proceso eliminará los archivos y código que no uses.")
    print("  Esta acción NO se puede deshacer fácilmente.")
    
    print(f"\n{Colors.BOLD}¿Deseas continuar con esta configuración? [s/n]:{Colors.ENDC}", end=" ")
    choice = input().strip().lower()
    
    return choice in ['s', 'si', 'sí', 'y', 'yes']


def clean_unified_hybrid(base_path):
    """
    Limpia el template para: Lógica Unificada + Interfaz Híbrida
    Mantiene: main.py con CLI y GUI
    Elimina: launcher.py, ui/, core/, utils/
    """
    print_section("🧹 Limpiando archivos innecesarios...")
    
    files_to_remove = [
        'launcher.py',
    ]
    
    dirs_to_remove = [
        'ui',
        'core',
        'utils',
    ]
    
    for file in files_to_remove:
        file_path = base_path / file
        if file_path.exists():
            file_path.unlink()
            print_success(f"Eliminado: {file}")
    
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print_success(f"Eliminado directorio: {dir_name}/")


def clean_unified_gui_only(base_path):
    """
    Limpia el template para: Lógica Unificada + Solo GUI
    Mantiene: main.py solo con GUI
    Elimina: launcher.py, ui/, core/, utils/, y código CLI de main.py
    """
    print_section("🧹 Limpiando archivos innecesarios...")
    
    # Eliminar archivos y directorios
    files_to_remove = ['launcher.py']
    dirs_to_remove = ['ui', 'core', 'utils']
    
    for file in files_to_remove:
        file_path = base_path / file
        if file_path.exists():
            file_path.unlink()
            print_success(f"Eliminado: {file}")
    
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print_success(f"Eliminado directorio: {dir_name}/")
    
    # Modificar main.py para eliminar CLI
    main_path = base_path / 'main.py'
    if main_path.exists():
        new_content = '''# Aplicación Python con interfaz gráfica (GUI)

import sys

def run_gui():
    """Ejecuta la interfaz gráfica"""
    print("Iniciando aplicación gráfica...")
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
    run_gui()

if __name__ == "__main__":
    main()
'''
        main_path.write_text(new_content)
        print_success("Modificado: main.py (eliminado código CLI)")


def clean_unified_cli_only(base_path):
    """
    Limpia el template para: Lógica Unificada + Solo CLI
    Mantiene: main.py solo con CLI
    Elimina: launcher.py, ui/, core/, utils/, y código GUI de main.py
    """
    print_section("🧹 Limpiando archivos innecesarios...")
    
    # Eliminar archivos y directorios
    files_to_remove = ['launcher.py']
    dirs_to_remove = ['ui', 'core', 'utils']
    
    for file in files_to_remove:
        file_path = base_path / file
        if file_path.exists():
            file_path.unlink()
            print_success(f"Eliminado: {file}")
    
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print_success(f"Eliminado directorio: {dir_name}/")
    
    # Modificar main.py para eliminar GUI
    main_path = base_path / 'main.py'
    if main_path.exists():
        new_content = '''# Aplicación Python con interfaz de línea de comandos (CLI)

def run_cli():
    """Ejecuta la interfaz de línea de comandos"""
    print("Iniciando aplicación CLI...")
    nombre = input("¿Cuál es tu nombre? ")
    print(f"Hola, {nombre} (desde CLI)")
    
    # Aquí va tu lógica de línea de comandos
    # Puedes añadir más funcionalidades según necesites

def main():
    run_cli()

if __name__ == "__main__":
    main()
'''
        main_path.write_text(new_content)
        print_success("Modificado: main.py (eliminado código GUI)")


def clean_separated_hybrid(base_path):
    """
    Limpia el template para: Lógica Separada + Interfaz Híbrida
    Mantiene: launcher.py, ui/, core/, utils/
    Elimina: main.py
    """
    print_section("🧹 Limpiando archivos innecesarios...")
    
    files_to_remove = ['main.py']
    
    for file in files_to_remove:
        file_path = base_path / file
        if file_path.exists():
            file_path.unlink()
            print_success(f"Eliminado: {file}")


def clean_separated_gui_only(base_path):
    """
    Limpia el template para: Lógica Separada + Solo GUI
    Mantiene: launcher.py solo con GUI, ui/gui/, core/, utils/
    Elimina: main.py, ui/cli/, y código CLI de launcher.py
    """
    print_section("🧹 Limpiando archivos innecesarios...")
    
    # Eliminar archivos y directorios
    files_to_remove = ['main.py']
    dirs_to_remove = ['ui/cli']
    
    for file in files_to_remove:
        file_path = base_path / file
        if file_path.exists():
            file_path.unlink()
            print_success(f"Eliminado: {file}")
    
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print_success(f"Eliminado directorio: {dir_name}/")
    
    # Modificar launcher.py para eliminar CLI
    launcher_path = base_path / 'launcher.py'
    if launcher_path.exists():
        new_content = '''# Aplicación Python con interfaz gráfica (GUI) y lógica modular

import sys
from ui.gui.gui_app import run_gui

def main():
    """Punto de entrada de la aplicación"""
    run_gui()

if __name__ == "__main__":
    main()
'''
        launcher_path.write_text(new_content)
        print_success("Modificado: launcher.py (eliminado código CLI)")


def clean_separated_cli_only(base_path):
    """
    Limpia el template para: Lógica Separada + Solo CLI
    Mantiene: launcher.py solo con CLI, ui/cli/, core/, utils/
    Elimina: main.py, ui/gui/, y código GUI de launcher.py
    """
    print_section("🧹 Limpiando archivos innecesarios...")
    
    # Eliminar archivos y directorios
    files_to_remove = ['main.py']
    dirs_to_remove = ['ui/gui']
    
    for file in files_to_remove:
        file_path = base_path / file
        if file_path.exists():
            file_path.unlink()
            print_success(f"Eliminado: {file}")
    
    for dir_name in dirs_to_remove:
        dir_path = base_path / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print_success(f"Eliminado directorio: {dir_name}/")
    
    # Modificar launcher.py para eliminar GUI
    launcher_path = base_path / 'launcher.py'
    if launcher_path.exists():
        new_content = '''# Aplicación Python con interfaz de línea de comandos (CLI) y lógica modular

import sys
from ui.cli.cli_app import run_cli

def main():
    """Punto de entrada de la aplicación"""
    run_cli()

if __name__ == "__main__":
    main()
'''
        launcher_path.write_text(new_content)
        print_success("Modificado: launcher.py (eliminado código GUI)")


def apply_configuration(logic_type, interface_type, base_path):
    """
    Aplica la configuración seleccionada limpiando archivos apropiados
    
    Args:
        logic_type: 'unified' o 'separated'
        interface_type: 'hybrid', 'gui_only' o 'cli_only'
        base_path: Path al directorio base del proyecto
    """
    print_header("🔧 Aplicando Configuración")
    
    # Mapeo de combinaciones a funciones de limpieza
    cleanup_functions = {
        ('unified', 'hybrid'): clean_unified_hybrid,
        ('unified', 'gui_only'): clean_unified_gui_only,
        ('unified', 'cli_only'): clean_unified_cli_only,
        ('separated', 'hybrid'): clean_separated_hybrid,
        ('separated', 'gui_only'): clean_separated_gui_only,
        ('separated', 'cli_only'): clean_separated_cli_only,
    }
    
    # Obtener la función de limpieza apropiada
    cleanup_func = cleanup_functions.get((logic_type, interface_type))
    
    if cleanup_func:
        cleanup_func(base_path)
        print_success("\n✓ Configuración aplicada exitosamente")
    else:
        print_error(f"Combinación no válida: {logic_type} + {interface_type}")
        return False
    
    return True


def show_next_steps(logic_type, interface_type):
    """Muestra los siguientes pasos después de la configuración"""
    print_header("🎉 ¡Configuración Completada!")
    
    logic_name = "Lógica Unificada (main.py)" if logic_type == "unified" else "Lógica Separada (launcher.py)"
    interface_names = {
        "hybrid": "Híbrida (CLI + GUI)",
        "gui_only": "Solo GUI",
        "cli_only": "Solo CLI"
    }
    interface_name = interface_names[interface_type]
    
    print(f"{Colors.GREEN}{Colors.BOLD}✓ Tu template ha sido configurado con:{Colors.ENDC}")
    print(f"  • {logic_name}")
    print(f"  • {interface_name}")
    
    print_section("📝 Siguientes Pasos")
    
    # Determinar el archivo principal
    main_file = "main.py" if logic_type == "unified" else "launcher.py"
    
    print(f"\n{Colors.BOLD}1. Instalar dependencias{Colors.ENDC}")
    
    if interface_type in ['hybrid', 'gui_only']:
        print(f"   {Colors.CYAN}pip install -r requirements.txt{Colors.ENDC}")
        print("   (Instala PySide6 para la interfaz gráfica)")
    else:
        print(f"   {Colors.CYAN}# No se requieren dependencias adicionales para CLI{Colors.ENDC}")
    
    print(f"\n{Colors.BOLD}2. Ejecutar tu aplicación{Colors.ENDC}")
    
    if interface_type == 'hybrid':
        print(f"   {Colors.CYAN}# Modo GUI (por defecto):{Colors.ENDC}")
        print(f"   python {main_file}")
        print(f"\n   {Colors.CYAN}# Modo CLI:{Colors.ENDC}")
        print(f"   python {main_file} --cli")
    elif interface_type == 'gui_only':
        print(f"   {Colors.CYAN}python {main_file}{Colors.ENDC}")
    else:  # cli_only
        print(f"   {Colors.CYAN}python {main_file}{Colors.ENDC}")
    
    print(f"\n{Colors.BOLD}3. Personalizar tu aplicación{Colors.ENDC}")
    
    if logic_type == 'unified':
        print(f"   • Edita {main_file} con tu lógica")
        if interface_type == 'hybrid':
            print(f"   • Modifica run_cli() para tu CLI")
            print(f"   • Modifica run_gui() para tu GUI")
        elif interface_type == 'gui_only':
            print(f"   • Modifica run_gui() para tu GUI")
        else:
            print(f"   • Modifica run_cli() para tu CLI")
    else:  # separated
        if interface_type == 'hybrid':
            print(f"   • CLI: edita ui/cli/cli_app.py")
            print(f"   • GUI: edita ui/gui/gui_app.py")
            print(f"   • Lógica compartida: core/logica.py")
        elif interface_type == 'gui_only':
            print(f"   • GUI: edita ui/gui/gui_app.py")
            print(f"   • Lógica compartida: core/logica.py")
        else:
            print(f"   • CLI: edita ui/cli/cli_app.py")
            print(f"   • Lógica compartida: core/logica.py")
    
    print(f"\n{Colors.BOLD}4. Leer la documentación{Colors.ENDC}")
    print(f"   • Consulta README.md para más información")
    
    print_section("💡 Consejos")
    
    if logic_type == 'unified':
        print("  • Mantén el código organizado aunque esté en un archivo")
        print("  • Si el proyecto crece, considera migrar a lógica separada")
    else:
        print("  • Aprovecha la modularización para mantener el código limpio")
        print("  • Añade tests en una carpeta tests/ para asegurar calidad")
    
    if interface_type == 'hybrid':
        print("  • Mantén consistencia entre CLI y GUI")
        print("  • Comparte lógica común para evitar duplicación")
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}¡Feliz desarrollo! 🚀{Colors.ENDC}\n")


def main():
    """Función principal del script de configuración"""
    try:
        # Obtener el directorio base (donde está este script)
        base_path = Path(__file__).parent.resolve()
        
        # Paso 0: Bienvenida
        show_welcome()
        
        # Paso 1: Explicar y seleccionar tipo de lógica
        explain_logic_types()
        logic_type = select_logic_type()
        
        # Paso 2: Explicar y seleccionar tipo de interfaz
        explain_interface_types()
        interface_type = select_interface_type()
        
        # Paso 3: Confirmar selección
        if not confirm_selection(logic_type, interface_type):
            print_warning("\n❌ Configuración cancelada por el usuario.")
            print("   No se realizaron cambios en el template.")
            sys.exit(0)
        
        # Paso 4: Aplicar configuración
        if apply_configuration(logic_type, interface_type, base_path):
            # Paso 5: Mostrar siguientes pasos
            show_next_steps(logic_type, interface_type)
        else:
            print_error("\n❌ Error al aplicar la configuración.")
            sys.exit(1)
        
    except KeyboardInterrupt:
        print_warning("\n\n❌ Proceso interrumpido por el usuario.")
        print("   No se completó la configuración.")
        sys.exit(1)
    except Exception as e:
        print_error(f"\n❌ Error inesperado: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
