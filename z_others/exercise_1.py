"""Work History Modeling
    Provided in positions_data is a list of work history positions from a job candidate who wants
    to work at a facility (hospital). We want to create a set of functions that can parse through
     this data.
    Feel free to change the programming language, but you may have to change positions_data based
    on the language you choose.
    After writing code on the left side, you can hit “Run” and your code will run in an interactive
     REPL.

    1. Parse Dates
        Write a function that can parse a string and return a date object.
        Date string format: YYYY-MM-DD
        Invalid or null strings should return null without raising exceptions.
        Use this function to convert the position dates in the positions_data.
        Print the first position’s start date.

    2. Duration
        Write a function that accepts a list of positions and returns a float of the years of
         experience.
        Print the total years of experience for all positions.

    3. Specialty Experience
        Write a function that accepts a list of positions and returns the years of experience
        grouped by specialty.
        For each specialty print it’s years of experience on a new line.
        Print the specialty experience in sorted order going from most experience to least

    4. Identify Gaps
        Write a function that accepts a list of positions and returns a boolean if the positions
         contain gaps.
        A gap is defined as period of time greater than 30 days between two adjacent positions on
         a timeline
        Print the result of this function for all positions
        Print the result of this function for positions excluding “Per Diem RN”

    5. Count Gaps
    Update your gap identify function to return the number of gaps found.
    Print the result of this function for all positions
    Print the result of this function for positions exluding “Travel RN”

---
Start Call
Brendan Blackwood
Frank Ricardo Ramirez"""

from datetime import date, datetime

positions_data = [
    {
        "start_date": "2011-03-15",
        "end_date": "2013-02-11",
        "specialty": "NICU",
        "facility_name": "St Thomas",
        "title": "Staff RN"
    },
    {
        "start_date": "2013-03-20",
        "end_date": "2014-09-01",
        "specialty": "NICU",
        "facility_name": "Memorial Hosptial",
        "title": "Travel RN"
    },
    {
        "start_date": "2014-09-01",
        "end_date": "2015-08-15",
        "specialty": "NICU",
        "facility_name": "St Thomas",
        "title": "Staff RN"
    },
    {
        "start_date": "2015-04-15",
        "end_date": "2018-02-11",
        "specialty": "Urgent Care",
        "facility_name": "Speedy Care",
        "title": "Per Diem RN"
    },
    {
        "start_date": "2015-09-25",
        "end_date": "2019-01-10",
        "specialty": "Dialysis",
        "facility_name": "Duke Hosptial",
        "title": "Staff RN"
    },
    {
        "start_date": "2019-03-15",
        "end_date": "2020-02-11",
        "specialty": "Med-Surg",
        "facility_name": "St Thomas",
        "title": "Travel RN"
    },
    {
        "start_date": "2020-02-10",
        "end_date": None,
        "specialty": "Dialysis",
        "facility_name": "Duke Hosptial",
        "title": "Staff RN"
    }
]


# write code here
def parse_date(date_str: str) -> date or None:
    if not date_str:
        return None

    return datetime.strptime(date_str, '%Y-%m-%d').date()


def get_days(item) -> float:
    start_date = parse_date(item["start_date"])
    end_date = parse_date(item["end_date"]) or date.today()

    return float((end_date - start_date).days)


def main():
    duration = sum([get_days(item) for item in positions_data])

    print(duration)

