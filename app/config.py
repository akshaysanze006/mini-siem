import os

OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST", "localhost")
OPENSEARCH_PORT = int(os.getenv("OPENSEARCH_PORT", 9200))
LOGS_INDEX = "siem-logs"
ALERTS_INDEX = "siem-alerts"
