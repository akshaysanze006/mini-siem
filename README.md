# 🛡️ Mini-SIEM: Real-Time Security Information & Event Management

A lightweight, containerized SIEM platform built with **FastAPI**, **OpenSearch 2.12.0**, and **OpenSearch Dashboards**. The system ingests security log telemetry, evaluates detections against MITRE ATT&CK techniques, and visualizes threats on a real-time SOC command dashboard.

---

## 🏗️ System Architecture

1. **Ingestion Layer:** FastAPI REST API accepts log payloads via JSON endpoints.
2. **Detection Engine:** Stateful detection rules evaluate incoming event sequences (e.g., Brute Force T1110).
3. **Storage Layer:** OpenSearch stores raw logs (`siem-logs*`) and triggered alerts (`siem-alerts*`).
4. **Visualization Layer:** OpenSearch Dashboards provides operational visibility via interactive charts and widgets.

---

## ⚡ Quickstart

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
* Python 3.10+ (for local API development)

### 1. Clone or Extract the Repository
```bash
git clone https://github.com/YOUR_USERNAME/mini-siem.git
cd mini-siem
```

### 2. Launch Infrastructure
Start OpenSearch and OpenSearch Dashboards in single-node dev mode:
```bash
docker compose up -d
```

### 3. Run Ingestion API
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

---

## 📊 Accessing the SOC Dashboard

1. Open **OpenSearch Dashboards** at `http://localhost:5601`.
2. Open **FastAPI Documentation** at `http://localhost:8000/docs`.
3. Ingest sample logs using the Swagger UI or the automation script:
   ```bash
   python scripts/generate_telemetry.py
   ```
4. Access the **Mini-SIEM Command Center** under **Dashboards** to view live threat graphs.

---

## 🎯 Supported Detections & Mappings

| Threat Scenario | Event Type | Threshold | MITRE ATT&CK Technique |
| :--- | :--- | :--- | :--- |
| **Brute Force Attack** | `failed_login` | 5 failures / source IP | `T1110` |
| **Suspicious Execution** | `suspicious_command` | Immediate | `T1059` |

---

## 🛡️ License
Distributed under the MIT License.
