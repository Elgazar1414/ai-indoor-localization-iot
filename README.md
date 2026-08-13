<p align="center">
  <img src="./assets/readme/hero_animation.gif" alt="AI-Based Indoor Localization and Tracking for IoT Networks" width="100%">
</p>

<h1 align="center">AI-Based Indoor Localization and Tracking for IoT Networks</h1>

<p align="center">
  <b>Hybrid IoT Localization • Embedded Systems • Wireless Signal Processing</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/MicroPython-ESP32-black" alt="MicroPython">
  <img src="https://img.shields.io/badge/ESP32-IoT-red?logo=espressif" alt="ESP32">
  <img src="https://img.shields.io/badge/Raspberry%20Pi-Localization-C51A4A?logo=raspberrypi&logoColor=white" alt="Raspberry Pi">
  <img src="https://img.shields.io/badge/MQTT-Communication-purple" alt="MQTT">
  <img src="https://img.shields.io/badge/Wi--Fi-RSSI-blue" alt="Wi-Fi RSSI">
  <img src="https://img.shields.io/badge/Bluetooth-BLE-0082FC?logo=bluetooth&logoColor=white" alt="Bluetooth BLE">
  <img src="https://img.shields.io/badge/Status-Prototype-orange" alt="Prototype">
</p>

<p align="center">
  Experimental hybrid IoT localization platform combining ESP32 sensing, Raspberry Pi processing,
  wireless RSSI measurements, MQTT communication, and trilateration-based position estimation.
</p>

---

## System Overview

<p align="center">
  <img src="./assets/readme/esp32_acquisition.gif" alt="ESP32 Data Acquisition" width="100%">
</p>

<p align="center">
  The ESP32 collects Wi-Fi RSSI, BLE RSSI, MPU6050 IMU data, temperature, and hall-sensor readings,
  then publishes the payload through MQTT.
</p>

---

## Localization Pipeline

<p align="center">
  <img src="./assets/readme/raspberry_pi_localization.gif" alt="Raspberry Pi Localization Pipeline" width="100%">
</p>

<p align="center">
  The Raspberry Pi / Linux application combines GPS, Wi-Fi, Bluetooth, and experimental LoRa data,
  then estimates position using trilateration and SciPy numerical optimization.
</p>

---

## Technology Stack

<p align="center">
  <img src="./assets/readme/tech_stack.gif" alt="Technology Stack" width="100%">
</p>

### Core Technologies

- **Python** — localization, processing, and visualization
- **MicroPython** — ESP32 firmware
- **ESP32** — wireless and sensor data acquisition
- **Raspberry Pi / Linux** — localization-side processing
- **MQTT** — IoT messaging
- **Wi-Fi & BLE RSSI** — wireless signal measurements
- **GPS** — reference location input
- **SciPy** — numerical optimization for trilateration
- **NumPy** — numerical operations
- **Matplotlib & Seaborn** — visualization
- **Bleak** — Bluetooth Low Energy scanning
- **Geopy** — geographic distance calculations

---

## Repository Structure

```text
ai-indoor-localization-iot/
├── assets/
│   └── readme/
│       ├── hero_animation.gif
│       ├── esp32_acquisition.gif
│       ├── raspberry_pi_localization.gif
│       └── tech_stack.gif
│
├── docs/
│
├── firmware/
│   └── esp32/
│       ├── main.py
│       └── config.example.py
│
├── src/
│   └── raspberry_pi_localization.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ESP32 Firmware

The ESP32 firmware is implemented in **MicroPython** and performs:

- Wi-Fi RSSI scanning
- BLE RSSI scanning
- MPU6050 accelerometer acquisition
- ESP32 temperature acquisition
- Hall-sensor acquisition
- MQTT publishing

### ESP32 Configuration

Copy:

```text
firmware/esp32/config.example.py
```

to:

```text
firmware/esp32/config.py
```

Then add your local Wi-Fi and MQTT settings.

> `config.py` should remain excluded from Git so credentials are not committed to the repository.

---

## Raspberry Pi Localization

The Raspberry Pi / Linux-side application performs:

- GPS location acquisition
- Wi-Fi scanning through `nmcli`
- BLE scanning using Bleak
- Experimental LoRa signal simulation
- Trilateration-based position estimation
- Signal-source visualization
- Signal-strength-versus-distance visualization

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Elgazar1414/ai-indoor-localization-iot.git
cd ai-indoor-localization-iot
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the localization application

```bash
python src/raspberry_pi_localization.py
```

---

## Prototype Notes

This repository represents an **experimental academic prototype**.

The current Raspberry Pi implementation uses:

- simulated LoRa measurements
- experimental signal-source positions around the GPS reference point
- trilateration-based estimation using numerical optimization

These components can later be replaced or extended with real fixed anchors, measured LoRa gateway data, calibrated RSSI models, filtering, and additional localization techniques.

---

## Future Improvements

- Real fixed anchor coordinates
- Real LoRa RSSI measurements
- Persistent MQTT subscriber integration on Raspberry Pi
- RSSI calibration models
- Kalman filtering for tracking
- Fingerprinting datasets
- Machine-learning localization experiments
- Automated evaluation and benchmarking
- Real-time dashboard visualization
- Unit and integration tests

---

## Documentation

Project documentation, dissertation material, presentation files, and related academic assets are available in the [`docs/`](./docs/) directory.

---

## Academic Project

**Project:** AI-Based Indoor Localization and Tracking for IoT Networks  
**Author:** Mostafa Elgazar  
**Department:** Electrical and Communication Engineering  
**Institution:** The British University in Egypt  
**Project Type:** Bachelor’s Graduation Project

---

<p align="center">
  <b>Built as an academic IoT localization prototype for indoor positioning research and experimentation.</b>
</p>
