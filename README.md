# SmartDocSearch

A FastAPI-based RAG (Retrieval-Augmented Generation) application that enables users to upload PDF documents and ask questions about their content. The application uses LangChain, ChromaDB for vector storage, and Google's Gemini 1.5 Flash model for generating responses.

## Features

- PDF document upload and processing
- Text extraction and chunking
- Vector storage using ChromaDB
- Question answering using RAG architecture
- FastAPI-based REST API endpoints
- Google Gemini 1.5 Flash integration
- HuggingFace embeddings

## Prerequisites

- Python 3.10 or higher
- Environment variables configured (especially for Google Gemini API access)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/glitchySid/SmartDocSearch.git
cd SmartDocSearch
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r pyproject.toml
```

## Project Structure

```
└── glitchySid-SmartDocSearch/
    ├── README.md
    ├── pyproject.toml          # Project configuration and dependencies
    ├── .python-version        # Python version specification
    ├── persistent/            # ChromaDB persistence directory
    └── src/
        └── langchainproject2/
            ├── api/           # API endpoints
            ├── chains/        # RAG chain implementation
            ├── models/        # LLM and embeddings configuration
            └── utils/         # Utility functions
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
LANGCHAIN_TRACING_V2=your_langchain_tracing_v2_key_here
LANGCHAIN_ENDPOINT=your_langchain_endpoint_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_PROJECT=your_langchain_project_here
TOKENIZERS_PARALLELISM=false
```

## API Endpoints

### Upload PDF
```
POST /uploadfile/
```
- Accepts PDF files for processing
- Extracts text, splits into chunks, and stores in vector database
- Returns success message or error details

### Question Answering
```
GET /output/{question}
```
- Parameter: `question` (string) - Your question about the uploaded document
- Returns: JSON response with the answer based on the document content

## Components

### Vector Store
- Uses ChromaDB for storing document embeddings
- Persistent storage in `./persistent` directory
- HuggingFace embeddings for vector generation

### Text Processing
- PDF text extraction using `pdfplumber`
- Text splitting using `RecursiveCharacterTextSplitter`
- Chunk size: 1000 characters
- Chunk overlap: 200 characters

### LLM Integration
- Uses Google's Gemini 1.5 Flash model
- RAG implementation with LangChain
- Prompt template from LangChain Hub ("rlm/rag-prompt")

## Usage

1. Start the FastAPI server:
```bash
uvicorn langchainproject2:app --reload
```

2. Upload a PDF document:
```bash
curl -X POST -F "file=@your_document.pdf" http://localhost:8000/uploadfile/
```

3. Ask questions about the document:
```bash
curl "http://localhost:8000/output/what%20is%20this%20document%20about"
```

## Development

The project uses modern Python packaging with `pyproject.toml`. Key dependencies include:
- langchain and related packages (chroma, google-genai, etc.)
- FastAPI for the web API
- pypdf and pdfplumber for PDF processing
- python-dotenv for environment management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Author

glitchySid (siddheshmhatre2005@gmail.com)
