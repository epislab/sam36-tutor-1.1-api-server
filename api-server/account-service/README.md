# Auth Service

A FastAPI-based authentication service.

## Setup

1. Make sure you have Docker and Docker Compose installed
2. Clone this repository
3. Create a `.env` file based on the example provided

## Running the Service

To start the service, run:

```bash
docker-compose up --build
```

The API will be available at:
- API: http://localhost:8888
- Swagger UI: http://localhost:8888/docs
- ReDoc: http://localhost:8888/redoc

## API Endpoints

- GET `/api/` - Welcome message 