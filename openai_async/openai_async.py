import httpx


def _send_to_openai(endpoint_url: str,):
    async def send_to_openai(api_key: str, timeout: float, payload: dict) -> httpx.Response:
        """
        Send a request to openai.
        :param api_key: your api key
        :param timeout: timeout in seconds
        :param payload: the request body, as detailed here: https://beta.openai.com/docs/api-reference
        """
        async with httpx.AsyncClient() as client:
            return await client.post(
                url=endpoint_url,
                json=payload,
                headers={"content_type": "application/json", "Authorization": f"Bearer {api_key}"},
                timeout=timeout,
            )

    return send_to_openai


complete = _send_to_openai("https://api.openai.com/v1/completions")
generate_img = _send_to_openai("https://api.openai.com/v1/images/generations")
embeddings = _send_to_openai("https://api.openai.com/v1/embeddings")
chat_complete = _send_to_openai("https://api.openai.com/v1/chat/completions")
