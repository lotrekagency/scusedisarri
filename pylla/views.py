class View:

    def on_get(self, req, resp, **kwargs):
        self.get(req, **kwargs).to_response(resp)
