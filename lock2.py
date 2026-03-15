import asyncio
from switchbot.discovery import GetSwitchbotDevices
from switchbot.devices import lock
from switchbot.const import SwitchbotModel

# --- CONFIGURATION ---
BLE_MAC="FF:B4:AF:5C:4B:63"  # MAC address of your lock
KEY_ID = "3c"                  # Key-ID from SwitchBot API
ENC_KEY = "7fe3283b22eee778ac4727d900972e23" # Encryption key
LOCK_MODEL = SwitchbotModel.LOCK # Or LOCK

async def main():
    # 1. Discover or specifically address the lock
    lock_device = lock.SwitchbotLock(
        device=None, # Usually set by GetSwitchbotDevices, can be handled separately
        key_id=KEY_ID,
        key=ENC_KEY,
        model=LOCK_MODEL,
        mac=BLE_MAC
    )

    print("Attempting to Unlock...")
    # 2. Unlock action
    await lock_device.unlock()
    print("Unlock command sent.")

    # 3. Lock action
    # await lock_device.lock()

if __name__ == "__main__":
    asyncio.run(main())
