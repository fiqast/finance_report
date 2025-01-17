Student Financial Report
Project Description
The Student Financial Report project is a web application built with Flask that is used to manage and record financial transactions, both income and expenses, made by students. This application provides features to:

- Add Transactions: Record either income or expenses, categorized according to their type.
- View Financial Reports: Display reports in the form of tables and graphs (pie charts) showing income and expenses by month.
- Transaction Categories: Users can select predefined categories or create custom categories for their transactions.
- Balance: Automatically calculate the balance based on recorded income and expenses.
The application is also equipped with interactive data visualizations to provide a clear overview of the student's finances.

Features
1. Transaction Recording: Add income and expense transactions.
2. Transaction Categories: Categories can be selected based on transaction type (Income/Expense), and users can add custom categories.
3. Financial Reports: Display financial reports in table and graph formats.
4. Balance: Calculate balance based on recorded income and expenses.
5. Charts: Present financial data in pie chart format for easy visualization.

Technologies Used
- Flask: Python framework for building the web application.
- MySQL: Database used to store transaction data.
- Chart.js: JavaScript library for creating pie charts.
- HTML, CSS, JavaScript: Used to build the application's front-end interface.

Running the Project
Prerequisites
1. Python 3.x
2. MySQL
3. Flask

Installation
1. Clone this repository to your local machine:
   git clone https://github.com/fiqast/finance_report.git
2. Install dependencies: Make sure you have pip installed, then install Flask and other dependencies by running:
   pip install -r requirements.txt
3. Database Configuration: Ensure that you have created the keuangan_mahasiswa database in MySQL and run the script to create the necessary tables.
4. Run the application: Start the Flask application with the following command:
   python app.py

Folder Structure
- /static: This folder contains CSS and JavaScript files for the layout and interactivity.
- /templates: This folder contains the HTML files used for the application's views.
- app.py: The main file to run the Flask application.

Contributing
If you wish to contribute to this project, feel free to fork this repository, create a new branch, make your changes, and submit a pull request. All contributions are greatly appreciated!



