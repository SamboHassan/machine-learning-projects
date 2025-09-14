#  C:\...\PP4E\Dbase\Sql> python
#  >>> from sqlite3 import connect
#  >>> conn = connect('dbase1')
#  >>> curs = conn.cursor()
#  >>> curs.execute('delete from people')
#  >>> curs.execute('select * from people')
#  >>> curs.fetchall()
#  []
#          # empty the table
#  >>> file = open('data.txt')
#  >>> rows = [line.rstrip().split(',') for line in file]
#  >>> rows[0]
#  ['bob', 'devel', '50000']
#  >>> for rec in rows:
#  ...
# curs.execute('insert into people values (?, ?, ?)', rec)
#  ...
#  >>> curs.execute('select * from people')
#  >>> for rec in curs.fetchall(): print(rec)
#  ...
#  ('bob', 'devel', 50000)
#  ('sue', 'music', 60000)
#  ('ann', 'devel', 40000)
#  ('tim', 'admin', 30000)
#  ('kim', 'devel', 60000)


# >>> curs.execute("select sum(pay), avg(pay) from people where job = 'devel'")
# >>> curs.fetchall()
# [(150000, 50000.0)]


# >>> curs.execute("select name, pay from people where job = 'devel'")
#  >>> result = curs.fetchall()
#  >>> result
#  (('bob', 50000L), ('ann', 40000L), ('kim', 60000L))
#  >>> tot = 0
#  >>> for (name, pay) in result: tot += pay
#  ...
#  >>> print('total:', tot, 'average:', tot / len(result))
#  total: 150000 average: 50000.0
#          # use // to truncate


#  Or we can use more advanced tools such as comprehensions and generator expressions
#  to calculate sums, averages, maximums, and the like:
#  >>> print(sum(rec[1] for rec in result))
#          # generator expr
#  150000
#  >>> print(sum(rec[1] for rec in result) / len(result))
#  50000.0
#  >>> print(max(rec[1] for rec in result))
#  60000
