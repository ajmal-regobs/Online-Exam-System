from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Question
from app.schemas import QuestionCreate, QuestionResponse

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.post("/", response_model=QuestionResponse, status_code=201)
def add_question(question: QuestionCreate, db: Session = Depends(get_db)):
    db_question = Question(**question.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


@router.delete("/{question_id}", status_code=200)
def remove_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    db.delete(question)
    db.commit()
    return {"message": f"Question {question_id} deleted successfully"}


@router.get("/", response_model=list[QuestionResponse])
def list_questions(db: Session = Depends(get_db)):
    return db.query(Question).all()
