from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def read_root():
    return {
		"name": "AI Workflow Builder API",
  		"version": "0.1.0",
		"status": "healthy",
		"docs" : "/docs"
	}