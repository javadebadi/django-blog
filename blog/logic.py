class BlogTokenize:

    def __init__(self, text: str) -> None:
        self.text = text
        self.tokens = None

    def split(self, on="\n"):
        self.tokens = self.text.split(on)

    def clean(self):
        self.tokens = [item.strip() for item in self.tokens]

    def filter(self):
        self.tokens = list(filter(lambda item: bool(item), self.tokens))

    def find_tag(self, string):
        for i in range(6, 0, -1):
            if string.startswith('#'*i):
                return 'h' + str(i)
        if string.startswith('>>>'):
            return 'blockquote'
        else:
            return 'p'

    def remove_tags(self, string):
        for i in range(6, 0, -1):
            if string.startswith('#'*i):
                return string[i:]
        if string.startswith('>>>'):
            return string[3:]
        else:
            return string

    def tokenize(self):
        self.split()
        self.clean()
        self.filter()
        results = []
        for item in self.tokens:
            results.append(
                {
                    "text": self.remove_tags(item),
                    "tag": self.find_tag(item),
                }
            )
        return results