class BeforeAll():
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        None

    def process_response(self, request, response):
        print('+++++++++++++++++++++++++++++++++++++++++')
        response['x-powered-by'] = 'Ubuntu; Python; gunicorn/19.9.0;'
        return response

    def process_exception(self, request, exception):
        print exception.__class__.__name__
        print exception.message
        return None
