import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

DOMAIN="https://books.toscrape.com/"

@app.route('/')
def samplefunction():
    return_html = """
    <ul>
    """
    connection = None
    # return_array = []
    try:
        connection = psycopg2.connect(user="tuto",
                                    password="admingres",
                                    host="db",
                                    port="5432",
                                    database="books")
        cursor = connection.cursor()
        postgreSQL_select_Query = 'select * from "books"'

        cursor.execute(postgreSQL_select_Query)
        book_records = cursor.fetchall()

        for row in book_records:
            # return_array.append({
            #     "name": row[0],
            #     "url": row[1]
            # })
            return_html += '<li><h3>' + row[0] + '</h3> <img src=' + DOMAIN + row[1] + '></li>'

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return_html += '</ul>'
            return return_html

if __name__ == '__main__':
    port = 8080 
    app.run(host='0.0.0.0', port=port, debug=False)

