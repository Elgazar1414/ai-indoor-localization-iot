\# AI-Based Indoor Localization and Tracking for IoT Networks



A prototype IoT localization system that combines wireless signal measurements and embedded sensing to estimate and visualize device locations.



The project uses an \*\*ESP32\*\* for wireless and sensor data acquisition and a \*\*Raspberry Pi / Linux-based Python application\*\* for signal collection, localization, and visualization.



\## Project Overview



Indoor localization is challenging because GPS performance is limited inside buildings and wireless signals are affected by obstacles, interference, and multipath propagation.



This project explores a hybrid localization approach using:



\* Wi-Fi RSSI

\* Bluetooth RSSI

\* GPS reference data

\* LoRa signal simulation

\* ESP32 sensor measurements

\* IMU data

\* Trilateration-based position estimation



\## System Architecture



```text

ESP32

│

├── Wi-Fi RSSI

├── BLE RSSI

├── MPU6050 IMU

├── Temperature

└── Hall Sensor

&#x20;       │

&#x20;       ▼

&#x20;     MQTT

&#x20;       │

&#x20;       ▼

Raspberry Pi / Linux

│

├── Wi-Fi scanning

├── Bluetooth scanning

├── GPS

├── LoRa simulation

│

&#x20;       ▼

Hybrid Localization

│

├── Signal processing

├── Trilateration

└── Numerical optimization

&#x20;       │

&#x20;       ▼

Estimated Position

&#x20;       │

&#x20;       ▼

Visualization \& Signal Analysis

```



\## ESP32 Data Acquisition



The ESP32 firmware is implemented using \*\*MicroPython\*\*.



It collects:



\* Nearby Wi-Fi RSSI measurements

\* Bluetooth Low Energy RSSI measurements

\* MPU6050 accelerometer measurements

\* ESP32 temperature information

\* Hall sensor measurements



The collected data is published to an MQTT topic periodically.



\## Raspberry Pi Localization



The Raspberry Pi / Linux-side Python application performs:



\* GPS location acquisition

\* Wi-Fi scanning using `nmcli`

\* Bluetooth scanning using Bleak

\* LoRa signal simulation

\* Signal-based distance estimation

\* Trilateration

\* Position visualization

\* Signal-strength-versus-distance visualization



The trilateration algorithm minimizes localization error using SciPy numerical optimization.



\## Technologies



\*\*Programming\*\*



\* Python

\* MicroPython



\*\*Hardware / Embedded\*\*



\* ESP32

\* Raspberry Pi

\* MPU6050 IMU



\*\*Wireless / IoT\*\*



\* Wi-Fi

\* Bluetooth Low Energy

\* MQTT

\* LoRa



\*\*Python Libraries\*\*



\* NumPy

\* SciPy

\* Matplotlib

\* Seaborn

\* Bleak

\* Geopy

\* gpsd-py3



\## Repository Structure



```text

ai-indoor-localization-iot/

│

├── src/

│   └── raspberry\_pi\_localization.py

│

├── firmware/

│   └── esp32/

│       ├── main.py

│       └── config.example.py

│

├── docs/

│   ├── dissertation.pdf

│   ├── project\_poster.pptx

│   └── project\_presentation.pptx

│

├── data/

├── results/

├── assets/

│

├── requirements.txt

├── .gitignore

└── README.md

```



\## Installation



Clone the repository:



```bash

git clone https://github.com/YOUR-USERNAME/ai-indoor-localization-iot.git

cd ai-indoor-localization-iot

```



Install the Raspberry Pi / Python dependencies:



```bash

pip install -r requirements.txt

```



\## ESP32 Configuration



Copy:



```text

firmware/esp32/config.example.py

```



to:



```text

firmware/esp32/config.py

```



Then configure your own:



\* Wi-Fi SSID

\* Wi-Fi password

\* MQTT broker address



`config.py` is excluded from Git to prevent credentials from being committed.



\## Running the Raspberry Pi Localization Application



Run:



```bash

python src/raspberry\_pi\_localization.py

```



The application scans available wireless signals, estimates a position, displays localization information, and generates visualization plots.



\## Current Prototype Notes



This repository represents an experimental academic prototype.



The current Raspberry Pi implementation uses simulated LoRa measurements and generates experimental signal-source positions around the GPS reference position for visualization and localization testing.



Future implementations can replace these simulated values with measured anchor coordinates and real LoRa gateway measurements.



\## Future Improvements



\* Use fixed real-world anchor coordinates

\* Integrate real LoRa RSSI measurements

\* Add persistent MQTT subscriber integration on the Raspberry Pi

\* Add RSSI calibration models

\* Add Kalman filtering for tracking

\* Integrate fingerprinting datasets

\* Evaluate machine-learning localization models

\* Add real-time dashboard visualization

\* Add automated tests and evaluation datasets



\## Academic Project



\*\*Project:\*\* AI-Based Indoor Localization and Tracking for IoT Networks



\*\*Author:\*\* Mostafa Elgazar



\*\*Department:\*\* Electrical and Communication Engineering



\*\*Institution:\*\* The British University in Egypt



\*\*Project Type:\*\* Bachelor’s Graduation Project



\## License



This repository is provided for academic and educational purposes.



