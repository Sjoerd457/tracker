import logging
from app.db.base_old import database
from app.db.models import form_data
from datetime import datetime

async def store_form_db(form_dict):
    try:
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
        logging.info(f'Successfully saved in db: {query}')
    except:
        logging.error(f'Failed to save the following query: {query}')