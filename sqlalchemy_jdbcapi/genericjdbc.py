from __future__ import absolute_import
from __future__ import unicode_literals

import os
from sqlalchemy.engine.default import DefaultDialect

from sqlalchemy_jdbcapi.base import BaseDialect, MixedBinary


class GenericJDBCDialect(BaseDialect, DefaultDialect):
    before_connect = None

    def initialize(self, connection):
        super(GenericJDBCDialect, self).initialize(connection)

    def create_connect_args(self, url):
        if url is None:
            return
        jdbc_url: str = str(url).split("//", 1)[-1]
        # add driver information
        if not jdbc_url.startswith("jdbc"):
            jdbc_url = f"jdbc:{self.jdbc_db_name}://{jdbc_url}"
        kwargs = {
            "jclassname": self.jdbc_driver_name,
            "url": jdbc_url,
            # pass driver args via JVM System settings
            "driver_args": []
        }

        if self.before_connect:
            self.before_connect()

        return ((), kwargs)

    @property
    def driver(self):
        return self.dbapi

dialect = GenericJDBCDialect
