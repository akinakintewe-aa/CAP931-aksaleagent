from openai import OpenAI
from config import OPENAI_MODEL
client = OpenAI() 
response = client.chat.completions.create(
    model=OPENAI_MODEL,
    messages=[
        {"role": "system", "content": "You are a friendly coding coach."},
        {"role": "user", "content": "Welcome me to AI engineering in one sentence"},
    ]
)        
print(response.choices[0].message.content) 
print(response.usage)
    


