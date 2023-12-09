Here we collect some general notes on python learnings. These are specific use cases for specific tasks. However, they are not big enough to be grouped into a folder of their own. Hence, they will be noted down here. If at a later point of time, they get big enough to be made into a specific folder, it will be moved. 

# Connections to Databases
## Snowflake connection

There are two ways to connect to snowflake db using python:
- using ```snowflake-connector-python``` package and directly making the connection
- using ```snowflake-sqlalchemy``` package to make the connection using sqlalchemy

### Using snowflake connector: 
In most cases, the purpose of connecting to the database would be to execute a query on the database and load the results on to a pandas dataframe. For such cases, the recommended approach is to use the ```snowflake-connector``` :

Make sure you install the snowflake-connector package with the extras for pandas: 
```
pip install "snowflake-connector-python[pandas]"
```

Make the connection: 
```
import snowflake.connector
con = snowflake.connector.connect(
    user='XXXX',
    password='XXXX',
    account='XXXX',
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials',
    }
)
```
The advantage with this is that it lets you set session_parameters which is not available with the sql-alchemy connection. Also, as long as the use-case is to retrieve data from the db into a pandas df, this can  be the preferred approach. 

Run the query and retrive into pandas: 
```
# Create a cursor object.
cur = con.cursor()

# Execute a statement that will generate a result set.
sql = "select * from t"
cur.execute(sql)

# Fetch the result set from the cursor and deliver it as the Pandas DataFrame.
df = cur.fetch_pandas_all()
```

### Using sql-alchemy: 
If you are using sql-alchemy, then this is the way to make the connection: 
```
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine

engine = create_engine(URL(
    account = 'myorganization-myaccount',
    user = 'testuser1',
    password = '0123456',
    database = 'testdb',
    schema = 'public',
    warehouse = 'testwh',
    role='myrole',
))

connection = engine.connect()
try:
    connection.execute(<SQL>)
finally:
    connection.close()
    engine.dispose()
```

In our case, we did not choose to go ahead with this approach as the first approach seemed very much sufficient. All this is clearly documented in the below link: <br>
[snowflake documentation](https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-install)