import pytest
import openai_async
import os
from openai_async import test_utils

_OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")


@pytest.mark.asyncio
async def test_complete():
    response = await openai_async.complete(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={
            "model": "text-davinci-003",
            "prompt": "How much is 1 + 2?",
            "temperature": 0.0,
        },
    )
    assert response.json()["choices"][0]["text"].strip() == "1 + 2 = 3"


@pytest.mark.asyncio
async def test_generate_img():
    response = await openai_async.generate_img(
        _OPEN_AI_API_KEY,
        timeout=8,
        payload={
            "prompt": "a white siamese cat",
            "n": 1,
            "size": "256x256"
        },
    )
    assert test_utils.is_image_url(response.json()["data"][0]["url"])


@pytest.mark.asyncio
async def test_embeddings():
    response1 = await openai_async.embeddings(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={"model": "text-embedding-ada-002", "input": "tooth doctor"},
    )
    response2 = await openai_async.embeddings(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={"model": "text-embedding-ada-002", "input": "dentist"},
    )
    assert (
        test_utils.cosine_similarity(
            response1.json()["data"][0]["embedding"],
            response2.json()["data"][0]["embedding"],
        )
        > 0.9
    )


@pytest.mark.asyncio
async def test_chat_complete():
    response = await openai_async.chat_complete(
        _OPEN_AI_API_KEY,
        timeout=2,
        payload={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Hello!"}],
            "temperature": 0.0,
        },
    )
    assert response.json()["choices"][0]["message"] == {
        "role": "assistant",
        "content": "\n\nHello there! How can I assist you today?",
    }
