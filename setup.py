from setuptools import setup

setup(
    name='onemind-metaplex-api',
    version='1.0',
    packages=['api', 'metaplex'],
    url='https://github.com/metaplex-foundation/python-api',
    license='',
    author=' Metaplex Foundation',
    author_email='',
    description='Process data from Solana / Metaplex',
    install_requires=[
        "anyio==3.3.4",
        "aiohttp==3.8.3",
        "attrs==22.1.0",
        "base58==2.1.1",
        "cachetools==4.2.4",
        "certifi==2022.9.24",
        "cffi==1.15.0",
        "chardet==4.0.0",
        "charset-normalizer==2.1.1",
        "cheroot==8.5.2",
        "CherryPy==18.6.1",
        "construct==2.10.67",
        "cryptography<39,>=38.0.0",
        "ed25519==1.5",
        "h11==0.12.0",
        "httpcore==0.15.0",
        "httpx==0.23.0",
        "idna==3.4",
        "iniconfig==1.1.1",
        "jaraco.classes==3.2.1",
        "jaraco.collections==3.4.0",
        "jaraco.functools==3.3.0",
        "jaraco.text==3.5.1",
        "more-itertools==8.10.0",
        "packaging==21.3",
        "pluggy==1.0.0",
        "portend==3.0.0",
        "py==1.10.0",
        "pycparser==2.20",
        "PyNaCl==1.4.0",
        "pyparsing==3.0.9",
        "pytest==6.2.5",
        "pytz==2022.5",
        "requests==2.28.1",
        "rfc3986==1.5.0",
        "six==1.16.0",
        "sniffio==1.2.0",
        "solana==0.28.1",
        "tempora==4.1.2",
        "toml==0.10.2",
        "typing-extensions==4.2.0",
        "urllib3==1.26.12",
        "websockets==10.4",
        "zc.lockfile==2.0",
    ]
)
