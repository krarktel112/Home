from python_switchbot_v2 import SwitchBot

# Replace with your API Token and Secret Key
YOUR_SWICH_BOT_TOKEN = '44a34b2c9a2648af1ec327a7cca30bab1eb078780528165304bedcf0f00c0582497b7328124a016ec6844c5fcb0945f0'
YOUR_SWITCH_BOT_SECRET = '4e295a159d6b99dd5bc7f32147c5c3da'

switchbot = SwitchBot(token=YOUR_SWICH_BOT_TOKEN, secret=YOUR_SWITCH_BOT_SECRET)

# List all devices to find your lock's ID
devices = switchbot.devices()
for device in devices:
    print(device) # Look for a line like 'Lock(id=CD0A1221C291)'

# If you know the device ID (replace with your lock's actual ID):
lock_id = 'FFB4AF5C4B63' 
lock = switchbot.device(id=lock_id)

# Command the lock
print(f"Status: {lock.status()}") # Query the current status

# Lock the door
#lock.command('lock')
#print("Commanded to lock.")

# Unlock the door
lock.command('unlock')
print("Commanded to unlock.")
