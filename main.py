""" A python program that scrapes news articles, classifies their sentiment, and creates a time series of sentiment over time """
import os
import openai

# Set OpenAI API key from environment
openai.api_key = os.environ.get('OPENAI_API_KEY', '')

def classify(query, search_model="ada", model="davinci"):
    openai.Classification.create(
        search_model=search_model,
        model=model,
        examples=[
            [""],
            [""],
            [""],
            [""],
        ],
        query=query,
        labels=[
            "Very Positive",
            "Mostly Positive",
            "Neutral",
            "Mostly Negative"
            "Very Negative",
        ]
    )

if __name__ == "__main__":
    print(openai.Model.list())