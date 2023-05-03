import sqlite3
from pathlib import Path
from datetime import datetime
from typing import List

BASE_PATH = Path(__file__).absolute().parent


from collections import namedtuple

Sample = namedtuple('Sample', ['timestamp', 'temperature', 'moisture'])


class DB:

    def __init__(self, db_name: str) -> None:
        db_path = BASE_PATH.joinpath(db_name)
        self.table = 'Plant'
        self.db = sqlite3.connect(str(db_path), check_same_thread=False)

    def close(self) -> None:
        self.db.close()

    def insert(self, moisture: float, temperature: float) -> None:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = f'INSERT INTO {self.table} values (' + \
                f'"{timestamp}", {moisture}, {temperature})'
        self._query(query, True)
        
    def get_table_info(self) -> tuple:
        return self._query(f'PRAGMA table_info({self.table});')

    def get_samples_all(self) -> List[Sample]:
        return self._sql_entries_to_py_pbj(self._query(f'SELECT * FROM {self.table};'))

    def get_samples_last_24h(self) -> List[Sample]:
        return self._sql_entries_to_py_pbj(self._query(f'SELECT * FROM {self.table} WHERE timestamp > datetime("now","-24 hour");'))

    def get_samples_last_week(self) -> List[Sample]:
        return self._sql_entries_to_py_pbj(self._query(f'SELECT * FROM {self.table} WHERE timestamp > datetime("now","-7 day");'))
    
    def get_samples_last_month(self) -> List[Sample]:
        return self._sql_entries_to_py_pbj(self._query(f'SELECT * FROM {self.table} WHERE timestamp > datetime("now","-1 month");'))

    def get_samples_last_year(self) -> List[Sample]:
        return self._sql_entries_to_py_pbj(self._query(f'SELECT * FROM {self.table} WHERE timestamp > datetime("now","-1 year");'))

    def _query(self, query: str, commit: bool = False) -> None:
        print(f'QUERY: {query}')
        cursor = self.db.execute(query)
        if commit:
            if commit:
                self.db.commit()
        return cursor.fetchall()

    def _sql_entries_to_py_pbj(self, samples: List[Sample]) -> List[Sample]:
        return [Sample(*args)._asdict() for args in samples]
    