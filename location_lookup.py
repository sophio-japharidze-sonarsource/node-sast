import json
import os
import socket


GEO_SERVICE_HOST = "192.168.45.10"
GEO_SERVICE_PORT = 8125

CACHE_PATH = "/tmp/location_cache.json"


def _load_cache():
    if not os.path.exists(CACHE_PATH):
        return {}
    with open(CACHE_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def _save_cache(cache):
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f)


def _query_service(ip_address):
    with socket.create_connection((GEO_SERVICE_HOST, GEO_SERVICE_PORT), timeout=2) as sock:
        sock.sendall(f"LOOKUP {ip_address}\n".encode("utf-8"))
        data = sock.recv(4096).decode("utf-8").strip()
    parts = data.split("|")
    if len(parts) < 3:
        return None
    return {"country": parts[0], "region": parts[1], "city": parts[2]}


def lookup(ip_address):
    cache = _load_cache()
    if ip_address in cache:
        return cache[ip_address]

    result = _query_service(ip_address)
    if result is not None:
        cache[ip_address] = result
        _save_cache(cache)
    return result


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    print(lookup(target))
