tool_list = {
    
}

def tool(func):
    def wrapper():
        func_name, desc, _func_run = func()
        tool_list['Tool Name'] = {'func_name': func_name,
                                  'desc': desc,
                                  'how to run': _func_run}
    return wrapper
