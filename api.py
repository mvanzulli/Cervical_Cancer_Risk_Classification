from fastapi import FastAPI
from pydantic import BaseModel
from model import infer_output_json

class Item(BaseModel):
    "Item for data validation and serialization"
    Age: int
    Number_of_sexual_partners: float
    First_sexual_intercourse: float
    Num_of_pregnancies: int
    Smokes: int
    Smokes_years: float
    Smokes_packs_year: int
    Hormonal_Contraceptives: int
    Hormonal_Contraceptives_years: float
    IUD: int
    IUD_years: float
    STDs: int
    STDs_number: int
    STDs_condylomatosis: int
    STDs_cervical_condylomatosis: int
    STDs_vaginal_condylomatosis: int
    STDs_vulvo_perineal_condylomatosis: int
    STDs_syphilis: int
    STDs_pelvic_inflammatory_disease: int
    STDs_genital_herpes: int
    STDs_molluscum_contagiosum: int
    STDs_AIDS: int
    STDs_HIV: int
    STDs_Hepatitis_B: int
    STDs_HPV: int
    STDs_Number_of_diagnosis: int
    Dx_Cancer: int
    Dx_CIN: int
    Dx_HPV: int
    Dx: int

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "Hello": "This is an app to predict cervical cancer risk. Vist /docs for more info.",
    }

@app.post("/predict/")
def predict(item: Item):
    prediction = infer_output_json(item.dict())
    return prediction
