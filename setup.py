import setuptools

with open("README.md", "r") as fh:
    _LONG_DESCRIPTION = fh.read()


setuptools.setup(
    name="openai-async",
    license='MIT',
    author="itayzit",
    version="0.0.1",
    author_email="itayzit@gmail.com",
    long_description=_LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/itayzit/openai-async",
    packages=setuptools.find_namespace_packages(),
    install_requires=["httpx", "pytest"],
)