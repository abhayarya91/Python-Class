#Authentication

class IoTDevice:
    def __init__(self, device_id, secret_key):
        self.device_id = device_id
        self.secret_key = secret_key

    def authenticate(self, provided_secret):
        return self.secret_key == provided_secret

class IoTNetwork:
    def __init__(self):
        self.authorized_devices = {}

    def register_device(self, device_id, secret_key):
        if device_id not in self.authorized_devices:
            self.authorized_devices[device_id] = IoTDevice(device_id, secret_key)
            print(f"Device {device_id} registered successfully.")
        else:
            print(f"Device {device_id} already registered.")

    def authenticate_device(self, device_id, provided_secret):
        if device_id in self.authorized_devices:
            device = self.authorized_devices[device_id]
            if device.authenticate(provided_secret):
                print(f"Device {device_id} authenticated successfully.")
            else:
                print(f"Authentication failed for device {device_id}. Invalid secret key.")
        else:
            print(f"Authentication failed for device {device_id}. Device not registered.")

# # Example usage
# if __name__ == "__main__":
#     iot_network = IoTNetwork()

#     # Register IoT devices with their unique IDs and secret keys
#     iot_network.register_device("device1", "secret123")
#     iot_network.register_device("device2", "password456")
#     iot_network.register_device("device3", "secure789")

#     # Authentication of IoT devices
#     iot_network.authenticate_device("device1", "secret123")
#     iot_network.authenticate_device("device2", "wrongpass")
#     iot_network.authenticate_device("device3", "secure789")
#     iot_network.authenticate_device("device4", "newdevicekey")
