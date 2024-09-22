from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Medication
from database import SessionLocal
from services.medication_service import MedicationService
from typing import List
import json

router = APIRouter()
medication_service = MedicationService()

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

@router.get("/", response_model=List[Medication])
def read_medications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    medications = db.query(Medication).offset(skip).limit(limit).all()
    return medications

@router.post("/recognize")
def recognize_medication(detected_pill: dict):
    # Load annotations from the file
    annotations_file = 'path/to/your/annotations.json'  # Update the path as needed
    annotations = medication_service.load_annotations(annotations_file)
    
    # Calculate similarities
    similarities = medication_service.calculate_similarity(detected_pill, annotations)
    
    # Find the best match
    best_match = medication_service.find_best_match(similarities)
    
    if best_match:
        return {"recognized_medication": best_match}
    return {"error": "No matching medication found"}