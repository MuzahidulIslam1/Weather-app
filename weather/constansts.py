from dotenv import load_dotenv
import os 


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

API_HOST = os.getenv("API_HOST")


print(API_HOST, API_HOST, API_URL, API_KEY)