# syntax=docker/dockerfile:1.4
# Для минимизации размера образа будем использовать поэтапный процесс сборки,
# для того чтобы использовать только необходимые файлы библиотек/пакетов для приложения
# ПЕРВЫЙ ЭТАП, назовем его firststage
FROM python:3.13-slim AS firststage
 
# Создание и установка рабочего каталога для приложения в контейнере
WORKDIR /backend
 
# Установка переменных 
# Запрещает Python писать кэш файлы бай-кода (*.pyc) на диск
ENV PYTHONDONTWRITEBYTECODE=1
#Отключаем буферизацию вывода в stdout stderr в Python
ENV PYTHONUNBUFFERED=1 
 
# Обновление систему управления пакетами/библиотеками pip
RUN pip install --upgrade pip 

# Копируем файл со списком необходимых библиотек/пакетов Python
COPY requirements.txt .
 
# Установка необходимых библиотек/пакетов для (проекта) Python 
RUN pip install --no-cache-dir -r requirements.txt

# ВТОРОЙ ЭТАП. Создание образа с приложением
# Используем минимальный образ Python с версией 3.13
FROM python:3.13-slim

# Создание системной группы и учетной записи,
# создание каталога и установка владельца на директорию приложения
RUN addgroup --system appgroup \
    && adduser --system appuser --ingroup appgroup \
    && mkdir /backend \
    && chown -R appuser:appgroup /backend

# Копируем необходимые каталоги пакетов/библиотек Python из первого этапа сборки
COPY --from=firststage /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=firststage /usr/local/bin/ /usr/local/bin/

# Установка рабочего каталога в контейнере
WORKDIR /backend

# Копируем файлы / устанвливаем права владения
COPY --chown=appuser:appgroup /backend/ .
COPY --chown=appuser:appgroup createsu.py .

# Установка переменных 
# Запрещает Python писать кэш файлы бай-кода (*.pyc) на диск
ENV PYTHONDONTWRITEBYTECODE=1
#Отключаем буферизацию вывода в stdout stderr в Python
ENV PYTHONUNBUFFERED=1 

# Указываем пользователя для запуска приложения в контейнере
USER appuser