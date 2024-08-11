# datetime-strptime for date validation,
# date for today's date, timedelta to perform arithmetic to date
from datetime import datetime, date, timedelta 
import time # for hazzy
import os # for path

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

def file_opener(filename, mode):
    storage_dir = f"{os.path.dirname(__file__)}/records"
    try:
        os.mkdir(storage_dir)
    except FileExistsError:
        pass

    try:
        file = open(f"{storage_dir}/{filename}.txt", mode)
        return file

    except FileNotFoundError as err:
        raise LoggerError(f"File Not Found", err, True)

    except IOError as err:
        raise LoggerError(f"I/O error occured", err)

    except:
        raise LoggerError(f"Some other Error Occured")
    
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
    file=None

    try:
        temperature = InputHandler("Enter today's temperature: ", int)
        humidity = InputHandler(message="Enter today's humidity: ", type=int, positive=True)
        weather_condition = InputHandler(message="Enter today's weather's condition: ", scope=WEATHER_CONDITIONS)

        file = file_opener(str(date.today()), 'w')
        file.write(f"""Date: {str(date.today())}
Temperature: {temperature}
Humidity: {humidity}
Conditions: {weather_condition}
    """)

        print("\n File Created Successfully!!!")

    except LoggerError as e:
        e.printErr()

    except:
        print("Some unraised error caught...")

    finally:
        file.close() if file else None

def view_record():
    try:
        record_date= InputHandler("Enter the date in format of (YYYY-MM-DD) to view the record for: ")
        # conversion of user record_dat to actual data format for validity of the user input
        datetime.strptime(record_date, "%Y-%m-%d").date()

        file = file_opener(record_date, 'r')
        content = file.read()
        file.close()

        print('\n')
        print(content)

    except ValueError: # date conversion wala...
        print("The record desired to visit seem to have fluk_thua.\nInvalid date format")

    except LoggerError as errInstance:
        errInstance.printErr()

    except:
        print("Uncaught error caught!!!, kudos?!")

# helper for analytics
def temp_hum_value_passer():
    # could try and get user's range but will bring extra complexity to already complex app
    # for 7 days, hardcoded
    # data format ={
    #  "content": <fileread_content>[],
    #   "temperature": <temperature>[]
    #   "humidity": <humidity>[] 
    # }

    data = {
        "content": [],
        "temperature": [],
        "humidity": []
    }

    try:
        today = date.today()
        file=None

        for prev_day in range(MAX_PREV_DAYS):
            prev_date = today - timedelta(days=prev_day) # get prev-dates

            try:
                file = file_opener(prev_date, 'r')
            except LoggerError as err:
                if err.file_not_found:
                    continue
                else:
                    break

            content = file.read()
            prev_date_temperature=None
            prev_date_humidity=None

            for idx, each_block in enumerate(content.split('\n')):
                if (len(each_block)>1):
                    if (idx == FILE_READ_KEYS.get("Temperature")):
                        prev_date_temperature = each_block.replace("Â°C", '').split(": ")[1]
                    elif (idx == FILE_READ_KEYS.get("Humidity")):
                        prev_date_humidity = each_block.replace("%", '').split(": ")[1]

            data["content"].append(content)
            data["temperature"].append(int(prev_date_temperature))
            data["humidity"].append(int(prev_date_humidity))


        if len(data["content"]) == 0:
            print("No Records found...\n")
        return data

    except LoggerError as err:
        err.printErr()
    except Exception as err:
        print("Unexpected error caught!!!, kudos?!")

    finally:
        file.close() if file else None

def show_avg(temperature=True):
    data = temp_hum_value_passer()
    total_tempOr_hum = 0

    if temperature:
        for temp in data["temperature"]:
            total_tempOr_hum+=temp

        avg_temp = total_tempOr_hum/len(data["temperature"])
        print('The Average Temperature was: ', avg_temp)

    else:
        for hum in data["humidity"]:
            total_tempOr_hum+=hum

        avg_hum = total_tempOr_hum/len(data["humidity"])
        print('The Average Humidity was: ', avg_hum)

def show_max(temperature=True):
    data = temp_hum_value_passer();
    max_Idx = 0
    max_value = 0

    if len(data["content"]) < 0:
        print("No records to read from...")
        return
    
    itr_string = "temperature" if temperature else "humidity"

    for idx, certain_pattern in enumerate(data[itr_string]): # certain_pattern is either temperature/humidity value
        if certain_pattern > max_value:
            max_value = certain_pattern
            max_Idx= idx
    
    print(f"\n The max {itr_string} recorded during {MAX_PREV_DAYS}day period was {max_value}{"\u00B0C" if temperature else "%"}");
    print("\nOther details during that period: ")
    print(data["content"][max_Idx].replace('Â',''))

def show_min(temperature=True):
    data = temp_hum_value_passer();
    min_Idx = 0
    min_value = 0

    if len(data["content"]) < 0:
        print("No records to read from...")
        return
    
    itr_string = "temperature" if temperature else "humidity"

    for idx, certain_pattern in enumerate(data[itr_string]): # certain_pattern is either temperature/humidity value
        if certain_pattern < min_value:
            min_value = certain_pattern
            min_Idx= idx
    
    print(f"\n The minimum {itr_string} recorded during {MAX_PREV_DAYS}day period was {min_value}{"\u00B0C" if temperature else "%"}");
    print("\nOther details during that period: ")
    print(data["content"][min_Idx].replace('Â',''))

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
    today = date.today()
    file=None

    # displaying of week record
    for prev_day in range(MAX_PREV_DAYS):
        prev_date = today - timedelta(days=prev_day)
        try:
            file = file_opener(prev_date, 'r')
            content = file.read()

            print('\n')
            print(content)
            print('-'*40)
            hazzyEffect(0.3)

        except LoggerError as err:
            if err.file_not_found:
                continue
            err.printErr()
        finally: 
            file.close() if file else None


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
    main()