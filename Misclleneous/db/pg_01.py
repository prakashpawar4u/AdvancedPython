# import psycopg2

# # Step 1: Establish a connection to the PostgreSQL database
# conn = psycopg2.connect(
#     dbname="otaf_git11",  # replace with your database name
#     user="postgres",  # replace with your username
#     password="postgres",  # replace with your password
#     host="192.168.56.114",  # replace with your database host (e.g., localhost or IP address)
#     port="5432",  # default PostgreSQL port
# )

# # Step 2: Create a cursor object to interact with the database
# cur = conn.cursor()

# # Step 3: Write your SQL query (replace "your_table_name" with your actual table name)
# query = "SELECT * FROM job_creation_details;"

# # Step 4: Execute the query
# cur.execute(query)

# # Step 5: Fetch the results
# rows = cur.fetchall()

# # Step 6: Process and print the results
# for row in rows:
#     print(row)

# # Step 7: Close the cursor and connection
# cur.close()
# conn.close()


from tenacity import retry, stop_after_attempt, wait_fixed


class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def connect(self):
        import psycopg2

        try:
            self.connection = psycopg2.connect(**self.db_config)
            print("Database connection established.")
            return self.connection
        except Exception as e:
            raise Exception(f"Error connecting to database: {e}")

    def is_connection_alive(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                return True
        except Exception as e:
            print(f"Database connection is not alive: {e}")
            print("retrying to connect to database")
            try:
                import psycopg2

                self.connection = psycopg2.connect(**self.db_config)
                print("Database connection established.")
                return True
            except Exception as e:
                print(f"Error connecting to database: {e}")
                return False

    def execute_query(self, query):
        if not self.is_connection_alive():
            print("Database connection is not established.")
            return None
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
                if query.strip().upper().startswith("SELECT"):
                    return self.fetch_results(cursor)
                return (
                    cursor.rowcount
                )  # Return the number of affected rows for non-SELECT queries
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_results(self, cursor):
        try:
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching results: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


# Define your database configuration
if __name__ == "__main__":
    print("create config")
    db_config = {
        "dbname": "otaf_git11",
        "user": "postgres",
        "password": "postgres",
        "host": "192.168.56.114",
        "port": "5432",
    }
    print("Creating DB object")
    # Create an instance of the Database class
    db = Database(db_config)

    print("calling db connect")
    # Connect to the database
    db.connect()

    # Define your query to read from the job_creation_details table
    query = "SELECT * FROM job_creation_details"

    # Execute the query
    results = db.execute_query(query)

    # Print the results
    if results:
        for row in results:
            print(row)

    # Close the database connection
    db.close()
