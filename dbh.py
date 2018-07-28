# DATABASE HANDLER
import sqlite3

def setupConnetion():
    return sqlite3.connect('test2_db.db')

def dbSetup(conn):
    c= conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS stock_data (
                DATE varchar(255) not null,
                STOCK varchar(255) not null,
                OPEN float not null,
                HIGH float not null,
                LOW float not null,
                CLOSE_VALUE float not null,
                VOLUME integer not null
    )""")
    
    # print(feedback)
    conn.commit()

def addData(conn, ot_date, stock, opens, high, low, close, volume):

    c= conn.cursor()
    sql = "INSERT INTO stock_data VALUES (:DATE, :STOCK, :OPEN, :HIGH, :LOW, :CLOSE_VALUE, :VOLUME)"
    c.execute(sql, {'DATE': ot_date, 'STOCK': stock , 'OPEN': opens, 'HIGH': high, 'LOW': low, 'CLOSE_VALUE': close, 'VOLUME': volume})
    conn.commit()

    # print(ot_date, stock, opens, high, low, close, volume)
