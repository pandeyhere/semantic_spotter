# Semantic Spotter



Problem Statement - Fans of Paul Graham's essays want a reliable way to ask questions and know whether Paul Graham has made comments on that topic or not. Paul Graham's essays are currently stored as separate documents a folder. Our task is to build a proper Q/A bot using RAG, that the users can interact with and get answers from..

Create and activate a virtual environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

```

Install dependencies:

```
pip3 install -r requirements.txt
```

Set your OpenAI API key as an environment variable:
```
export OPENAI_API_KEY='your_openai_api_key'  # On Windows, use `set OPENAI_API_KEY='your_openai_api_key'`
```

Run the Python App:

```
python3 helpmate.py

```


Give the Input:
```
What is the revenue of uber in 2022?

```
