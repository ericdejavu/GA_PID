import requests,json

class Postboy:
    def __init__(self):
        self.base_url = BASE_URL

    def login(self):
        pass

    def token(self):
        pass

    def status(self,response):
        code = response.status_code
        if code == 404:
            pass
        elif code == 500:
            pass
        elif code == 503:
            pass

    def update_header(self):
        self.headers...

    def send(self,addr,data):
        return requests.post(self.base_url + addr, data = json.dumps(data), headers = headers)

    def origin_sync(self,origin):
        response = self.send(ORIGIN_ADDR, origin)

    def measure_sync(self,measure):
        response = self.send(MEASURE_ADDR, measure)

    def analyse_sync(self,analyse):
        response = self.send(ANALYZE_ADDR, analyse)

    def get_project_group(self):
        pass

    def pid_group_sync(self,pid_group):
        response = self.send(NOTIFY_ADDR, pid_group)

    def sub_group_sync(self,sub):
        response = self.send(NOTIFY_ADDR, sub)

    def continue_group_sync(self,continue_group):
        response = self.send(NOTIFY_ADDR, continue_group)
