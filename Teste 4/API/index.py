from fastapi import FastAPI
from convert_csv import convert_csv_to_list

data = convert_csv_to_list("files/Relatorio_cadop.csv")
print(data)

app = FastAPI()

@app.get("/")
def health():
    return {"Health": "Running"}