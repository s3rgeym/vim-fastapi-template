# Проект FastAPI с Vim и Vimspector

## Требования

- Python 3.11+
- FastAPI
- Uvicorn
- Vim с плагином Vimspector

## Установка

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/s3rgeym/vim-fastapi-template
   cd vim-fastapi-template
   ```
1. **Создайте виртуальное окружение**:

   ```bash
   python -m venv .venv
   . .venv/bin/activate
   ```

1. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

1. **Установите плагины Vim**:

   Если вы используете `vim-plug`, добавьте следующие строки в ваш `.vimrc` или `init.vim`:

   ```vim
   Plug 'puremourning/vimspector'
   ```

   Затем выполните команду для установки плагинов:

   ```vim
   :PlugInstall
   ```

## Использование отладчика Vimspector

1. **Установите брейкпоинт**:

   В режиме редактирования (insert mode) нажмите `<F9>`, чтобы установить брейкпоинт.

1. **Запустите отладчик**:

   Нажмите `<F5>`, чтобы запустить отладчик.

1. **Проверьте вывод отладчика**:

   В браузере откройте [http://localhost:8000/hello/gay](http://localhost:8000/hello/gay). Отладчик остановится на брейкпоинте, и вы сможете проверить значения переменных и выполнить другие действия отладки.

## Структура проекта

```
.
├── main.py
├── requirements.txt
└── .vimspector.json
```

- **`main.py`**: Основной файл приложения FastAPI.
- **`requirements.txt`**: Файл с зависимостями проекта.
- **`.vimspector.json`**: Конфигурационный файл для Vimspector.
