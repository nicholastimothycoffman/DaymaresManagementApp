# Daymares Manager

A CRM API for independent bands and artists to organize contacts such as venues, promoters, labels, and booking agents. The current backend supports contact and tag management with FastAPI, SQLAlchemy, and SQLite.

## Run locally

From the repository root with Python 3.12:

```sh
cd backend
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open [the interactive API docs](http://127.0.0.1:8000/docs) to try the tagging workflow.

1. Create a contact with `POST /entities/`. Use a body such as `{"name":"Example Venue","entity_type":"venue"}`.
2. Create a tag with `POST /tags/`. Use a body such as `{"name":"booking-priority"}`.
3. Use the returned IDs with `PUT /entities/{entity_id}/tags/{tag_id}`. The contact response includes its tags.
4. Filter contacts with `GET /entities/?tag_id={tag_id}`.
5. Remove the assignment with `DELETE /entities/{entity_id}/tags/{tag_id}`. The tag stays available for other contacts.
