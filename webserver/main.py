import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI( openapi_url=None, docs_url=None)
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
            return templates.TemplateResponse("access_denied.html", {"request": request})


#@app.get("/wawa")
#async def plots(request: Request):
            #fname = "2022-03-25_HSI_warrants.html"
            #return templates.TemplateResponse("plots.html", {"request": request, "fname": fname})


@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return templates.TemplateResponse("page_does_not_exist.html", {"request": request})


@app.exception_handler(HTTPException)
async def exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("page_does_not_exist.html", {"request": request})



if __name__ == '__main__':
    #uvicorn.run( "main:app", host="0.0.0.0", port=8000, reload=True)
    uvicorn.run( "main:app", host="0.0.0.0", port=8000)




#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

#@app.get("/url-list")
#async def get_all_urls():
    ##url_list = [{"path": route.path, "name": route.name} for route in app.routes]
    #return url_list
    #return {"message": "hello world"}


#@app.get("/{NApath}")
#async def read_item(NApath: str):
    #if f"/{NApath}" not in url_list:
        #print(url_list)
        #print(NApath)
        #print("in Error")
        #raise HTTPException(status_code=404, detail="Item not found")
    #else:
        #print("in redirect")
        #return RedirectResponse( url="/url-list", status_code=302)


#-----------------------------------------------------------------------------------------