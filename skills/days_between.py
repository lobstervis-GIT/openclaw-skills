import sys
from datetime import date

def days_between(d1, d2):
    d1 = date(*map(int, d1.split('-')))
    d2 = date(*map(int, d2.split('-')))
    return abs((d2 - d1).days)

if __name__ == "__main__":
    try:
        date_str = sys.argv[1]
        start_date, end_date = date_str.split(' ')
        print(days_between(start_date, end_date))
    except Exception as e:
        print(f"錯誤: {e}")