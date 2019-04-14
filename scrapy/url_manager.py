class Url_Manager(object):

    # 创建两个集合,存储待爬和已爬URL地址
    def __init__(self):
        # {} 空dict  set()
        self.new_url = set()
        self.old_url = set()

    # 把新的url地址添加到待爬集合中
    def add_url(self, url):
        # 判断当前地址是否追加
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)

    # 支持添加url序列
    def add_urls(self, urls):
        for url in urls:
            self.add_url(url)

    # 返回一个待爬URL地址
    def get_url(self):
        # 随机返回一个url地址
        url = self.new_url.pop()
        # 此地址应该添加到已爬的url中
        self.old_url.add(url)
        return url

    # 判断当前待爬url集合中是否有地址
    def has_url(self):
        return len(self.new_url) > 0

if __name__ == "__main__":
    um = Url_Manager();
    l = ["aa",'aa','bb','cc']
    um.add_urls(l)
    print(um.new_url , um.old_url)
    url = um.get_url()
    print(um.new_url, um.old_url)
    print(um.has_url())