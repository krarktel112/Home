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
    bot_lock = lock.SwitchbotLock(
        lock_device[BLE_MAC].device, 
        KEY_ID, 
        ENC_KEY, 
        model=LOCK_MODEL
    )

    print("Attempting to Unlock...")
    # 2. Unlock action
    await bot_lock.unlock()
    print("Unlock command sent.")

    # 3. Lock action
    # await lock_device.lock()

if __name__ == "__main__":
    asyncio.run(main())
