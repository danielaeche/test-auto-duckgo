
# Test Automation - Google (Firefox version)

Este proyecto contiene una prueba automatizada básica usando **Selenium**, **pytest** y **Firefox**, diseñada para ejecutarse tanto localmente como en un pipeline CI con **GitHub Actions**.

---

## 🚀 Objetivo

Automatizar una búsqueda en un motor de búsqueda (ej: DuckDuckGo) como prueba mínima para entender cómo funciona un flujo completo de CI/CD en GitHub.

---

## 📁 Estructura del proyecto

```

test-automation-google/
├── .github/workflows/ci.yml       # Configuración del pipeline
├── tests/
│   └── test\_google.py             # Prueba automatizada con Selenium
├── requirements.txt               # Dependencias del proyecto
├── README.md                      # Este archivo
└── .gitignore                     # Archivos a excluir del repositorio

````

---

## ⚙️ Instalación local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
````

> Asegurate de tener Firefox y Geckodriver instalados en tu sistema.

---

## 🔁 CI/CD con GitHub Actions

Cada vez que se hace un **push al repositorio**, se ejecuta automáticamente el test usando Ubuntu + Python + Firefox en un runner de GitHub.

---

## 🧪 Tecnologías usadas

* Python 3
* Selenium
* pytest
* GitHub Actions

---

## 📝 Notas

Este proyecto es un punto de partida mínimo para aprender cómo integrar pruebas automatizadas con un flujo de entrega continua. Se puede extender fácilmente para testear otras aplicaciones, agregar más validaciones, o integrarse a pipelines reales.

```





