import math
import re


def cosine_similarity(vec1, vec2):
    dot_product = sum([x * y for x, y in zip(vec1, vec2)])
    norm1 = math.sqrt(sum([x ** 2 for x in vec1]))
    norm2 = math.sqrt(sum([x ** 2 for x in vec2]))
    norm_product = norm1 * norm2
    if norm_product == 0:
        return 0
    else:
        return dot_product / norm_product


def is_image_url(url: str) -> bool:
    return any(re.search(pattern, url, re.IGNORECASE) for pattern in ['.jpg', '.jpeg', '.png', '.gif'])
