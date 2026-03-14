import asyncio
from bleak import BleakScanner

async def main():
    print("Scanning for Bluetooth LE devices...")
    # Discover devices within range
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"Address: {d.address}, Name: {d.name}")

if __name__ == "__main__":
    asyncio.run(main())
