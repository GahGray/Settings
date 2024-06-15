######### settings #################
    def Add_Category(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='toor' , db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''' , (category_name,))
        self.db.commit()
        self.statusBar().showMessage('New Category Addedd ')
        self.lineEdit_19.setText('')
        self.Show_Category()
        self.Show_Category_Combobox()



    def Show_Category(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='toor' , db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category''')
        data = self.cur.fetchall()

        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form) :
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)



    def Add_Author(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='toor' , db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_20.text()
        self.cur.execute('''
            INSERT INTO authors (author_name) VALUES (%s)
        ''' , (author_name,))
        self.db.commit()
        self.lineEdit_20.setText('')
        self.statusBar().showMessage('New Author Addedd ')
        self.Show_Author()
        self.Show_Author_Combobox()


    def Show_Author(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM authors''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)


    def Add_Publisher(self):
        self.db = MySQLdb.connect(host='localhost' , user='root' , password ='toor' , db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_21.text()
        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES (%s)
        ''' , (publisher_name,))

        self.db.commit()
        self.lineEdit_21.setText('')
        self.statusBar().showMessage('New Publisher Addedd ')
        self.Show_Publisher()
        self.Show_Publisher_Combobox()


    def Show_Publisher(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='toor', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher''')
        data = self.cur.fetchall()


        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position);
