import asyncio
from bleak import BleakClient

# SwitchBot Service and RX/TX Characteristics
# The specific characteristic for locks is not public, this is general
# SwitchBot characteristic usually: cba20002-224d-11e6-9fb8-0002a5d5c51b
LOCK_CHARACTERISTIC = "cba20002-224d-11e6-9fb8-0002a5d5c51b"
LOCK_MAC = "FF:B4:AF:5C:4B:63"

async def control_lock(address, command_bytes):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        # Send encrypted command
        await client.write_gatt_char(LOCK_CHARACTERISTIC, command_bytes)
        print("Command sent.")

# Example command bytes need to be encrypted with key_id
# This is a place holder for the encrypted payload
# encrypted_payload = encrypt_cmd("unlock", key) 
# loop.run_until_complete(control_lock(LOCK_MAC, encrypted_payload))
