# Python Workshop - Gomendra Multiple Campus


## Assignment no 2


#### 1. Journal Entry: 
Write a Python program that allows users to create a daily journal. Each entry should be saved in a text file with the date as the filename. Users should also be able to read and display previous journal entries.

1. **Create a Journal Entry**:

    - The program will prompt the user to write a journal entry.
    - The entry will be saved in a text file named with the current date (e.g., `2024-08-11.txt`).

2. **Read Previous Entries**:

    - The program will list all available journal entries (based on the filenames).
    - The user can select a date, and the program will display the contents of the corresponding journal entry.

#### Output Summary:


- When a user writes a new journal entry, a text file named with the current date is created, containing the entry.
- If the user chooses to read a previous entry, the program will display the contents of the selected date’s journal file.



#### 2. Weather Logger
Task: Create a Python program that records daily weather observations. Users should be able to enter the temperature, humidity, and general weather conditions (e.g., sunny, rainy). Each observation should be saved in a text file with the date as the filename. The program should allow users to view past weather data and display trends over time (e.g., average temperature for the week).



#### Example Output:

1. **Recording Data:**
   - **User inputs:**
     - Date: `2024-08-11`
     - Temperature: `30°C`
     - Humidity: `60%`
     - Conditions: `Sunny`
   - The data is saved in a file named `2024-08-11.txt` with the following content:
   ```yaml
   Date: 2024-08-11
   Temperature: 30°C
   Humidity: 60%
   Conditions: Sunny
   
   
2. Viewing Past Data:
- When the user requests to view weather data for a specific date  `(e.g., 2024-08-11)`, the program reads from the corresponding file and displays the recorded data.

3. Displaying Trends:
- The program might calculate and display trends, like the average temperature over the last week, by reading data from multiple files (e.g., `2024-08-10.txt, 2024-08-09.txt`) and summarizing it for the user.



  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





# Steps of submitting your assignments
This repo represents the assignment done by Gomendra Multiple College BCA Students.

To submit the Python assignment by forking this repository and pushing the individual student's code(name.py or name.ipynb) into a branch created with their own name, follow these steps:

1. Fork this repository by clicking on the "Fork" button at the top right corner of the repository page. This will create a copy of the repository under your GitHub account.

2. Clone the forked repository to your local machine using the following command in your terminal or command prompt:
   ```sh
   https://github.com/Sushantshah222/Python_Gomendra.git
   
3. Navigate to the cloned repository on your local machine:

    ```sh
    cd repository-name
    
4. Create a new branch with the student's name using the following command:

    ```sh
    git checkout -b student-name
5. create a folder of your name.
6. create and open the `name.py` file or `name.ipynb` file in a text editor.
(note: `.ipynb` file is suggested)

7. Solve your assignment in a single python/Jupyter notebook file.

8. Save the changes to the file.

9. Add the modified folder of your name to the staging area using the following command and commit it:
    ```sh
   git add `your name`
   git commit -m" your commit msg" 


10. Push the changes to the forked repository on GitHub using the following command:

    ```sh        
    git push origin student-name

11. Go to the forked repository on your GitHub and you will see a new branch named "student-name". 

12. Click on the "Compare & pull request" button next to the branch name.

13. Review the changes and click on the "Create pull request" button to submit the code for review.


Your Assignment will be approved by looking onto it and feedback will be provided if needed.
Do not use GPT or any AI for the solutions.


