# Utiliser une image de base Python
FROM python:3.9-slim

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir flask

# Copier le code source dans l'image
COPY ghostbuster_service_http.py /app/ghostbuster_service_http.py

# Définir le répertoire de travail
WORKDIR /app

# Exposer le port HTTP (8081)
EXPOSE 8081

# Commande pour démarrer l'application
CMD ["python", "ghostbuster_service_http.py"]
