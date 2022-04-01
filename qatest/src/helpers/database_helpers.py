import pymysql


def read_from_db(sql):
    # connect to database
    connection = pymysql.connect(host='127.0.0.1', port=8889,
                                 user='root', password='root')
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return db_data


def get_order_from_db_by_order_no(order_no):
    sql = f"SELECT * FROM quicksitedb.wp_posts WHERE ID = {order_no} AND post_type = 'shop_order';"

    db_order = read_from_db(sql)
    #import pdb;pdb.set_trace()

    return db_order



