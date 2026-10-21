
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import folium

df = pd.read_csv("interpreter.csv")

df = df.rename(columns={
    "@lat": "latitude",
    "@lon": "longitude"
})

df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

df = df.dropna(subset=["latitude", "longitude"]).copy()

df["name"] = df["name"].fillna("Unknown place").astype(str)

coordinates = df[["latitude", "longitude"]].to_numpy()
coordinates_rad = np.radians(coordinates)

earth_radius = 6371.0088

model = DBSCAN(
    eps=0.5 / earth_radius,
    min_samples=3,
    metric="haversine"
)

df["cluster"] = model.fit_predict(coordinates_rad)

colors = [
    "blue", "red", "green", "purple",
    "orange", "darkred", "cadetblue", "darkgreen"
]

warangal_map = folium.Map(
    location=[17.99, 79.59],
    zoom_start=13
)

for _, row in df.iterrows():
    if row["cluster"] == -1:
        color = "gray"
        cluster_name = "Noise"
    else:
        color = colors[int(row["cluster"]) % len(colors)]
        cluster_name = f"Cluster {row['cluster']}"

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5,
        popup=f"{row['name']} - {cluster_name}",
        color=color,
        fill=True,
        fill_color=color
    ).add_to(warangal_map)

warangal_map.save("warangal_clusters.html")

print("Warangal map saved successfully!")

print("\nTotal locations:", len(df))
print("\nCluster results:")
print(df["cluster"].value_counts().sort_index())

print("\nLocation details:")
print(df[["name", "latitude", "longitude", "cluster"]].head(20))

plt.figure(figsize=(12, 8))

for cluster in sorted(df["cluster"].unique()):
    cluster_data = df[df["cluster"] == cluster]

    if cluster == -1:
        label = "Noise"
    else:
        label = f"Cluster {cluster}"

    plt.scatter(
        cluster_data["longitude"],
        cluster_data["latitude"],
        label=label,
        s=60
    )

plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Warangal Location Clustering using DBSCAN")
plt.legend()
plt.show()

print("\nPlaces in each cluster:")

for cluster in sorted(df["cluster"].unique()):
    cluster_data = df[df["cluster"] == cluster]

    if cluster == -1:
        print("\nNoise locations:")
    else:
        print(f"\nCluster {cluster}:")

    print(cluster_data["name"].head(10).to_string(index=False))

cluster_summary = df.groupby("cluster").agg(
    total_locations=("name", "count"),
    places=("name", lambda names: ", ".join(
        names.dropna().astype(str).head(10)
    ))
).reset_index()

cluster_summary.to_csv("cluster_summary.csv", index=False)

print("\nCluster summary saved successfully!")
print(cluster_summary)
