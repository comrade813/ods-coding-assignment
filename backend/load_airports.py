from dotenv import load_dotenv
load_dotenv()

from database import DB
from typing import List, Tuple
from sql import SELECT_ALL_DESTINATION_AIRPORTS, \
                SELECT_ALL_ORIGIN_AIRPORTS, \
                INSERT_ALL_AIRPORTS
from error import DB_WRITE_ERR

db = DB()

airports = dict()
def add_to_airports(data: List[Tuple[str, str]]):
    for abbr, full in data:
        airports[abbr] = full

results = db.read(SELECT_ALL_DESTINATION_AIRPORTS)
add_to_airports(results)

results = db.read(SELECT_ALL_ORIGIN_AIRPORTS)
add_to_airports(results)

try:
    db.write(INSERT_ALL_AIRPORTS, list(airports.items()))
except Exception as e:
    print(DB_WRITE_ERR, e.args[0])