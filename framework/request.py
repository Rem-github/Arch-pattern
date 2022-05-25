class Request:

    def __init__(self, environ):
        self.method = environ.get('REQUEST_METHOD').lower()
        self.path = environ.get('PATH_INFO')
        self.querystring = self._get_query_string(environ)
        self.headers = self._get_headers(environ)

    def _get_headers(self, environ):

        headers = {}
        for key, value in environ.items():
            if key.startswith('HTTP_'):
                headers[key[5:].lower()] = value
        return headers

    def _get_query_string(self, environ):
        query_strings = {}
        qs = environ.get('QUERY_STRING')
        if qs:
            ql = qs.split('&')
            for el in ql:
                key, value = el.split('=')
                if key not in query_strings:
                    query_strings[key] = list(value)
                else:
                    query_strings[key].append(value)
        return query_strings
