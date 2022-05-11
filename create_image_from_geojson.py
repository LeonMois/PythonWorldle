import geopandas as gpd
import matplotlib.pyplot as plt


def create_countries():
    df = gpd.read_file("countries.geojson")
    for i in range(0, len(df)):
        country = df.loc[[i], "geometry"]
        country_name = df.loc[[i], "ADMIN"]
        country.plot()
        plt.axis("off")
        plt.savefig(f"country_pics/{country_name[i]}.png", bbox_inches='tight')
        plt.clf()


create_countries()
