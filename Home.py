from switchbot import SwitchBot

# Replace with your actual token and secret key
YOUR_SWITCH_BOT_TOKEN = '44a34b2c9a2648af1ec327a7cca30bab1eb078780528165304bedcf0f00c0582497b7328124a016ec6844c5fcb0945f0'
YOUR_SWITCH_BOT_SECRET = '4e295a159d6b99dd5bc7f32147c5c3da'

# Initialize the SwitchBot client
switchbot = SwitchBot(token=YOUR_SWITCH_BOT_TOKEN, secret=YOUR_SWITCH_BOT_SECRET)

# List all devices to find the lock's ID (optional, but useful for verification)
devices = switchbot.devices()
for device in devices:
    print(device) # Example output: Lock(id=CD0A1221C291)

# Assuming you have the device ID for your lock
#LOCK_DEVICE_ID = 'YOUR_LOCK_DEVICE_ID' 

# Get a specific lock device object
#lock = switchbot.device(id=LOCK_DEVICE_ID)

# Lock the door
#print("Locking the door...")
#lock.lock()

# Unlock the door
# print("Unlocking the door...")
# lock.unlock()

# Toggle the lock status
# print("Toggling the lock status...")
# lock.toggle()
