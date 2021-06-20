import usocket

class Response:

    def __init__(self, f):
        self.raw = f
        self.encoding = "utf-8"
        self._cached = None

    def close(self):
        if self.raw:
            self.raw.close()
            self.raw = None
        self._cached = None

    @property
    def content(self):
        if self._cached is None:
            try:
                self._cached = self.raw.read()
            finally:
                self.raw.close()
                self.raw = None
        return self._cached

    @property
    def text(self):
        return str(self.content, self.encoding)

    def json(self):
        import ujson
        return ujson.loads(self.content)


def request(method, url, data=None, json=None, headers={}, stream=None):
    try:
        proto, dummy, host, path = url.split("/", 3)
    except ValueError:
        proto, dummy, host = url.split("/", 2)
        path = ""
    if proto == "http:":
        port = 80
    elif proto == "https:":
        import ussl
        port = 443
    else:
        raise ValueError("Unsupported protocol: " + proto)

    if ":" in host:
        host, port = host.split(":", 1)
        port = int(port)

    ai = usocket.getaddrinfo(host, port, 0, usocket.SOCK_STREAM)
    ai = ai[0]
    #print("UR:ai[0]=",end='')
    #print(ai)
    s = usocket.socket(ai[0], ai[1], ai[2])
    try:
        respSuccess=True
        #print("sconnect CMD=s.connect(",end='')
        #print(ai[-1])
        s.connect(ai[-1])
        print("PROTO|",end='')
        if proto == "https:":
            s = ussl.wrap_socket(s, server_hostname=host)
        print("WRPD|",end='')
        s.write(b"%s /%s HTTP/1.0\r\n" % (method, path))
        print("HOST|",end='')
        if not "Host" in headers:
            s.write(b"Host: %s\r\n" % host)
        # Iterate over keys to avoid tuple alloc
        print("k|",end='')
        for k in headers:
            s.write(k)
            s.write(b": ")
            s.write(headers[k])
            s.write(b"\r\n")
        print("j|",end='')
        if json is not None:
            assert data is None
            import ujson
            data = ujson.dumps(json)
            s.write(b"Content-Type: application/json\r\n")
        print("d1|",end='')
        if data:
            s.write(b"Content-Length: %d\r\n" % len(data))
        s.write(b"\r\n")
        print("d2|",end='')
        if data:
            s.write(data)

        l = s.readline()
        #print(l)
        l = l.split(None, 2)
        status = int(l[1])
        reason = ""
        if len(l) > 2:
            reason = l[2].rstrip()
        print("w|",end='')
        while True:
            l = s.readline()
            if not l or l == b"\r\n":
                break
            #print(l)
            if l.startswith(b"Transfer-Encoding:"):
                if b"chunked" in l:
                    raise ValueError("Unsupported " + l)
            elif l.startswith(b"Location:") and not 200 <= status <= 299:
                raise NotImplementedError("Redirects not yet supported")
    except (OSError,IndexError):
        print("ERR HTTP: error...maybe couldnt reach host? or IndexError in data parameter")
        s.close()
        respSuccess=False
        #raise

    if respSuccess==True:
        resp = Response(s)
        resp.status_code = status
        resp.reason = reason
        return resp
    else:
        return "XXX"


def head(url, **kw):
    return request("HEAD", url, **kw)

def get(url, **kw):
    return request("GET", url, **kw)

"""
        dat={"deviceToken": mID,"altitude":mp3, "batteryV":battery_voltage, "connType":connType, "event":i }
        r = urequest.post("https://amvader.net/iot/pycom/elcom-hook.php",json=dat,headers={"content-type":"application/json"})
"""
def post(url, **kw):
    return request("POST", url, **kw)

def put(url, **kw):
    return request("PUT", url, **kw)

def patch(url, **kw):
    return request("PATCH", url, **kw)

def delete(url, **kw):
    return request("DELETE", url, **kw)
