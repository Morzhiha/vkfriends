import requests


class VK:

    def __init__(self, options):
        self.id = options['myID']
        self.token = options['token']
        self.api = options['api']

    # формируем стркоу запроса
    def getURL(self, methodName, params, token=True):
        url = 'https://api.vk.com/method/{method_name}?{params}&v={api_v}'.format(
            method_name=methodName, api_v=self.api, params=params)
        if token:
            url = '{}&access_token={token}'.format(url, token=self.token)
        return url

    # выполняем любой запрос
    @staticmethod
    def makeRequest(url, data=False):
        if data:
            result = requests.post(url, data).json()
        else:
            result = requests.get(url).json()
        if result and 'response' in result.keys():
            return result['response']
        return result
