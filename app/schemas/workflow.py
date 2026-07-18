from pydantic import BaseModel, Field


class WorkflowCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)


class WorkflowUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=500)


class WorkflowResponse(BaseModel):
    id: int
    name: str
    description: str

    model_config = {
        "from_attributes": True
    }

