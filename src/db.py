import os
from sqlalchemy import create_engine, MetaData, Table, Column, String, Text, DateTime
from databases import Database
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Database setup
database = Database(DATABASE_URL)
metadata = MetaData()

form_data = Table(
    "form_data",
    metadata,
    Column("clickid", String(50), primary_key=True),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("telephone", String(50)),
    Column("city", String(50)),
    Column("postcode", String(20)),
    Column("country", String(50)),
    Column("address", Text),
    Column("offer_link", Text),
    Column("tracker_url", Text),
    Column("user_agent", Text),
    Column("ip_address", String(50)),
    Column("timestamp", DateTime, default=datetime.utcnow),
)

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)

async def store_form_db(form_dict):
    query = form_data.insert().values(
        clickid=form_dict['clickid'],
        first_name=form_dict['firstName'],
        last_name=form_dict['lastName'],
        telephone=form_dict['telephone'],
        city=form_dict['city'],
        postcode=form_dict['postcode'],
        country=form_dict['country'],
        address=form_dict['address'],
        offer_link=form_dict.get('offer_link', ''),
        tracker_url=form_dict.get('tracker_url', ''),
        user_agent=form_dict.get('user_agent', ''),
        ip_address=form_dict.get('ip_address', ''),
        timestamp=datetime.utcnow()
    )
    await database.execute(query)
    print('Succesfully saved in db')
