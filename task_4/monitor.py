import subprocess
import psutil

while True:
    speedtest_output = subprocess.run(
        ["speedtest-cli", "--simple"], capture_output=True, text=True
    )

    if speedtest_output.returncode == 0:
        print(speedtest_output.stdout)
        print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
        print(" ")
    else:
        print("Failed to run speedtest-cli command.")
