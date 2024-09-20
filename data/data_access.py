import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import mysql.connector

load_dotenv()

class Mysql_config:
    def __init__(self, host, user, password, database, raise_on_warnings):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.raise_on_warnings = raise_on_warnings

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')


def get_mysql_conn():

    return mysql.connector.connect(Mysql_config(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, True))


