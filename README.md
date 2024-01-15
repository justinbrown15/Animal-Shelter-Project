# Title: Animal Shelter MongoDB

## Description:
This Python project provides CRUD (Create, Read, Update, Delete) operations for an Animal collection in MongoDB. It includes a Python library for interacting with the database and a dashboard created using Dash for data visualization.

## Why?:
A way to interact with a vast database and be able to visualize the data in a more digestible way.

## Quick Start:
1. Clone the repository:
      git clone https://github.com/your-username/Animal-Shelter-Project.git
2. Install dependencies:
   pip install -r requirements.txt
3. Run the Jupyter Notebook containing the dashboard code
   jupyter notebook ProjectTwoDashboard(1).ipynb

## Usage

### Using the Animal Shelter Dashboard

1. **Run the Dashboard:**
   - Open the Jupyter Notebook file `ProjectTwoDashboard(1).ipynb` in a Jupyter environment.
   - Execute the cells to run the dashboard.

2. **Interact with the Dashboard:**
   - Explore the data table to view details about animals in the shelter.
   - Use the provided buttons to filter data based on rescue types.
   - Check the interactive pie chart for breed distribution.
   - Explore the geolocation chart to visualize the location of animals on a map.

### AnimalShelter Python Library

If you want to use the Python library (`animal_shelter(1).py`) in your own Python scripts:

1. **Initialize the AnimalShelter Object:**

   from animal_shelter import AnimalShelter

   username = "your-mongodb-username"
   password = "your-mongodb-password"
   shelter = AnimalShelter(username, password)
