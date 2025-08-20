# QA Automation Template

Framework de pruebas automatizadas con **Selenium + Pytest + Allure**  
Ejemplo usando [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login).

## 🚀 Cómo ejecutar (local)
```bash
# Crear entorno
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Correr pruebas
pytest -m smoke --alluredir=allure-results

# Generar reporte Allure (si tienes allure instalado)
allure serve allure-results
```

## 🛠️ Stack
- Selenium
- Pytest
- Allure Reports
- GitHub Actions (CI)
