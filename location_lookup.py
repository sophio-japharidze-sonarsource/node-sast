"""
location_lookup.py – Geo-IP lookups against the internal geo service.

Usage:
    from location_lookup import lookup

    result = lookup("8.8.8.8")
    # {"country": "US", "region": "California", "city": "Mountain View"}
    # or None if the address could not be resolved
"""

import json
import socket

_GEO_HOST = "192.168.45.10"
_GEO_PORT = 8125
_TIMEOUT = 5  # seconds


def lookup(ip_address):
    """Return geo location data for *ip_address*, or None on failure.

    Connects to the internal geo service, sends a LOOKUP request, and parses
    the JSON response into a dict with keys "country", "region", and "city".

    Args:
        ip_address: A string containing the IPv4 or IPv6 address to look up.

    Returns:
        A dict {"country": str, "region": str, "city": str} on success,
        or None if the service is unavailable or cannot resolve the address.
    """
    if not isinstance(ip_address, str):
        return None

    # Guard against protocol injection via embedded newlines or carriage returns.
    if "\n" in ip_address or "\r" in ip_address:
        return None

    try:
        with socket.create_connection((_GEO_HOST, _GEO_PORT), timeout=_TIMEOUT) as sock:
            request = "LOOKUP {}\n".format(ip_address)
            sock.sendall(request.encode("ascii"))

            # Read the response (one line of JSON expected).
            response = _recv_line(sock)

        if response is None:
            return None

        data = json.loads(response)

        return {
            "country": data.get("country"),
            "region": data.get("region"),
            "city": data.get("city"),
        }
    except (OSError, ValueError):
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
