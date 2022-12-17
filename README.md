# openai-async

An asynchronous client for openai services - completion, image generation and embeddings.<br><br>
For the full documentation, go to the [openAI website](https://beta.openai.com/docs/api-reference).


# Installation

`pip install openai-async`

# Use

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
Visit the [official documentation](https://beta.openai.com/docs/api-reference/completions) for more info.
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

<img alt="a cat" src="https://oaidalleapiprodscus.blob.core.windows.net/private/org-1yFGEVR2Z2q0cjpxYXoEQ9mE/user-I8zlH1LhK7LToUCDLQObNQNk/img-ilgejxsjIvGiGMNqzLC9Nbxw.png?st=2022-12-17T18%3A58%3A14Z&se=2022-12-17T20%3A58%3A14Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2022-12-17T12%3A17%3A09Z&ske=2022-12-18T12%3A17%3A09Z&sks=b&skv=2021-08-06&sig=E0SqiNHnQuPunDUoOB%2BU/AoUxuNU0TEw6tPZTVcs2Ko%3D" width="60%">
<br><br>
Visit the official documentation for more info: https://beta.openai.com/docs/api-reference/images/create

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