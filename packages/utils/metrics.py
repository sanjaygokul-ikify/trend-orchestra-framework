import time
from prometheus_client import Counter

metrics = Counter('orchestra_requests_total', 'Total number of requests')

def configure_metrics():
    metrics.inc(0)
