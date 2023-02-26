# AirBnB Clone Project
This project is a clone of the AirBnB website that consists of multiple parts, each representing a particular segment of the project.

Repository Structure
models/: This directory contains the implementation of the models that the project uses. It has a separate file for each model, including a base model that all other models inherit from.
tests/: This directory contains the tests that verify the correctness of the implementation of the models.
console.py: This file implements a command line interpreter that allows users to interact with the models via a command-line interface.
README.md: This file contains the documentation for the project.
AUTHORS: This file contains the list of contributors to the project.

## Models

### BaseModel
The BaseModel class serves as the parent class for all other classes in the project. It defines the basic attributes and methods that all other classes use, such as id, created_at, updated_at, and to_dict().

### FileStorage
The FileStorage class is responsible for serializing and deserializing instances of the models to and from a JSON file. It uses a dictionary to store all instances of the models, where the keys are the names of the classes and the IDs of the instances, and the values are the instances themselves.

### User
The User class represents the users of the AirBnB website. It has attributes such as email, password, first_name, and last_name.

### State
The State class represents the states of the United States. It has an attribute name.

### City
The City class represents the cities in a state. It has attributes such as state_id (the ID of the state that the city is in) and name.

### Amenity
The Amenity class represents the amenities that can be provided in a place. It has an attribute name.

### Place
The Place class represents the places that are available for rent on the AirBnB website. It has attributes such as city_id (the ID of the city where the place is located), user_id (the ID of the user who owns the place), name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, and amenity_ids (a list of the IDs of the amenities provided in the place).

### Review
The Review class represents the reviews that users can leave for a place. It has attributes such as place_id (the ID of the place that the review is for), user_id (the ID of the user who left the review), and text (the text of the review).

### Console:
The console is an interactive command-line interface that allows the user to manipulate the objects stored in the JSON files using the classes and methods defined in the project. The console provides the following functionalities:

Create a new object: Creates a new object and saves it to the JSON file.
Show an object: Shows the object with the given ID or class name and ID.
Destroy an object: Deletes the object with the given ID or class name and ID from the JSON file.
All objects: Displays all objects of a specific class or all objects in the JSON file.
Update an object: Updates the attributes of an object with the given ID or class name and ID.
The console can also run non-interactive commands by passing the command as a string argument to the console instance.

### Testing:
The AirBnB clone project uses unittests to test the functionality of its classes and methods. The tests are written in the test_.py files located in the tests/ directory. Each test_ module corresponds to a class defined in the models/ directory, and each test_* module contains test cases for the methods defined in its corresponding class.

The tests use assert methods to check the expected output against the actual output of a method call. For example, to test the to_dict() method of the BaseModel class, a test case might create a new instance of the BaseModel class and call its to_dict() method, then use assertEqual() to compare the expected dictionary representation of the object with the actual dictionary returned by the to_dict() method.

To run the tests, simply navigate to the root directory of the project and run the command python -m unittest discover tests/. This will discover all the test modules in the tests/ directory and run all the test cases defined in them.

To run the tests, execute the following command from the root directory of the project:

sh
Copy code
python3 -m unittest discover tests
Authors
This project was created by [your name]. Please see the AUTHORS file for
