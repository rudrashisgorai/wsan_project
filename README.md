# Wireless Pulse Monitoring System (WSAN)

### **Course**: ECPS 205  
### **Team Members**:  
- **Rudrashis Gorai**  
- **Hridya Satish Pisharady**  
- **Rohankumar Barouliya**

---

## **Project Overview**

The Wireless Pulse Monitoring System is designed to monitor pulse signals using two Raspberry Pi units. The system captures pulse data through a sensor, transmits it over Bluetooth, and visualizes it on a GUI at the receiving end. Additionally, it computes relevant health metrics such as BPM, IPM, HRSTD, and RMSSD.

---

## **Materials Needed**
1. **Two Raspberry Pi units**  
2. **Analog-to-Digital Converter (ADC)** (e.g., MCP3008)  
3. **Pulse sensor**  
4. **Necessary cables and accessories**  

---

## **Project Breakdown**

### **1. Setup and Sensor Integration**
- **Task 1.1**:  
  - Understand the operation of the pulse sensor and the requirement for an ADC module.  
  - Note: Raspberry Pi lacks built-in ADC, which is necessary for handling analog pulse signals.  
- **Task 1.2**:  
  - Configure the first Raspberry Pi to integrate the pulse sensor and ADC module.

---

### **2. Data Transmission**
- **Task 2.1**:  
  - Establish a Bluetooth connection between the two Raspberry Pi units.  
  - Use libraries like [BlueDot](https://github.com/martinohanlon/BlueDot) or similar for ease of implementation.  
- **Task 2.2**:  
  - Program the first Raspberry Pi to transmit pulse data wirelessly to the second Raspberry Pi.

---

### **3. GUI Development and Data Representation**
- **Task 3.1**:  
  - Develop a GUI on the second Raspberry Pi to display received pulse data.  
- **Task 3.2**:  
  - Add functionality in the GUI to compute and represent health metrics such as:  
    - **BPM** (Beats Per Minute)  
    - **IPM** (Impulses Per Minute)  
    - **HRSTD**  
    - **RMSSD** (Root Mean Square of Successive Differences)  

---

### **4. Testing and Documentation**
- **Task 4.1**:  
  - Test the system for accuracy and reliability, ensuring seamless communication and data representation.  
- **Task 4.2**:  
  - Document:  
    - The setup process.  
    - The codebase and functionality.  
    - Observations and results in a comprehensive report.  

---

## **Getting Started**

### **Installation**
1. Clone this repository:  
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install required Python libraries:  
   ```bash
   pip install -r requirements.txt
   ```

---

### **Usage**
1. **First Raspberry Pi (Sender):**
   - Connect the pulse sensor to the ADC module and the Raspberry Pi.
   - Run the script to collect and transmit data via Bluetooth:  
     ```bash
     python sender.py
     ```

2. **Second Raspberry Pi (Receiver):**
   - Pair the Raspberry Pi with the sender unit via Bluetooth.
   - Run the GUI application to visualize pulse data:  
     ```bash
     python receiver.py
     ```

---

## **Technical Details**
- **Programming Language**: Python  
- **Libraries Used**:  
  - `BlueDot` for Bluetooth communication  
  - `matplotlib` or `tkinter` for GUI development  
  - `numpy` for data calculations  

---

## **Contributing**
We welcome contributions to enhance this project!  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit changes:  
   ```bash
   git commit -m "Add feature-name"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```  
5. Create a pull request.

---


## **Contact**
For questions or collaboration, feel free to reach out:  
- **Rudrashis Gorai**: 
- **Hridya Satish Pisharady**:
- **Rohankumar Barouliya**: 

--- 

### **Acknowledgments**
We extend our gratitude to the ECPS 205 faculty for their guidance and support throughout this project.
