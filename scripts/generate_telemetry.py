import requests
import time
from datetime import datetime

API_URL = "http://127.0.0.1:8000/logs"

def send_test_logs():
    payloads = [
        {"event_type": "failed_login", "username": "admin", "source_ip": "10.0.0.88", "timestamp": datetime.utcnow().isoformat(), "source": "linux_auth"},
        {"event_type": "failed_login", "username": "admin", "source_ip": "10.0.0.88", "timestamp": datetime.utcnow().isoformat(), "source": "linux_auth"},
        {"event_type": "failed_login", "username": "admin", "source_ip": "10.0.0.88", "timestamp": datetime.utcnow().isoformat(), "source": "linux_auth"},
        {"event_type": "failed_login", "username": "admin", "source_ip": "10.0.0.88", "timestamp": datetime.utcnow().isoformat(), "source": "linux_auth"},
        {"event_type": "failed_login", "username": "admin", "source_ip": "10.0.0.88", "timestamp": datetime.utcnow().isoformat(), "source": "linux_auth"},
        {"event_type": "suspicious_command", "username": "root", "source_ip": "10.0.0.150", "timestamp": datetime.utcnow().isoformat(), "source": "bash_history"}
    ]
    
    for p in payloads:
        try:
            r = requests.post(API_URL, json=p)
            print(f"Sent: {p['event_type']} from {p['source_ip']} -> Response: {r.status_code}")
        except Exception as e:
            print(f"Failed to send log: {e}")
        time.sleep(0.5)

if __name__ == "__main__":
    send_test_logs()
