import bluetooth
import random
import time

# Function to send mock pulse data over Bluetooth
def send_pulse_data(client_socket):
    while True:
        # Simulating pulse data (values can be replaced with actual sensor data)
        red = random.randint(1000, 5000)
        ir = random.randint(1000, 5000)
        bpm = random.uniform(60, 100)  # Random BPM in the range of 60 to 100
        hrstd = random.uniform(0.5, 2.0)  # Random HRSTD
        rmssd = random.uniform(0.5, 2.0)  # Random RMSSD

        # Format the data to send
        data = f"{red},{ir},{bpm:.2f},{hrstd:.2f},{rmssd:.2f}"
        
        # Send data over Bluetooth
        try:
            client_socket.send(data)
            print(f"Sent Data: {data}")
        except bluetooth.BluetoothError as e:
            print(f"Bluetooth Error: {e}")
            break
        
        time.sleep(1)  # Send data every 1 second

# Set up Bluetooth connection to the receiver
def setup_bluetooth_connection():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)  # Only use lookup_names
    print("Found devices:", nearby_devices)
    
    # Here, choose the address of the receiver from the list of nearby devices
    # For example, assume the receiver's Bluetooth address is "2C:CF:67:03:0B:C5"
    receiver_address = "2C:CF:67:03:0B:C5"  # Replace with your receiver's address
    
    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((receiver_address, 1))  # 1 is the port
    print(f"Connected to {receiver_address}")
    return client_socket

# Main function
def main():
    client_socket = setup_bluetooth_connection()
    send_pulse_data(client_socket)

if __name__ == "__main__":
    main()
