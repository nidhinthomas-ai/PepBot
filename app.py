from openai import AsyncOpenAI
import chainlit as cl
client = AsyncOpenAI()

# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-4-turbo",
    "temperature": 0.1,
}

@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are an expert in peptide therapeutics and protein engineering. You respond to questions related to peptides, proteins and amino acids.",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
