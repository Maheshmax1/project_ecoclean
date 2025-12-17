from fastapi import FastAPI
from routers import user, admin, volunteer, event, event_registration, contact_message, temp
from routers.admin_panel import router as admin_panel_router


from db.database import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(admin.router)
app.include_router(volunteer.router)
app.include_router(event.router)
app.include_router(event_registration.router)
app.include_router(contact_message.router)
app.include_router(temp.router)
app.include_router(admin_panel_router)



