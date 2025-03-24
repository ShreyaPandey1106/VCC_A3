import os
import psutil
import time

def monitor_cpu(threshold=75):
    while True:
        cpu_utilization = psutil.cpu_percent(interval=1)
        print(f"CPU Utilization: {cpu_utilization}%")
        if cpu_utilization > threshold:
            print("Threshold exceeded! Initiating migration...")
            os.system("python migrate_to_gcp.py")
        time.sleep(5)  # Check CPU every 5 seconds

if __name__ == "__main__":
    monitor_cpu()
