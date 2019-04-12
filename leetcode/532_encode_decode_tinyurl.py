class Codec:

    def __init__(self):
        self.url_dict = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        hash_value = str(hash(longUrl))
        if hash_value in self.url_dict:
            return self.url_dict[hash_value]
        else:
            self.url_dict[hash_value] = longUrl
            return hash_value

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        longUrl = self.url_dict[shortUrl]
        return longUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
