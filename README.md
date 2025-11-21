# 🐍 Python Hybrid Template

> Template profesional para crear aplicaciones Python con **interfaz dual CLI/GUI** desde un único código base.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PySide6](https://img.shields.io/badge/GUI-PySide6-green.svg)](https://pypi.org/project/PySide6/)

---

## 🎯 ¿Qué es esto?

Un **template arquitectónico** que te permite crear aplicaciones Python que funcionan en:

- 🖥️ **CLI** (Command Line Interface) - Interfaz de línea de comandos
- 🎨 **GUI** (Graphical User Interface) - Interfaz gráfica

**Desde el mismo código base**, seleccionando el modo en tiempo de ejecución.

---

## ✨ Características Principales

✅ **Dual Mode**: CLI y GUI en una sola aplicación  
✅ **Arquitectura Modular**: Código organizado y escalable  
✅ **Dos Enfoques**: Simple (main.py) o Profesional (launcher.py)  
✅ **Lógica Compartida**: DRY entre interfaces  
✅ **Multiplataforma**: Windows, macOS, Linux  
✅ **Flexible**: Elige tu framework GUI favorito  

---

## 🚀 Inicio Rápido

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/Party-Templates/template-python-hybrid.git
cd template-python-hybrid

# Instalar dependencias
pip install -r requirements.txt
```

### Uso

```bash
# Ejecutar en modo GUI (por defecto)
python main.py
# o
python launcher.py

# Ejecutar en modo CLI
python main.py --cli
# o
python launcher.py --cli
```

---

## 🏗️ Arquitectura

### Estructura del Proyecto

```
template-python-hybrid/
│
├── main.py              # Enfoque 1: Lógica unificada (simple)
├── launcher.py          # Enfoque 2: Lógica modular (profesional)
│
├── ui/                  # Módulos de interfaz (solo con launcher.py)
│   ├── cli/
│   │   └── cli_app.py  # Implementación CLI
│   └── gui/
│       └── gui_app.py  # Implementación GUI
│
├── core/
│   └── logica.py       # Lógica de negocio compartida
│
├── utils/
│   └── helpers.py      # Funciones auxiliares
│
├── data/
│   └── config.json     # Configuraciones
│
└── requirements.txt    # Dependencias
```

---

## 🎨 Dos Enfoques de Desarrollo

### 📄 ENFOQUE 1: `main.py` - Lógica Unificada

**Filosofía**: Todo el código en un solo archivo

**Ideal para**:
- ✅ Prototipos rápidos
- ✅ Proyectos pequeños (< 500 líneas)
- ✅ Aprendizaje del concepto
- ✅ Scripts personales

**Ventajas**:
- 🚀 Arranque ultra-rápido
- 📖 Fácil de entender
- 🎯 Todo en un lugar

**Limitaciones**:
- ❌ Difícil de escalar
- ❌ Testing complicado
- ❌ Mantenimiento limitado

### 📦 ENFOQUE 2: `launcher.py` - Lógica Modularizada

**Filosofía**: Código organizado en módulos separados

**Ideal para**:
- ✅ Proyectos profesionales
- ✅ Aplicaciones de producción
- ✅ Trabajo en equipo
- ✅ Proyectos a largo plazo

**Ventajas**:
- 📁 Código organizado
- 🧪 Fácil de testear
- 📈 Altamente escalable
- 👥 Colaboración eficiente

**Estructura**:
- Usa carpeta `ui/` con módulos separados
- Lógica CLI en `ui/cli/cli_app.py`
- Lógica GUI en `ui/gui/gui_app.py`

---

## 📊 Comparación de Enfoques

| Característica | main.py | launcher.py |
|----------------|---------|-------------|
| **Archivos** | 1 | 3+ |
| **Complejidad inicial** | Baja | Media |
| **Escalabilidad** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Mantenibilidad** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Testing** | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Tiempo de setup** | 5 min | 15 min |
| **Proyectos ideales** | Prototipos | Producción |

---

## 🎓 Conceptos Clave

### Sistema Híbrido CLI/GUI

El template permite ejecutar la **misma aplicación** de dos formas:

1. **Sin argumentos** → Inicia GUI (ventana gráfica)
2. **Con `--cli`** → Inicia CLI (terminal)

### Separación de Responsabilidades

| Módulo | Responsabilidad |
|--------|----------------|
| `main.py` / `launcher.py` | Punto de entrada y enrutamiento |
| `ui/cli/` | Lógica de interfaz CLI |
| `ui/gui/` | Lógica de interfaz GUI |
| `core/` | Lógica de negocio compartida |
| `utils/` | Funciones auxiliares |
| `data/` | Configuraciones y datos |

### Flujo de Ejecución

```
Usuario ejecuta script
        ↓
argparse analiza argumentos
        ↓
¿Tiene flag --cli?
    ↓           ↓
   SÍ          NO
    ↓           ↓
run_cli()   run_gui()
    ↓           ↓
Terminal    Ventana
```

---

## 🔧 Stack Tecnológico

### Core
- **Python 3.8+**: Lenguaje base
- **argparse**: Parseo de argumentos CLI (incluido en Python)

### GUI (Opcional - Elige uno)
- **PySide6** (Recomendado): Qt para Python, profesional y multiplataforma
- **Tkinter**: Incluido en Python, simple y funcional
- **NiceGUI**: Moderno, basado en web
- **Kivy**: Para aplicaciones móviles y táctiles

### Estructura
- **Módulos Python**: Organización del código
- **JSON**: Configuración y datos

---

## 📚 Casos de Uso

### 1. Herramientas de Desarrollo
```bash
# CLI: Automatización
python app.py --cli --process data.csv

# GUI: Uso interactivo
python app.py
```

### 2. Aplicaciones de Datos
```bash
# CLI: Procesamiento batch
python app.py --cli --export-report

# GUI: Visualización
python app.py
```

### 3. Utilidades del Sistema
```bash
# CLI: Administración remota
python app.py --cli --backup

# GUI: Panel de control
python app.py
```

---

## 🎯 Guía de Selección

### ¿Cuándo usar `main.py`?

✅ **Úsalo si:**
- Estás prototipando
- Proyecto < 500 líneas
- Solo tú trabajas en él
- Necesitas velocidad de desarrollo
- Es temporal o personal

### ¿Cuándo usar `launcher.py`?

✅ **Úsalo si:**
- Proyecto profesional
- Trabajo en equipo
- Necesitas tests
- Aplicación de producción
- Mantenimiento a largo plazo

---

## 📖 Principios de Diseño

### 1. DRY (Don't Repeat Yourself)
- Lógica compartida en `core/`
- UI solo maneja presentación
- Sin duplicación entre CLI y GUI

### 2. Separación de Responsabilidades
- **UI**: Presentación y entrada
- **Core**: Lógica de negocio
- **Utils**: Funciones auxiliares
- **Data**: Configuración

### 3. Flexibilidad
- Mismo ejecutable, múltiples modos
- Configuración externa
- Sin hardcoding

### 4. Escalabilidad Progresiva
- Empezar simple
- Migrar cuando crezca
- Estructura preparada

---

## 🔗 Comandos Útiles

### Ejecución
```bash
# GUI por defecto
python main.py
python launcher.py

# Modo CLI
python main.py --cli
python launcher.py --cli
```

### Instalación
```bash
# Dependencias base
pip install -r requirements.txt

# PySide6 para GUI
pip install PySide6

# Otras alternativas GUI
pip install tkinter  # Ya incluido en Python
pip install nicegui
pip install kivy
```

### Desarrollo
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Activar entorno (Linux/Mac)
source venv/bin/activate
```

---

## 📦 Dependencias

### requirements.txt
```
PySide6>=6.0.0    # Framework GUI (opcional)
```

**Nota**: Puedes usar otros frameworks GUI modificando `ui/gui/gui_app.py`

---

## 🚦 Migración entre Enfoques

### De main.py a launcher.py

Cuando tu proyecto crece y necesitas modularizar:

1. **Crear estructura de carpetas**
   ```
   mkdir -p ui/cli ui/gui core utils data
   ```

2. **Extraer lógica CLI**
   - Mover función `run_cli()` → `ui/cli/cli_app.py`

3. **Extraer lógica GUI**
   - Mover función `run_gui()` → `ui/gui/gui_app.py`

4. **Extraer lógica compartida**
   - Mover funciones comunes → `core/logica.py`

5. **Usar launcher.py**
   - Cambiar imports y ejecutar desde `launcher.py`

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el template:

1. Fork el proyecto
2. Crea una rama feature (`git checkout -b feature/mejora`)
3. Commit tus cambios (`git commit -m 'Añadir mejora'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - mira el archivo [LICENSE](LICENSE) para más detalles.

---

## 🎓 Recursos Adicionales

### Documentación Oficial
- [Python argparse](https://docs.python.org/3/library/argparse.html)
- [PySide6](https://doc.qt.io/qtforpython-6/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)

### Tutoriales Recomendados
- Conceptos básicos de CLI en Python
- Introducción a PySide6/PyQt
- Arquitectura modular en Python

---

## 💡 Filosofía del Template

> **"Un código base, múltiples interfaces, arquitectura flexible"**

Este template promueve:
- ✅ Flexibilidad sin complejidad
- ✅ Escalabilidad desde el inicio
- ✅ Separación clara de responsabilidades
- ✅ Código mantenible y testeable
- ✅ Adaptabilidad a diferentes contextos

---

## 📞 Soporte

¿Preguntas o problemas?

- 🐛 [Reportar un bug](https://github.com/Party-Templates/template-python-hybrid/issues)
- 💡 [Solicitar una feature](https://github.com/Party-Templates/template-python-hybrid/issues)
- 📧 Contacto: [GitHub](https://github.com/Party-Templates)

---

## 🌟 Agradecimientos

Gracias a la comunidad de Python por las herramientas y frameworks que hacen posible este template.

---

## 📊 Estado del Proyecto

- ✅ Arquitectura base implementada
- ✅ Dos enfoques de desarrollo
- ✅ Documentación completa
- 🔄 En desarrollo activo
- 🎯 Buscando contribuidores

---

**Hecho con ❤️ por [Party-Templates](https://github.com/Party-Templates)**

*¿Te gusta este template? Dale una ⭐ en GitHub!*
