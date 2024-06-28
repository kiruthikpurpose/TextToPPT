from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="Your OpenAI key")

async def generate_response():
    completion = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "What's the most popular ski resort in Europe?"}]
    )
    return completion.choices[0].message['content']

async def main():
    response = await generate_response()
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
