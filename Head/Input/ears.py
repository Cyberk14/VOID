# the ear file will be used to listen to USER and work-mate Ai-AGENTS prompts.

class _ears:
    def listen(self):
        prompt = input("Listening: ")
        return prompt
    
ears = _ears()
message = ears.listen()
