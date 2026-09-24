from opensearchpy import OpenSearch
from app.config import OPENSEARCH_HOST, OPENSEARCH_PORT, LOGS_INDEX, ALERTS_INDEX

client = OpenSearch(
    hosts=[{'host': OPENSEARCH_HOST, 'port': OPENSEARCH_PORT}],
    use_ssl=False,
    verify_certs=False
)

def index_log(log_data: dict):
    return client.index(index=LOGS_INDEX, body=log_data)

def index_alert(alert_data: dict):
    return client.index(index=ALERTS_INDEX, body=alert_data)

def search_failed_logins(source_ip: str) -> int:
    query = {
        "query": {
            "bool": {
                "must": [
                    {"term": {"source_ip.keyword": source_ip}},
                    {"term": {"event_type.keyword": "failed_login"}}
                ]
            }
        }
    }
    try:
        response = client.count(index=LOGS_INDEX, body=query)
        return response.get("count", 0)
    except Exception:
        return 0
