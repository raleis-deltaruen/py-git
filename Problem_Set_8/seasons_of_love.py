import inflect
p = inflect.engine()
from datetime import datetime

class Date:
    def __init__(self, time_passed=0):
        self.time_passed = time_passed

    def __str__(self):
        return str(self.time_passed)
    
    @classmethod
    def get(cls, date):
        result = date.split("-")
        year = int(result[0])
        month = int(result[1])
        day = int(result[2])

        date_temp = str(datetime.today()).split("-")
        date_temp_time = date_temp[2].split(" ")[0]
        date_temp[2] = date_temp_time
        
        date_year = int(date_temp[0])
        date_month = int(date_temp[1])
        date_day = int(date_temp[2])

        a = datetime(date_year, date_month, date_day, 0, 0, 0)
        b = datetime(year, month, day, 0, 0, 0)

        days = (a - b).days
        minutes = days * 24 * 60
        time_passed = p.number_to_words(minutes).replace("and ", "") 
        return str(cls(time_passed))

        

        
def main():

    time = Date.get("2024-11-10")
    print(time)

if __name__ == "__main__":
    main()
