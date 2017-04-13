
def app (environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    body = [i + '\n' for i in environ['QUERY_STRING'].split('&')]
    return body