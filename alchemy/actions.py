from utilities.session_db import session


class ActionsOnTables:
    def __init__(self):
        self._session = session

    def insert_new(self, record):
        self._session.add(record)
        self._session.commit()

    def get_all_new(self, record_class):
        all_records = self._session.query(record_class).all()
        for record in all_records:
            print(f'\n{record}')
        return all_records
