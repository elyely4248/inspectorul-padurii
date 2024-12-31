
#%%


### this extracts data from inspectorul padurii for harti STAT 
### it divides romania into 10 rectangles - had problems with the 3rd one due to too much data,
### I extracted the 3rd rectangle data by dividing it into other 5 rectangles in the next jupyter cell


import requests
import json

# Base URL of the API
BASE_URL = "https://inspectorulpadurii.ro/api/layer/harti-amenajistice-stat"

# Function to fetch data for a specific bbox
def fetch_data(bbox):
    url = f"{BASE_URL}?bbox={bbox},urn:ogc:def:crs:EPSG:4326"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Define a large bbox (modify as needed for your region)
rectangles = [
    (43.618682, 20.261906, 44.548316, 24.939314),  # Rectangle 1
    (43.618682, 24.939314, 44.548316, 29.616722),  # Rectangle 2
    (44.548316, 20.261906, 45.47795, 24.939314),   # Rectangle 3
    (44.548316, 24.939314, 45.47795, 29.616722),   # Rectangle 4
    (45.47795, 20.261906, 46.407584, 24.939314),   # Rectangle 5
    (45.47795, 24.939314, 46.407584, 29.616722),   # Rectangle 6
    (46.407584, 20.261906, 47.337218, 24.939314),  # Rectangle 7
    (46.407584, 24.939314, 47.337218, 29.616722),  # Rectangle 8
    (47.337218, 20.261906, 48.266850, 24.939314),  # Rectangle 9
    (47.337218, 24.939314, 48.266850, 29.616722)   # Rectangle 10
]

i=0
for bbox in rectangles:
    # Format the bbox into a string
    bbox_string = f"{bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}"
    data = fetch_data(bbox_string)
    
    if data:
        with open(f"shapes{i}.json", "w") as f:
            json.dump(data, f)
            print("Data saved to shapes.json")
    else:
        print("No data retrieved.")
    
    i+=1


# Save or process data

    
# %%

#getting the third rectangle (index 2 in name of document)
# Original bounding box
lat_min, lon_min, lat_max, lon_max = 44.548316, 20.261906, 45.47795, 24.939314

# Number of rectangles to split into
num_rectangles = 5

# Calculate the height (latitude difference) of each rectangle
lat_diff = lat_max - lat_min
lat_step = lat_diff / num_rectangles

# Generate the 5 smaller bounding boxes
rectangles = []
for i in range(num_rectangles):
    # Calculate the new latitude range for each rectangle
    new_lat_min = lat_min + i * lat_step
    new_lat_max = new_lat_min + lat_step
    
    # Keep the original longitude range the same
    new_lon_min = lon_min
    new_lon_max = lon_max
    
    # Append the new rectangle to the list
    rectangles.append((new_lat_min, new_lon_min, new_lat_max, new_lon_max))
    
    
    
print(rectangles)


i=0
for bbox in rectangles:
    # Format the bbox into a string
    bbox_string = f"{bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}"
    data = fetch_data(bbox_string)
    
    if data:
        with open(f"rectangle_2_div_shapes{i}.json", "w") as f:
            json.dump(data, f)
            print("Data saved to shapes.json")
    else:
        print("No data retrieved.")
    
    i+=1

# %%


import requests
import json

# Base URL of the API
BASE_URL = "https://inspectorulpadurii.ro/api/layer/harti-amenajistice-privat"
# Function to fetch data for a specific bbox
def fetch_data(bbox):
    url = f"{BASE_URL}?bbox={bbox},urn:ogc:def:crs:EPSG:4326"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Define a large bbox (modify as needed for your region)
rectangles = [
    (43.618682, 20.261906, 44.548316, 24.939314),  # Rectangle 1
    (43.618682, 24.939314, 44.548316, 29.616722),  # Rectangle 2
    (44.548316, 20.261906, 45.47795, 24.939314),   # Rectangle 3
    (44.548316, 24.939314, 45.47795, 29.616722),   # Rectangle 4
    (45.47795, 20.261906, 46.407584, 24.939314),   # Rectangle 5
    (45.47795, 24.939314, 46.407584, 29.616722),   # Rectangle 6
    (46.407584, 20.261906, 47.337218, 24.939314),  # Rectangle 7
    (46.407584, 24.939314, 47.337218, 29.616722),  # Rectangle 8
    (47.337218, 20.261906, 48.266850, 24.939314),  # Rectangle 9
    (47.337218, 24.939314, 48.266850, 29.616722)   # Rectangle 10
]

i=0
for bbox in rectangles:
    # Format the bbox into a string
    bbox_string = f"{bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}"
    data = fetch_data(bbox_string)
    
    if data:
        with open(f"privat{i}.json", "w") as f:
            json.dump(data, f)
            print("Data saved to shapes.json")
    else:
        print("No data retrieved.")
    
    i+=1


# Save or process data
# %%
