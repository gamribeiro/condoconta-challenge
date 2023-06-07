import json
import os
import pytest
from infrastructure.database.connection_factory import Session, Base


@pytest.mark.integration
class IntegrationTest:
    # WARNING: Take care with this, it will truncate all tables in db.
    # (!!!) Do not run tests pointing to prod environments!

    # FIXME: ideally we should not need this. Instead all tests should run
    #  inside a transaction e be rolled back in the end, keeping the db
    #  clean and allowing tests to run in parallel.
    #
    # Some migrations could load data into the database, if that's the case
    # we could run this only once per testing session.

    @staticmethod
    def _do_truncate_all_tables(session):
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())

        session.commit()

    @pytest.fixture(scope="session")
    def before_session(self):
        s = Session()
        s.expire_all()
        s.rollback()
        self._do_truncate_all_tables(s)
        s.commit()
        s.close()
        Session.close_all()

    @pytest.fixture(autouse=True)
    def session(self, before_session):
        Session.remove()
        s = Session()
        # conn = s.connection()
        # trans = conn.begin()
        try:
            with s.begin_nested():
                yield s
        except Exception:
            pass

        # s.rollback()
        # trans.rollback()
