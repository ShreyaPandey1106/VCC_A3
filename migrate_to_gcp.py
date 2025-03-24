import subprocess

def migrate_to_gcp(instance_group, zone, new_size):
    try:
        command = f"gcloud compute instance-groups managed resize {instance_group} --size={new_size} --zone={zone}"
        subprocess.run(command, shell=True, check=True)
        print("Migration to GCP completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during migration: {e}")

if __name__ == "__main__":
    INSTANCE_GROUP = "autoscale"
    ZONE = "us-central1-c"
    NEW_SIZE = 2  # Scale to 2 instances
    migrate_to_gcp(INSTANCE_GROUP, ZONE, NEW_SIZE)