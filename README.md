# 📦 CTkPlus

[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)

🇺🇸 [Read in English](#english) | 🇷🇺 [Читать на русском](#русский)

---

## English

**CTkPlus** is a library for CustomTkinter that adds new useful widgets and UI elements, so you don't have to create them manually from scratch.

> ⚠️ **Project is under development:** It is currently in beta testing, so bugs may occur.

### ✨ Features
- **🧩 New components** — adds UI elements that are missing in the standard toolkit.
- **🛠️ Native style** — the look of the elements completely matches standard CustomTkinter widgets.
- **⚡ Simple setup** — the library easily connects to the project and works without complex workarounds.

### 📥 Installation
Install the library via terminal:
```bash
pip install ctkplus
```

### 🚀 Usage
Short working code to launch a window with a spinbox:
```python
import customtkinter as ctk
import ctkplus as ctp

app = ctk.CTk()
app.geometry("400x300")
app.title("CTkPlus Test")

# Create and place a spinbox
spinbox = ctp.CTkSpinBox(master=app, start_value=0, min_value=0, max_value=100)
spinbox.pack(pady=50, padx=50)

app.mainloop()
```

### 📄 License
This project is licensed under the **MIT** License. You are free to use and modify this code.

---

## Русский

**CTkPlus** — это библиотека для CustomTkinter, которая добавляет новые полезные виджеты и элементы управления, чтобы не создавать их вручную с нуля.

> ⚠️ **Проект находится в разработке:** Сейчас идет этап бета-тестирования, поэтому могут встречаться баги.

### ✨ Возможности (Features)
- **🧩 Новые компоненты** — добавляет элементы интерфейса, которых изначально нет в стандартном наборе.
- **🛠️ Нативный стиль** — внешний вид элементов полностью совпадает со стандартными виджетами CustomTkinter.
- **⚡ Простая настройка** — библиотека легко подключается к проекту и работает без сложных костылей.

### 📥 Установка (Installation)
Установите библиотеку через терминал:
```bash
pip install ctkplus
```

### 🚀 Пример использования (Usage)
Короткий рабочий код, как запустить окно со спинбоксом:
```python
import customtkinter as ctk
import ctkplus as ctp

app = ctk.CTk()
app.geometry("400x300")
app.title("CTkPlus Тест")

# Создаем и размещаем спинбокс
spinbox = ctp.CTkSpinBox(master=app, start_value=0, min_value=0, max_value=100)
spinbox.pack(pady=50, padx=50)

app.mainloop()
```

### 📄 Лицензия (License)
Проект распространяется под открытой лицензией **MIT**. Вы можете свободно использовать и менять этот код.
