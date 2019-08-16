import sqlite3 as s

conn = s.connect("D:\\Python\\ScorePython\\sdb")
c = conn.cursor()

c.execute("drop table if exists tab")
c.execute("create table tab(menu char(20), price int)")
c.execute("insert into tab values('짜장면', 6000)")
c.execute("insert into tab values('짬뽕', 8000)")

conn.commit()

c.execute("select * from tab")
k = c.fetchall()

for row in k:
    print("{}  {}".format(row[0], row[1]))


c.close()
conn.close()    