from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.workflow import (
    WorkflowCreate,
    WorkflowUpdate,
    WorkflowResponse,
)
from app.services.workflow_service import (
    create_workflow,
    get_all_workflows,
    get_workflow,
    update_workflow,
    delete_workflow,
)

router = APIRouter(
    prefix="/workflows",
    tags=["Workflows"],
)


@router.post(
    "/",
    response_model=WorkflowResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(
    workflow: WorkflowCreate,
    db: Session = Depends(get_db),
):
    return create_workflow(db, workflow)


@router.get(
    "/",
    response_model=list[WorkflowResponse],
)
def read_all(
    db: Session = Depends(get_db),
):
    return get_all_workflows(db)


@router.get(
    "/{workflow_id}",
    response_model=WorkflowResponse,
)
def read_one(
    workflow_id: int,
    db: Session = Depends(get_db),
):
    return get_workflow(db, workflow_id)


@router.put(
    "/{workflow_id}",
    response_model=WorkflowResponse,
)
def update(
    workflow_id: int,
    workflow: WorkflowUpdate,
    db: Session = Depends(get_db),
):
    return update_workflow(
        db,
        workflow_id,
        workflow,
    )


@router.delete(
    "/{workflow_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete(
    workflow_id: int,
    db: Session = Depends(get_db),
):
    delete_workflow(
        db,
        workflow_id,
    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)