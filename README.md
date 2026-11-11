# Smart Home Pantry Manager 🏠🥫

A comprehensive data management system built with Python and MySQL to track household inventory, manage quantities, and demonstrate robust data pipelines and error handling.

## The Problem
Managing household groceries manually leads to waste and running out of essential items. This system solves this by importing pantry data from a flat text file, migrating it into a relational database, and allowing real-time querying and management.

##  Core Features
- **Data Ingestion:** Reads initial inventory data from a formatted text file (`pantry.txt`).
- **Database Migration:** Automatically creates a MySQL database and table, and migrates the text data into it.
- **Advanced Querying:** Supports searching for items by starting letter (e.g., `LIKE 'R%'`), viewing all items, and managing stock quantities.
- **Data Manipulation:** Add new items, update quantities, and delete items dynamically.
- **Robust Error Handling:** Implements comprehensive exception handling for missing files, invalid data types, empty fields, and database connection failures.

## Tech Stack & Concepts Applied
- **Language:** Python
- **Database:** MySQL (using `mysql-connector-python`)
- **Concepts:** File I/O, Relational Database Design, SQL Queries (SELECT, INSERT, ALTER, DELETE), Exception Handling, and Data Validation.

##  How to Run
1. Ensure you have MySQL installed and running on your machine.
2. Clone the repository:
   `git clone https://github.com/[Ur name]/Smart-Pantry-Manager.git`
3. Install the required dependencies:
   `pip install -r requirements.txt`
4. Update the database credentials in the Python script (`password="YOUR_PASSWORD"`).
5. Run the application:
   `python main.py`
