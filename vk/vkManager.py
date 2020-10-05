from vk.vkRequest import VK


class VKManager:

    def __init__(self, options):
        self.token = options['token']
        self.api = options['api']
        self.vk = VK(options)

    def getBaseInfo(self, id):
        url = self.vk.getURL('users.get', 'user_ids=%s&fields=photo' % str(id))
        return self.vk.makeRequest(url)

    def getFriends(self, id):
        url = self.vk.getURL('friends.get', 'user_id=%s&fields=uid,first_name,last_name,photo' % id)
        friends = self.vk.makeRequest(url)
        if 'items' in friends.keys():
            return friends['items']
        return []
