#!/bin/bash
set -e

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Coletando arquivos estáticos..."

echo "Aplicando migrações..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py collectstatic --noinput