def query(sql, db):
    """
    function; use sql statement to get student information.
    parameter: sql(string)
    """

    cur = db.cursor()
    try:
        cur.execute(sql)
        result = cur.fetchall()
        db.commit()
    except:
        db.rollback()
    cur.close()
    return result


def update(sql, db):
    """
    function; use sql statement to get student information.
    parameter: sql(string)
    """
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
    cur.close()


def insert(sql, data, db):
    cur = db.cursor()
    try:
        cur.execute(sql, data)
        db.commit()
    except:
        db.rollback()
    cur.close()


def insert_many(sql, data, db):
    cur = db.cursor()
    try:
        cur.executemany(sql, data)
        db.commit()
    except:
        db.rollback()
    cur.close()


def delete(sql, db):
    cur = db.cursor()
    try:
        cur.execute(sql)
        db.commit()
    except:
        db.rollback()
    cur.close()
