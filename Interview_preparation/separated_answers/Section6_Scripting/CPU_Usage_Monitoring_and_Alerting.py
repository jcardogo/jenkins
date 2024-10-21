import psutil
import requests

# CPU usage threshold (percentage)
CPU_THRESHOLD = 80

def send_alert(message):
    # Send alert using your preferred notification service (e.g., PagerDuty, Slack)
    requests.post("https://your-notification-service.com/alert", json={"message": message})

def monitor_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        send_alert(f"CPU usage exceeded {CPU_THRESHOLD}%: {cpu_usage}%")

while True:
    monitor_cpu_usage()
    time.sleep(60)  # Monitor CPU usage every minute