import pytest
import openai_async
import os
import re

_OPEN_AI_API_KEY = os.getenv("OPENAI_API_KEY")


def _is_image_url(url: str) -> bool:
    return any(re.search(pattern, url, re.IGNORECASE) for pattern in ['.jpg', '.jpeg', '.png', '.gif'])


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
    assert _is_image_url(response.json()["data"][0]["url"])