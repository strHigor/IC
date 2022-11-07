from fastapi import FastAPI
from methods import convert_csv_to_list, dict_search
from fastapi.middleware.cors import CORSMiddleware

data = convert_csv_to_list("files/Relatorio_cadop.csv")
app = FastAPI()
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"Health": "Running"}

@app.get("/operadoras/{value}")
def search(value: str):
    return dict_search(value,data)