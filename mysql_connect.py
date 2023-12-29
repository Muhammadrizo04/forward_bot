from multiprocessing.connection import answer_challenge
import pymysql

def mysql_setter(query:str,*vals):
    """Berilgan mysql sorovni bazaga bog'lovchi funksiya Bazaga ma'lumot yuborish va saqlash uchun """
    con=0
    try:
        con=pymysql.connect(
            host=HOST,
            port=PORT,
            user=DBUSER,
            password=PASSWORD,
            database=DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )
        cur=con.cursor()
        cur.execute(query,[*vals])
        con.commit()
        #print('mysql_connect success')
        #con.close(b)
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()
        

def mysql_getter(query:str,*vals):

    con=0
    try:
        con=pymysql.connect(
            host=HOST,
            port=PORT,
            user=DBUSER,
            password=PASSWORD,
            database=DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )
        cur=con.cursor()
        cur.execute(query,[*vals])
        answer=cur.fetchall()
        #print('mysql_connect success')
        #con.close(b)
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()
            return answer

