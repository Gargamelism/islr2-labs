import csv
from enum import Enum
from typing import List, Dict


class DatasetOptionsEnum(Enum):
    ADVERTISING = 'Advertising'
    AUTO = 'Auto'
    BIKESHARE = 'Bikeshare'
    BOSTON = 'Boston'
    BRAINCANCER = 'BrainCancer'
    CARAVAN = 'Caravan'
    CARSEATS = 'Carseats'
    CH12EX13 = 'Ch12Ex13'
    COLLEGE = 'College'
    CREDIT = 'Credit'
    DEFAULT = 'Default'
    FUND = 'Fund'
    HEART = 'Heart'
    HITTERS = 'Hitters'
    INCOME1 = 'Income1'
    INCOME2 = 'Income2'
    OJ = 'OJ'
    PORTFOLIO = 'Portfolio'
    PUBLICATION = 'Publication'
    SMARKET = 'Smarket'
    WAGE = 'Wage'
    WEEKLY = 'Weekly'


def load_dataset(dataset: DatasetOptionsEnum) -> List[Dict[str, str]]:
    with open(f'../../assets/datasets/{dataset.value}.csv', newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]