

class news:
    def __init__(self, news):
        self.title = news["title"]
        self.top_image = news["top_image"]
        self.images = news["images"]
        self.videos = news["videos"]
        self.url = news["url"]
        self.date = news["date"]
        self.short_description = news["short_description"]
        self.text = news["text"]
        self.publisher = news["publisher"]["title"]
        self.publisher_url = news["publisher"]["href"]

    