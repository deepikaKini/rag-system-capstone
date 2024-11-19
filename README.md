# Retrieval-Augmented Generation (RAG) System for Academic Notes

This project implements a Retrieval-Augmented Generation (RAG) system designed to assist students by providing concise answers to queries based on both their personal notes and reference materials. It leverages state-of-the-art Natural Language Processing (NLP) techniques, including document embedding, similarity search, and interaction with a large language model (LLM).

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Document Retrieval:** Fetches and embeds documents from a SQLite database.
- **Similarity Search:** Uses FAISS for efficient vector similarity search.
- **Language Generation:** Generates answers using Google's Gemini LLM.
- **Interactive CLI:** Provides a command-line interface for user queries.
- **Modular Design:** Organized code with clear separation of concerns.

## Prerequisites

- Python 3.7 or higher
- SQLite database with student and reference documents
- Google Gemini API access (get it and store in env file)

## Installation

### Create a Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt` should include:**

```text
torch
transformers
faiss-cpu
google-generativeai
python-dotenv
```

### Set Up the SQLite Database:

Ensure you have a SQLite database named `CapstoneV1.db` with the required tables and data.

## Configuration

### Set the Google Gemini API Key:

Create a `.env` file in the project root directory.

```bash
touch .env
```

Add your API key to the `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

**Note:** Replace `your_api_key_here` with your actual API key. **Do not share this key publicly or commit it to version control.**

### Environment Variables:

The script uses the `dotenv` package to load environment variables from the `.env` file.

### Add `.env` to `.gitignore`:

Ensure your `.gitignore` file includes the `.env` file to prevent it from being tracked by version control.

```gitignore
.env
```

## Usage

### Run the Script:

```bash
python rag_system.py
```

### Follow the Prompts:

#### Enter the Topic:

When prompted, enter the topic you want to query.

```
Enter the topic you want to query:
```

#### Ask Questions:

You can now ask questions related to the topic.

```
Enter your query for the topic (or type 'exit' to end):
```

#### Exit the Program:

Type `exit` to end the session.

```
Exiting the RAG system. Goodbye!
```

## Project Structure

- `rag_system.py`: Main script containing the RAG system implementation.
- `CapstoneV1.db`: SQLite database file (not included in the repository).
- `.env`: Environment file containing sensitive configurations (not included in the repository).
- `requirements.txt`: List of Python dependencies.
- `README.md`: Documentation for the project.
- `.gitignore`: Specifies intentionally untracked files to ignore.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with clear messages.
4. Submit a pull request for review.

