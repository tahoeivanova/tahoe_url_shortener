from flask import Flask, render_template, request, redirect
import uuid
import sqlite3
app = Flask(__name__)

HOSTNAME = 'http://127.0.0.1:5000'


"""

sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS url_table (\
                                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                original_url TEXT NOT NULL UNIQUE,
                                short_url VARCHAR(255) NOT NULL UNIQUE)'''

"""

@app.route("/", methods=['GET', 'POST'])
def get_original_url():
    if request.method == 'POST':
        original_url = request.form['original_url']
        print(original_url, type(original_url))

        sqliteConnection = sqlite3.connect('url.db')
        cursor = sqliteConnection.cursor()

        cursor.execute("SELECT short_url FROM url_table WHERE original_url = '%s'" % original_url)
        short_url = cursor.fetchone()

        if short_url == None:
            short_url = str(uuid.uuid1())[:6]

            cursor.execute("INSERT INTO url_table (original_url, short_url) VALUES (?,?)", (original_url, short_url))
            sqliteConnection.commit()



        cursor.execute("SELECT short_url FROM url_table WHERE original_url = '%s'" % original_url)
        short_url = cursor.fetchone()[0]
        short_url = f'{HOSTNAME}/{short_url}'

        return render_template('short_url.html', short_url=short_url)

    return render_template('main.html')

@app.route('/<short_url>')
def redirect_to_original(short_url):
    sqliteConnection = sqlite3.connect('url.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT original_url FROM url_table WHERE short_url = '%s'" % short_url)
    original_url = cursor.fetchone()[0]
    print(original_url)
    return redirect(original_url)


if __name__ == "__main__":
    app.run(debug=True)