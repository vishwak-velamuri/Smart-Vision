from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Medication
from database import SessionLocal

router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Medication)
def create_medication(medication: Medication, db: Session = Depends(get_db)):
    db.add(medication)
    db.commit()
    db.refresh(medication)
    return medication

@router.get("/{medication_id}", response_model=Medication)
def read_medication(medication_id: int, db: Session = Depends(get_db)):
    medication = db.query(Medication).filter(Medication.id == medication_id).first()
    if medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return medication

@router.get("/", response_model=list[Medication])
def read_medications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    medications = db.query(Medication).offset(skip).limit(limit).all()
    return medications