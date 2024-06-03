from collections import defaultdict
import random

class ThreatDetector:
    def __init__(self):
        # Dictionary to store past attack patterns and their frequencies
        self.attack_patterns = defaultdict(int)
        # Threshold for considering behavior as suspicious
        self.suspicious_threshold = 0.7

    def record_attack(self, attack_pattern):
        # Record the occurrence of an attack pattern
        self.attack_patterns[attack_pattern] += 1

    def analyze_behavior(self, behavior_data):
        # Perform behavior analysis to detect anomalies or suspicious activities
        # For simplicity, this example calculates the ratio of 1s to total data points
        ratio_of_ones = sum(behavior_data) / len(behavior_data)
        return ratio_of_ones > self.suspicious_threshold

    def prevent_access(self, device_id):
        # Implement access prevention mechanisms
        print(f"Unauthorized access detected for device {device_id}. Access prevented.")

    def prevent_malware(self, device_id):
        # Implement malware prevention mechanisms
        print(f"Malware detected on device {device_id}. Malware prevented.")

# Example usage
if __name__ == "__main__":
    threat_detector = ThreatDetector()

    # Simulate past attacks and record them
    past_attacks = ["DDoS", "Ransomware", "Phishing", "Brute Force"]
    for attack in past_attacks:
        threat_detector.record_attack(attack)

    # Simulate behavior analysis for an IoT device
    behavior_data = [random.randint(0, 1) for _ in range(100)]  # Simulated behavior data
    is_suspicious = threat_detector.analyze_behavior(behavior_data)

    if is_suspicious:
        # If behavior is suspicious, prevent access and check for malware
        threat_detector.prevent_access("iot_device_id_123")
        threat_detector.prevent_malware("iot_device_id_123")
    else:
        print("No suspicious behavior detected.")
