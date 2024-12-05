# Utiliser une image de base Python
FROM python:3.9-slim

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir grpcio grpcio-tools
RUN pip install grpcio

# Copier les fichiers nécessaires dans l'image
COPY ghostbuster_api_grpc.py /app/ghostbuster_api_grpc.py
COPY ghostbuster_pb2.py /app/ghostbuster_pb2.py
COPY ghostbuster_pb2_grpc.py /app/ghostbuster_pb2_grpc.py

# Définir le répertoire de travail
WORKDIR /app

# Exposer le port gRPC (50051)
EXPOSE 50051

# Commande pour démarrer l'application
CMD ["python", "ghostbuster_api_grpc.py"]
