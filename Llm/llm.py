import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-pro-1.0")




prompt = """
    You are a helpful assistant that help in the analysis of stock data including prices, financial data and statements, edgar statement an many more including raw html to 
    pick the useful text.
    
    with the provided data below {data} sumarize into understable chunks 
"""
class Model:
    def __init__(self, model):
        
        
         






