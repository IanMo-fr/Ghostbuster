from flask import Flask, jsonify
import threading
import time

app = Flask(__name__)

# Variables globales pour gérer les états des probes
is_ready = False
is_alive = True

# Simule un délai avant que le service soit prêt
def simulate_readiness():
    global is_ready
    time.sleep(10)  # Simule un délai de 10 secondes
    is_ready = True

# Simule un délai avant que le service devienne vivant
def simulate_liveness():
    global is_alive
    time.sleep(35)  # Simule un délai de 35 secondes
    is_alive = True

# Démarre les threads pour simuler readiness et liveness
threading.Thread(target=simulate_readiness, daemon=True).start()
threading.Thread(target=simulate_liveness, daemon=True).start()

# Endpoint pour readinessProbe
@app.route("/health/ready", methods=["GET"])
def readiness_probe():
    """
    Readiness probe: retourne un statut 200 si le service est prêt,
    sinon retourne un statut 503 (Service Unavailable).
    """
    if is_ready:
        return jsonify({"status": "ready"}), 200
    else:
        return jsonify({"status": "not ready"}), 503

# Endpoint pour livenessProbe
@app.route("/health/live", methods=["GET"])
def liveness_probe():
    """
    Liveness probe: retourne un statut 200 si le service est vivant,
    sinon retourne un statut 500 (Internal Server Error).
    """
    if is_alive:
        return jsonify({"status": "alive"}), 200
    else:
        return jsonify({"status": "not alive"}), 500

# Endpoint principal pour tester le fonctionnement général
@app.route("/", methods=["GET"])
def home():
    """
    Endpoint principal pour vérifier que le service répond aux requêtes HTTP.
    """
    return jsonify({"message": "Welcome to ghostbuster_http!"}), 200

if __name__ == "__main__":
    # Démarrage du serveur Flask
    # Le service écoute sur le port 8080 (standard pour les probes Kubernetes)
    app.run(host="0.0.0.0", port=8081)
