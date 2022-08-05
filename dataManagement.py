import psycopg2 as psql

#id calculation
def idCalk(table, id=1):
    con = psql.connect(database="mcinfini", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM "+ table +" WHERE id = %s)", [id]);
    rows = cur.fetchall()
    if rows[0][0] != False:
        con.close()
        return idCalk(table, id+1)
    else:
        con.close()
        return id

"""#blocks
def insertResource(id,tag,name,color,allsided,topbot,side,dark,light,stone,soil,wood):
    fileO = "D:\\Coding\\PersonalCode\\MC\\SpritesToUse\\blocks\\done\\raw\\" + name + ".png"
    im = cv2.imread(fileO, cv2.IMREAD_UNCHANGED)
    image = im.tolist()
    con = psql.connect(database="mcinfini", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("INSERT INTO block_sprites (id,tag,name,image,color,allsided,topbot,side,dark,light,stone,soil,wood)    "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id,tag,name,image,color,allsided,topbot,side,dark,light,stone,soil,wood));
    con.commit()
    con.close()
"""
"""#resources and armor
def insertResource(id,tag,name,color,dark,light,resource,armor,tool,unique_item):
    fileO = "D:\\Coding\\PersonalCode\\MC\\SpritesToUse\\items\\armor\\" + name + ".png"
#    file1 = "D:\\Coding\\PersonalCode\\MC\\SpritesToUse\\items\\armor\\" + name + "_model.png"
    im = cv2.imread(fileO, cv2.IMREAD_UNCHANGED)
#    im1 = cv2.imread(file1, cv2.IMREAD_UNCHANGED)
    image = im.tolist()
#    image1 = im1.tolist()
    con = psql.connect(database="mcinfini", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("INSERT INTO item_sprites (id,tag,name,image,color,dark,light,resource,armor,tool,unique_item)    "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id,tag,name,image,color,dark,light,resource,armor,tool,unique_item));
    con.commit()
    con.close()
"""
"""#tools
def insertResource(id,tag,name,color,dark,light,resource,armor,tool,unique_item):
    fileO = "D:\\Coding\\PersonalCode\\MC\\SpritesToUse\\items\\tool\\" + name + ".png"
    file1 = "D:\\Coding\\PersonalCode\\MC\\SpritesToUse\\items\\tool\\" + tag + "_handle.png"
    im = cv2.imread(fileO, cv2.IMREAD_UNCHANGED)
    im1 = cv2.imread(file1, cv2.IMREAD_UNCHANGED)
    image = im.tolist()
    image1 = im1.tolist()
    con = psql.connect(database="mcinfini", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("INSERT INTO item_sprites (id,tag,name,image,imagelayer1,color,dark,light,resource,armor,tool,unique_item)    "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (id,tag,name,image,image1,color,dark,light,resource,armor,tool,unique_item));
    con.commit()
    con.close()
"""

def fetchResource1(table, columns, column, operation, value):
    con = psql.connect(database="mcinfini", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT "+ columns +" FROM "+ table +" WHERE "+ column +" "+ operation +" "+ str(value));
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def fetchResource2(table, columns, column1, operation1, value1, column2, operation2, value2):
    con = psql.connect(database="mcinfini", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT "+ columns +" FROM "+ table +" WHERE "+ column1 +" "+ operation1 +" "+str(value1)+" AND "+ column2 +" "+ operation2 +" "+str(value2));
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def fetchResource3(table, columns, column1, operation1, value1, column2, operation2, value2, column3, operation3, value3):
    con = psql.connect(database="mcinfini", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT "+ columns +" FROM "+ table +" WHERE "+ column1 +" "+ operation1 +" "+str(value1)+" AND "+ column2 +" "+ operation2 +" "+str(value2)+" AND "+ column3 +" "+ operation3 +" "+str(value3));
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

