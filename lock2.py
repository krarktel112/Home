import asyncio
from bleak import BleakClient, BleakScanner

async def list_characteristics(device_address: str):
    print(f"Connecting to {device_address}...")
    try:
        # Use BleakClient to connect to the device
        async with BleakClient(device_address) as client:
            print(f"Connected: {client.is_connected}")
            
            # Discover all services and characteristics
            services = await client.get_services()
            print(f"Discovered {len(services)} services.")

            for service in services:
                print(f"\n[Service] {service.uuid} (Handle: {service.handle})")
                for char in service.characteristics:
                    print(f"  [Characteristic] {char.uuid} (Handle: {char.handle}) | Properties: {char.properties}")
                    for descriptor in char.descriptors:
                        print(f"    [Descriptor] {descriptor.uuid} (Handle: {descriptor.handle})")

    except Exception as e:
        print(f"An error occurred: {e}")

# Replace "YOUR_DEVICE_ADDRESS" with the actual address of your BLE device.
# On macOS, this might be a UUID. On Windows/Linux, it's typically a MAC address.
device_address_to_connect = "FF:B4:AF:5C:4B:63"

# Run the asynchronous function
if __name__ == "__main__":
    asyncio.run(list_characteristics(device_address_to_connect))
