# a router-style server that serves both static files and WSGI apps:
import os
from wsgiref.simple_server import make_server
from urllib.parse import unquote

# Map URL paths to WSGI apps
from apps import greet  # you can import more apps

wsgi_apps = {
    "/greet": greet.app,
}

WEBROOT = "static"  # folder with HTML, CSS, JS


def dispatcher(environ, start_response):
    path = environ.get("PATH_INFO", "/")

    # If path matches a WSGI app
    if path in wsgi_apps:
        return wsgi_apps[path](environ, start_response)

    # Otherwise, try serving static files
    filepath = os.path.join(WEBROOT, unquote(path.lstrip("/")))

    if os.path.isdir(filepath):
        filepath = os.path.join(filepath, "index.html")

    if os.path.exists(filepath) and os.path.isfile(filepath):
        with open(filepath, "rb") as f:
            content = f.read()
        start_response("200 OK", [("Content-Type", guess_type(filepath))])
        return [content]

    # Not found
    start_response("404 Not Found", [("Content-Type", "text/plain")])
    return [b"404 Not Found"]


def guess_type(filename):
    if filename.endswith(".html"):
        return "text/html"
    if filename.endswith(".css"):
        return "text/css"
    if filename.endswith(".js"):
        return "application/javascript"
    return "application/octet-stream"


if __name__ == "__main__":
    with make_server("", 8081, dispatcher) as server:
        print("Serving on http://localhost:8081 ...")
        server.serve_forever()
