"""
Flat files
Text and bytes stored directly on your computer
DBM keyed files
Keyed access to strings stored in dictionary-like files

Pickled objects
 Serialized Python objects saved to files and streams
 Shelve files
 Pickled Python objects saved in DBM keyed files
 Object-oriented databases (OODBs)
 Persistent Python objects stored in persistent dictionaries (ZODB, Durus)
 SQL relational databases (RDBMSs)
 Table-based storage that supports SQL queries (SQLite, MySQL, PostGreSQL,
 etc.)
 Object relational mappers (ORMs)
 Mediators that map Python classes to relational tables (SQLObject, SQLAlchemy)

"""

# For instance, given a DBM file object:
#  • Indexing by key fetches data from the file.
#  • Assigning to an index stores data in the file.


# C:\...\PP4E\Dbase> python
# >>> import dbm
# >>> file = dbm.open('movie', 'c')
# >>> file['Batman'] = 'Pow!'
# >>> file.keys()
# [b'Batman']
# >>> file['Batman']
# b'Pow!'
# >>> who  = ['Robin', 'Cat-woman', 'Joker']
# >>> what = ['Bang!', 'Splat!', 'Wham!']
# >>> for i in range(len(who)):
#         file[who[i]] = what[i]
# get interface: bsddb, gnu, ndbm, dumb
# make a DBM file called 'movie'
# store a string under key 'Batman'
# get the file's key directory
# fetch value for key 'Batman'
# add 3 more "records"
# ...
# >>> file.keys()
# [b'Cat-woman', b'Batman', b'Joker', b'Robin']
# >>> len(file), 'Robin' in file, file['Joker']


#  (4, True, b'Wham!')
#  >>> file.close()              # close sometimes required

# Further, DBM files always
#  store both keys and values as bytes objects; interpretation as arbitrary types of Unicode
#  text is left to the client application. We can use either bytes or str strings in our code
#  when accessing or storing keys and values—using bytes allows your keys and values
#  to retain arbitrary Unicode encodings, but str objects in our code will be encoded to
#  bytes internally using the UTF-8 Unicode encoding by Python’s DBM implementation.


# >>> file = dbm.open("movie", "c")
# >>> file
# <dbm.sqlite3._Database object at 0x00000211449E34D0>
# >>> list(file)
# [b'Batman', b'Fati', b'Umar']
# >>> for f in file:
# ...     print(f)
# ...
# b'Batman'
# b'Fati'
# b'Umar'
# >>> list(file.key())
# Traceback (most recent call last):
#   File "<python-input-19>", line 1, in <module>
#     list(file.key())
#          ^^^^^^^^
# AttributeError: '_Database' object has no attribute 'key'. Did you mean: 'keys'?
# >>> list(file.keys())
# [b'Batman', b'Fati', b'Umar']
# >>> list(file.items())
# [(b'Batman', b'Pow'), (b'Fati', b'685'), (b'Umar', b'324')]
# >>> for key in file:
# ...     print(key, file[key])
# ...
# b'Batman' b'Pow'
# b'Fati' b'685'
# b'Umar' b'324'
# >>> for key in file:
# ...     print(key.decode(), file[key].decode())
# ...
# Batman Pow
# Fati 685
# Umar 324


# >>> file['Batman'] = 'Ka-Boom!'   # change Batman slot
# >>> del file['Robin']            # delete the Robin entry
# >>> file.close()                 # close it after changes


# Cursor objects
#  Represent an SQL statement submitted as a string and can be used to access and
#  step through SQL statement results.
#  Query results of SQL select statements
#  Are returned to scripts as Python sequences of sequences (e.g., a list of tuples),
#  representing database tables of rows. Within these row sequences, column field
#  values are normal Python objects such as strings, integers, and floats (e.g., [('bob',
#  48), ('emily',47)]). Column values may also be special types that encapsulate
#  things such as date and time, and database NULL values are returned as the Python
#  None object.


#  • DDL definition statements (e.g., CREATE TABLE)
#  • DML modification statements (e.g., UPDATE or INSERT)
#  • DQL query statements (e.g., SELECT)


# After running an SQL statement, the cursor’s rowcount attribute gives the number of
#  rows changed (for DML changes) or fetched (for DQL queries), and the cursor’s
#  description attribute gives column names and types after a query; execute also returns
#  the number of rows affected or fetched in the most vendor interfaces. For DQL query
#  statements, you must call one of the fetch methods to complete the operation:
#  tuple       = cursobj.fetchone()
# listoftuple = cursobj.fetchmany([size])
# listoftuple = cursobj.fetchall()
# fetch next row of a query result
#  fetch next set of rows of query result
#  fetch all remaining rows of the result


#  query = 'SELECT name, shoesize FROM spam WHERE job = ? AND age = ?'
#  cursobj.execute(query, (value1, value2))
#  results = cursobj.fetchall()
#  for row in results: ...


# Although SQLite implements a complete relational database system, it
#  takes the form of an in-process library instead of a server.


# This generally makes it better
#  suited for program storage than for enterprise-level data needs.
