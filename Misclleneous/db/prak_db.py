# Note: Install pandas, sqlalchemy and psycopg2
import traceback
import json
from typing import Optional, Literal
import pandas as pd
import sqlalchemy
import openpyxl
import logging
from tenacity import retry, stop_after_attempt, wait_fixed


# create logger object
log = logging.getLogger(__name__)


class DataBaseException(Exception):
    """Custom exception for errors related to data base exception."""

    def __init__(self, message: str = "DataBase Exception Raised"):
        """
        Initialize the exception with a custom message.

        Args:
            message (str, optional): The error message.
            Defaults to "DataBase Exception Raised".
        """
        self.msg = message
        self.traceback_str = traceback.format_exc()
        super().__init__(self.msg)

    def __str__(self):
        """Return the exception message along with the traceback."""
        return f"{self.msg}\n{self.traceback_str}"


class DataBase:
    """
    A class for interacting with a PostgreSQL database using SQLAlchemy.

    This class provides methods for database connection management,
    reading tables into pandas DataFrames, saving data to various file formats,
    inserting data into tables, deleting tables, creating tables,
    and updating specific columns in tables.
    """

    def __init__(
        self,
        db_type: str,
        username: str,
        password: str,
        host: str,
        port: str,
        db_name: str,
    ) -> None:
        """Initialize the DataBase object with connection details.

        Args:
            db_type (str): The type of the database (e.g., 'postgresql').
            username (str): The username for connecting to the database.
            password (str): The password for connecting to the database.
            host (str): The hostname or IP address of the database server.
            port (str): The port number of the database server.
            db_name (str): The name of the database.
        """
        self.db_type = db_type
        self.username = username
        self.password = password
        self.host_ip = host
        self.port = port
        self.db_name = db_name
        self.connection_string = self.get_connection_string()
        self.engine = self.create_engine()

    def get_connection_string(self) -> str:
        """
        Constructs the connection string for the database.

        Returns:
            str: The constructed connection string.
        """
        return (
            f"{self.db_type}://{self.username}:{self.password}@"
            f"{self.host_ip}:{self.port}/{self.db_name}"
        )

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
    def create_engine(self) -> sqlalchemy.engine.base.Engine:
        """
        Establishes a connection to the database using SQLAlchemy and returns an engine object.

        Returns:
            sqlalchemy.engine.base.Engine: The SQLAlchemy engine object that allows
            interaction with the database.

        Raises:
            DataBaseException: If the engine creation fails after the retry attempts.
        """
        try:
            return sqlalchemy.create_engine(self.connection_string)
        except (Exception, DataBaseException) as exc:
            raise DataBaseException("Failed to create a engine") from exc

    @retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
    def is_engine_alive(self) -> bool:
        """
        Checks if the database connection is alive.

        Returns:
            bool: True if the connection is alive, False otherwise.
        """
        try:
            with self.engine.connect() as connection:
                connection.execute(sqlalchemy.text("SELECT 1"))
                return True
        except Exception as ex:
            log.warning(f"Database Engine instance check failed, {str(ex)}")
            log.info("Retrying to create database engine instance...")
            try:
                self.engine = self.create_engine()
                with self.engine.connect() as connection:
                    connection.execute(sqlalchemy.text("SELECT 1"))
                    log.info("Database connection is established.")
                    return True
            except (Exception, DataBaseException) as exc:
                raise DataBaseException(
                    "Failed to create the database engine instance"
                ) from exc

    def read_table(
        self, table_name: str, sql_query: str = None
    ) -> Optional[pd.DataFrame]:
        """
        Reads a specified table from the connected database into a pandas DataFrame.

        Args:
            table_name (str): The name of the table to read from the database.
            sql_query (str, optional): Custom SQL query to execute. Defaults to None.

        Returns:
            Optional[pd.DataFrame]: A DataFrame containing the data from the specified table.
            or None if the database is not connected.
        """
        df = None
        try:
            query = f"SELECT * FROM {table_name}" if sql_query is None else sql_query
            log.info(f"Reading data from the '{table_name}' table...")

            if self.is_engine_alive():
                df = pd.read_sql_query(query, self.engine)
            log.info(f"Successfully read data from the '{table_name}' table.")
            return df
        except (Exception, DataBaseException) as exc:
            raise DataBaseException(
                f"Failed to read the {table_name} table: {exc}"
            ) from exc

    @staticmethod
    def save_data(
        df: pd.DataFrame,
        file_path: str,
        file_format: str = "csv",
        engine: openpyxl = "openpyxl",
    ) -> None:
        """
        Saves the DataFrame to a file in the specified format (CSV, Excel, or JSON).

        Args:
            df (pd.DataFrame): The DataFrame to be saved.
            file_path (str): The path where the file will be saved.
            file_format (str, optional): The format of the file ('csv', 'excel', 'json').
            Defaults to 'csv'.
            engine (str, optional): The engine to use for Excel files ('openpyxl' or 'xlsxwriter').
            Defaults to 'openpyxl'.

        Raises:
            ValueError: If an invalid file format is provided.
        """
        try:
            if file_format.lower() == "csv":
                df.to_csv(file_path, index=False)
            elif file_format.lower() == "excel":
                df.to_excel(file_path, index=False, engine=engine)
            elif file_format.lower() == "json":
                df.to_json(file_path, orient="records")
            else:
                raise ValueError(
                    "Invalid file format. Supported formats: 'csv', 'excel', 'json'."
                )
        except ValueError as ve:
            log.exception(f"ValueError: {ve}")
        except (Exception, DataBaseException) as exc:
            log.exception(f"Failed to save data, {exc}")

    def insert_data(
        self,
        df: pd.DataFrame,
        table_name: str,
        if_exists: Literal["fail", "replace", "append"] = "append",
    ) -> None:
        """
        Inserts data from a DataFrame into the specified table in the database.

        Args:
            df (pd.DataFrame): The DataFrame containing the data
            to be inserted.
            table_name (str): The name of the table where data will be inserted.
            if_exists (str, optional): The behavior when the table already exists.
            Defaults to 'append'. Options are 'fail', 'replace', 'append'.

        Raises:
            ValueError: If an invalid value for if_exists is provided.
        """
        try:
            if if_exists not in ["fail", "replace", "append"]:
                raise ValueError(
                    "Invalid value for if_exists. Options are 'fail', 'replace', 'append'."
                )
            if self.is_engine_alive():
                df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)
        except ValueError as ve:
            log.exception(f"ValueError: {ve}")
        except (Exception, DataBaseException) as exc:
            log.exception(f"Failed to insert data into table '{table_name}': {exc}")

    def delete_table(self, table_name: str) -> None:
        """
        Deletes the specified table from the database.

        Args:
            table_name (str): The name of the table to delete.
        """
        try:
            if self.is_engine_alive():
                with self.engine.connect() as connection:
                    connection.execute(
                        sqlalchemy.text(f"DROP TABLE IF EXISTS {table_name}")
                    )
                    connection.commit()
                    log.info(f"Table '{table_name}' deleted successfully.")
        except (Exception, DataBaseException) as exc:
            log.exception(f"Failed to delete the table '{table_name}': {str(exc)}")

    def create_table(self, table_name: str, schema: str) -> None:
        """
        Creates a new table in the database with the specified schema.

        Args:
            table_name (str): The name of the table to create.
            schema (str): The schema of the table to create.
        """
        try:
            if self.is_engine_alive():
                with self.engine.connect() as connection:
                    connection.execute(
                        sqlalchemy.text(
                            f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"
                        )
                    )
                    connection.commit()
                    log.info(f"Table '{table_name}' created successfully.")
        except (Exception, DataBaseException) as exc:
            log.exception(f"Failed to create the table '{table_name}': {exc}")

    @staticmethod
    def _validate_and_execute_update(
        connection: sqlalchemy.engine.base.Connection,
        conditions: dict,
        data: dict,
        table_name: str,
    ) -> None:
        """
        Validates the existence of columns and rows based on provided conditions,
        and executes an update query to modify the specified data in the given table.

        This method performs the following operations:
        1. Validates that each column in the `conditions` exists in the specified table.
        2. Checks if a row matching the `conditions` exists in the table.
        3. Constructs and executes an SQL `UPDATE` statement to modify the data for the matched row.

        Args:
            connection (sqlalchemy.engine.Connection): An active connection to the database.
            conditions (dict): A dictionary specifying the conditions to identify the row to be updated.
                               Keys are column names, and values are the expected values in those columns.
            data (dict): A dictionary containing the column names and the corresponding new values to update.
            table_name (str): The name of the table where the update should be performed.

        Raises:
            ValueError: If any of the columns in `conditions` do not exist in the specified table,
                        or if no row matching the `conditions` is found.
        """
        # Check if the columns in conditions exist in the table
        for column in conditions.keys():
            column_exists = connection.execute(
                sqlalchemy.text(
                    f"""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name = :table_name AND column_name = :column
                    """
                ),
                {"table_name": table_name, "column": column},
            ).fetchone()

            if not column_exists:
                raise ValueError(
                    f"The '{column}' column does not exist in the table '{table_name}'"
                )

        # Check if the row with the specified conditions exists
        where_clause = " AND ".join([f"{col} = :{col}" for col in conditions.keys()])
        row_exists = connection.execute(
            sqlalchemy.text(f"SELECT 1 FROM {table_name} WHERE {where_clause}"),
            conditions,
        ).fetchone()

        if not row_exists:
            raise ValueError(
                f"No row found with conditions {conditions} in the table '{table_name}'"
            )

        # Construct the update query
        update_query = f"UPDATE {table_name} SET "
        update_query += ", ".join([f"{column} = :{column}" for column in data.keys()])
        update_query += f" WHERE {where_clause}"

        # Prepare the parameters for the update
        params = data.copy()
        params.update(conditions)

        # Execute the update query
        connection.execute(sqlalchemy.text(update_query), params)

        # Commit the transaction after all updates are done
        connection.execute(sqlalchemy.text("COMMIT"))

    def update_columns(self, table_name: str, conditions: dict, data: dict) -> bool:
        """
        Adds or updates columns in the specified table for a specific row.

        Args:
            table_name (str): The name of the table where columns will be added or updated.
            conditions (dict): A dictionary with column names as keys and the conditions to be matched as values.
            data (dict): A dictionary with column names as keys and the data to be added or updated as values.
        """
        try:
            if self.is_engine_alive():
                with self.engine.connect() as connection:
                    # check the columns status, prepare the update query and execute
                    DataBase._validate_and_execute_update(
                        connection=connection,
                        conditions=conditions,
                        data=data,
                        table_name=table_name,
                    )
                    log.info(
                        f"Successfully added or updated columns in the table '{table_name}'"
                    )

                    return True
        except (Exception, DataBaseException) as exc:
            log.exception(
                f"Failed to add or update columns in the table '{table_name}': {exc}"
            )
            log.exception(traceback.format_exc())
            return False

    def update_multiple_rows(
        self, table_name: str, update_data: list, jsonb: bool = False
    ) -> bool:
        """
        Perform a bulk update on multiple rows in the specified table.

        Args:
            table_name (str): The name of the table where rows will be updated.
            update_data (list): A list of dictionaries, where each dictionary contains
                                the conditions and data for updating a single row.
            jsonb (bool): Whether the data values should be treated as JSONB.

        Example of `update_data` format:
            [
                {"conditions": {"id": 1}, "data": {"column1": "value1", "column2": "value2"}},
                {"conditions": {"id": 2}, "data": {"column1": "value3", "column2": "value4"}},
            ]
        """
        updates = {}
        ids_list = []

        try:
            if self.is_engine_alive():
                with self.engine.connect() as connection:
                    for entry in update_data:
                        conditions = entry.get("conditions", {})
                        data = entry.get("data", {})

                        if not conditions or not data:
                            raise ValueError(
                                "Both 'conditions' and 'data' must be provided for each update."
                            )

                        # Build the CASE statement for the data to be updated
                        condition_clause = " AND ".join(
                            [f"{key} = '{value}'" for key, value in conditions.items()]
                        )

                        for column, value in data.items():
                            if column not in updates:
                                updates[column] = []
                            if jsonb:
                                updates[column].append(
                                    f"WHEN {condition_clause} THEN '{json.dumps(value)}'::jsonb"
                                )
                            else:
                                updates[column].append(
                                    f"WHEN {condition_clause} THEN '{value}'"
                                )

                        ids_list.append(condition_clause)

                    # Combine CASE statements for each column
                    case_statements = []
                    for column, cases in updates.items():
                        case_statement = " ".join(cases)
                        case_statements.append(f"{column} = CASE {case_statement} END")

                    # Final query
                    case_clause = ", ".join(case_statements)
                    where_clause = " OR ".join([f"({item})" for item in ids_list])

                    update_query = f"""
                        UPDATE {table_name}
                        SET {case_clause}
                        WHERE {where_clause};
                    """

                    # Prepare the parameters for the update
                    params = update_data.copy()

                    # Execute the update query
                    connection.execute(sqlalchemy.text(update_query), params)

                    # Commit the transaction after all updates are done
                    connection.execute(sqlalchemy.text("COMMIT"))
                    log.info(
                        f"Successfully added or updated columns in the table '{table_name}'"
                    )
                    return True
        except (Exception, DataBaseException) as exc:
            log.exception(
                f"Failed to add or update multiple rows in the table '{table_name}': {exc}"
            )
            log.exception(traceback.format_exc())
            return False

    def close(self) -> bool:
        """
        Closes the database connection by disposing of the SQLAlchemy engine.
        """
        try:
            if self.engine:
                self.engine.dispose()
            return True
        except Exception as exc:
            log.exception(f"Failed to close the database connection: {exc}")
            log.exception(traceback.format_exc())
            return False


if __name__ == "__main__":

    print("Create db object")
    db = DataBase(
        "postgresql", "postgres", "postgres", "10.2.2.149", "5432", "prak_dec_24"
    )
    job_queue = "job_creation_details"
    tc_queue_table = "job_testcase_mapping"

    import pdb

    pdb.set_trace()

    job_creation_df = db.read_table(table_name=job_queue)
    print(job_creation_df)

    job_creation_df = job_creation_df.iloc[0]

    job_id = job_creation_df["job_id"].iloc[0]
    testline = job_creation_df["testline"].iloc[0]
    feature = job_creation_df["feature"].iloc[0]
    log_file = "/root/Prakash"

    query = f"SELECT selected_testcases FROM {tc_queue_table} WHERE job_id = {job_id}"

    # SELECT selected_testcases FROM job_testcase_mapping WHERE job_id = 1

    get_tc_list = db.read_table(table_name=tc_queue_table, sql_query=query)

    bringup_query = "SELECT * FROM job_testcase_results WHERE feature = 'Bringup Steps' AND job_id = 1;"

    bringuptc_list = db.read_table(table_name=tc_queue_table, sql_query=bringup_query)

    cucp_bringup_tc = bringuptc_list[bringuptc_list["testcase"] == "CUCP Bringup"].iloc[
        0
    ]["testcase"]

    # UPDATE job_testcase_results SET result = 'Passed' WHERE testcase='CUCP Bringup';
    success = db.update_columns(
        table_name="job_testcase_results",
        conditions={"job_id": "1", "testcase": cucp_bringup_tc},
        data={"result": "Passed"},
    )

    success = db.update_columns(
        table_name=job_queue,
        conditions={"job_id": job_id},
        data={"log_path": log_file},
    )

    db.update_columns(
        table_name=job_queue,
        conditions={"job_id": job_id},
        data={"status": "Executing"},
    )

    db.update_columns(
        table_name=job_queue,
        conditions={"job_id": job_id},
        data={"status": "Queued"},
    )

    success = db.update_columns(
        table_name=job_queue,
        conditions={"job_id": 1},
        data={"log_path": "/root/Prakash"},
    )
