import numpy as np
import time

class SynchronousRAM:
    def __init__(self, addr_width=4, data_width=8):
        self.addr_width = addr_width
        self.data_width = data_width
        self.size = 2**addr_width  # Memory Size
        self.memory = np.zeros(self.size, dtype=np.uint8)  # Initialize RAM with zeros
        self.clock = 0

    def write(self, address, data):
        """Write data to a specific address"""
        if 0 <= address < self.size:
            self.memory[address] = data
            print(f"Clock Cycle {self.clock}: Written {hex(data)} at Address {address}")
        else:
            print("Error: Address out of range")

    def read(self, address):
        """Read data from a specific address"""
        if 0 <= address < self.size:
            data = self.memory[address]
            print(f"Clock Cycle {self.clock}: Read {hex(data)} from Address {address}")
            return data
        else:
            print("Error: Address out of range")
            return None

    def clock_cycle(self):
        """Simulate a clock cycle"""
        self.clock += 1
        time.sleep(0.5)  # Simulate delay for real-time effect

# Create RAM instance
ram = SynchronousRAM(addr_width=4, data_width=8)

# Write Data
ram.clock_cycle()
ram.write(1, 0xA5)  # Writing 0xA5 at address 1
ram.clock_cycle()
ram.write(2, 0x5A)  # Writing 0x5A at address 2

# Read Data
ram.clock_cycle()
ram.read(1)  # Reading from address 1
ram.clock_cycle()
ram.read(2)  # Reading from address 2


