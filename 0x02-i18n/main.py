import subprocess
import threading
import os
import sys


def on_process_terminate():
    print("Flask process has terminated.")


def run_flask_in_background():
    if sys.stdout.isatty() and sys.stderr.isatty():
        print("Running Flask in the background...")

    command = ["flask", "run", "--host=0.0.0.0", "--port=5000"]

    log_file = open("flask.log", "w")
    error_file = open("flask_error.log", "w")

    # Start the Flask process
    process = subprocess.Popen(command, stdout=log_file, stderr=error_file)

    # Start a thread to monitor the process
    def monitor_process():
        process.wait()  # Wait for the process to finish
        log_file.close()
        error_file.close()
        on_process_terminate()  # Call the termination handler

    # Run the monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_process)
    monitor_thread.start()

    print(f"Flask app is running in the background with PID {process.pid}.")
    return process


if __name__ == "__main__":
    # Ensure the FLASK_APP environment variable is set
    os.environ["FLASK_APP"] = "app.py"
    run_flask_in_background()
