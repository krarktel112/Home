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
    # Discover devices and select the lock
    devices = GetSwitchbotDevices()
    lock_device = await devices.get_locks()

    # Create lock object
    bot_lock = lock.SwitchbotLock(
        lock_device[BLE_MAC].device, 
        KEY_ID, 
        ENC_KEY, 
        model=LOCK_MODEL
    )

    # --- Actions ---
    #print("Locking...")
    #await bot_lock.lock()
    
    print("Unlocking...")
    await bot_lock.unlock()

asyncio.run(main())
