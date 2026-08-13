import network
import ubinascii
import machine
import time
from umqtt.simple import MQTTClient
from esp32 import raw_temperature, hall_sensor
from machine import Pin, ADC, I2C
import bluetooth
from BLE import BLEScanner

# Wi-Fi Configuration
SSID = "WE123"
PASSWORD = "0123456789"
MQTT_BROKER = "192.168.12.63"
MQTT_TOPIC = "esp32/localization"

# Initialize Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)
while not wifi.isconnected():
    time.sleep(1)
print("Wi-Fi Connected! IP:", wifi.ifconfig()[0])

# MQTT Configuration
client = MQTTClient("ESP32", MQTT_BROKER)
client.connect()

# Initialize BLE Scanner
ble_scanner = BLEScanner()

# Initialize Sensors (IMU and ADC for RSSI Processing)
i2c = I2C(scl=Pin(22), sda=Pin(21))
imu = machine.I2C(1, scl=Pin(22), sda=Pin(21))  # MPU6050 IMU
adc = ADC(Pin(34))  # Analog RSSI Processing
adc.atten(ADC.ATTN_11DB)


# Function to Read RSSI from Wi-Fi
def get_rssi():
    wifi.scan()
    rssi_values = {}
    for ssid, bssid, channel, rssi, authmode, hidden in wifi.scan():
        rssi_values[ubinascii.hexlify(bssid).decode()] = rssi
    return rssi_values


# Function to Read BLE RSSI
def get_ble_rssi():
    return ble_scanner.scan()


# Function to Read IMU Data
def get_imu_data():
    try:
        data = i2c.readfrom_mem(0x68, 0x3B, 6)  # MPU6050 register
        acc_x = (data[0] << 8 | data[1]) / 16384.0
        acc_y = (data[2] << 8 | data[3]) / 16384.0
        acc_z = (data[4] << 8 | data[5]) / 16384.0
        return acc_x, acc_y, acc_z
    except:
        return 0, 0, 0


# Main Loop
while True:
    wifi_rssi = get_rssi()
    ble_rssi = get_ble_rssi()
    imu_data = get_imu_data()

    payload = {
        "wifi_rssi": wifi_rssi,
        "ble_rssi": ble_rssi,
        "imu": imu_data,
        "temperature": raw_temperature(),
        "hall": hall_sensor()
    }

    client.publish(MQTT_TOPIC, str(payload))
    print("Published:", payload)

    time.sleep(5)
