import uuid
from datetime import datetime

def check_brute_force(source_ip: str, username: str, failed_count: int, threshold: int = 5):
    if failed_count >= threshold:
        return {
            "alert_id": f"ALT-{uuid.uuid4().hex[:8].upper()}",
            "title": "Possible Brute Force Attack",
            "severity": "HIGH",
            "mitre_technique": "T1110",
            "source_ip": source_ip,
            "username": username,
            "failed_attempts": failed_count,
            "status": "OPEN",
            "created_at": datetime.utcnow().isoformat()
        }
    return None
