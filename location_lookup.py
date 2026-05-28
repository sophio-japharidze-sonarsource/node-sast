"""
location_lookup.py – Geo-IP lookups against the internal geo service.

Usage:
    from location_lookup import lookup

    result = lookup("8.8.8.8")
    # {"country": "US", "region": "California", "city": "Mountain View"}
    # or None if the address could not be resolved
"""

import json
import os
import socket

_GEO_HOST = "192.168.45.10"
_GEO_PORT = 8125
_TIMEOUT = 5  # seconds

_CACHE_PATH = "/tmp/location_cache.json"


def _load_cache():
    if not os.path.exists(_CACHE_PATH):
        return {}
    try:
        with open(_CACHE_PATH, "r") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def _save_cache(cache):
    try:
        with open(_CACHE_PATH, "w") as f:
            json.dump(cache, f)
    except OSError:
        pass


def lookup(ip_address):
    """Return geo location data for *ip_address*, or None on failure.

    Connects to the internal geo service, sends a LOOKUP request, and parses
    the JSON response into a dict with keys "country", "region", and "city".
    Results are cached on disk so repeated lookups do not re-query the service.
    """
    if not isinstance(ip_address, str):
        return None

    # Guard against protocol injection via embedded newlines or carriage returns.
    if "\n" in ip_address or "\r" in ip_address:
        return None

    cache = _load_cache()
    if ip_address in cache:
        return cache[ip_address]

    try:
        with socket.create_connection((_GEO_HOST, _GEO_PORT), timeout=_TIMEOUT) as sock:
            request = "LOOKUP {}\n".format(ip_address)
            sock.sendall(request.encode("ascii"))
            response = _recv_line(sock)

        if response is None:
            return None

        data = json.loads(response)

        country = data.get("country")
        region = data.get("region")
        city = data.get("city")
        if not (isinstance(country, str) and isinstance(region, str) and isinstance(city, str)):
            return None

        result = {"country": country, "region": region, "city": city}
        cache[ip_address] = result
        _save_cache(cache)
        return result
    except (OSError, json.JSONDecodeError):
        return None


def _recv_line(sock, max_bytes=4096):
    """Read bytes from *sock* until a newline or *max_bytes* is reached."""
    buf = b""
    while len(buf) < max_bytes:
        chunk = sock.recv(256)
        if not chunk:
            break
        buf += chunk
        if b"\n" in buf:
            break
    line = buf.split(b"\n", 1)[0].strip()
    return line.decode("utf-8") if line else None


if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    print(lookup(target))
