tool_store = {}

def tool(func):
    def wrapper():
        name, desc = func()
        tool_store['name']={"func_name": func.__name__,
                            "func_desc": desc}