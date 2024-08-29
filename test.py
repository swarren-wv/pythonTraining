import pyodbc

# Define the connection string
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=EDWSQL;"
    "DATABASE=EDW_PRSNT;"
    "UID=swarren@worldvision.org;"
    "PWD=M7Wif3ishot!"
)

# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()

# Define the SQL query 
query = "select distinct s.WVUS_Constituent_Account_Nbr from RESTRICTED.Constituent_Source_Dim_V s where s.Constituent_Status_Nm = 'ACTIVE' and Person_Last_Nm = 'WARREN'"

# Execute the query
cursor.execute(query)

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
