# Utiliser une image de base Python
FROM python:3.9-slim

# Copier le code source dans l'image
COPY ghostbuster_service_tcp.py /app/ghostbuster_service_tcp.py

# Définir le répertoire de travail
WORKDIR /app

# Exposer le port TCP principal (configurable dans le script)
EXPOSE 9999

# Commande pour démarrer l'application
CMD ["python", "ghostbuster_service_tcp.py"]
