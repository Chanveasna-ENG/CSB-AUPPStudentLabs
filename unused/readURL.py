import urllib.request

class web_data:
    def __init__(self, url):
        self.url = url
        self.data = None
        try:
            request = urllib.request.Request(
                url,
                data=None, 
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                }
            )
            self.data = urllib.request.urlopen(request).read().decode('utf-8')

        except Exception as e:
            print('There was an Error loading the file:', e)

print(web_data('https://www.youtube.com/').data)