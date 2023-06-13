import zmq

class Broker:
    def __init__(self) -> None:
        self.context = zmq.Context()
        self.edge_sub_socket = self.context.socket(zmq.REP)  # XSUB socket for receiving messages from multiple publishers
        self.edge_sub_socket.bind("tcp://127.0.0.1:5560")  # Bind frontend socket to port 5559
        
        self.server_pub_socket = self.context.socket(zmq.XPUB)
        self.server_pub_socket.bind("tcp://127.0.0.1:5559")  # Bind backend socket to port 5560
    
    def poll(self):
        while True:
            print("waiting for msg")
            message = self.edge_sub_socket.recv()
            print(message)
    
if __name__ == "__main__":
    broker = Broker()
    broker.poll()