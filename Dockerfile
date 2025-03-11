# Utilise une image Python officielle comme image de base
FROM python:3.12-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installe les dépendances Python et Gunicorn
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copie le reste du code de l'application dans le répertoire de travail
COPY . .

# Collecte les fichiers statiques
RUN python manage.py collectstatic --noinput

# Ajoute la variable d'environnement pour Django
ENV PYTHONUNBUFFERED=1
ENV DEBUG=False

# Expose le port 8000
EXPOSE 8000

# Définit la commande par défaut pour exécuter l'application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]