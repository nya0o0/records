import toyplot
import requests
import pandas as pd

class Records:
    def __init__(self, genusKey=None, year=None):
        # store input params
        self.genusKey = genusKey
        self.year = year
        self.df = None  # DataFrame to store results
        self.json = None  # JSON dictionary to store results
        self.base_url = "https://api.gbif.org/v1/occurrence/search"  # GBIF API endpoint

        # will be used to store output results
        self.df = None
        self.json = None

    def get_single_batch(self, offset=0, limit=20):
        "returns JSON result for a small batch query"
        # Set the parameter dictionary
        params = {
            "genusKey": self.genusKey,
            "year": self.year,
            "offset": offset,
            "limit": limit
        }
        # create a Response instance
        response = requests.get(self.base_url, params=params)

        # Check whether the request worked
        if response.status_code == 200:
            return response.json() # Return the JSON result
        else:
            response.raise_for_status()

    def get_all_records(self):
        "stores result for all records to self.json and self.df"
        # For storing results
        alldata = []
        offset = 0
        max_limit = 300  # Maximum allowed by GBIF API per request

        while True:
            # Get JASON for one search
            batch = self.get_single_batch(offset=offset, limit=max_limit)

            offset += max_limit  # Move to the next batch
            alldata.extend(batch["results"])

            # stop when end of record is reached
            if batch["endOfRecords"]:
                print(f'Done. Found {len(alldata)} records')
                break
            # print a dot on each rep to show progress
            print('.', end='')
            
        # Store results in instance variables
        self.json = alldata
        self.df = pd.DataFrame(alldata) if alldata else pd.DataFrame()