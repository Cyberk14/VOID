
import utils

def plan(task: str):
    prompt = f"""You are tasked to make plan for a certain task,
the should be in steps for example:

'''Task: Place a Trade of the best company to invest in this financial fiscal year of USA.

Steps: 
1. Research what the USA financial fiscal year prioritizes the most.
2. Research what companies that fit the priorities of the financial fiscal year and will be most likely to benefit those priorities.
3. Research performance on their Company Balance Sheets.
    a. Research balance sheets of Company a
    b. Research balance sheets of Company b
    c. Research balance sheets of Company c
    d. Research balance sheets of Company ...
4. Get their financial trade data according to the company Ticker and perform technical Analysis.
5. Set a possible price target.
6. Use a broker to place the order according to the set price target.
7. Occasionally monitor any financial news or events to capture any fluctuation'''

make a plan for this Task: {task},

Steps:
"""
    response = utils.send_str(prompt)
    
    return response

def add_to_plan_db(data: str):
    with open('plan_data.txt', 'a') as file:
        file.write(data)
        
def fetch_plan_data(path: str = 'plan_data.txt'):
    with open(path, 'r') as file:
        plan_data = file.read()
        
    return plan_data

def execute(task: str):
    steps = plan(task)
    
    prompt = f"""you are tasked to turn a number of steps into function calls. In this stage is where tools are used then there response is gathered.

here are the tools {utils.Youtube.register(), utils.Search.register(), utils.AlphaVantage.register()} read the ``description`` and follow the ``how to``, let's think step by step

- Call the tool displaying there how_to according argument 

for example: 
'''
Steps: 
1. Research what the USA financial fiscal year prioritizes the most.
2. Research what companies that fit the priorities of the financial fiscal year and will be most likely to benefit those priorities.
3. Research performance on their Company Balance Sheets.
    a. Research balance sheets of Company a
    b. Research balance sheets of Company b
    c. Research balance sheets of Company c
    d. Research balance sheets of Company ...
4. Get their financial trade data according to the company Ticker and perform technical Analysis.
5. Set a possible price target.
6. Use a broker to place the order according to the set price target.
7. Occasionally monitor any financial news or events to capture any fluctuation

Steps//Actions:
Steps: 
1. Research what the USA financial fiscal year prioritizes the most. // Search.run("what the USA financial fiscal 2024 prioritizes the most?")
2. Research what companies that fit the priorities of the financial fiscal year and will be most likely to benefit those priorities. // Search.run("Companies that fit in the priorities of the Renewable energy sector")
3. Research performance on their Company Balance Sheets.
    a. Research balance sheets of Company a // Search.run("balance sheets of company a")
    b. Research balance sheets of Company b // Search.run("balance sheets of company b")
    c. Research balance sheets of Company c // Search.run("balance sheets of company c")
    d. Research balance sheets of Company ... // Search.run("balance sheets of company ...")
4. Get their financial trade data according to the company Ticker and perform technical Analysis. 
5. Set a possible price target.
6. Use a broker to place the order according to the set price target.
7. Occasionally monitor any financial news or events to capture any fluctuation
''' """
    
    tool_steps = utils.send_str(prompt)
    
    utils.action(tool_steps)
