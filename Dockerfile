# Utilise une image Python officielle comme image de base
FROM python:3.12-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie le fichier requirements.txt dans le répertoire de travail
COPY requirements.txt .

# Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code de l'application dans le répertoire de travail
COPY . .

# Ajoute la variable d'environnement pour Django
ENV PYTHONUNBUFFERED=1

# Collecte les fichiers statiques
#RUN python manage.py collectstatic --noinput

# Définit la commande par défaut pour exécuter l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
