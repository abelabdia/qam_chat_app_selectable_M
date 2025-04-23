# QAM Chat App for Raspberry Pi (Selectable M-QAM)

This app allows Raspberry Pis to chat over Wi-Fi using M-QAM (4, 8, 16, 64, 256). It uses a GUI and real-time QAM modulation/demodulation.

## Setup

1. Install dependencies:
```bash
sudo apt install python3-tk
pip3 install numpy
```

2. Set the correct IP of the other Raspberry Pi in `config.py`.

3. Run the app on both Pis:
```bash
python3 chat_ui.py
```

## Features

- Tkinter chat UI
- Selectable QAM levels
- UDP communication with custom starter bit