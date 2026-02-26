import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Dis bonjour en français"}
    ]
)

print(response.content[0].text)pyth

GET /hello.htm HTTP/1.1 

