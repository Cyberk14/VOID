# this file will be used to see/spot the info the internet an the files the use r will have complied inform of .pdf files and images.

from Lower_Torso.Tools.tools import _web

class _Eyes:
    def __init__(self, query=None, image=None, data=None, *args, **kwargs):
        self.message = "these are your eyes, You use them to read and send the info read to the brain you read all kinds of info like text(PDF files, youtube transcripts, market_news, SEC_fillings, etc) and Images(chart_images, screen_shots or any images)"
        self.query = query
        self.data = data
        self.args = args
        self.kwargs = kwargs
        self.Image = image
        self.lens = _web()
        
    def use(self):
        
