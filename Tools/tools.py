class Tool:
    def __init__(self, name: str, desc: str, func: object):  # noqa: F821
        self.name = name
        self.desc = desc
        self.func = func
        self.tools = []
        
    def saveTool(self):
        toolist = []
        
        toolist.append(self.name)
        toolist.append(self.desc)
        toolist.append(self.func)
        
        self.tools.append(toolist)
        
webBrowser = Tool("webBrowser",
                  "used when in need for searching",
                  "web.search(query)")

webBrowser.saveTool()

print(webBrowser.tools)