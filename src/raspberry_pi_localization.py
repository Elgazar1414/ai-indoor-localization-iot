import time
import asyncio
import gpsd
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from bleak import BleakScanner
from geopy.distance import geodesic


# Reference Points (you can change these)
REFERENCE_WIFI_SSID = "Osman"
REFERENCE_WIFI_SSIDD = "Mostafa"

REFERENCE_BT_MAC = "F8:6E:58:1D:DB:5E"
REFERENCE_BT_MACC = "30:22:00:00:7A:F2"
REFERENCE_BT_MACCC = "F4:4E:FC:00:5F:C4"


# Connect to GPS
def get_gps_location():
    try:
        gpsd.connect()
        packet = gpsd.get_current()
        if packet.mode >= 2:
            return packet.lat, packet.lon
    except Exception as e:
        print("GPS Error:", e)
    return 30.0444, 31.2357  # Default to Cairo, Egypt


# Get WiFi signal strength
def get_wifi_signal():
    try:
        output = subprocess.check_output(
            ["nmcli", "-t", "-f", "SSID,SIGNAL", "dev", "wifi"]
        ).decode("utf-8")
        networks = [line.split(":") for line in output.strip().split("\n") if line]
        return [(ssid, int(signal)) for ssid, signal in networks]
    except Exception as e:
        print("Wi-Fi Error:", e)
        return []


# Get Bluetooth devices using Bleak
async def get_bluetooth_devices():
    try:
        devices = await BleakScanner.discover()
        return [(device.address, device.rssi) for device in devices]
    except Exception as e:
        print("Bluetooth Error:", e)
        return []


# Simulate LoRa signal (replace with actual data if available)
def get_lora_signal():
    return [("LoRa-Gateway-1", -70), ("LoRa-Gateway-2", -65), ("LoRa-Gateway-3", -80)]


# Trilateration algorithm
def trilateration(anchors, distances):
    def error_function(x):
        return sum((np.linalg.norm(x - np.array(a)) - d) ** 2 for a, d in zip(anchors, distances))

    initial_guess = np.mean(anchors, axis=0)
    result = minimize(error_function, initial_guess, method="L-BFGS-B")
    return result.x if result.success else (None, None)


# Main localization function
async def hybrid_localization():
    lat, lon = get_gps_location()
    wifi_data = get_wifi_signal()
    bluetooth_data = await get_bluetooth_devices()
    lora_data = get_lora_signal()

    anchors = [(lat, lon)]
    distances = [1]

    for ssid, signal in wifi_data:
        anchors.append(
            (lat + np.random.uniform(-0.0001, 0.0001), lon + np.random.uniform(-0.0001, 0.0001))
        )
        distances.append(abs(signal / 10))

    for address, signal in bluetooth_data:
        anchors.append(
            (lat + np.random.uniform(-0.0001, 0.0001), lon + np.random.uniform(-0.0001, 0.0001))
        )
        distances.append(abs(signal / 10))

    for gateway, signal in lora_data:
        anchors.append(
            (lat + np.random.uniform(-0.0001, 0.0001), lon + np.random.uniform(-0.0001, 0.0001))
        )
        distances.append(abs(signal / 10))

    final_location = trilateration(anchors, distances)
    return final_location, wifi_data, bluetooth_data, lora_data

# Distance print function
def print_distances(location, signal_sources):
    print("\n--- Distances from estimated location ---")
    for name, (lat, lon) in signal_sources.items():
        distance_m = geodesic(location, (lat, lon)).meters
        print(f"{name} is {distance_m:.2f} meters away.")


# Plotting function
def plot_location(location, wifi_data, bluetooth_data, lora_data):
    plt.figure(figsize=(8, 6))
    plt.scatter(location[0], location[1], c="red", marker="x", label="Estimated Position")

    signal_sources = {}

    # To avoid duplicate labels in legend
    wifi_plotted = False
    bt_plotted = False
    lora_plotted = False

    # Plot Wi-Fi points
    for i, (ssid, _) in enumerate(wifi_data):
        offset_lat = location[0] + np.random.uniform(-0.0001, 0.0001)
        offset_lon = location[1] + np.random.uniform(-0.0001, 0.0001)
        distance = geodesic(location, (offset_lat, offset_lon)).meters
        if ssid == REFERENCE_WIFI_SSID:
            plt.scatter(offset_lat, offset_lon, c="cyan", marker="s", label="WiFi Reference")
        else:
            if not wifi_plotted:
                plt.scatter(offset_lat, offset_lon, c="blue", marker="o", label="WiFi")
                wifi_plotted = True
            else:
                plt.scatter(offset_lat, offset_lon, c="blue", marker="o")

        plt.text(offset_lat, offset_lon, f"SSID: {ssid}\n{distance:.1f}m", fontsize=8)
        signal_sources[f"WiFi: {ssid}"] = (offset_lat, offset_lon)

    # Plot Bluetooth points
    for i, (address, _) in enumerate(bluetooth_data):
        offset_lat = location[0] + np.random.uniform(-0.0001, 0.0001)
        offset_lon = location[1] + np.random.uniform(-0.0001, 0.0001)
        distance = geodesic(location, (offset_lat, offset_lon)).meters
        if address in (REFERENCE_BT_MAC, REFERENCE_BT_MACC, REFERENCE_BT_MACCC):
            plt.scatter(offset_lat, offset_lon, c="orange", marker="D", label="BT Reference")
        else:
            if not bt_plotted:
                plt.scatter(offset_lat, offset_lon, c="green", marker="^", label="Bluetooth")
                bt_plotted = True
            else:
                plt.scatter(offset_lat, offset_lon, c="green", marker="^")

        plt.text(offset_lat, offset_lon, f"MAC: {address}\n{distance:.1f}m", fontsize=8)
        signal_sources[f"BT: {address}"] = (offset_lat, offset_lon)

    # Plot LoRa points
    for i, (gateway, _) in enumerate(lora_data):
        offset_lat = location[0] + np.random.uniform(-0.0001, 0.0001)
        offset_lon = location[1] + np.random.uniform(-0.0001, 0.0001)
        distance = geodesic(location, (offset_lat, offset_lon)).meters
        if not lora_plotted:
            plt.scatter(offset_lat, offset_lon, c="purple", marker="v", label="LoRa")
            lora_plotted = True
        else:
            plt.scatter(offset_lat, offset_lon, c="purple", marker="v")

        plt.text(offset_lat, offset_lon, f"Gateway: {gateway}\n{distance:.1f}m", fontsize=8)
        signal_sources[f"LoRa: {gateway}"] = (offset_lat, offset_lon)

    plt.xlabel("Latitude")
    plt.ylabel("Longitude")
    plt.legend()
    plt.title("Hybrid IoT Signal Localization")
    plt.grid()
    plt.tight_layout()
    plt.show()

    # Print distances
    print_distances(location, signal_sources)
def plot_signal_strength_vs_distance(location, wifi_data, bluetooth_data, lora_data):
    import seaborn as sns

    sns.set(style="whitegrid")

    def plot_signals(data, title, color, label_prefix):
        distances = []
        signals = []
        labels = []

        for name, signal in data:
            offset_lat = location[0] + np.random.uniform(-0.0001, 0.0001)
            offset_lon = location[1] + np.random.uniform(-0.0001, 0.0001)
            dist = geodesic(location, (offset_lat, offset_lon)).meters
            distances.append(dist)
            signals.append(signal)
            labels.append(f"{label_prefix}: {name}")

        plt.figure()
        plt.scatter(distances, signals, color=color)
        for i, txt in enumerate(labels):
            plt.annotate(txt, (distances[i], signals[i]))
        plt.xlabel("Distance from Estimated Location (m)")
        plt.ylabel("Signal Strength (dBm)")
        plt.title(f"{title} Signal Strength vs Distance")
        plt.grid()
        plt.tight_layout()
        plt.show()

    plot_signals(wifi_data, "Wi-Fi", "blue", "SSID")
    plot_signals(bluetooth_data, "Bluetooth", "green", "BT")
    plot_signals(lora_data, "LoRa", "purple", "LoRa")


# Main loop
if __name__ == "__main__":
    while True:
        location, wifi_data, bluetooth_data, lora_data = asyncio.run(hybrid_localization())
        print("\nEstimated Position:", location)

        for ssid, signal in wifi_data:
            print(f"Wi-Fi SSID: {ssid}, Signal Strength: {signal} dBm")
        for address, signal in bluetooth_data:
            print(f"Bluetooth Device: {address}, RSSI: {signal} dBm")
        for gateway, signal in lora_data:
            print(f"LoRa Gateway: {gateway}, Signal Strength: {signal} dBm")

        plot_location(location, wifi_data, bluetooth_data, lora_data)
        plot_signal_strength_vs_distance(location, wifi_data, bluetooth_data, lora_data)

        time.sleep(10)