# 🐍 Template para App Híbrida en Python: CLI y GUI en el mismo proyecto

Este proyecto permite ejecutar una aplicación Python en **modo CLI** (línea de comandos) o **modo GUI** (interfaz gráfica) usando un solo punto de entrada (`main.py`) o (`launcher.py`).

(`main.py`) interface hibrida que puede ejecutarse en modo CLI o GUI con la lógica unificada en el mismo archivo.
(`launcher.py`) interface hibrida que puede ejecutarse en modo CLI o GUI con la lógica separada archivos individuales "UI".

La estructura es modular, limpia y escalable desde el inicio. Se debe definir una de las logicas.

En el caso de main.py, con la logica unificada no necesitamos la carpeta "UI" ni del launcher.py ya que el codigo es mucho mas extenso y contiene las logicas unificadas.

En el caso de launcher.py, no necesitamos de main.py pero si necesitamos la carpeta "UI" donde estará cada logica dividida.

---

## 📁 Estructura del Proyecto

---

```
template-python-hybrid/
│
├── main.py                  # Punto de entrada UNITE   (Logica CLI y GUI unificadas en el mismo archivo)
├── launcher.py              # Punto de entrada Hibrido (Logica CLI y GUI separadas en "UI")
│
├── ui/
│   ├── cli/
│   │   └── cli_app.py       # Lógica del modo CLI
│   └── gui/
│       └── gui_app.py       # Lógica del modo GUI (PySide6, Tkinter, NiceGUI, etc.)
│
├── core/
│   └── logica.py            # Lógica compartida entre CLI y GUI
│
├── utils/
│   └── helpers.py           # Utilidades (parseadores, validadores, etc.)
│
├── data/
│   └── config.json          # Datos, configuraciones, plantillas, imágenes, etc.
│
└── requirements.txt         # Dependencias (puedes agregar requirements-gui.txt, requirements-cli.txt)
```

---

## 🚀 Ejecución

Desde la raíz del proyecto (`tu_app/`), ejecuta:

### ▶️ GUI por defecto:

```bash
python main.py
o
python launcher.py
```

### 💬 Modo CLI:

```bash
python main.py --cli
o
python launcher.py --cli
```

---
