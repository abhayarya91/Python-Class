class DDoSDetector:
    def __init__(self, threshold=100):
        self.threshold = threshold
        self.request_count = 0

    def process_request(self):
        self.request_count += 1

    def detect_ddos_attack(self):
        if self.request_count > self.threshold:
            print("DDoS attack detected! Request count:", self.request_count)
            return True
        else:
            print("No DDoS attack detected. Request count:", self.request_count)
            return False

    def reset_counter(self):
        self.request_count = 0

if __name__ == "__main__":
    ddos_detector = DDoSDetector(threshold=100)
    for i in range(150):
        ddos_detector.process_request()
    ddos_detector.detect_ddos_attack()
    ddos_detector.reset_counter()







# class DDoSDetector:
#     def __init__(self, threshold=100):
#         self.threshold = threshold  # Threshold for identifying a DDoS attack
#         self.request_count = 0      # Counter for incoming requests

#     def process_request(self):
#         self.request_count += 1

#     def detect_ddos_attack(self):
#         # Check if the request count exceeds the threshold
#         if self.request_count > self.threshold:
#             print("DDoS attack detected! Request count:", self.request_count)
#             return True
#         else:
#             print("No DDoS attack detected. Request count:", self.request_count)
#             return False

#     def reset_counter(self):
#         self.request_count = 0

# # Example usage
# if __name__ == "__main__":
#     # Create a DDoS detector instance with a threshold of 100 requests
#     ddos_detector = DDoSDetector(threshold=100)

#     # Simulate incoming requests
#     for i in range(150):
#         ddos_detector.process_request()

#     # Detect DDoS attack
#     ddos_detector.detect_ddos_attack()

#     # Reset counter after handling the requests
#     ddos_detector.reset_counter()
