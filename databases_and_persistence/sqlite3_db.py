# SQLite also accepts
#  that special string “:memory:” to create a temporary database in memory instead.

# Once we’ve gotten past this platform
# specific call, though, the rest of the API is largely database neutral.

# Making databases and tables
# Next, let’s make a cursor for submitting SQL statements to the database server, and
# submit one to create a first table:

# Notice the module’s paramstyle—this tells us what style
# it uses for substitution targets in the statement string. Here, qmark means this module
# accepts ? for replacement targets.


# >>> rows = [['Tom', 'mgr', 100000],
#  ...
# ['Kim', 'adm', 30000],
#  ...
# ['pat', 'dev', 90000]]
#  >>> for row in rows:
#  ...
# curs.execute('insert into people values (? , ?, ?)', row)
#  ...
#  >>> conn.commit()
#  Blending Python and SQL like this starts to open up all sorts of interesting possibilities.
#  Notice the last command; we always need to call the connection’s commit method to
#  write our changes out to the database.


# Otherwise, when the connection is closed, our
#  changes may be lost. In fact, until we call the commit method, none of our inserts may
#  be visible from other database connections.


# >>> import sqlite3
# >>> conn = sqlite3.connect("dbase1") # use full path for files elsewhere
# >>> curs = conn.cursor()
# >>> create_table_query_str = 'create table people (name char(30), job char(10), pay int(4))'
# >>> curs.execute(create_table_query_str)
# <sqlite3.Cursor object at 0x000002371DF83DC0>
# >>> curs.execute('insert into people values (?, ?, ?)', ('Bob', 'dev', 5000))
# <sqlite3.Cursor object at 0x000002371DF83DC0>
# >>> curs.rowcount
# 1
# >>> sqlite3.paramstyle
# 'qmark'                                                                                           >>> curs.executemany('insert into people values (?, ?, ?)', [ ('Sue', 'mus', '70000'),          ..... ('Ann', 'mus', '60000')])
# >>> curs.rowcount
# 2
# >>> conn.commit()


# Technically, the API suggests that a connection object should automatically call its
# rollback method to back out changes that have not yet been committed, when it is
# closed (which happens manually when its close method is called, or automatically
# when the connection object is about to be garbage collected). For database systems
# that don’t support transaction commit and rollback operations, these calls may do
# nothing. SQLite implements both the commit and rollback methods; the latter rolls
# back any changes made since the last commit.


# >>> curs.execute('select * from people')
#  >>> curs.fetchall()


#  >>> curs.execute('select * from people')
#  >>> for (name, job, pay) in curs.fetchall():
#  ...
# print(name, ':', pay)
#  ...
#  Bob : 5000
#  Sue : 70000
#  Ann : 60000
#  Tom : 100000
#  Kim : 30000
#  pat : 90000


# >>> curs.execute('select * from people')
# >>> while True:
# ...
# ...
# ...
# row = curs.fetchone()
# if not row: break
# print(row)
# ...
# ('Bob', 'dev', 5000)
# ('Sue', 'mus', 70000)
# ('Ann', 'mus', 60000)
# ('Tom', 'mgr', 100000)
# ('Kim', 'adm', 30000)
# ('pat', 'dev', 90000)


# >>> curs.execute('select * from people')
# >>> while True:
# ...
# ...
# ...
# ...
# rows = curs.fetchmany()
# if not rows: break
# for row in rows:
# print(row)
# ...
# ('Bob', 'dev', 5000)
# ('Sue', 'mus', 70000)
# ('Ann', 'mus', 60000)
# ('Tom', 'mgr', 100000)
# ('Kim', 'adm', 30000)
# ('pat', 'dev', 90000)


# >>> curs.execute('update people set pay=? where pay <= ?', [65000, 60000])
# >>> curs.rowcount
# 3
# >>> curs.execute('select * from people')
# >>> curs.fetchall()
# [('Bob', 'dev', 65000), ('Sue', 'mus', 70000), ('Ann', 'mus', 65000), ('Tom', 'mgr',
# 100000), ('Kim', 'adm', 65000), ('pat', 'dev', 90000)]


# >>> curs.execute('delete from people where name = ?', ['Bob'])
# >>> curs.execute('delete from people where pay >= ?',(90000,))
# >>> curs.execute('select * from people')
# >>> curs.fetchall()
# [('Sue', 'mus', 70000), ('Ann', 'mus', 65000), ('Kim', 'adm', 65000)]
# >>> conn.commit()

# >>> curs.description
# (('name', None, None, None, None, None, None), ('job', None, None, None, None, None,
# None), ('pay', None, None, None, None, None, None))

# Formally, the description is a sequence of column-description sequences, each of the
# following form. See the DB API for more on the meaning of the type code slot—it maps
# to objects at the top level of the database interface module, but the sqlite3 module
# implements only the name component:
# (name, type_code, display_size, internal_size, precision, scale, null_ok)

# >>> curs.execute('select * from people')
# >>> colnames = [desc[0] for desc in curs.description]
# >>> colnames
# ['name', 'job', 'pay']
# >>> for row in curs.fetchall():
# ...
# for name, value in zip(colnames, row):
# ...
# ...
# print(name, '\t=>', value)
# print()
# ...
# name    => Sue
# job     => mus
# pay     => 70000
# name    => Ann
# job     => mus
# pay     => 65000


# >>> curs.execute("select * from people")
# <sqlite3.Cursor object at 0x000002371D967CC0>
# >>> row = curs.execute("select * from people")
# >>> rows = curs.execute("select * from people")
# >>> for row in rows.fetchall():
# ...     for name, value in zip(colnames, row):
# ...         print(name, value)
# ...
# name Bob
# job dev
# pay 5000
# name Sue
# job mus
# pay 70000
# name Ann
# job mus
# pay 60000


# >>> curs.execute('select * from people')
#  >>> colnames = [desc[0] for desc in curs.description]
#  >>> rowdicts = []
#  >>> for row in curs.fetchall():
#  ...
# newdict = {}
#  ...
# ...
# ...
# for name, val in zip(colnames, row):
#  newdict[name] = val
#  rowdicts.append(newdict)
#  ...
#  >>> for row in rowdicts: print(row)
#  ...
#  {'pay': 70000, 'job': 'mus', 'name': 'Sue'}
#  {'pay': 65000, 'job': 'mus', 'name': 'Ann'}
#  {'pay': 65000, 'job': 'adm', 'name': 'Kim'}


# >>> curs.execute('select * from people')
#  >>> colnames = [desc[0] for desc in curs.description]
#  >>> rowdicts = []
#  >>> for row in curs.fetchall():
#  ...
# rowdicts.append( dict(zip(colnames, row)) )


# >>> curs.execute('select * from people')
#  >>> colnames = [desc[0] for desc in curs.description]
#  >>> rowdicts = [dict(zip(colnames, row)) for row in curs.fetchall()]
#  >>> rowdicts[0]
#  {'pay': 70000, 'job': 'mus', 'name': 'Sue'}
