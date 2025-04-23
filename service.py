from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_persons(db: Session):

    persons_all = db.query(models.Persons).all()
    persons_all = [new_data.to_dict() for new_data in persons_all] if persons_all else persons_all

    res = {
        'persons_all': persons_all,
    }
    return res

async def get_persons_rollnumber(db: Session, rollnumber: int):

    persons_one = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first() 
    persons_one = persons_one.to_dict() if persons_one else persons_one

    res = {
        'persons_one': persons_one,
    }
    return res

async def post_persons(db: Session):
    res = {
    }
    return res

async def put_persons_rollnumber(db: Session, raw_data: schemas.PutPersonsRollnumber):
    rollnumber:str = raw_data.rollnumber
    fullname:str = raw_data.fullname
    age:str = raw_data.age
    profession:str = raw_data.profession


    persons_edited_record = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()
    for key, value in {'rollnumber': rollnumber, 'fullname': fullname, 'age': age, 'profession': profession}.items():
          setattr(persons_edited_record, key, value)
    db.commit()
    db.refresh(persons_edited_record)
    persons_edited_record = persons_edited_record.to_dict() 

    res = {
        'persons_edited_record': persons_edited_record,
    }
    return res

async def delete_persons_rollnumber(db: Session, rollnumber: int):

    persons_deleted = None
    record_to_delete = db.query(models.Persons).filter(models.Persons.rollnumber == rollnumber).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        persons_deleted = record_to_delete.to_dict() 

    res = {
        'persons_deleted': persons_deleted,
    }
    return res

async def get_addresses(db: Session):

    addresses_all = db.query(models.Addresses).all()
    addresses_all = [new_data.to_dict() for new_data in addresses_all] if addresses_all else addresses_all

    res = {
        'addresses_all': addresses_all,
    }
    return res

async def get_addresses_id(db: Session, id: int):

    addresses_one = db.query(models.Addresses).filter(models.Addresses.id == id).first() 
    addresses_one = addresses_one.to_dict() if addresses_one else addresses_one

    res = {
        'addresses_one': addresses_one,
    }
    return res

async def post_addresses(db: Session, raw_data: schemas.PostAddresses):
    city:str = raw_data.city
    state:str = raw_data.state
    country:str = raw_data.country
    postal_code:str = raw_data.postal_code
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at


    record_to_be_added = {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}
    new_addresses = models.Addresses(**record_to_be_added)
    db.add(new_addresses)
    db.commit()
    db.refresh(new_addresses)
    addresses_inserted_record = new_addresses.to_dict()



    boolearn_var: bool = False



    list_big = []  # Creating new list



# Add element to the list 'list_big'
    list_big.insert(0, list_big)


    hello = {}  # Creating new dict



    hello['asdas'] = id
    res = {
        'addresses_inserted_record': addresses_inserted_record,
    }
    return res

async def put_addresses_id(db: Session, raw_data: schemas.PutAddressesId):
    id:str = raw_data.id
    street:str = raw_data.street
    city:str = raw_data.city
    state:str = raw_data.state
    country:str = raw_data.country
    postal_code:str = raw_data.postal_code
    created_at:str = raw_data.created_at
    updated_at:str = raw_data.updated_at


    addresses_edited_record = db.query(models.Addresses).filter(models.Addresses.id == id).first()
    for key, value in {'id': id, 'street': street, 'city': city, 'state': state, 'country': country, 'postal_code': postal_code, 'created_at': created_at, 'updated_at': updated_at}.items():
          setattr(addresses_edited_record, key, value)
    db.commit()
    db.refresh(addresses_edited_record)
    addresses_edited_record = addresses_edited_record.to_dict() 

    res = {
        'addresses_edited_record': addresses_edited_record,
    }
    return res

async def delete_addresses_id(db: Session, id: int):

    addresses_deleted = None
    record_to_delete = db.query(models.Addresses).filter(models.Addresses.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        addresses_deleted = record_to_delete.to_dict() 

    res = {
        'addresses_deleted': addresses_deleted,
    }
    return res

