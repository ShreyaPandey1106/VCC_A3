# Autoscaling Assignment

This repository demonstrates autoscaling from a local Virtual Machine (VM) to Google Cloud Platform (GCP) based on CPU utilization. It includes monitoring scripts, migration logic, and a Flask-based simulation application where users can generate CPU loads interactively.

## Features

- **CPU Monitoring**:
  - Tracks CPU utilization on a local VM.
  - Triggers scaling when utilization exceeds 75%.

- **Scaling to GCP**:
  - Automatically increases instances in a Managed Instance Group on GCP when the local VM is under high load.

- **Descaling**:
  - Reduces the instance count to one when the load drops.

- **Interactive Simulation**:
  - Flask application with a user interface to generate and stop CPU load.

## File Descriptions

- **monitor_cpu.py**:
  - Monitors CPU utilization on the local VM.
  - Initiates migration to GCP when utilization exceeds the threshold.

- **migrate_to_gcp.py**:
  - Handles scaling of a Managed Instance Group on GCP.
  - Uses the `gcloud` CLI to resize instances.

- **scale_down.py**:
  - Reduces the instance count in GCP to one when the load drops below the threshold.

- **app.py**:
  - Flask application with a UI for simulating CPU load.
  - Users can start and stop load generation interactively.

- **templates/index.html**:
  - HTML template for the Flask UI.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ShreyaPandey1106/VCC_A3.git
   cd VCC_A3

2. Install dependencies:
   ```bash
   pip install psutil flask

4. Set up Google Cloud CLI:
   - Install Google Cloud SDK.
   - Authenticate with your GCP account:
     ```bash
     gcloud auth login
     gcloud config set project [PROJECT_ID]

5. Create a GCP Managed Instance Group:
   -Follow the steps outlined in migrate_to_gcp.py to create and configure the group.

## Running the Project

1. Start the Flask application:
   ```bash
   python3 app.py
   
  Access the UI at http://127.0.0.1:5000/.

3. Start the CPU monitoring script:
   ```bash
   python3 monitor_cpu.py

5. Simulate load from the UI and observe scaling behavior in GCP Console.

## Demo Workflow

1. Scaling:
   - Generate CPU load using the UI.
   - Watch the CPU utilization exceed 75% and trigger scaling.

2. Descaling:
   - Stop the simulation and observe instance count reducing to one.
   
