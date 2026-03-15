import asyncio
from switchbot.discovery import GetSwitchbotDevices
from switchbot.devices import lock
from switchbot.const import SwitchbotModel

BLE_MAC="XX:XX:XX:XX:XX:XX" # The MAC of your lock
KEY_ID="3c" # The key-ID of your encryption-key for your lock
ENC_KEY="7fe3283b22eee778ac4727d900972e23" # The encryption-key with key-ID "XX"
LOCK_MODEL=SwitchbotModel.LOCK_PRO # Your lock model (here we use the Lock-Pro)


async def main():
    wolock = await GetSwitchbotDevices().get_locks()
    await lock.SwitchbotLock(
        wolock[BLE_MAC].device, KEY_ID, ENCRYPTION_KEY, model=LOCK_MODEL
    ).lock()


asyncio.run(main())
