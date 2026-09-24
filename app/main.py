from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from app.services.opensearch_client import index_log, index_alert, search_failed_logins
from app.rules.brute_force import check_brute_force

app = FastAPI(title="Mini-SIEM Ingestion & Detection API", version="1.0.0")

class LogPayload(BaseModel):
    event_type: str
    username: str
    source_ip: str
    timestamp: str
    source: str

@app.get("/")
def root():
    return {"status": "online", "system": "Mini-SIEM Framework"}

@app.post("/logs")
def ingest_log(payload: LogPayload):
    log_data = payload.dict()
    # Index raw log
    res = index_log(log_data)
    
    # Evaluate brute force rule if failed login
    if payload.event_type == "failed_login":
        recent_count = search_failed_logins(payload.source_ip)
        alert = check_brute_force(payload.source_ip, payload.username, recent_count)
        if alert:
            index_alert(alert)
            return {"status": "ingested", "alert_triggered": True, "alert": alert}
            
    return {"status": "ingested", "alert_triggered": False}
