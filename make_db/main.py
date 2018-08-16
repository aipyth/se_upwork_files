# -*- coding: utf-8 -*-
import sqlite3 as sql
import os
import sys

# Path to the folder
PATH = 'C:\\Users\\apython\\Pictures\\Saved Pictures'
DB_NAME = 'images.db'
TABLE = 'images'
# Columns which will be created in db
COLUMNS = ['id INT', 'image_path TEXT']

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
            sd = "\'" + data[counter] + "\'"
        request = "INSERT INTO {} VALUES({}, {})".format(
            TABLE, counter + 1, sd)
        print(request)
        cur.execute(request)


def del_db():
    """
    Deletes a database
    :return:
    """
    try:
        os.remove('{}'.format(DB_NAME))
    except FileNotFoundError:
        return

def main():
    # get images
    images_path = get_images(PATH)

    # create db and cursor
    connection = sql.connect(DB_NAME)
    cursor = connection.cursor()

    # create table and insert data
    create_table(cursor)
    insert_data(cursor, images_path)\

    # save changes and exit
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    del_db()
    main()