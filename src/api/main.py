from fastapi import FastAPI

from src.api.routes.query_routes import (
    router as query_router
)

from src.api.routes.analytics_routes import (
    router as analytics_router
)

from src.api.routes.session_routes import (
    router as session_router
)

from src.api.routes.upload_routes import (
    router as upload_router
)

from src.api.routes.investigator_routes import (
    router as investigator_router
)

app = FastAPI(

    title="Investigator AI",

    version="1.0.0"
)

app.include_router(

    query_router,

    prefix="/query",

    tags=["Query"]
)

app.include_router(

    analytics_router,

    prefix="/analytics",

    tags=["Analytics"]
)

app.include_router(

    session_router,

    prefix="/session",

    tags=["Session"]
)

app.include_router(

    upload_router,

    prefix="/upload",

    tags=["Upload"]
)

app.include_router(
    investigator_router,
    prefix="/investigator",
    tags=["Investigator"]
)


@app.get("/")
def root():

    return {

        "application":
            "Investigator AI",

        "status":
            "running"
    }