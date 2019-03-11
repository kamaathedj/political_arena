class message:
    def __init__(self,text):
        self.text=text
    def success(self):
        pass
    def error(self):
        return self.text
