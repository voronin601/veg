import psycopg2 as pg2

conn = pg2.connect(dbname = 'postgres', user = 'postgres', password = 'vovavoronin@1999', host = '127.0.0.1', port = '5432')
cursor = conn.cursor()

#проверка существования пользователя в бд reg
def proof_reg(num = ""):
    if num: 
        cursor.execute("SELECT * FROM users WHERE number LIKE '%s';" %('%' + num[:len(num)-6] + '%'))
        #сделать более грамотную ообработку (если таких значений больше 1)
        if len(cursor.fetchall()) == 1: return True
        elif len(cursor.fetchall()) == 0: 
            if reg(num = num):
                return True
            else: return False
        else: return False
    else: return False


def reg(num = ""):
    if num:
        cursor.execute("INSERT INTO users VALUES ('%s');" %num)
        conn.commit()
        return True
    else: return False