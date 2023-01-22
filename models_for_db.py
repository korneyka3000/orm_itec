import sqlite3
class CharField:
    sqlite_type = 'TEXT'
    postgres_type = 'VARCHAR'

    def __init__(self, row_name: str, max_length: int, verbose_name: str):
        self.row_name = row_name
        self.max_length = max_length
        self.verbose_name = verbose_name
        self.sql_name = 'TEXT'

    def __repr__(self):
        return f"{self.__class__.__name__}:({self.row_name},)"


class CustomTable:
    def __init__(self, name: str, *args):
        self.table_name = name
        self.rows = args

    def __repr__(self) -> str:
        row_names = ''
        for row in self.rows:
            row_names += f" {row.row_name}"
        return f'{self.__class__.__name__}: {self.table_name.capitalize()} | Rows:' + row_names

    def __len__(self) -> int:
        return len(self.rows)

    def __bool__(self):
        return bool(len(self.rows))

    def __getitem__(self, item):
        return self.rows[item]

table1 = CustomTable('first_table',
                     CharField('id', max_length=20, verbose_name='primary key'),
                     CharField('name', max_length=20, verbose_name='username'))

# print(len(table1))
# for i in table1:
#     print(i)



class DB_EXECUTOR:
    @staticmethod
    def prepare_for_create(db_name, table: CustomTable) -> str:
        sql_query = f'CREATE TABLE if not exists {db_name} ('
        for row in table:
            sql_query += f'{row.row_name} {row.sql_name}({row.max_length}),'

        sql_query = sql_query[:-1]
        print(sql_query)
        sql_query += ');'
        print(sql_query)
        return sql_query


    @classmethod
    def create_table(cls, db_name: str, table_to_create: CustomTable):
        raw_sql = cls.prepare_for_create(db_name, table_to_create)
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        st = cursor.execute(raw_sql)
        print(st)
        connection.close()

query = DB_EXECUTOR.create_table('my_db',table1)