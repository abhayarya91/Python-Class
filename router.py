class Router:
    def __init__(self):
        self.firmware_version = "1.0"
        self.password = "StrongPassword"
        self.telnet_enabled = False
        self.firewall_config = {"IoT_Devices": ["192.168.1.0/24"]}
        self.access_control_list = {}

    def update_firmware(self, new_version):
        self.firmware_version = new_version
        print(f"Router firmware updated to version {new_version}")

    def change_password(self, new_password):
        self.password = new_password
        print("Router password changed successfully")

    def enable_telnet(self):
        self.telnet_enabled = True
        print("Telnet enabled")

    def disable_telnet(self):
        self.telnet_enabled = False
        print("Telnet disabled")

    def configure_firewall(self, rule_name, rule_details):
        self.firewall_config[rule_name] = rule_details
        print("Firewall rule configured successfully")

    def add_acl_entry(self, device_ip, permission):
        self.access_control_list[device_ip] = permission
        print(f"Access control entry added for {device_ip}")

# Instantiate a Router object
router = Router()

# Update firmware
router.update_firmware("2.0")

# Change router password
router.change_password("NewStrongPassword")

# Enable Telnet (for demonstration purposes)
router.enable_telnet()

# Disable Telnet
router.disable_telnet()

# Configure firewall to segment IoT devices
router.configure_firewall("IoT_Devices", ["192.168.1.0/24"])

# Add an access control entry for an IoT device
router.add_acl_entry("192.168.1.10", "Allow")
