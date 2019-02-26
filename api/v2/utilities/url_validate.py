import re
class url:
    def __init__(self,data):
        self.email=data
    def validateUrl(self):
        pattern=r'https?://(www\.)?(\w+)(\.\w+)'
        pat=re.compile(pattern)
        match=pat.finditer(self.email)
        for match in match:
            print(match.group(0))
            return True
        return "didnt enter matching"