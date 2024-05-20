from sqlalchemy import Table, Column, String, Text, DateTime
from app.db.base import metadata
from datetime import datetime

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