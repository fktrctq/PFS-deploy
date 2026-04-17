# Django + PostgreSQL + Nginx + Let's Encrypt Dockerized Project с Ansible

Этот проект — готовый к развёртыванию стек Django, PostgreSQL и Nginx с поддержкой SSL и автоматизацией через Ansible.

## Структура проекта

```plaintext
ansible/
  ├── playbook.yml                      # Главный Ansible playbook
  ├── inventory/
  │   └── inventory.yml                 # Инвентори для окружений
  ├── group_vars/
  │   ├── prod.yml                      # Переменные для продакшена
  │   └── dev.yml                       # Переменные для dev окружения
  ├── roles/
  │   ├── ssl_for_nginx/
  │   │   └── tasks/
  │   │       ├── self_signed_ssl.yml
  │   │       ├── letsencrypt_ssl.yml
  │   │       └── check_ssl_validity.yml
  │   ├── firewall/
  │   │   └── tasks/
  │   │       └── enabled_firewall.yml
  │   ├── docker_install/
  │   │   └── tasks/
  │   │       ├── install_docker.yml
  │   │       └── check_versions.yml
  │   └── deploy_project/
  │       └── tasks/
  │           └── main.yml
  └── templates/
      ├── docker-compose.yml.j2        # Jinja2 шаблон docker-compose
      └── nginx.conf.j2                # Jinja2 шаблон конфигурации Nginx

docker/
  ├── django/
  │   ├── Dockerfile                   # Многоступенчатый Dockerfile для Django
  │   ├── createsu.py                  # Скрипт создания суперпользователя Django
  │   └── backend/                     # Код Django проекта
  └── nginx/
      └── Dockerfile                   # Dockerfile для Nginx образа
```
---
## Требования

- Docker >= 20.10  
- Docker Compose >= 1.29  
- Ansible >= 2.9  
- Доменное имя. 

---
## Быстрый старт
### Клонируйте репозиторий:
```bash
git clone https://github.com/fktrctq/PFS-deploy.git
cd PFS-deploy
```

### Настройте инвентори и переменные окружения
- ansible/inventory/inventory.yml
- ansible/group_vars/{prod.yml, dev.yml}

### Запустите playbook Ansible для установки Docker, настройки фаервола, SSL и деплоя проекта:
```bash
ansible-playbook -i ansible/inventory/inventory.yml ansible/playbook.yml
```

### Роли Ansible
- docker_install — установка и проверка версии Docker и Docker Compose
- firewall — настройка и включение брандмауэра
- ssl_for_nginx — генерация и обновление SSL сертификатов (Let's Encrypt или self-signed)
- deploy_project — деплой Docker Compose проекта с Django, PostgreSQL и Nginx

### Ключевые особенности
- Автоматический запуск миграций Django и создание суперпользователя
- Настройка Nginx с SSL (Let's Encrypt или self-signed)
- Многоступенчатая сборка Docker образов для уменьшения размера
- Healthchecks для всех сервисов
- Логирование с ротацией
- Гибкая конфигурация через Ansible переменные и шаблоны
