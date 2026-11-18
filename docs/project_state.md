# DaymaresManagementApp

## Vision

A CRM-style management platform for independent bands and artists.

The application will centralize:

* Contacts and organizations
* Promoters, venues, labels, media, and agents
* Communication history
* Booking pipelines
* Show management
* Follow-up tasks and reminders
* Relationship tracking

---

## Current Architecture

### Backend

* FastAPI
* SQLAlchemy ORM
* SQLite (development)
* PostgreSQL (planned)

### Backend Module Structure

* entities ✅
* tags ✅
* interactions ⏳
* bookings ⏳
* shows ⏳
* tasks ⏳

### Package Structure

```text
app/
├── core/
├── entities/
├── tags/
├── interactions/
├── bookings/
├── shows/
├── tasks/
└── main.py
```

Each module follows:

```text
module/
├── models.py
├── schemas.py
├── service.py
└── routes.py
```

Responsibilities:

* models.py → SQLAlchemy models
* schemas.py → Pydantic DTOs
* service.py → business/database logic
* routes.py → FastAPI endpoints

---

## Entities Module Status

Implemented:

* Entity model
* Entity schemas
* Entity service layer
* Entity routes
* CRUD foundation

Planned entity categories:

* Venue
* Promoter
* Festival
* Label
* Radio Station
* Blog / Media Outlet
* Booking Agent
* Manager
* Band
* Artist
* Photographer
* Videographer
* Other

---

## Tags Module Status

Implemented:

* Tag model
* Tag schemas
* Tag service layer
* Tag routes
* Name normalization strategy
* Unique tag enforcement

* Many-to-many association between entities and tags
* Tag assignment and removal endpoints
* Entity responses include tags
* Entity list can filter by tag ID

Examples:

* promoter
* venue
* media
* booking-priority
* follow-up
* texas
* mexico
* psych-rock

---

## Next Backend Priority

1. Interactions Module
2. Tasks Module
3. Bookings Module
4. Shows Module

---

## Frontend Roadmap

### Guided scheduling

Start with **What would you like to do?** Offer actions such as **Book shows** and **Schedule a photoshoot**, then reveal only the questions relevant to the selection. Use dropdowns for short lists and searchable selectors for cities and venues.

* **One show** — Ask for the city and a date or date range, then let the user choose a venue from the CRM. For example, selecting Austin, TX could display a city map with selectable pins for saved venues alongside a searchable list.
* **Multiple shows** — Ask for an approximate date range and a geographic scope. For a U.S. tour, show selectable city pins on a country map. Let the user add and reorder stops, then choose a venue within each city. Keep the target show count optional so a seven-show tour can start with only a few known stops.
* **Photoshoot** — Ask for a date and time and whether the location is known. Show existing commitments while choosing a time and offer a map when choosing a location.

### Calendar and scheduling conflicts

Show scheduled activities in one calendar, including tentative holds, confirmed commitments, and travel blocks when tour planning is added. Check for overlaps as soon as the user enters a time. Warn about overlapping tentative holds and show a stronger warning that names any conflicting confirmed commitment.

### Build order

1. **First scheduling workflow** — Set up the React frontend and build single-show scheduling with a calendar. Reuse CRM venue records. Let the user pick a venue, hold a date, check for conflicts, and confirm the show.
2. **Venue map and contact management** — Add the venue map as a second way to choose from the same list. Build entity management screens, an entity detail page, and tag management.
3. **Broader scheduling** — Add photoshoot scheduling, the multi-show flow with city maps and travel blocks, and a booking pipeline board. Build the interaction timeline and task dashboard as their backend modules become available.
4. **Later additions** — Reporting and broader search and filtering.

---

## Long-Term Goals

* PostgreSQL migration
* Authentication and user accounts
* Multi-band support
* Email integration
* Calendar integration
* Automated follow-up reminders
* Analytics and relationship insights
* Deployment to cloud infrastructure

