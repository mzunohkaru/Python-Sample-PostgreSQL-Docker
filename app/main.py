import psycopg2

# データベースとのコネクションを確立します。
connection = psycopg2.connect("host=db dbname=dev user=root password=password")

# カーソルをオープンします
cursor = connection.cursor()


cursor.execute("SELECT * FROM mybook")
query_result = cursor.fetchall()
print(query_result)
