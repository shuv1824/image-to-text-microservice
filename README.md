# Image to Text OCR Web Application

A FastAPI-based web application that extracts text from images using Optical Character Recognition (OCR) powered by Tesseract.

## Features

- **OCR Text Extraction**: Upload images and extract text using Tesseract OCR
- **REST API**: Clean API endpoints for programmatic access
- **Web Interface**: Simple HTML interface for manual image uploads
- **Authentication**: Bearer token authentication for API security
- **Image Echo**: Optional endpoint to echo back uploaded images
- **Docker Support**: Containerized deployment ready
- **Configurable Settings**: Environment-based configuration

## Prerequisites

- Python 3.10+
- Tesseract OCR engine
- Docker (optional, for containerized deployment)

## Installation

### Local Development

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd image-to-text
   ```

2. **Install system dependencies**

   ```bash
   # On Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install tesseract-ocr

   # On macOS
   brew install tesseract
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

5. **Run the application**

   ```bash
   uvicorn app.main:app --reload
   ```

### Docker Deployment

1. **Build the Docker image**

   ```bash
   docker build -t image-to-text .
   ```

2. **Run the container**

   ```bash
   docker run -p 8000:8000 -e APP_AUTH_TOKEN=your-secret-token image-to-text
   ```

## Configuration

Configure the application using environment variables:

| Variable         | Description                         | Default  |
| ---------------- | ----------------------------------- | -------- |
| `APP_AUTH_TOKEN` | Authentication token for API access | `secret` |
| `DEBUG`          | Enable debug mode                   | `False`  |
| `ECHO_ACTIVE`    | Enable image echo endpoint          | `False`  |
| `SKIP_AUTH`      | Skip authentication (debug only)    | `False`  |
| `PORT`           | Port for the application            | `8000`   |

## API Endpoints

### GET /

- **Description**: Home page with web interface
- **Response**: HTML page for manual image uploads

### POST /

- **Description**: Extract text from uploaded image
- **Authentication**: Bearer token required
- **Request**: Multipart form data with image file
- **Response**:

  ```json
  {
    "results": ["line1", "line2", "..."],
    "original": "line1\nline2\n..."
  }
  ```

### POST /img-echo/

- **Description**: Echo back uploaded image (if enabled)
- **Authentication**: None required
- **Request**: Multipart form data with image file
- **Response**: Returns the uploaded image file

## Usage Examples

### Using cURL

```bash
# Extract text from image
curl -X POST "http://localhost:8000/" \
  -H "Authorization: Bearer your-secret-token" \
  -F "file=@path/to/your/image.jpg"
```

### Using Python requests

```python
import requests

url = "http://localhost:8000/"
headers = {"Authorization": "Bearer your-secret-token"}
files = {"file": open("image.jpg", "rb")}

response = requests.post(url, headers=headers, files=files)
result = response.json()
print(result["original"])
```

### Using the Web Interface

1. Open your browser to `http://localhost:8000/`
2. Use the web interface to upload images manually

## Supported Image Formats

The application supports common image formats including:

- PNG
- JPEG/JPG
- GIF
- BMP
- TIFF

## Development

### Running Tests

```bash
pytest app/test_endpoints.py
```

### Pre-commit Hooks

This project uses pre-commit hooks for code quality:

```bash
pre-commit install
pre-commit run --all-files
```

### Project Structure

```
image-to-text/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application
│   ├── ocr.py           # OCR utility functions
│   ├── templates/       # HTML templates
│   │   ├── base.html
│   │   └── home.html
│   ├── images/          # Sample images
│   └── test_endpoints.py # API tests
├── Dockerfile           # Container configuration
├── entrypoint.sh        # Docker entrypoint script
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```

## Security Notes

- Always use strong authentication tokens in production
- Set `SKIP_AUTH=False` in production environments
- Consider implementing rate limiting for production deployments
- Validate file types and sizes before processing

## Troubleshooting

### Common Issues

1. **Tesseract not found**: Ensure Tesseract OCR is installed on your system
2. **Authentication errors**: Check that you're using the correct `APP_AUTH_TOKEN`
3. **Image format errors**: Verify the uploaded file is a valid image format
4. **Port conflicts**: Change the port using the `PORT` environment variable

### OCR Quality Tips

- Use high-resolution images for better text recognition
- Ensure good contrast between text and background
- Images with clear, printed text work better than handwritten text
- Consider image preprocessing for better OCR results
