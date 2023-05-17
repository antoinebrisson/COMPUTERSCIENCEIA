import mysql.connector

class ImageDB:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="yourdatabase"
        )
        self.cursor = self.db.cursor()

    def add_image(self, filename, path):
        sql = "INSERT INTO images (filename, path) VALUES (%s, %s)"
        values = (filename, path)
        self.cursor.execute(sql, values)
        self.db.commit()

    def get_images(self):
        sql = "SELECT * FROM images"
        self.cursor.execute(sql)
        images = self.cursor.fetchall()
        return images

    def close(self):
        self.cursor.close()
        self.db.close()
