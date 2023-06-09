#nesting

travel_log ={
    "USA": "NYC",
    "Portugal": {"cities_visited":["Lisbon", "Porto", "Algarve"], "total": 3} ,
    "Luxemburg": "Luxemburg",
    "Italy": ["Cagliari", "Olbia", "Sedilo"],
    "Argentina" : ["Buenos Aires", "El Calaffate"]
}

#nesting dictionary in a list

travel_log =[
    {
        "Country" : "USA",
        "cities_visited" : "NYC"
    },
    {
        "Country" : "Portugal",
        "cities_visited": ["Lisbon", "Porto", "Algarve"], 
        "total": 3 
    },
    {
        "Country": "Luxemburg",
        "cities_visited": "Luxemburg"
    },
    {
        "Country": "Italy",
        "cities_visited": ["Cagliari", "Olbia", "Sedilo"]
    },
    {
        "Country": "Argentina" 
        "cities_visited": ["Buenos Aires", "El Calaffate"]
    }
]
