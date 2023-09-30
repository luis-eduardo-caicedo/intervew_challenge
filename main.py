from fastapi import FastAPI, status, Depends
from sqlalchemy.orm import Session
from database import engine, session
import models.models as models
import models.schemas as schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_session():
    connection = session
    try:
        yield connection
    finally:
        connection.close()


@app.get("/api/v1/list/user", status_code=status.HTTP_200_OK)
def list_users():
    results = session.query(models.User).all()
    return {"data": results}


@app.get("/api/v1/list/countrys", status_code=status.HTTP_200_OK)
def list_countrys():
    addresses = session.query(models.Address.country).all()
    countries = []
    for address in addresses:
        country = address.country
        if country not in countries:
            countries.append(country)
    return {"data": countries}


@app.post("/api/v1/list/user_country/", status_code=status.HTTP_200_OK)
def list_user_country(name_country: schemas.AddressByCity):
    list_user = []
    country = name_country.country
    addresses = (
        session.query(models.Address).filter(models.Address.country == country).all()
    )
    for addres_id in addresses:
        user = (
            session.query(models.User)
            .filter(models.User.address_id == addres_id.id)
            .first()
        )
        json = {
            "id_user": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "address_id": user.id,
            "address_1": addres_id.address_1,
            "address_2": addres_id.address_2,
            "city": addres_id.city,
            "state": addres_id.state,
            "zip": addres_id.zip,
            "country": addres_id.country,
        }
        list_user.append(json)

    return {"data": list_user}


@app.post("/api/v1/create/user", status_code=status.HTTP_201_CREATED)
def saved_user(user: schemas.UserCreate, connection: Session = Depends(get_session)):
    address = models.Address(
        address_1=user.address_1,
        address_2=user.address_2,
        city=user.city,
        state=user.state,
        zip=user.zip,
        country=user.country,
    )

    connection.add(address)
    connection.commit()
    connection.refresh(address)

    users = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password,
        address_id=address.id,
    )

    connection.add(users)
    connection.commit()
    connection.refresh(users)
    return {"data": users}
