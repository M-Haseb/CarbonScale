import time
import random

class CarbonScale:
    def __init__(self, threshold, region):
        self.threshold = threshold  # gCO2eq/kWh
        self.region = region
        self.current_replicas = 1

    def get_carbon_intensity(self):
        """
        In a real scenario, this would call the Electricity Maps API.
        For this PoC, we simulate volatile grid data.
        """
        return random.randint(200, 600)

    def scale_logic(self):
        intensity = self.get_carbon_intensity()
        print(f"Current Intensity in {self.region}: {intensity} gCO2eq/kWh")

        if intensity <= self.threshold:
            print("Target: LOW CARBON WINDOW. Scaling up GPU Pods...")
            self.current_replicas = 10 
        else:
            print("Target: HIGH CARBON INTENSITY. Scaling down to minimum...")
            self.current_replicas = 1

        return self.current_replicas

if __name__ == "__main__":
    # Example threshold for a "Green" policy
    scaler = CarbonScale(threshold=350, region="US-VA")
    
    for i in range(5):
        replicas = scaler.scale_logic()
        print(f"Kubernetes state: {replicas} pods running.\n")
        time.sleep(2)
