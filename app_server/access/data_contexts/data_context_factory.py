import mysql.connector
from mysql.connector import errorcode

config = {
  "user" : "root",
  "password" : "",
  "host" : "127.0.0.1",
  "database" : "database1"
}

class DataContextFactory:
    def factory(self, row_no):

        try:
            #cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1', database='database1')
            cnx = mysql.connector.connect(**config)
        except mysql.connector.Error as err:
          if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
              print("Something is wrong with your user name or password")
          elif err.errno == errorcode.ER_BAD_DB_ERROR:
              print("Database does not exist")
          else:
              print(err)

        cursor = cnx.cursor()

        row_no = int(row_no)
        query = ("SELECT Message FROM comments WHERE Id = {}")
        query = query.format(row_no)
        cursor.execute(query)

        text = ""
        for(Message) in cursor:
              text = text + str(Message) + "\n"

        cursor.close()
        cnx.close()

        return text
