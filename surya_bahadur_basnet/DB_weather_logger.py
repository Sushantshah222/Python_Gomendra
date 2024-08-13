from datetime import datetime, date, timedelta 
import time 
import os 
import sqlite3


TABLE_NAME="AAHA_TAMATAR"
MAX_PREV_DAYS=7

FILE_READ_KEYS= {"Temperature": 1, "Humidity": 2}
CMDS = ("add", "view", "analytic", "display", "cls", "exit")
WEATHER_CONDITIONS=("sunny", "rainy", "windy", "snowy")

CMD_MEANING = (
    "Adding new weather records",
    "Viewing today's or previous records",
    "View the trends and patterns in specific weather condition",
    "Displaying of all weather record in a week",
    "clearing screen",
    "Exiting",
)

class LoggerError(RuntimeError):
    def __init__(self, message="Something happened", err="", file_not_found=False):

        super().__init__(message)
        self.message = f"Error Occured: {message}, donkey! \n{f'Error: {err}' if err else ''}"
        self.file_not_found=file_not_found

    def printErr(self):
        print(self.message)

# utils
def clear_screen():
    print('\033[2J\033[1;1H')

def hazzyEffect(sleep_time=0.2):
    time.sleep(sleep_time)

def InputHandler(message, type=str, scope=[], positive=False):
    try:
        user_input = type(input(f"{f"\nOut Of {scope}\n" if scope else ''}{message}"))

        if type==int and positive and not (0< user_input <= 100):
            raise LoggerError("The value must be positive number, greater than 0 and less than or equal to 100")
        if not user_input:
            raise LoggerError(f"The Field mustn't be empty.")

        if scope and user_input not in scope:
            raise LoggerError (f"The input must be one of ", scope)

        return user_input
    except ValueError as e:
        raise LoggerError(f"Value doesn't meet required typing", e)

    except LoggerError as err:
        raise err

    except:
        raise LoggerError("Some other error occured")

# main functions
def add_weather_record():
    try:
        temperature = InputHandler("Enter today's temperature: ", int)
        humidity = InputHandler(message="Enter today's humidity: ", type=int, positive=True)
        weather_condition = InputHandler(message="Enter today's weather's condition: ", scope=WEATHER_CONDITIONS)
        
        cursor.execute(f"""
            INSERT INTO {TABLE_NAME} (DATE, TEMPERATURE, HUMIDITY, CONDITIONS)
            VALUES (?,?,?,?)
        """, (str(date.today()), temperature, humidity, weather_condition)
        )
        connection.commit()

        print("\n Data Insertion in DB Successfully!!!")

    except LoggerError as e:
        e.printErr()

    except:
        print("Some DB thingy error caught...")

def view_record():
    try:
        record_date= InputHandler("Enter the date in format of (YYYY-MM-DD) to view the record for: ")
        # conversion of user record_dat to actual data format for validity of the user input
        datetime.strptime(record_date, "%Y-%m-%d").date()

        cursor.execute(f"""
            SELECT * from {TABLE_NAME} WHERE DATE = ?
""", (record_date,))
        content = cursor.fetchone()

        if (content):
            print('\n')
            print(f"id  {"date":<20}  {"temperature":<30}  humidity ")
            print(f"{content[0]}   {content[1]:<20}     {f"{content[2]}\u00B0C":<30} {content[3]}%")
                

    except ValueError: # date conversion wala...
        print("The record desired to visit seem to have fluk_thua.\nInvalid date format")

    except LoggerError as errInstance:
        errInstance.printErr()

    except:
        print("Uncaught error caught!!!, kudos?!")

# helper for analytics
def temp_hum_value_passer():
    data = []

    try:
        to_date = date.today()
        from_date = to_date - timedelta(days=7)

        cursor.execute(f"""
        SELECT TEMPERATURE, HUMIDITY FROM {TABLE_NAME}
        WHERE DATE BETWEEN ? AND ?
""", (str(from_date), str(to_date)))
        
        data = cursor.fetchall()
        return data

    except LoggerError as err:
        err.printErr()
    except sqlite3.OperationalError as err:
        print(err)
    except Exception as err:
        print("Unexpected error caught!!!, kudos?!")


def show_avg(temperature=True):
    data = temp_hum_value_passer()
    total_temp= 0
    total_hum= 0

    for temp, hum in data:
        total_temp+=temp
        total_hum+=hum

        avg_temp = total_temp/len(data)
        avg_hum = total_hum/len(data)
        
    if temperature:
        print('The Average Temperature was: ', avg_temp)
    else:
        print('The Average Humidity was: ', avg_hum)

def show_max(temperature=True):
    data = temp_hum_value_passer();
    max_value = 0

    idxForCondition = 0 if temperature else 1

    if len(data) == 0:
        print("No records to read from...")
        return
    
    itr_string = "temperature" if temperature else "humidity"

    for certain_pattern in data[idxForCondition]: # certain_pattern is either temperature/humidity value
        if certain_pattern > max_value:
            max_value = certain_pattern
    
    print(f"\nThe max {itr_string} recorded during {MAX_PREV_DAYS}day period was {max_value}{"\u00B0C" if temperature else "%"}");

def show_min(temperature=True):
    data = temp_hum_value_passer();
    min_value = 0
    idxForCondition = 0 if temperature else 1

    if len(data) == 0:
        print("No records to read from...")
        return
    
    itr_string = "temperature" if temperature else "humidity"

    for certain_pattern in data[idxForCondition]: # certain_pattern is either temperature/humidity value
        if certain_pattern < min_value:
            min_value = certain_pattern
    
    print(f"\n The minimum {itr_string} recorded during {MAX_PREV_DAYS}day period was {min_value}{"\u00B0C" if temperature else "%"}");

def analytic():
    try:
        ANALYTIC_CMD = ("avg_temp", "max_temp", "min_temp", "avg_hum", "max_hum", "min_hum" )
        ANALYTIC_CMD_MEANING = ("Average temperature", "Maximum temperature", "Minimum Temperature", "Average Humidity", "Maximum Humidity", "Minimum Humidity" )

        print(f"\n{"Commmand":<20} ==> Respective Command Action ")
        for cmd, cmd_meaning in zip(ANALYTIC_CMD, ANALYTIC_CMD_MEANING):
            print(f"{cmd:<20} ==> {cmd_meaning}")
            hazzyEffect()

        user_choice = input(":> ")

        print('\n')
        if user_choice not in ANALYTIC_CMD:
            print("Invalid Command given, please, try again!")
            return

        match user_choice:
            case "avg_hum":
                show_avg(temperature=False)

            case "min_hum":
                show_min(temperature=False)

            case "max_hum":
                show_max(temperature=False)

            case "avg_temp":
                show_avg()

            case "min_temp":
                show_min()

            case "max_temp":
                show_max()


    except LoggerError as errInstance:
        errInstance.printErr()
    
    except:
        print('Uncaught error caught!!!, kudos?!')

def display_week_record():
    to_date = date.today()
    from_date = to_date - timedelta(days=7) 

    # TODO:
    
    cursor.execute(f"""
        SELECT * FROM {TABLE_NAME}
        WHERE DATE BETWEEN ? AND ?
    """, (str(from_date), str(to_date)))
    
    data = cursor.fetchall()
    if not len(data):
        print("No Previous record found !!!")
    # displaying of week record
    for _id, rec_date, temperature, humidity, condition in data:
        print(f"Id: {_id}")
        print(f"Date: {rec_date}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Condition: {condition}")
        print('-'*40)
        hazzyEffect(0.3)
        
    print('\n')

def main():
    while True:
        _ = input('Press any key for new transaction...')
        clear_screen()

        print(f"{"\nCommands":<{20}}  ==>   Respective Command action\n")
        for cmd, cmdInfo in zip(CMDS, CMD_MEANING): # zip for parallel looping in iterable datatype
            print(f"{cmd:<{20}} ==>   {cmdInfo}")
            hazzyEffect(0.1)
        

        choice = input("\nChoose an option: ")

        if choice not in CMDS:
            print("Invalid Command given, please, try again!")
            continue
        
        match choice:
            case "add":
                add_weather_record()

            case "analytic":
                analytic()

            case "cls":
                clear_screen()

            case "display":
                display_week_record()
            
            case "view":
                view_record()
            
            case "exit":
                print("Exiting", end='')
                for _ in range(6):
                    print('.', end='', flush=True) # flush lea, turunta output print gari halxa, na garea ma data buffer ma basthyo ra antim ma matra output nikalthyo
                    hazzyEffect(0.3)
                return


if __name__ == "__main__":
    dbname = os.getenv("DB_NAME", "weather_thingy.db")

    connection = sqlite3.connect(dbname)
    cursor = connection.cursor()

    try:
        # NOTE: AUTOINCREMENT for only INTEGER, INT ma kam gardaina
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                _id INTEGER PRIMARY KEY AUTOINCREMENT,
                DATE TEXT NOT NULL,
                TEMPERATURE INT NOT NULL,
                HUMIDITY INT NOT NULL,
                CONDITIONS TEXT NOT NULL )
    """)
    except sqlite3.OperationalError as err:
        print(err)

    main()