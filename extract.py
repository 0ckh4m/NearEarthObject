"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path="data/neos.csv"):
    """Read near-Earth object information from a CSV file.
    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    neos_collection = []
    with open(neo_csv_path) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            neos_collection.append(NearEarthObject(row[3], row[4], row[15], row[7]))
    return neos_collection


def load_approaches(cad_json_path="data/cad.json"):
    """Read close approach data from a JSON file.
    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    ca_collection = []
    with open(cad_json_path) as file:
        contents = json.load(file)
        for entry in contents["data"]:
            designation = entry[0]
            time = entry[3]
            distance = entry[4]
            velocity = entry[7]
            ca_collection.append(CloseApproach(designation, time, distance, velocity))
    return ca_collection


