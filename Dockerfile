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

# Définit la commande par défaut pour exécuter l'application
CMD ["python", "app.py"]
