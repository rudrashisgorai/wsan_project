import tkinter as tk
import random
import time
import threading
import bluetooth  # PyBluez library
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
# Bluetooth Setup: Assuming you're using bluetoothctl to connect devices manually
def bluetooth_connect():
    # The Bluetooth address of the connected sender device (replace with your device's address)
    sender_address = "XX:XX:XX:XX:XX:XX"  # Replace with your sender device's Bluetooth MAC address
   
    # Establishing Bluetooth connection
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        sock.connect((sender_address, 1))  # Channel 1 is commonly used
        print("Connected to Bluetooth device!")
    except bluetooth.btcommon.BluetoothError as err:
        print(f"Failed to connect: {err}")
        sock.close()
        return None
    return sock

# Simulate Random Metrics for testing
def get_random_metrics():
    bpm = random.randint(40, 120)  # Random BPM between 40 and 120
    hrstd = round(random.uniform(0.5, 3.0), 2)  # Random HRSTD between 0.5 and 3.0
    rmssd = round(random.uniform(10, 80), 2)  # Random RMSSD between 10 and 80
    return bpm, hrstd, rmssd
   
# Calculate Health Status based on BPM
def get_health_status(bpm):
    if bpm < 60:
        return "Low BP", "red"
    elif bpm > 100:
        return "High BP", "red"
    else:
        return "Normal BP", "green"

# Create the main window
root = tk.Tk()
root.title("Pulse Rate Monitoring System")
root.geometry("900x700")
root.config(bg="#2c3e50")

# Font Styles
font_title = ("Helvetica", 20, "bold")
font_subtitle = ("Helvetica", 14)
font_data = ("Helvetica", 12)

# Title Section
title_frame = tk.Frame(root, bg="#2980b9", pady=20)
title_frame.pack(fill="x")
title_label = tk.Label(title_frame, text="Pulse Rate Monitoring", font=font_title, fg="white", bg="#2980b9")
title_label.pack()
# Data Display Section (for pulse data)
data_frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
data_frame.pack(fill="both", expand=True)
# Red and IR Data
label_red = tk.Label(data_frame, text="Red LED:", font=font_subtitle, fg="white", bg="#34495e")
label_red.grid(row=0, column=0, sticky="w", padx=10)

label_ir = tk.Label(data_frame, text="IR LED:", font=font_subtitle, fg="white", bg="#34495e")
label_ir.grid(row=1, column=0, sticky="w", padx=10)

data_value_red = tk.Label(data_frame, text="---", font=font_data, fg="yellow", bg="#34495e")
data_value_red.grid(row=0, column=1, sticky="w", padx=10)

data_value_ir = tk.Label(data_frame, text="---", font=font_data, fg="yellow", bg="#34495e")
data_value_ir.grid(row=1, column=1, sticky="w", padx=10)

# Health Metrics Section
label_bpm = tk.Label(data_frame, text="BPM:", font=font_subtitle, fg="white", bg="#34495e")
label_bpm.grid(row=2, column=0, sticky="w", padx=10)

label_ipm = tk.Label(data_frame, text="IPM:", font=font_subtitle, fg="white", bg="#34495e")
label_ipm.grid(row=3, column=0, sticky="w", padx=10)

label_hrstd = tk.Label(data_frame, text="HRSTD:", font=font_subtitle, fg="white", bg="#34495e")
label_hrstd.grid(row=4, column=0, sticky="w", padx=10)

label_rmssd = tk.Label(data_frame, text="RMSSD:", font=font_subtitle, fg="white", bg="#34495e")
label_rmssd.grid(row=5, column=0, sticky="w", padx=10)

data_value_bpm = tk.Label(data_frame, text="---", font=font_data, fg="green", bg="#34495e")
data_value_bpm.grid(row=2, column=1, sticky="w", padx=10)
data_value_ipm = tk.Label(data_frame, text="---", font=font_data, fg="green", bg="#34495e")
data_value_ipm.grid(row=3, column=1, sticky="w", padx=10)

data_value_hrstd = tk.Label(data_frame, text="---", font=font_data, fg="green", bg="#34495e")
data_value_hrstd.grid(row=4, column=1, sticky="w", padx=10)

data_value_rmssd = tk.Label(data_frame, text="---", font=font_data, fg="green", bg="#34495e")
data_value_rmssd.grid(row=5, column=1, sticky="w", padx=10)

# Health Status Section (Dynamic feedback like "Normal BP", "High BP")
label_health_status = tk.Label(data_frame, text="Health Status:", font=font_subtitle, fg="white", bg="#34495e")
label_health_status.grid(row=6, column=0, sticky="w", padx=10)

data_value_health = tk.Label(data_frame, text="---", font=font_data, fg="yellow", bg="#34495e")
data_value_health.grid(row=6, column=1, sticky="w", padx=10)
# Pulse Data Plotting
fig, ax = plt.subplots(figsize=(6, 3))
ax.set_title("Pulse Data (Real-time)")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Pulse Value")
x_vals = []
y_vals = []

# Function to update the GUI with data from Bluetooth
def update_gui(sock):
    global x_vals, y_vals
    while True:
        try:
            # Receive data from Bluetooth sender (assuming sender sends "red, ir, bpm, hrstd, rmssd")
            data = sock.recv(1024).decode('utf-8')
            if data:
                # Parse the received data (expected format: "red,ir,bpm,hrstd,rmssd")
                red, ir, bpm, hrstd, rmssd = map(float, data.split(','))
               
                # Update GUI components with received data
                data_value_red.config(text=f"{int(red)}")
                data_value_ir.config(text=f"{int(ir)}")
                data_value_bpm.config(text=f"{bpm:.2f}")
                data_value_hrstd.config(text=f"{hrstd:.2f}")
                data_value_rmssd.config(text=f"{rmssd:.2f}")
                # Get health status based on BPM
                health_status, health_color = get_health_status(bpm)
                data_value_health.config(text=health_status, fg=health_color)
               
                # Update plot data
                x_vals.append(time.time())
                y_vals.append(red)  # For example, plot the Red LED data
                ax.clear()
                ax.plot(x_vals, y_vals, label="Red LED Data", color="blue")
                ax.set_xlabel("Time (s)")
                ax.set_ylabel("Pulse Value")
                ax.set_title("Pulse Data (Real-time)")

                # Redraw the plot on Tkinter window
                canvas.draw()

        except bluetooth.btcommon.BluetoothError as err:
            print(f"Bluetooth Error: {err}")
            sock.close()
            break
       
        time.sleep(1)

# Plot embedded into Tkinter window
canvas_frame = tk.Frame(root)
canvas_frame.pack(padx=20, pady=20)
canvas = FigureCanvasTkAgg(fig, canvas_frame)
canvas.get_tk_widget().pack()

# Connect to Bluetooth device
sock = bluetooth_connect()

# Start updating the GUI in a separate thread
if sock:
    data_thread = threading.Thread(target=update_gui, args=(sock,), daemon=True)
    data_thread.start()

# Start the Tkinter main loop
root.mainloop()
