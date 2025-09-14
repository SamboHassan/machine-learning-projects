# Each file in apps/ just defines a callable app.


def app(environ, start_response):
    query = environ.get("QUERY_STRING", "")
    user = "stranger"
    if query.startswith("user="):
        user = query.split("=", 1)[1]

    start_response("200 OK", [("Content-Type", "text/html")])
    html = f"<h1>Hello, {user}!</h1>"
    return [html.encode("utf-8")]
