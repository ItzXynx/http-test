import sys
import urllib.request
import json
import time

if __name__ == "__main__":
    url = sys.argv[1]
    method = sys.argv[2].upper() if len(sys.argv) > 2 else "GET"
    body = sys.argv[3].encode() if len(sys.argv) > 3 else None
    
    headers = {"User-Agent": "http-tester/1.0"}
    if body:
        headers["Content-Type"] = "application/json"
    
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    start = time.time()
    try:
        with urllib.request.urlopen(req) as r:
            elapsed = (time.time()-start)*1000
            content = r.read().decode(errors="replace")
            print(f"status: {r.status}")
            print(f"time: {elapsed:.0f}ms")
            print(f"size: {len(content)} bytes")
            print(f"body: {content[:200]}")
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code}")
# updated
