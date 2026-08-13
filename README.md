<p align="center">

&#x20; <img src="assets/readme/hero\_animation.gif"

&#x20;      alt="AI-Based Indoor Localization and Tracking for IoT Networks"

&#x20;      width="100%">

</p>



<h1 align="center">

AI-Based Indoor Localization and Tracking for IoT Networks

</h1>



<p align="center">

&#x20; <b>Hybrid IoT Localization • Embedded Systems • Wireless Signal Processing</b>

</p>



<p align="center">



<img src="https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white">

<img src="https://img.shields.io/badge/MicroPython-ESP32-black?logo=micropython">

<img src="https://img.shields.io/badge/ESP32-IoT-red?logo=espressif">

<img src="https://img.shields.io/badge/Raspberry%20Pi-Localization-C51A4A?logo=raspberrypi">

<img src="https://img.shields.io/badge/MQTT-Communication-purple">

<img src="https://img.shields.io/badge/Wi--Fi-RSSI-blue">

<img src="https://img.shields.io/badge/Bluetooth-BLE-0082FC?logo=bluetooth">

<img src="https://img.shields.io/badge/Status-Prototype-orange">



</p>



<p align="center">

An experimental IoT localization platform combining ESP32-based sensing with Raspberry Pi processing, wireless RSSI measurements, MQTT communication, and trilateration-based position estimation.

</p>

<p align="center">
An experimental IoT localization platform combining ESP32-based sensing with Raspberry Pi processing, wireless RSSI measurements, MQTT communication, and trilateration-based position estimation.
</p>
<p align="center">
  <img src="assets/readme/hero\_animation.gif" alt="AI-Based Indoor Localization and Tracking for IoT Networks" width="100%">
</p>

<p align="center">
  <b>Hybrid IoT localization prototype using ESP32, Raspberry Pi, Wi-Fi/BLE RSSI, GPS, MQTT, and trilateration.</b>
</p>

\---

## System Overview

<p align="center">
  <img src="assets/readme/esp32\_acquisition.gif" alt="ESP32 Data Acquisition" width="100%">
</p>

<p align="center">
  ESP32 collects Wi-Fi RSSI, BLE RSSI, MPU6050 IMU data, temperature, and hall-sensor readings, then publishes the payload through MQTT.
</p>

\---

## Localization Pipeline

<p align="center">
  <img src="assets/readme/raspberry\_pi\_localization.gif" alt="Raspberry Pi Localization Pipeline" width="100%">
</p>

<p align="center">
  The Raspberry Pi / Linux application combines GPS, Wi-Fi, Bluetooth, and simulated LoRa measurements, then estimates position using trilateration and SciPy optimization.
</p>

\---

## Technology Stack

<p align="center">
  <img src="assets/readme/tech\_stack.gif" alt="Technology Stack" width="100%">
</p>

\---

## Repository Structure

```text
ai-indoor-localization-iot/
├── src/
│   └── raspberry\_pi\_localization.py
├── firmware/
│   └── esp32/
│       ├── main.py
│       └── config.example.py
├── docs/
├── assets/
│   └── readme/
├── requirements.txt
├── .gitignore
└── README.md
```

\---

## Quick Start

```bash
git clone https://github.com/Elgazar1414/ai-indoor-localization-iot.git
cd ai-indoor-localization-iot
pip install -r requirements.txt
python src/raspberry\_pi\_localization.py
```

> \*\*Prototype note:\*\* the current Raspberry Pi script uses simulated LoRa values and experimental signal-source positions for localization testing and visualization.

\---

## Academic Project

**AI-Based Indoor Localization and Tracking for IoT Networks**  
**Mostafa Elgazar** — Electrical and Communication Engineering  
The British University in Egypt

