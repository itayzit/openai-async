# openai-async

A light-weight, asynchronous client for OpenAI API - chat completion, text completion, image generation and embeddings.<br><br>
For the full documentation, go to the [openAI website](https://beta.openai.com/docs/api-reference).


# Installation

`pip install openai-async`

# Use

## Chat completion
    response = await openai_async.chat_complete(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Hello!"}],
        },
    )
    print(response.json()["choices"][0]["message"])
    >>> {"role": "assistant", "content": "\n\nHello there! How can I assist you today?"}
Visit the [official documentation](https://platform.openai.com/docs/api-reference/chat) for more info.
## Text completion
    import openai_async

    response = await openai_async.complete(
        "<API KEY>",
        timeout=2,
        payload={
            "model": "text-davinci-003",
            "prompt": "Correct this sentence: Me like you.",
            "temperature": 0.7,
        },
    )
    print(response.json()["choices"][0]["text"].strip())
    >>> "I like you."
Visit the [official documentation](https://platform.openai.com/docs/api-reference/completions) for more info.
## Image generation
    import openai_async
    import urllib.request
    from PIL import Image

    response = await openai_async.generate_img(
        "<API KEY>",
        timeout=8,
        payload={
            "prompt": "a white siamese cat",
            "n": 1,
            "size": "512x512"
        },
    )
    urllib.request.urlretrieve(response.json()["data"][0]["url"], "img.png")
    Image.open("img.png").show()

<img alt="a cat" src="https://cdn.openai.com/API/images/guides/image_generation_simple.webp" width="60%">
<br>

## Embeddings
    import openai_async

    response = await openai_async.embeddings(
        <API_KEY>,
        timeout=2,
        payload={"model": "text-embedding-ada-002", "input": "a cat"},
    )
    print(response.json()["data"][0]["embedding"])
    >>> [-0.019408401,
    -0.009246278,
    -0.014390069,
    -0.012294915,
    -0.0025609178,
    0.021252638,
    ...]

Visit the [official documentation](https://beta.openai.com/docs/api-reference/embeddings) for more info.

# Get an API key
To generate an openAI API key, while in the [openAI website](https://beta.openai.com), click on your username in the top right corner, then go to "View API keys" and create a key.
<br><br>

### Disclaimer

This repository has no connection whatsoever to openAI.