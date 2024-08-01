JDBC Connection for SQLAlchemy.
===============================
.. image:: https://img.shields.io/pypi/dm/sqlalchemy-jdbcapi.svg
        :target: https://pypi.org/project/sqlalchemy-jdbcapi/

The primary purpose of this dialect is to provide JDBC connection using provided driver(JAR).

Installation
------------

Installing the dialect is straightforward::

     python3 -m pip install sqlalchemy-jdbcapi


Usage
-----
Set an environment variable  `export CLASSPATH=<path>/ojdbc8.jar:<path>/postgresql-42.2.9.jre7.jar`

PostgressSQL::

    from sqlalchemy import create_engine
    create_engine('jdbcapi+pgjdbc://{}:{}@{}/{}'.format(username, password, <ip:host>', <database name>))

Oracle::

    create_engine("jdbcapi+oraclejdbc://username:password@HOST:1521/Database")

OceanBase::

    from urllib.parse import quote
    user = quote('username@tenant#cluster')
    create_engine("jdbcapi+oceanbasejdbc://user:password@HOST:2881/Database")

GenericJDBCConnection::

        Set an environment variable `CLASSPATH`

        // your dialect.py
        class SQLBaseJDBCDialect(GenericJDBCDialect):
            jdbc_db_name = "sqlbase"
            jdbc_driver_name = "jdbc.gupta.sqlbase.SqlbaseDriver"

        // __init__.py
        rom sqlalchemy.dialects import registry

        registry.register(
            "jdbcapi.sqlbase", "dialect", "SQLBaseJDBCDialect"
        )

        // Your database.py
        create_engine("jdbcapi+sqlbase://localhost:2881/TEST")

Supported databases
-------------------

In theory every database with a suitable JDBC driver should work.

* SQLite
* Hypersonic SQL (HSQLDB)
* IBM DB2
* IBM DB2 for mainframes
* Oracle
* Teradata DB
* Netezza
* Mimer DB
* Microsoft SQL Server
* MySQL
* PostgreSQL
* many more...

Contributing
------------

Please submit `bugs and patches
<https://github.com/daneshpatel/sqlalchemy-jdbcapi/issues>`_.
All contributors will be acknowledged. Thanks!

Changelog
------------
- 1.4.0 - 2024-08-1
  - add genericjdbc and sample, use poetry, flake and nix

- 1.3.0 - 2023-08-23
  - add oceanbase's Oracle mode support.

- 1.2.2 - 2020-10-16
  - SSL Support from URL.
  
- 1.2.1 - 2020-09-9
  - Minor fix.

- 1.2.0 - 2020-09-1
  - Issue: PGarray not iterable.

- 1.1.0 - 2020-08-4
  - Initial release.
