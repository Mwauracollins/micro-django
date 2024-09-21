class HttpResponse:
    def __init__(self, content='', status_code=200, content_type='text/html'):
        self.content = content
        self.status_code = status_code
        self.headers = {'Content-Type': content_type}
        self.reason_phrase = self.get_reason_phrase()

    def get_reason_phrase(self):
        reason_phrases = {
            200: "OK",
            404: "Not Found",
            500: "Internal Server Error",
        }
        return reason_phrases.get(self.status_code, "Unknown Status")

    def get_content(self):
        return self.content.encode('utf-8')