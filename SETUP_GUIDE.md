# 🎯 Guía del Configurador Interactivo (`setup.py`)

## 📖 Índice
- [¿Qué es el Configurador?](#qué-es-el-configurador)
- [¿Por qué usarlo?](#por-qué-usarlo)
- [Cómo Usarlo](#cómo-usarlo)
- [Opciones Disponibles](#opciones-disponibles)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Preguntas Frecuentes](#preguntas-frecuentes)

---

## ¿Qué es el Configurador?

El **Configurador Interactivo** (`setup.py`) es un asistente CLI que adapta el template Python Hybrid a tus necesidades específicas mediante un proceso guiado de 3 pasos.

### 🎯 Objetivos
- Simplificar la configuración inicial del template
- Eliminar código y archivos que no necesitas
- Proporcionar recomendaciones basadas en mejores prácticas
- Dejar el proyecto listo para empezar a desarrollar

---

## ¿Por qué usarlo?

### ✅ Ventajas

**1. Template Personalizado**
- Solo conservas lo que necesitas
- Código más limpio y fácil de entender
- Menos archivos que gestionar

**2. Guía Educativa**
- Explicaciones detalladas de cada opción
- Comparaciones lado a lado
- Recomendaciones de casos de uso

**3. Ahorro de Tiempo**
- Configuración en 2 minutos
- No necesitas borrar archivos manualmente
- Instrucciones claras de siguientes pasos

**4. Prevención de Errores**
- Limpieza inteligente que preserva funcionalidad
- Confirmación antes de realizar cambios
- Validación de selecciones

### ❌ ¿Cuándo NO usarlo?

- Si quieres explorar todo el template completo
- Si planeas cambiar de enfoque más adelante
- Si estás aprendiendo y quieres ver todas las opciones

---

## Cómo Usarlo

### Paso 1: Ejecutar el Script

```bash
cd template-python-hybrid
python setup.py
```

### Paso 2: Seguir el Asistente

El script te guiará a través de 3 decisiones:

1. **Tipo de Lógica** (Unificada o Separada)
2. **Tipo de Interfaz** (Híbrida, Solo GUI, o Solo CLI)
3. **Confirmación** (Revisar y confirmar cambios)

### Paso 3: Desarrollo

Una vez completado:
- Los archivos innecesarios habrán sido eliminados
- El código estará adaptado a tu elección
- Tendrás instrucciones claras de los siguientes pasos

---

## Opciones Disponibles

### 📚 Tipo de Lógica

#### 1️⃣ Lógica Unificada (`main.py`)

```
📄 Estructura Final:
template-python-hybrid/
├── main.py         ← Todo el código aquí
├── data/
└── README.md
```

**Características:**
- Un solo archivo con toda la lógica
- CLI y GUI en el mismo archivo
- Perfecto para prototipos

**Ideal para:**
- ✅ Prototipos rápidos
- ✅ Proyectos < 500 líneas
- ✅ Scripts personales
- ✅ Aprendizaje

**Ejemplo de código resultante:**
```python
# main.py
import argparse
import sys

def run_cli():
    # Tu lógica CLI aquí
    pass

def run_gui():
    # Tu lógica GUI aquí
    pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cli", action="store_true")
    args = parser.parse_args()
    
    if args.cli:
        run_cli()
    else:
        run_gui()
```

#### 2️⃣ Lógica Separada (`launcher.py`)

```
📦 Estructura Final:
template-python-hybrid/
├── launcher.py     ← Punto de entrada
├── ui/
│   ├── cli/
│   │   └── cli_app.py
│   └── gui/
│       └── gui_app.py
├── core/
│   └── logica.py
├── utils/
│   └── helpers.py
├── data/
└── README.md
```

**Características:**
- Código modularizado
- Separación clara de responsabilidades
- Fácil de testear y escalar

**Ideal para:**
- ✅ Proyectos profesionales
- ✅ Trabajo en equipo
- ✅ Aplicaciones de producción
- ✅ Proyectos a largo plazo

**Ejemplo de código resultante:**
```python
# launcher.py
import argparse
from ui.cli.cli_app import run_cli
from ui.gui.gui_app import run_gui

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cli", action="store_true")
    args = parser.parse_args()
    
    if args.cli:
        run_cli()
    else:
        run_gui()
```

---

### 🎨 Tipo de Interfaz

#### 1️⃣ Híbrida (CLI + GUI)

**Mantiene:**
- Código CLI completo
- Código GUI completo
- Argparse para selección de modo

**Ejecución:**
```bash
python main.py           # Abre GUI
python main.py --cli     # Usa CLI
```

**Ideal para:**
- ✅ Herramientas de desarrollo
- ✅ Aplicaciones de datos
- ✅ Utilidades del sistema
- ✅ Máxima flexibilidad

---

#### 2️⃣ Solo GUI

**Mantiene:**
- Solo código GUI
- Sin argparse
- Sin código CLI

**Elimina:**
- Todo el código CLI
- Carpeta `ui/cli/` (si es lógica separada)

**Ejecución:**
```bash
python main.py           # Abre GUI directamente
```

**Ideal para:**
- ✅ Apps de escritorio
- ✅ Usuarios no técnicos
- ✅ Interfaces visuales
- ✅ Herramientas multimedia

---

#### 3️⃣ Solo CLI

**Mantiene:**
- Solo código CLI
- Sin dependencias de GUI

**Elimina:**
- Todo el código GUI
- Carpeta `ui/gui/` (si es lógica separada)
- Dependencia de PySide6

**Ejecución:**
```bash
python main.py           # Ejecuta CLI directamente
```

**Ideal para:**
- ✅ Scripts de automatización
- ✅ Herramientas de servidor
- ✅ Procesamiento batch
- ✅ CI/CD

---

## Ejemplos de Uso

### Ejemplo 1: Prototipo con CLI y GUI

**Escenario:** Estás creando un prototipo que necesita CLI para pruebas y GUI para demos.

**Selección:**
1. **Lógica:** Unificada (1)
2. **Interfaz:** Híbrida (1)

**Resultado:**
- Un solo archivo `main.py`
- Soporta `--cli` flag
- Rápido de desarrollar

```bash
$ python setup.py
[Seleccionar 1, 1, s]

$ python main.py         # GUI
$ python main.py --cli   # CLI
```

---

### Ejemplo 2: Aplicación Empresarial GUI

**Escenario:** Desarrollando una app de escritorio para el equipo de ventas.

**Selección:**
1. **Lógica:** Separada (2)
2. **Interfaz:** Solo GUI (2)

**Resultado:**
- Código modular en `launcher.py`
- Solo interfaz gráfica
- Fácil de mantener por equipo

```bash
$ python setup.py
[Seleccionar 2, 2, s]

$ python launcher.py     # Abre GUI
```

---

### Ejemplo 3: Herramienta CLI para DevOps

**Escenario:** Script de automatización para CI/CD.

**Selección:**
1. **Lógica:** Unificada (1)
2. **Interfaz:** Solo CLI (3)

**Resultado:**
- Archivo simple `main.py`
- Sin dependencias de GUI
- Ultraligero

```bash
$ python setup.py
[Seleccionar 1, 3, s]

$ python main.py         # Ejecuta CLI
```

---

### Ejemplo 4: Proyecto Profesional Multi-Interfaz

**Escenario:** Aplicación empresarial que necesita CLI para administradores y GUI para usuarios.

**Selección:**
1. **Lógica:** Separada (2)
2. **Interfaz:** Híbrida (1)

**Resultado:**
- Arquitectura modular completa
- CLI y GUI separadas
- Lógica compartida en `core/`

```bash
$ python setup.py
[Seleccionar 2, 1, s]

$ python launcher.py         # GUI para usuarios
$ python launcher.py --cli   # CLI para admins
```

---

## Matriz de Decisión

Usa esta tabla para decidir qué configuración elegir:

| Tu Situación | Lógica | Interfaz | Razón |
|--------------|--------|----------|-------|
| "Quiero un prototipo rápido" | Unificada | Híbrida | Velocidad + flexibilidad |
| "App de escritorio simple" | Unificada | Solo GUI | Simple y directo |
| "Script de automatización" | Unificada | Solo CLI | Ligero y rápido |
| "Proyecto de equipo" | Separada | Híbrida | Organización + flexibilidad |
| "App empresarial GUI" | Separada | Solo GUI | Profesional y mantenible |
| "Herramienta de servidor" | Separada | Solo CLI | Escalable sin GUI |

---

## Preguntas Frecuentes

### ❓ ¿Puedo revertir los cambios?

No fácilmente. El script elimina archivos permanentemente. 

**Recomendación:** Haz una copia de seguridad antes de ejecutar o clona el repositorio nuevamente si necesitas empezar de cero.

---

### ❓ ¿Qué pasa si elijo mal?

Puedes volver a clonar el template y ejecutar `setup.py` nuevamente con la configuración correcta.

---

### ❓ ¿Puedo usar el template sin ejecutar setup.py?

Sí, absolutamente. El template funciona completamente sin configurar. El script solo optimiza para tu caso de uso específico.

---

### ❓ ¿Se pueden añadir más opciones después?

Depende:
- **De Unificada a Separada:** Requiere refactorización manual
- **De CLI a GUI o viceversa:** Requiere añadir código manualmente
- **De GUI/CLI a Híbrida:** Más fácil, puedes añadir la otra interfaz

**Consejo:** Si no estás seguro, elige Lógica Separada + Híbrida para máxima flexibilidad.

---

### ❓ ¿El script modifica mi código existente?

No. El script solo trabaja con los archivos del template. Si has hecho cambios antes de ejecutarlo, podrías perder esos cambios.

**Recomendación:** Ejecuta `setup.py` inmediatamente después de clonar el template, antes de hacer cualquier modificación.

---

### ❓ ¿Qué archivos se conservan siempre?

Independientemente de tu selección:
- ✅ `README.md`
- ✅ `LICENSE`
- ✅ `data/` (carpeta de configuración)
- ✅ `.gitignore`

---

### ❓ ¿El script requiere conexión a internet?

No. Todo se ejecuta localmente.

---

### ❓ ¿Funciona en Windows/Mac/Linux?

Sí, el script es completamente multiplataforma y funciona en:
- ✅ Windows
- ✅ macOS
- ✅ Linux

---

## 🎓 Consejos Finales

### Para Principiantes
1. Ejecuta el script inmediatamente después de clonar
2. Elige **Lógica Unificada** + **Híbrida** para experimentar
3. Lee las explicaciones detenidamente

### Para Profesionales
1. Elige **Lógica Separada** para proyectos serios
2. Considera tus necesidades de despliegue (GUI/CLI)
3. Piensa en el largo plazo al elegir

### Para Equipos
1. Discute la configuración antes de ejecutar
2. Usa **Lógica Separada** para mejor colaboración
3. Documenta la decisión en el README del proyecto

---

## 📞 Soporte

Si tienes problemas con el configurador:

1. **Revisa esta guía** para casos de uso similares
2. **Lee el README principal** para más contexto
3. **Abre un issue** en GitHub con detalles del problema

---

**¡Feliz configuración! 🚀**
