# -*- coding: utf-8 -*-
import numpy as np
import sqlite3 as sql
import os
import sys

SORT = True

# Path to the folder
PATH = r'C:\Users\se\Downloads\manual classifier\labelImg-master\demo'
DB = 'images.db'
TABLE = 'images'
# Columns which will be created in db
COLUMNS = ['id INT', 'image_path TEXT']


def get_numerical_list(l):
    result = []

    for item in l:
        item = item.split('\\')[-1]
        i = item.split('-')
        result += [i[:3]]
        if i[3] != 'large.jpg':
            assert False

    return result

def list_into_str(l):
    l = l.tolist()
    # print(l)
    # print(len(l))
    s = '-'.join(l)
    return s

def get_images(path):
    """
    Get all .jpg files pathes from path
    :param path: path to the folder
    :return: list of images pathes
    """
    path, dir, files = os.walk(path).__next__()
    images = [image for image in files if image.split('.')[-1] == 'jpg']

    return images

def create_table(cur):
    """
    Creates a table in db
    :param cur: cursor obj (connection.cursor)
    :return: None
    """
    col = ', '.join(COLUMNS)
    cur.execute("CREATE TABLE {}({})".format(TABLE, col))

def insert_data(cur, data):
    """
    Inserts data into the db
    :param cur: cursor obj
    :param data: list of data
    :return:
    """
    im_num = len(data)
    for counter in range(im_num):
        if type(data[counter]) == list:
            sd = "\'" + "\', \'".join(data[counter]) + "\'"
        else:
            sd = "\'" + PATH + '\\' + data[counter] + "\'"
        request = "INSERT INTO {} VALUES({}, {})".format(
            TABLE, counter + 1, sd)
        # print(request)
        cur.execute(request)


def del_db():
    """
    Deletes a database
    :return:
    """
    try:
        os.remove('{}'.format(DB))
    except FileNotFoundError:
        return

def main():
    # get images
    images_path = get_images(PATH)

    # create db and cursor
    connection = sql.connect(DB)
    cursor = connection.cursor()

    # create table and insert data
    create_table(cursor)
    insert_data(cursor, images_path)\

    # save changes and exit
    connection.commit()
    cursor.close()
    connection.close()

def main2():
    # Getting info from db
    connection = sql.connect(DB)
    cur = connection.cursor()

    cur.execute("SELECT * FROM {}".format(TABLE))
    result = cur.fetchall()

    cur.close()
    connection.close()

    # Sorting all this stuff from db
    img_list = [r[1] for r in result]
    img_list = np.array(img_list)

    img_list = np.array(get_numerical_list(img_list), dtype=int)# after this list will be like
                                                                # [[1 1 1], [1 10 23], ...]

    img_list = img_list[np.lexsort(([img_list[:, i] for i in range(img_list.shape[1] - 1, -1, -1)]))]    # sorting
    img_list = np.array(img_list, dtype=str)                    # getting all ints into strs
    larges_list = [['large.jpg'] for i in range(len(img_list))] # needed for building a final strings
    img_list = np.hstack((img_list, larges_list))               # building a list of strings

    imgs = []                                                   # here we store the final strings
    for item in img_list:
        item = list_into_str(item)
        imgs.append(item)

    del_db()

    connection = sql.connect(DB)
    cur = connection.cursor()

    create_table(cur)
    insert_data(cur, imgs)

    connection.commit()
    cur.close()
    connection.close()

if __name__ == "__main__":
    del_db()
    main()
    if SORT:
        main2()