# Core #
Orion runs on [Apache Airflow](https://github.com/apache/airflow). Core contains the DAG components and the ORMs used to connect to PostgreSQL DB.

## Config file ##
All of the credentials are stored in a config file that is not synced on GitHub. You should create a file in the following path:

```
orion/orion/core/config/orion_config.config
```

and with the following format:

```
[postgresdb]
DATABASE_URI=postgres+psycopg2://USER:PASSWORD@localhost:5432/bioarxiv
TEST_URI=postgres+psycopg2://USER:PASSWORD@localhost:5432/postgres

[mag]
MAG_API_KEY=MY_MAG_API_KEY

[google]
GOOGLE_KEY=MY_GOOGLE_API_KEY

[genderapi]
GENDER_API_KEY=MY_GENDER_API_KEY
```

### Notes ###
* **Important**: [`misctools.py`](https://github.com/kstathou/orion/blob/dev/orion/core/airflow_utils/misctools.py) is currently being used to pick up the required parts of the config file. This will probably be replaced in the future by `dotenv`. Thus, the format of the congif file will change too. 
* The database is actually stored on Amazon RDS. This means that you need an AWS account to access the data and the URI differs from the one above.

## How to setup and use a PostgreSQL DB ##
Install PostgreSQL:
* For macOS users, the fastest way is to download the [Postgres.app](https://postgresapp.com/) and follow the installation instructions. To connect to a database, make sure that the app is running.
* For all other users, you should be able to find a suitable distribution [here](https://www.postgresql.org/download/).

TODO: how to complete setup and use postgresdb.  

<!-- Then, run `python mag_orm.py` to create the project's database (`orion`) and its tables. -->

<!-- Note that the `.env` file contains two connections to PostgreSQL in the following format: -->

<!-- ``` python -->
<!-- postgresdb = postgres+psycopg2://postgres@localhost/orion -->
<!-- test_postgresdb = postgres+psycopg2://postgres@localhost/postgres -->
<!-- ``` -->

<!-- `orion`: the project's database.   -->
<!-- `postgres`: default database that is shipped with PostgreSQL and used here for testing the ORMs. -->
