from fastapi import FastAPI, Path

app = FastAPI()

launches = {
    1:{
        "Mission Name": "CRS-2",
        "Vehicle Name": "Falcon 9",
        "Mission Date": "15-08-2021",
        "Mission Status": "Pending"
    },
    2:{
        "Mission Name": "GPS-III",
        "Vehicle Name": "Falcon 9",
        "Mission Date": "30-08-2021",
        "Mission Status": "Pending"
    },
    3:{
        "Mission Name": "CRS-3",
        "Vehicle Name": "Falcon 9",
        "Mission Date": "21-08-2021",
        "Mission Status": "Pending"
    },
    4:{
        "Mission Name": "DART",
        "Vehicle Name": "Ariane 5",
        "Mission Date": "3-08-2021",
        "Mission Status": "Successful"
    },
    5:{
        "Mission Name": "CRS-2",
        "Vehicle Name": "Falcon 9",
        "Mission Date": "15-08-2021",
        "Mission Status": "Pending"
    },
    6:{
        "Mission Name": "CRS-2",
        "Vehicle Name": "Falcon 9",
        "Mission Date": "15-08-2021",
        "Mission Status": "Pending"
    }
}

@app.get('/')
def home():
    return {"data": "Welcome Home"}

@app.get('/launches/{launch_id}')
def get_launches(launch_id: int = Path(None, description="The ID of the Launch you are looking for", gt=0)):
    return launches[launch_id]

@app.get('/vehicles')
def get_vehicles(vehicle_name: str):
    results = []
    for launch in launches:
        if launches[launch]["Vehicle Name"] == vehicle_name:
            results.append({launch: launches[launch]})
    if len(results) == 0:
        results = "Vehicle Not Found"
    return {"data": results}
