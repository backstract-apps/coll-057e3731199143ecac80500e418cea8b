from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/persons/')
async def get_persons(db: Session = Depends(get_db)):
    try:
        return await service.get_persons(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/persons/rollnumber')
async def get_persons_rollnumber(rollnumber: int, db: Session = Depends(get_db)):
    try:
        return await service.get_persons_rollnumber(db, rollnumber)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/persons/')
async def post_persons(db: Session = Depends(get_db)):
    try:
        return await service.post_persons(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/persons/rollnumber/')
async def put_persons_rollnumber(raw_data: schemas.PutPersonsRollnumber, db: Session = Depends(get_db)):
    try:
        return await service.put_persons_rollnumber(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/persons/rollnumber')
async def delete_persons_rollnumber(rollnumber: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_persons_rollnumber(db, rollnumber)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/addresses/')
async def get_addresses(db: Session = Depends(get_db)):
    try:
        return await service.get_addresses(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/addresses/id')
async def get_addresses_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_addresses_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/addresses/')
async def post_addresses(raw_data: schemas.PostAddresses, db: Session = Depends(get_db)):
    try:
        return await service.post_addresses(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/addresses/id/')
async def put_addresses_id(raw_data: schemas.PutAddressesId, db: Session = Depends(get_db)):
    try:
        return await service.put_addresses_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/addresses/id')
async def delete_addresses_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_addresses_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

