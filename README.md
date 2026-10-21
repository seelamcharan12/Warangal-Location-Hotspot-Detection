Location Hotspot Detection in Warangal
About the Project
When we look at a city, some places are close to many other places,
while others are more spread out. I built this project to explore that
pattern using real location data from OpenStreetMap.

The project uses DBSCAN, an unsupervised machine learning algorithm,
to group nearby locations in Warangal, Telangana. I also created a
simple scatter plot and an interactive map so the clusters are easier to
explore visually.

This project helped me practise working with real-world location data,
applying clustering, and presenting the results in a useful way.
What This Project Does
- Reads location data containing place names and latitude/longitude.
- Cleans coordinate values and removes records with missing
  coordinates.
- Uses DBSCAN with the Haversine distance metric to group nearby
  locations.
- Labels locations that do not belong to a cluster as noise.
- Creates a Matplotlib plot to compare the detected clusters.
- Generates an interactive Folium map with colour-coded locations.
- Exports a CSV summary of the detected clusters.
Tools and Libraries
- Python --- main programming language
- Pandas --- loading and preparing the dataset
- NumPy --- converting coordinates to radians
- Scikit-learn --- DBSCAN clustering
- Matplotlib --- visualising the clusters
- Folium --- creating the interactive map
- OpenStreetMap --- source of the location data
How the Clustering Works
Latitude and longitude are geographic coordinates, so the project
converts them from degrees to radians before using DBSCAN's Haversine
distance metric.

The current configuration uses:
- eps: approximately 0.5 km
- min_samples: 3
- metric: haversine
In simple terms, DBSCAN looks for locations that are close enough to
form dense groups. Locations that do not fit into a group are marked as
noise (-1).

These settings are the values used in this version of the project.
Different settings may produce different clusters.
Results
With the current dataset and settings, the project produced the
following results:

  Cluster label     Number of locations
  Noise (-1)                       31
  Cluster 0                       1,266
  Cluster 1                           5
  Cluster 2                          28
  Cluster 3                           3
  Total                   1,333

Cluster 0 contains most of the records in this run. This can happen when
nearby dense areas are connected through other nearby points. The result
is specific to the current dataset and DBSCAN settings; it should not be
interpreted as proof that every location in the cluster is one
real-world hotspot.
Output Files
After running the project, these files are created:
- warangal_clusters.html --- interactive map with colour-coded
  cluster markers
- cluster_summary.csv --- summary of the detected clusters and
  example place names
The program also displays a Matplotlib scatter plot and prints cluster
details in the terminal.
How to Run the Project
1. Install the required libraries
python -m pip install pandas numpy matplotlib scikit-learn folium
2. Keep the files together
Place main.py and interpreter.csv in the same project folder. If
your Python file has a different name, use that name in the command
below.
3. Run the script
python main.py
The script should create warangal_clusters.html and
cluster_summary.csv in the working folder.
4. Open the interactive map
If opening the HTML file directly does not work in your browser, start a
local server from the project folder:
python -m http.server 8000
Then open this address in your browser:
http://localhost:8000/warangal_clusters.html
Keep the terminal running while viewing the map. Press Ctrl+C in the
terminal when you want to stop the server.
Project Structure
Location-Hotspot-Detection/
├── main.py
├── interpreter.csv
├── warangal_clusters.html
├── cluster_summary.csv
└── README.md
The HTML and CSV files are generated outputs, so they may appear only
after the script has been run.
What I Learned
While building this project, I got hands-on practice with:
- Cleaning real-world data before applying machine learning.
- Working with latitude and longitude.
- Understanding density-based clustering and noise points.
- Visualising model output in both a plot and an interactive map.
- Saving results in reusable output files.
Limitations and Future Improvements
- The results depend on the locations available in the input dataset
  and the DBSCAN parameters.
- A large cluster may contain several connected local areas, so the
  parameters should be tested with other distance settings.
- The dataset can be updated with more locations and checked for
  duplicates or incomplete place names.
- Future versions could compare multiple eps values and include a
  clearer summary of hotspot areas.
Data Source
Location data was collected from OpenStreetMap. OpenStreetMap data
is made available under the Open Data Commons Open Database License
(ODbL). If you redistribute the dataset or derived data, review the
attribution and licence requirements that apply to your specific export.
Author
Built as a hands-on machine learning project to explore geographic
clustering and interactive data visualisation.
Note: The cluster counts above reflect the current run described in
this README. If you change the dataset or DBSCAN settings, update the
results table accordingly.