import numpy as np

RECEIVER_IP = "192.168.11.156"  # Replace with the IP of the other Raspberry Pi
PORT = 5005
STARTER_BIT = np.array([1, 0, 1, 0, 1, 0, 1, 0], dtype=np.uint8)