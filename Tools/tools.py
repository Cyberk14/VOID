tool_store = {}

def tool(func: object) -> complex:
    def wrapper() -> complex:
        name, desc = func()
        tool_store[name]={"func_name": func.__name__,
                            "func_desc": desc}
        print(name, desc)
        
    return wrapper


