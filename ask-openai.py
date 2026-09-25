from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, NotFoundError, APIConnectionError

load_dotenv()

client = OpenAI()

messages=[
   {"role": "system", "content": "You are a helpful assistant.for Python programming. give me in short answers."}
]

while True:
    try:
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        print("Response:", response.choices[0].message.content) 
        messages.append({"role": "assistant", "content": response.choices[0].message.content})

    except AuthenticationError:
        print("Authentication failed. Please check your API key.")
    except NotFoundError:
        print("The requested resource was not found.")
    except APIConnectionError:
        print("Failed to connect to the OpenAI API. Please check your network connection.")
    except Exception as e:
        print(f"An error occurred: {e}")



print("messages:", messages )
print("messages length:", len(messages))
