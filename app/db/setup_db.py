from app.db.base import metadata, engine
from app.db.models import form_data  # Ensure the table is imported so it's registered with metadata

def setup_database():
    metadata.create_all(engine)
