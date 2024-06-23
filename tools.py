from youtube_transcript_api import YouTubeTranscriptApi as yta

tool_list = {
    
}

def tool(func):
    def wrapper(*args, **kwargs):
        func_name, desc, _func_run = func()
        tool_list['Tool Name'] = {'func_name': func_name,
                                  'desc': desc,
                                  'how to run': _func_run}
        return tool_list
    return wrapper

# https://www.youtube.com/watch?v=etbYpss3kDI
class youtube:
    def func():
        func_name = "Youtube"
        
        desc = """

        """
        how_to_run = "youtube.run(id)"
    def run(id):
        func_name = ('youtube')
        desc = """
        
        """
        vid = yta.get_transcript(id)
        
        transcript = []
        for text in vid:
            text = vid['text']
            transcrpit.append(text)
            
        transcript = " ".join(transcript)
        
    return transcript
