from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from urllib.parse import urlencode

app = FastAPI()

SERVER = "http://0.0.0.0:8000/sendOfferLink"

@app.get("/click/")
def simulate_tracker_response(origin: str, request: Request):

    # Mock offer link
    offer_link = "https://example.com/offer?c=1323&a=301"
    
    # Append parameters to the offer link
    redirect_url = f"{SERVER}?offer_link={offer_link}&clickid=1000"
    
    return RedirectResponse(url=redirect_url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)