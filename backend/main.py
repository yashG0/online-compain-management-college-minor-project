from fastapi import FastAPI
from dotenv import load_dotenv

app: FastAPI = FastAPI(
    title="Online Complaint Management System API",
    description=(
        "A centralized web-based API designed to handle online complaints "
        "for colleges or organizations. The system allows users to register "
        "complaints, track their status, and enables administrators to manage "
        "and resolve grievances efficiently with proper authentication "
        "and role-based access control."
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    contact={
        "name": "MCA Minor Project Team",
        "email": "yashcoder2004@gmail.com",
    },
    license_info={
        "name": "Academic Use Only",
    }
)

load_dotenv()


@app.get("/health")
async def health():
    return {"status": "ok"}
