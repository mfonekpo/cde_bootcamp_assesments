# Individual Assignment
You have been hired as a new Data Engineer at CoreDataEngineers. The CoreDataEngineers infrastructure is based on the Linux Operating System. Your manager has tasked you with the responsibility of managing the company’s data infrastructure and version control tool.

1. Your manager has assigned you the task of building a **Bash** script (use only bash scripting) that performs a simple ETL process:

   - **Extract:** Download a CSV file. You can access the CSV using this [link](https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv). Save it into a folder called `raw`. Your script should confirm that the file has been saved in the `raw` folder.
   
   - **Transform:** After downloading the file, perform a simple transformation by renaming the column named `Variable_code` to `variable_code`. Then, select only the following columns: `year, Value, Units, variable_code`. Save the content of these selected columns into a file named `2023_year_finance.csv`. This file should be saved in a folder called `Transformed`, your Bash script should confirm that it was loaded into the folder.
   
   - **Load:** Load the transformed data into a directory named `Gold`. Also, confirm that the file has been saved in the folder.

   Note: Use environment variables for the URL, and call it in your script. Write a well-detailed script, add sufficient comments to the script, and print out information for each step.

2. Your manager has asked you to schedule the script to run daily using cron jobs (research this). Schedule the script to run every day at 12:00 AM.

3. Write a Bash script to move all CSV and JSON files from one folder to another folder named `json_and_CSV`. Use any JSON and CSV of your choice; the script should be able to work with one or more JSON and CSV files. 

4. CoreDataEngineers is diversifying into the sales of goods and services. To understand the market, your organisation needs to analyse their competitor, `Parch and Posey`. Download the CSV file using this [link](https://we.tl/t-2xYLL816Yt) to your local PC. After downloading, do the following:

   - Write a Bash script that iterates over and copies each of the CSV files into a PostgreSQL database (name the database `posey`).
   
   - After this, write SQL scripts with detailed comments to answer the following questions posed by your manager (Ayoola):
   
     - /* Find a list of order IDs where either `gloss_qty` or `poster_qty` is greater than 4000. Only include the `id` field in the resulting table. */
     
     - /* Write a query that returns a list of orders where the `standard_qty` is zero and either the `gloss_qty` or `poster_qty` is over 1000. */
     
     - /* Find all the company names that start with a 'C' or 'W', and where the primary contact contains 'ana' or 'Ana', but does not contain 'eana'. */
     
     - /* Provide a table that shows the region for each sales rep along with their associated accounts. Your final table should include three columns: the region name, the sales rep name, and the account name. Sort the accounts alphabetically (A-Z) by account name. */

Document the solutions to these questions using a well-detailed GitHub README file. Upload all scripts into a folder named `Scripts`. Inside the `Scripts` folder, create separate folders to store the Bash scripts and SQL scripts. 

Push all work to GitHub (do not push the CSV files). Ensure that you do not push directly to the master branch but instead merge to master via a pull request (you should know what to do). 

Additionally, create an architectural diagram of the ETL pipeline as requested by your manager.

**N.B**: Students will be picked at random to review what they have done. So, ensure you do not use AI, else your assignment will be marked as Zero.


## Group Assignment 
For this, you will work in groups (which are the already created Circle Groups by the CDE Team). Design a PowerPoint with any insight that you got from the Posey database tables, do an exploratory analysis on the tables and come up with a Presentation for your manager. Give your group a name and choose a single person's GitHub account to document your insights (as images and text) and also to upload your PowerPoint files (all members are to contribute to the repository, through pull requests i.e each member should have different branches) 


**N.B** Both Personal and Group Assignments are due in 1 week and two days  (Wednesday, the **10th** of September 2025)
Submit the personal assignment(for the email section, use the Email used to register for the Bootcamp) with this [Assignment Submission Link](https://docs.google.com/forms/d/1JCEsUXK1qYxQIl3xCcm3BbW3sYkx4GzBIPgPHLtSGw8/edit). 
And the group with this [Group Submission Link](https://docs.google.com/forms/d/1JCEsUXK1qYxQIl3xCcm3BbW3sYkx4GzBIPgPHLtSGw8/edit)

I wish you all Goodluck.

---------------

# SOLUTION

This section is dedicated to the solution of the assignment.
The solutions are subdivided into question numbers.

## Question 1 - ETL Process
To run this ETL process, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the `assignment_2/question1` directory.
3. Run ```chmod +x etl.sh``` to make the bash script executable on your terminal.
4. Run ```./etl.sh``` to run the bash script.
5. The script will download the CSV file, transform it, and load it into the `Gold` directory as per requirement.

**Here is a sample log once the code is run:**
```log
ETL Process initialized...
Extraction Phase Started
Creating download directory 'raw'
Downloading datafile from url:
Download complete.
Extraction phase completed. survey.csv data file saved to directory
File exists
Begin Transformation Phase
Tranformation Phase Started
columns renamed from 'Variable_code' to 'variable_code'
File exists
Begin Loading Phase
Loading phase Started
File exists
ETL Process completed.
```

--------

## Question 2 - Cron Job
To schedule the script to run daily at 12:00 AM, follow these steps:

1. Open the terminal.
2. Type `crontab -e` to edit the crontab file.
3. Add the following line to the crontab file:
```bash
0 0 * * * /bin/bash /path/to/etl.sh
```
4. Save and exit the crontab file.
5. The script will now run daily at 12:00 AM as per requirement.

### NOTE:
- In scenarios you are asked to ```select-editor``` ensure you select the option >> ```  1. /bin/nano        <---- easiest```. This makes it easier to run the Cron job.
- Use ```sudo cat /var/log/syslog | grep CRON``` to check if the cron job is running as per requirement.

**Here is a sample log once the cron job is scheduled:**
```log
CRON[262911]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)
```
--------

## Question 3 - Move CSV and JSON files
To move all CSV and JSON files from one folder to another folder named `json_and_CSV`, follow these steps:

1. Open the terminal.
2. Ensure you type ```chmod +x filemove.sh``` to make the bash script executable.
3. Type ```./filemove.sh``` to run the bash script.
4. The files will now be moved to the `json_and_CSV` folder as per requirement.

**Here is a sample log once the code is run:**
```log
File move process initialized...
moving file to designated location...
File move process completed.
```

