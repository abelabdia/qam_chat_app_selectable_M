import socket
import threading
import numpy as np
from qam_utils import string_to_bits, qam_modulate, qam_demodulate, bits_to_string
from config import RECEIVER_IP, PORT, STARTER_BIT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', PORT))

def send_message(msg, M):
    bits = string_to_bits(msg)
    full_bits = np.concatenate((STARTER_BIT, bits))
    symbols = qam_modulate(full_bits, M)

    for i in range(0, len(symbols), 100):
        chunk = symbols[i:i+100].astype(np.complex64).tobytes()
        sock.sendto(chunk, (RECEIVER_IP, PORT))

def receive(chat_window, qam_option):
    buffer = bytearray()

    while True:
        data, _ = sock.recvfrom(2048)
        buffer.extend(data)
        symbols = np.frombuffer(buffer, dtype=np.complex64)
        M = int(qam_option.get())

        bits = qam_demodulate(symbols, M)
        for i in range(len(bits) - len(STARTER_BIT)):
            if np.array_equal(bits[i:i+len(STARTER_BIT)], STARTER_BIT):
                msg_bits = bits[i+len(STARTER_BIT):]
                try:
                    msg = bits_to_string(msg_bits)
                    chat_window.insert('end', "Friend: " + msg + "\n")
                    buffer.clear()
                    break
                except:
                    continue

def start_receiver_thread(chat_window, qam_option):
    thread = threading.Thread(target=receive, args=(chat_window, qam_option), daemon=True)
    thread.start()