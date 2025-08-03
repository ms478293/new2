from aiohttp import web
import dnslib
import socket
import os

async def handle_doh(request):
    try:
        if request.method == "POST":
            data = await request.read()
        else:
            dns_hex = request.query.get("dns")
            if not dns_hex:
                return web.Response(status=400, text="Missing 'dns'")
            data = bytes.fromhex(dns_hex)

        dns_request = dnslib.DNSRecord.parse(data)
        domain = str(dns_request.q.qname).rstrip(".")

        # Simple blocklist
        BLACKLIST = {"malware.com", "phish.com", "evil.com"}
        if domain in BLACKLIST:
            reply = dnslib.DNSRecord(dnslib.DNSHeader(id=dns_request.header.id, qr=1, rcode=3))
            return web.Response(body=reply.pack(), content_type="application/dns-message")

        # Forward to Google DNS
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, ("8.8.8.8", 53))
        response_data, _ = sock.recvfrom(1024)
        sock.close()

        return web.Response(body=response_data, content_type="application/dns-message")
    except Exception as e:
        return web.Response(status=500, text=str(e))

app = web.Application()
app.router.add_get("/dns-query", handle_doh)
app.router.add_post("/dns-query", handle_doh)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    web.run_app(app, port=port, host="0.0.0.0")