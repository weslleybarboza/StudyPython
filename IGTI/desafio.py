import pandas as pd

path = "D:\\Projects\\Weslley\\StudyPython\\IGTI\\sources\\users.csv"
cities = pd.read_csv(path)
cities.head(10)
type(cities)


class MapaPaisContinente():
    def __init__(self) -> None:
        self.mapeamento_continente = {}
    
    def mapear(self, country, region):
        df = pd.DataFrame()
        df["country"] = country
        df["region"] = region
        print(df)
    