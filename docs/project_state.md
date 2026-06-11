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
* tags ⏳
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

In Progress

Implemented:

* Tag model
* Tag schemas
* Tag service layer
* Tag routes
* Name normalization strategy
* Unique tag enforcement

Planned:

* entity_tags many-to-many relationship table
* Tag assignment endpoints
* Tag removal endpoints
* Tag filtering queries

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

## Current Task

Complete Tags Module

Remaining work:

* entity_tags association table
* Entity ↔ Tag relationships
* Assign tag endpoint
* Remove tag endpoint
* EntityRead tag serialization
* Router registration and testing

---

## Next Backend Priority

1. Interactions Module
2. Tasks Module
3. Bookings Module
4. Shows Module

---

## Frontend Roadmap

Phase 1

* React application setup
* Entity CRUD screens
* Tag management screens
* Entity detail page

Phase 2

* Interaction timeline
* Task dashboard
* Booking pipeline board

Phase 3

* Show calendar
* Reporting
* Search and filtering

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

