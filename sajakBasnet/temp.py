
import os
from datetime import datetime, timedelta

def current_date():
    return(datetime.now().strftime('%Y-%m-%d'))

def write_read_data_file(filename,mode, temp='', humidity='', conditions=''):
    today_date = current_date()
    if mode == 'w':
        with open(filename, mode) as file:
            file.write(f"Temperature: {temp}°C\n")
            file.write(f"Humidity: {humidity}%\n")
            file.write(f"Conditions: {conditions}\n")
            
        print(f"Weather data saved as {filename}")
        file.close()
            

    else:
        with open(filename, mode) as file:
            content = file.read()
        print(f"Weather data for {filename}:")
        print(content)
        file.close()

def record_weatherr_date():
    mode = 'w'
    today_date = current_date()
    filename = f"{today_date}.txt"

    print("Enter today's weather data: ")
    temperature = input("Temperature (°C): ")
    humidity = input("Humidity (%): ")
    conditions = input("Conditions (e.g., sunny, rainy): ")

    write_read_data_file(filename,mode, temperature, humidity, conditions)

def view_weathere_data():
    mode = 'r'
    files = [f for f in os.listdir() if f.endswith('.txt')]

    if not files:
        print("No weather data found!!")
        return
    
    print("Available weather data: ")
    for file in files:
        print(file)

    selected_file = input("Enter the filename of the weather data you want to view: ")

    if selected_file not in files:
        print("file not foundd")
        return
    
    #read and display (how to do haha use functionn)
    write_read_data_file(selected_file, mode)
    

def calculate_weekly_trends():
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    
    total_temperature = 0
    count = 0
    
    files = [f for f in os.listdir() if f.endswith('.txt')]
    
    if not files:
        print("No weather data found.")
        return
    
    for file in files:
        file_date = datetime.strptime(file.replace('.txt', ''), '%Y-%m-%d').date()
        
        if week_ago <= file_date <= today: #only files from the last week
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("Temperature:"):
                        temperature_line = line  # The temperature line is identifiead
                        break
                temperature = float(temperature_line.split(": ")[1].replace('°C', '').strip())
                total_temperature += temperature
                count += 1
    
    if count > 0:
        average_temperature = total_temperature / count
        print(f"Average temperature over the last week: {average_temperature:.2f}°C")
    else:
        print("No weather data found for the last week.")
def main():
    while True:
        print("WEATHER APPLICATION:")
        print("1. Record today's weather data")
        print("2. View past weather data")
        print("3. Display weekly trends")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '1':
            record_weatherr_date()
        elif choice == '2':
            view_weathere_data()
        elif choice == '3':
            calculate_weekly_trends()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()