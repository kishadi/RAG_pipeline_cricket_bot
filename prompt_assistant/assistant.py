import openai

try:
    from openai import OpenAI
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
except ImportError:
    client = None
    openai.api_key = "ollama"
    openai.api_base = "http://localhost:11434/v1"

SYSTEM_PROMPT = '''You are a cranky AI assistant. Answer the user's questions using the context provided. Also, behave like an assistant who greets the user well. If you do not know the answer based on the context, say "I don't know". Do not make things up.

    Context:
    {context}

    Question: 
    {query}

    Answer:
    '''


def prompt_response(query, context):
    sys_prompt = SYSTEM_PROMPT.format(context=context, query=query)

    if client is not None:
        response = client.chat.completions.create(
            model='qwen',
            messages=[{'role': "system", "content": sys_prompt},
                      {'role': "user", "content": query}],
            temperature=0.0
        )
    else:
        response = openai.ChatCompletion.create(
            model='qwen',
            messages=[{'role': "system", "content": sys_prompt},
                      {'role': "user", "content": query}],
            temperature=0.0
        )

    message = getattr(response.choices[0], 'message', None)
    if message is None:
        return response.choices[0]['text']
    return message.content




