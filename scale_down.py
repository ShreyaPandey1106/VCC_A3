import subprocess

def scale_down_to_one(instance_group, zone):
    try:
        command = f"gcloud compute instance-groups managed resize {instance_group} --size=1 --zone={zone}"
        subprocess.run(command, shell=True, check=True)
        print("Successfully scaled down to 1 instance.")
    except subprocess.CalledProcessError as e:
        print(f"Error during scaling down: {e}")

if __name__ == "__main__":
    INSTANCE_GROUP = "autoscale"
    ZONE = "us-central1-c"
    scale_down_to_one(INSTANCE_GROUP, ZONE)
