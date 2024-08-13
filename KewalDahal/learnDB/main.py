import sqlite3
from tabulate import tabulate  #used to display result in table

def search_by_country(cursor, countryName):
    query = "SELECT * FROM capitals WHERE country LIKE ?"
    cursor.execute(query, (f"%{countryName}%",))
    results = cursor.fetchall()
    return results

def search_by_continent(cursor, continent_name):
    query = "SELECT * FROM capitals WHERE continent LIKE ?"
    cursor.execute(query, (f"%{continent_name}%",))
    results = cursor.fetchall()
    return results

def display_results(results):
    if results:
        headers = ["Country", "Capital", "Continent", "Population"]
        table = tabulate(results, headers, tablefmt="pretty")  #yeah i used gpt to create table
        print(table)
    else:
        print("No results found.")

def main():
    connection = sqlite3.connect('capitals.db')
    cursor = connection.cursor()

    while True:
        print("\n--- Capital Finder ---")
        print("1. Search by Country")
        print("2. Search by Continent")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            countryName = input("Enter the country name: ")
            results = search_by_country(cursor, countryName)
            display_results(results)
        elif choice == '2':
            continent_name = input("Enter the continent name: ")
            results = search_by_continent(cursor, continent_name)
            display_results(results)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    connection.close()

if __name__ == "__main__":
    main()
