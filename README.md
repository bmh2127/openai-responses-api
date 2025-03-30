# OpenAI Responses API

A Python application that uses OpenAI's API to analyze PDF documents and answer questions about their content. This project demonstrates the use of OpenAI's file analysis capabilities with the GPT-4 model.

## Features

- PDF document analysis using OpenAI's API
- Question-answering capabilities about document content
- Environment variable management for API keys
- Modern Python project structure with uv package manager

## Prerequisites

- Python 3.12 or higher
- OpenAI API key
- PDF documents to analyze
- [uv](https://github.com/astral-sh/uv) package manager (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bmh2127/openai-responses-api.git
cd openai-responses-api
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies using uv:
```bash
uv pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```

## Project Structure

- `main.py`: Main application code for PDF analysis and question answering
- `pyproject.toml`: Project dependencies and metadata
- `uv.lock`: Lock file for dependency versions
- `.env`: Environment variables (not tracked in git)
- `.python-version`: Python version specification
- PDF files: Sample documents for analysis

## Usage

1. Place your PDF file(s) in the project directory
2. Run the main script:
```bash
python main.py
```

The script will:
1. Upload your PDF document to OpenAI
2. Process the document
3. Answer questions about the document's content

## Configuration

The project uses the following environment variables:
- `OPENAI_API_KEY`: Your OpenAI API key

## Dependencies

- openai >= 1.69.0
- python-dotenv >= 1.1.0

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.