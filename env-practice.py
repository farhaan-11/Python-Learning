
import os

from dotenv import load_dotenv

load_dotenv()

# Access environment variables
api_key = os.getenv("API_KEY")
print(f"API Key: {api_key}")

app_name = os.getenv("APP_NAME")
print(f"App Name: {app_name}")

my_key = os.getenv("MY_KEY")
print(f"My Key: {my_key}")

print("API Key:", os.getenv("OPENAI_API_KEY"))
print("App Name:", os.getenv("APP_NAME"))
print("My Key:", os.getenv("MY_KEY"))