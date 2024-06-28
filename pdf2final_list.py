from openai import AsyncOpenAI
import asyncio
import time

async def generate_openai_summary(prompt):
    client = AsyncOpenAI(api_key="Your OpenAI key")
    completion = await client.completions.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=200,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    response = completion.choices[0].text.strip()
    return response

def process(topic_list):
    data_list = []
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    for topic in topic_list:
        dct = {}
        summary = loop.run_until_complete(generate_openai_summary("I am giving you a topic. I want a summary of " + topic))
        dct["Topic"] = topic
        dct["Summary"] = summary.split("Summary:")[1].split("\n")
        print(dct)
        code = loop.run_until_complete(generate_openai_summary("I am giving you a topic... " + topic))
        code = code.replace("```python", "```")
        print(code)
        try:
            code = (code.split("```"))[1].split("```")[0]
        except:
            pass
        dct["Code"] = code
        data_list.append(dct)
        if len(topic_list) > 1:
            time.sleep(55)
    return data_list

# Example usage
'''topics = ["What's the most popular ski resort in Europe?", "Another topic"]
result = process(topics)
print(result)'''
