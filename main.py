"""
Todo:
1. Create database via docker-compose
2. Save data into database
3. 
"""

import httpx
import asyncio
from fastapi import FastAPI, Request, Form, BackgroundTasks, Query
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Setup CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for simplicity; restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Mount the assets directory to serve static files
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

# In-memory storage to simulate tracking and offer link sharing
offer_link_storage = {}
event_storage = {}

async def visit_tracker(tracker_url):
    """
    
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(tracker_url, follow_redirects=True)

@app.get("/sendOfferLink/")
async def extract_link(request: Request, clickid: str = Query(...)):
    """
    Extract the offer link for the given clickid.
    """
    request_params = dict(request.query_params)
    request_params.pop('clickid', None)  # Remove clickid from the parameters
    offer_link = request_params.pop('offer_link', None)  # Remove offer_link from the parameters

    if not offer_link:
        return JSONResponse(content={"error": "Missing offer_link parameter"}, status_code=400)
    
    offer_link += '&'.join(f"{key}={value}" for key, value in request_params.items())

    if clickid in event_storage:
        offer_link_storage[clickid] = offer_link
        event_storage[clickid].set()
        print(f"Click_id: {clickid} with offer link: {offer_link}")
    else:
        print("Error in extract_link")


@app.post("/click/")
async def handle_click(request: Request):
    form_data = await request.form()
    form_dict = dict(form_data)
    print("Form data received:", form_dict)
    
    # tracker_url = form_dict.get('trackerUrl')
    tracker_url = "http://0.0.0.0:8001/click/?origin=123"
    clickid = form_dict.get('clickid')

    if not clickid:
        raise ValueError("clickid is empty")

    # Create an event for this click_id
    event_storage[clickid] = asyncio.Event()
    asyncio.create_task(visit_tracker(tracker_url))

    # Wait for the event to be set by the visit_tracker function
    await event_storage[clickid].wait()
    
    # Now /sendOfferLink will be visited by the created client, 
    # Once the offerlink is extracted we will respond to the post of the real-client
    offer_link = offer_link_storage.pop(clickid, "https://example.com/fallback")
    print(offer_link)
    response_data = {
        "redirect": offer_link,
        "errors": []  # No errors in this mock response
    }
    return JSONResponse(content=response_data)


@app.get("/")
async def serve_index():
    return FileResponse("index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
