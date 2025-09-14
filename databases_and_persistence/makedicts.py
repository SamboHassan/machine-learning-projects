"""
convert list of row tuples to list of row dicts with field name keys
this is not a command-line utility: hardcoded self-test if run
"""


def makedicts(cursor, query, params=()):
    cursor.execute(query, params)
    colnames = [desc[0] for desc in cursor.description]
    rowdicts = [dict(zip(colnames, row)) for row in cursor.fetchall()]
    return rowdicts


if __name__ == "__main__":  # self test
    import sqlite3

    conn = sqlite3.connect("dbase1")
    cursor = conn.cursor()
    query = "select name, pay from people where pay < ?"
    lowpay = makedicts(cursor, query, [70000])
    for rec in lowpay:
        print(rec)


# run this file from the system command line as a script to invoke its
# self-test code:
# ...\PP4E\Dbase\Sql> makedicts.py
# {'pay': 65000, 'name': 'Ann'}
# {'pay': 65000, 'name': 'Kim'}


# Or we can import it as a module and call its function from another context, like the
# interactive prompt. Because it is a module, it has become a reusable database tool:
# ...\PP4E\Dbase\Sql> python
# >>> from makedicts import makedicts
# >>> from sqlite3 import connect
# >>> conn = connect('dbase1')
# >>> curs = conn.cursor()
# >>> curs.execute('select * from people')
# >>> curs.fetchall()
# [('Sue', 'mus', 70000), ('Ann', 'mus', 65000), ('Kim', 'adm', 65000)]
# >>> rows = makedicts(curs, "select name from people where job = 'mus'")
# >>> rows
# [{'name': 'Sue'}, {'name': 'Ann'}]


# >>> query = 'select name, pay from people where job = ? order by name'
# >>> musicians = makedicts(curs, query, ['mus'])
# >>> for row in musicians: print(row)
# ...
# {'pay': 65000, 'name': 'Ann'}
# {'pay': 70000, 'name': 'Sue'}
