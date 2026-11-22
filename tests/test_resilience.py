import os, time, requests
BASE = os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")

def test_health_completes_within_timeout():
    start = time.perf_counter()
    r = requests.get(f"{BASE}/health", timeout=5)
    assert r.status_code == 200
    assert time.perf_counter() - start < 5

def test_small_sequential_burst():
    codes = [requests.get(f"{BASE}/health", timeout=5).status_code for _ in range(5)]
    assert all(code == 200 for code in codes)

# Gaps: sustained load, concurrency, rate limits, memory/CPU,
# dependency outages, retry behaviour and recovery.
