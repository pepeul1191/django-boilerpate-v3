class BeforeAll():
    def __init__(self, get_response=None):
        self.get_response = get_response

    def process_request(self, request):
        None

    def process_response(self, request, response):
        print('+++++++++++++++++++++++++++++++++++++++++')
        response['x-powered-by'] = 'Ubuntu; Python; gunicorn/19.9.0;'
        return response

    def __call__(self, request):
        print('+++++++++++++++++++++++++++++++++++++++++')
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
