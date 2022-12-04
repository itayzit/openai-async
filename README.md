# openai-async

An asynchronous client for openai services - completion, image generation and embedding.<br><br>
For the full documentation, go to the [openAI website](https://beta.openai.com/docs/api-reference).


# Installation

`pip install openai-async`

# Use

## Text completion
    import openai_async

    response = await openai_async.complete(
        "<API KEY>",
        timeout=1,
        payload={
            "model": "text-davinci-003",
            "prompt": "Correct this sentence: Me like you.",
            "temperature": 0.7,
        },
    )
    print(response.json()["choices"][0]["text"].strip())
    >>> "I like you."

## Image generation
    import openai_async
    import urllib.request
    from PIL import Image

    response = await openai_async.generate(
        "<API KEY>",
        timeout=1,
        payload={
            "prompt": "a white siamese cat",
            "n": 1,
            "size": "1024x1024"
        },
    )
    urllib.request.urlretrieve(response["data"][0]["url"], "img.png")
    Image.open("img.png").show()

![A white siamese cat](https://oaidalleapiprodscus.blob.core.windows.net/private/org-1yFGEVR2Z2q0cjpxYXoEQ9mE/user-I8zlH1LhK7LToUCDLQObNQNk/img-63b5z1tNyTg9YFjYvAIGE8Sp.png?st=2022-12-03T22%3A14%3A44Z&se=2022-12-04T00%3A14%3A44Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-03T12%3A00%3A31Z&ske=2022-12-04T12%3A00%3A31Z&sks=b&skv=2021-08-06&sig=m%2BcY1Yo8jY9bJwXccZrbW7k8K7tOBPNT6VMJViiq5oE%3D)


# Getting an API key
To generate an openAI API key, while the openAI website, click your username on the right corner, then go to "View API keys" and create a key.
<br><br>
### Disclaimer

This repository has no connection whatsoever to the official openAI. 