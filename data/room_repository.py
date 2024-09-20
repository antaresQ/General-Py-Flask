from data_access import get_mysql_conn 


def create_room():

    conn = get_mysql_conn()
    cursor = conn.cursor()

    query = ('SELECT * FROM rooms')
    data = cursor.execute(query)
    
    cursor.close()
    conn.close()

    return data


def get_rooms():

    conn = get_mysql_conn()
    cursor = conn.cursor()

    query = ('SELECT * FROM rooms')
    data = cursor.execute(query)
    
    cursor.close()
    conn.close()

    return data
    
