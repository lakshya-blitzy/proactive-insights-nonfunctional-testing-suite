import os, requests
BASE = os.getenv("BASE_URL", "http://127.0.0.1:8000").rstrip("/")

def test_health_response_has_content_type():
    r = requests.get(f"{BASE}/health", timeout=5)
    assert "content-type" in r.headers

# Gaps: security headers, CORS, TLS, brute-force protection,
# input abuse, secret leakage and authorization boundaries.
