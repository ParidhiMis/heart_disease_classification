from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from model.logistic_model import predict_heart

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class HeartInput(BaseModel):
    age: float = Field(..., ge=1, le=120)
    sex: int = Field(..., ge=0, le=1)
    cp: int = Field(..., ge=0, le=3)
    trestbps: float = Field(..., ge=50, le=250)
    chol: float = Field(..., ge=50, le=700)
    fbs: int = Field(..., ge=0, le=1)
    restecg: int = Field(..., ge=0, le=2)
    thalach: float = Field(..., ge=50, le=250)
    exang: int = Field(..., ge=0, le=1)
    oldpeak: float = Field(..., ge=0, le=10)
    slope: int = Field(..., ge=0, le=2)
    ca: int = Field(..., ge=0, le=4)
    thal: int = Field(..., ge=0, le=3)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, result: str = None):
    # result is read from URL query like /?result=xxx
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result}
    )


@app.post("/predict")
async def predict(
    request: Request,
    age: float = Form(...),
    sex: int = Form(...),
    cp: int = Form(...),
    trestbps: float = Form(...),
    chol: float = Form(...),
    fbs: int = Form(...),
    restecg: int = Form(...),
    thalach: float = Form(...),
    exang: int = Form(...),
    oldpeak: float = Form(...),
    slope: int = Form(...),
    ca: int = Form(...),
    thal: int = Form(...)
):

    validated = HeartInput(
        age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol,
        fbs=fbs, restecg=restecg, thalach=thalach, exang=exang,
        oldpeak=oldpeak, slope=slope, ca=ca, thal=thal
    )

    features = [
        validated.age, validated.sex, validated.cp, validated.trestbps,
        validated.chol, validated.fbs, validated.restecg, validated.thalach,
        validated.exang, validated.oldpeak, validated.slope, validated.ca,
        validated.thal
    ]

    pred = predict_heart(features)

    result_text = (
        "❤️ Heart Disease Detected (High Risk)" if pred == 1
        else "💚 No Heart Disease Detected (Low Risk)"
    )

    return RedirectResponse(
        url=f"/?result={result_text}",
        status_code=303
    )
