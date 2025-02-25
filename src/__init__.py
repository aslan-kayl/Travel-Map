from fastapi import FastAPI
from src.admin_panel.banner.routes import banner_router
from fastapi.staticfiles import StaticFiles

version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix = f"/api/{version}"

app = FastAPI(
    title="Bookly",
    description=description,
    version=version,
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(banner_router, prefix=f"/api/{version}/banner", tags=["banner"])
