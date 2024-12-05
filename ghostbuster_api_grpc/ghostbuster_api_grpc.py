from concurrent import futures
import time
import grpc
import ghostbuster_pb2
import ghostbuster_pb2_grpc

# Variable pour simuler la readiness
is_ready = False

# Implémentation du service Ghostbuster
class GhostbusterService(ghostbuster_pb2_grpc.GhostbusterServicer):
    def SayHello(self, request, context):
        """
        Implémente la méthode SayHello, retourne un message de bienvenue.
        """
        if not is_ready:
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            context.set_details("Service not ready")
            return ghostbuster_pb2.HelloResponse()
        
        return ghostbuster_pb2.HelloResponse(
            message=f"Hello, {request.name}! Welcome to ghostbuster_grpc."
        )

# Fonction pour simuler readiness
def simulate_readiness(delay):
    global is_ready
    time.sleep(delay)
    is_ready = True
    print("Service is now ready!")

def serve():
    """
    Démarre le serveur gRPC.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ghostbuster_pb2_grpc.add_GhostbusterServicer_to_server(GhostbusterService(), server)

    # Le serveur écoute sur le port 50051
    server.add_insecure_port("[::]:50051")
    print("Starting server on port 50051...")
    server.start()

    # Simule un délai avant que le service soit prêt
    threading.Thread(target=simulate_readiness, args=(10,), daemon=True).start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Shutting down server...")

if __name__ == "__main__":
    import threading
    serve()
