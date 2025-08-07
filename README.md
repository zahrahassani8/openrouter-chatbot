# Chatbot with FastAPI and Bootstrap

This is a simple AI chatbot web app built with FastAPI backend and a Bootstrap-based frontend. It connects to the OpenRouter API using the Mistral 7B model to generate responses.

## Features

- Real-time chat interface with user and bot messages styled differently
- Copy and edit buttons on user messages for convenience
- Responsive UI with modern look using Bootstrap and custom CSS
- Uses OpenRouter API (Mistral 7B instruct model) for AI responses

## Prerequisites

- Python 3.8+
- An OpenRouter API key (set in `.env` as `OPENROUTER_API_KEY`)

## Setup

1. Clone this repository

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
