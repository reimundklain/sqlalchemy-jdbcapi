from sqlalchemy.dialects import registry

registry.register(
    "jdbcapi.pgjdbc", "sqlalchemy_jdbcapi.pgjdbc", "PGJDBCDialect"
)
registry.register(
    "jdbcapi.oraclejdbc", "sqlalchemy_jdbcapi.oraclejdbc", "OracleJDBCDialect"
)
registry.register(
    "jdbcapi.oceanbasejdbc", "sqlalchemy_jdbcapi.oceanbasejdbc", "OceanBaseJDBCDialect"
)

