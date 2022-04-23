class Note:
    def __init__(self, content, index) -> None:
        self.INDEX = index
        self.content = content

    def contains(self, i):
        """Checks if the content contains the passed argument."""
