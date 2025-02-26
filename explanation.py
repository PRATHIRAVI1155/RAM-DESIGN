# Explanation of Synchronous RAM Simulation Code**
This code simulates a **Synchronous RAM (Random Access Memory) Module** using Python and NumPy. It includes **Read and Write Operations** along with a simulated **clock cycle**.

---

### **🔹 Code Breakdown**
#### **1️⃣ Import Required Libraries**
```python
import numpy as np
import time
```
- `numpy` is used to create and manage the RAM memory array efficiently.  
- `time` is used to introduce delays to simulate **clock cycles**.

---

#### **2️⃣ Define the `SynchronousRAM` Class**
```python
class SynchronousRAM:
```
- This defines a **class** named `SynchronousRAM`, which will handle **RAM operations**.

---

#### **3️⃣ Initialize RAM Parameters**
```python
    def __init__(self, addr_width=4, data_width=8):
        self.addr_width = addr_width
        self.data_width = data_width
        self.size = 2**addr_width  # Memory Size
        self.memory = np.zeros(self.size, dtype=np.uint8)  # Initialize RAM with zeros
        self.clock = 0
```
- `addr_width=4`: **Number of address bits** (default is 4).  
  - **Total memory size = 2^4 = 16 locations**  
- `data_width=8`: Each memory location can hold **8-bit data**.  
- `self.memory = np.zeros(self.size, dtype=np.uint8)`:  
  - Initializes **RAM memory** with zeros (`uint8` means 8-bit storage).
- `self.clock = 0`: A counter to track **clock cycles**.

---

#### **4️⃣ Write Operation (Storing Data in RAM)**
```python
    def write(self, address, data):
        """Write data to a specific address"""
        if 0 <= address < self.size:
            self.memory[address] = data
            print(f"Clock Cycle {self.clock}: Written {hex(data)} at Address {address}")
        else:
            print("Error: Address out of range")
```
- This function **writes data** to a specific **memory address**.
- It **checks if the address is valid** (`0 ≤ address < size`).
- Stores the **data in memory** at the specified address.
- **Prints the operation details** (Clock Cycle, Data, Address).
- **If address is out of range**, it prints an error message.


---

#### **5️⃣ Read Operation (Retrieving Data from RAM)**
```python
    def read(self, address):
        """Read data from a specific address"""
        if 0 <= address < self.size:
            data = self.memory[address]
            print(f"Clock Cycle {self.clock}: Read {hex(data)} from Address {address}")
            return data
        else:
            print("Error: Address out of range")
            return None
```
- This function **reads data** from a specified memory **address**.
- **Checks if address is valid** (`0 ≤ address < size`).
- **Fetches and prints the data** from that address.
- **Returns the data** to the calling function.
- **If address is out of range**, prints an error.

Example:  
`ram.read(1)` → Reads **0xA5** from address **1**.

---

#### **6️⃣ Clock Cycle Simulation**
```python
    def clock_cycle(self):
        """Simulate a clock cycle"""
        self.clock += 1
        time.sleep(0.5)  # Simulate delay for real-time effect
```
- **Increments the clock cycle counter** (`self.clock += 1`).
- **Introduces a delay (`time.sleep(0.5)`)** to simulate real-world **clock operation**.

---

### **🔹 Main Execution (Using the `SynchronousRAM` Class)**

#### **7️⃣ Create a RAM Instance**
```python
ram = SynchronousRAM(addr_width=4, data_width=8)
```
- Creates a **RAM object** with **4-bit address (16 locations) and 8-bit data storage**.

---

#### **8️⃣ Write Data into RAM**
```python
ram.clock_cycle()
ram.write(1, 0xA5)  # Writing 0xA5 (165 in decimal) at address 1
ram.clock_cycle()
ram.write(2, 0x5A)  # Writing 0x5A (90 in decimal) at address 2
```
- **First Clock Cycle** → Writes **0xA5** at **address 1**.  
- **Second Clock Cycle** → Writes **0x5A** at **address 2**.

---

#### **9️⃣ Read Data from RAM**
```python
ram.clock_cycle()
ram.read(1)  # Reading from address 1
ram.clock_cycle()
ram.read(2)  # Reading from address 2
```
- **Third Clock Cycle** → Reads **data from address 1** (should return `0xA5`).  
- **Fourth Clock Cycle** → Reads **data from address 2** (should return `0x5A`).  

---

### **📌 Expected Output**
```
Clock Cycle 1: Written 0xa5 at Address 1
Clock Cycle 2: Written 0x5a at Address 2
Clock Cycle 3: Read 0xa5 from Address 1
Clock Cycle 4: Read 0x5a from Address 2
```
- Shows how data is stored and retrieved correctly with each **clock cycle**.

