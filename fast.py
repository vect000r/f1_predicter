from graph import *
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


def fast():
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    templates = Jinja2Templates(directory="templates")

    @app.get("/", response_class=HTMLResponse)
    async def plot_view(request: Request):
        return templates.TemplateResponse("index.html", {"request": request, "driver_plot_image": plot_graph(driver_data), "constructor_plot_image": plot_graph(constructor_data)})
    return app
