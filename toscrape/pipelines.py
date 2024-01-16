# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class ToscrapePipeline:

    def __init__(self):
        ## Connection Details
        hostname = 'db'
        username = 'tuto'
        password = 'admingres' # your password
        database = 'books'

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        DROP TABLE IF EXISTS books;
        CREATE TABLE books (
            title VARCHAR,
            url VARCHAR 
        );
        """)

    def process_item(self, item, spider):

        ## Define insert statement
        self.cur.execute(""" insert into books (title, url) values (%s,%s)""", (
            item["title"],
            item["url"]
        ))

        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
