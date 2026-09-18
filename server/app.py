existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def home():
    """Display the welcome message."""
    return "Welcome to Flatiron Cars!"


@app.route('/<model>')
def model(model):
    """Check whether the requested model exists in our fleet."""
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog."
