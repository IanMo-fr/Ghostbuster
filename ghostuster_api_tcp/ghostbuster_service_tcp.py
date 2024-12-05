import socket
import threading
import time

# Configuration des sockets
SOCKETS = {
    "ready_asap": {"port": 5000, "delay": 0},  # Prêt immédiatement
    "ready_after_10s": {"port": 5001, "delay": 10},  # Prêt après 10 secondes
    "ready_after_25s": {"port": 5002, "delay": 25},  # Prêt après 25 secondes
    "live_after_35s": {"port": 5003, "delay": 35},  # Crée mais prêt après 35 secondes
    "not_ready_until_20s": {"port": 5004, "delay": 20, "no_listen": True},  # Crée mais n'écoute pas
}

# Fonction pour créer un socket TCP
def start_socket(port, delay, no_listen=False):
    """
    Crée un socket TCP qui commence à écouter après un délai spécifié.
    
    :param port: Port sur lequel le socket écoutera.
    :param delay: Temps d'attente avant que le socket commence à écouter.
    :param no_listen: Si True, le socket est créé mais n'écoute pas (simulate readiness fail).
    """
    time.sleep(delay)  # Délai avant de démarrer le socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("0.0.0.0", port))
        if not no_listen:
            server_socket.listen(1)
            print(f"Socket listening on port {port} after {delay} seconds.")
            while True:
                try:
                    conn, addr = server_socket.accept()  # Accepte les connexions
                    print(f"Connection received on port {port} from {addr}.")
                    conn.close()  # Ferme immédiatement la connexion pour la simulation
                except Exception as e:
                    print(f"Error on port {port}: {e}")
        else:
            print(f"Socket created but not listening on port {port} after {delay} seconds.")
            while True:
                time.sleep(1)  # Maintient le socket actif sans écouter

# Crée des threads pour chaque socket configuré
for name, config in SOCKETS.items():
    threading.Thread(
        target=start_socket,
        args=(config["port"], config["delay"], config.get("no_listen", False)),
        daemon=True,
    ).start()

# Maintient le processus principal actif
print("ghostbuster_tcp service is running. Check the configured ports.")
while True:
    time.sleep(1)
