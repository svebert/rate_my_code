# 📦 rate-my-code

Ein witziges Toy-Package, das deinen Code (und manchmal auch deinen Kabeljau 🐟 oder … 🤢) bewertet.  
Ideal zum Lernen, wie man Python-Packages baut und veröffentlicht.  

---

## 🚀 Installation für Nutzer:innen

1. **Virtuelle Umgebung anlegen (empfohlen)**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux & Mac
   .venv\Scripts\activate      # Windows (PowerShell)
   ```

2. **Package aus dem Company Nexus installieren**  
   ```bash
   pip install --extra-index-url https://<company-nexus-url>/repository/pypi-all/simple rate-my-code
   ```
  > Hinweis: `--extra-index-url` fügt deinen internen Nexus als zusätzliche Quelle hinzu.  
  > Damit kann `pip` sowohl Pakete aus PyPI als auch aus Nexus installieren.
  
3. **Beispiele ausprobieren**  
   Im Ordner [`examples/`](examples/) findest du Demo-Skripte.  
   ```bash
   python examples/basic_demo.py
   ```

---

## 🧑‍💻 Entwicklung & Contribution

Falls du am Package mitarbeiten oder selbst erweitern möchtest:  

### 1. Installation im Editable Mode
```bash
pip install -e .[dev]
```

- `-e` = *editable mode* → Änderungen im Code sind sofort wirksam.  
- `[dev]` = installiert zusätzliche Abhängigkeiten für Entwicklung & Tests (siehe `pyproject.toml`).  

---

### 2. Tests ausführen

Alle Tests laufen lassen:
```bash
pytest -v
```

Wenn du **print-Ausgaben im Test sehen** möchtest, füge `-s` hinzu:
```bash
pytest -v -s
```

Einen einzelnen Test-File laufen lassen:
```bash
pytest tests/test_core.py -v
```

Einen spezifischen Test innerhalb einer Datei laufen lassen:
```bash
pytest tests/test_core.py::test_score_with_pythonic_comment -v
```

---

### 3. Code-Style & Checks

Optional kannst du folgende Tools nutzen, um deinen Code zu prüfen und sauber zu halten:

- **black** → formatiert deinen Code nach einem konsistenten Stil.
- **flake8** → überprüft deinen Code auf PEP8-Konformität, Einrückungen, Line-Length, ungenutzte Imports, einfache Fehler (z.B. undefinierte Variablen)
- **mypy** → prüfen von statische Typen: z.B. ob ein str an eine Funktion übergeben wird, die int erwartet, oder ob Rückgabetypen konsistent sind

#### Beispiel-Befehle:
```bash
black .
flake8 .
mypy rate_my_code
```

> ⚠️ Hinweis zu Flake8: Standardmäßig durchsucht `flake8 .` alle Unterverzeichnisse, inklusive `.venv`. Außerdem beklagt sich flake bei Zeilen die länger als 79 Zeichen sind.
> Wir nutzen die Konfigurationsdatei .flake8, um das Verhalten von flake für unser Paket anzupassen:

```ini
[flake8]
exclude = .venv
max-line-length = 88
```

### 4. Package manuell bauen

Falls du manuell ein Wheel erzeugen möchtest:

```bash
python -m build
```

Die fertigen Artefakte liegen danach im `dist/` Ordner:
- `dist/rate_my_code-0.1.0-py3-none-any.whl`
- `dist/rate_my_code-0.1.0.tar.gz`

Installation lokal:
```bash
pip install dist/rate_my_code-0.1.0-py3-none-any.whl
```

---

### 5. Publishing & CI/CD (Best Practice)

Statt das Package manuell hochzuladen, empfehlen wir die **GitHub Actions Pipeline**, um Releases automatisiert zu bauen und zu veröffentlichen.  

Es gibt zwei Pipelines:

- **CI-Pipeline (`ci.yml`)**: Läuft auf Pull Requests, prüft Codequalität und Tests.
- **Publish-Pipeline (`publish.yml`)**: Läuft bei Tags auf `main`, baut das Package und veröffentlicht es auf Nexus / PyPI / Artifactory.

---

#### 5.1 Entwicklung

1. **Neues Feature auf Feature-Branch entwickeln**
   ```bash
   git checkout -b feature/meine-neuerung
   ```
2. Branch zu Remote pushen
   ```bash
   git push -u origin feature/meine-neuerung
   ```
#### 5.1 Pull Request (PR) erstellen
Auf GitHub einen PR von `feature/meine-neuerung` → `main` erstellen.

- **CI Workflow (`ci.yml`) läuft automatisch**:
  - Code formatieren (black)
  - Linting (flake8)
  - Typprüfung (mypy)
  - Tests ausführen (pytest)

- Feedback prüfen, ggf. Änderungen einpflegen und PR mergen.

#### 5.2 Release erstellen
1. Auf main wechseln und pull
```bash
git switch main
git pull
```
2. Tag für Release erstellen
```bash
git tag -a v0.1.0 -m "Release v0.1.0"
git push -tags
```
3. Release auf GitHub erstellen
GitHub zeigt das neue Tag → Release erstellen → Changelog ggf. ergänzen.

#### 5.3 Publish Workflow
Workflow .github/workflows/publish.yml wird durch das Tag ausgelöst.

## 📁 Package-Struktur

Ein Python-Package ist ein **Verzeichnis**, das mindestens eine `__init__.py`-Datei enthält.  
Ein Package kann mehrere **Module** (Einzeldateien `.py`) und weitere Subpackages enthalten.

Beispielstruktur für `rate-my-code`:

```
rate_my_code/           # Package
├── __init__.py         # Initialisierung & zentrale Importe
├── core.py             # Modul
├── fish.py             # Modul
├── kot.py              # Modul
├── pylint.py           # Modul
tests/                  # Testcode, kein Package
├── test_core.py
├── test_fish.py
└── test_pylint.py
README.md
pyproject.toml
```

- **Module**: Einzelne `.py`-Dateien mit Funktionen, Klassen, Variablen  
- **Package**: Verzeichnis mit `__init__.py`, das Module und ggf. Subpackages zusammenfasst

---

### 1️⃣ `__init__.py`

- Wird beim Import des Packages ausgeführt.  
- Kann zentrale Funktionen der Submodule verfügbar machen:

```python
from .core import rate_my_code
from .fish import rate_my_cod
from .kot import rate_my_kot
from .pylint import run_pylint
```

So können Nutzer:innen alles direkt aus dem Package importieren:

```python
from rate_my_code import rate_my_code, run_pylint
```

---

### 2️⃣ `__all__`

```python
__all__ = ["rate_my_code", "rate_my_cod", "rate_my_kot", "run_pylint"]
```

- Legt fest, welche Symbole **öffentlich** sind.  
- Relevant für `from rate_my_code import *`.  
- Reihenfolge ist nicht wichtig, dient nur der Lesbarkeit.
