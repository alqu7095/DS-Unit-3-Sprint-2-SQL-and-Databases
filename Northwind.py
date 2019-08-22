import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()
query = '''SELECT * FROM Product
    ORDER BY UnitPrice;'''
query
curs = conn.cursor()
curs.execute(query)
curs.fetchall()

#Top 10 most expensive products:
#Cote de Blaye
#Thüringer Rostbratwurst
# Mishi Kobe Niku
# Sir Rodney's Marmalade
# Carnarvon Tigers
# Raclette Courdavault
# Manjimup Dried Apples
# Tarte au sucre
# Ipoh Coffee
# Rössle Sauerkraut

query = '''SELECT AVG(HireDate - BirthDate) as hired_age_avg  FROM Employee;'''
query
curs.execute(query)
curs.fetchall()

#37.22 years old

query = '''SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName FROM Product
LEFT OUTER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice;'''

query
curs.execute(query)
curs.fetchall()

#Top 10 most expensive products by Supplier:
#Cote de Blaye - Aux joyeux ecclésiastiques
#Thüringer Rostbratwurst - Plutzer Lebensmittelgroßmärkte AG
# Mishi Kobe Niku - Tokyo Traders
# Sir Rodney's Marmalade - Specialty Biscuits, Ltd.
# Carnarvon Tigers - Pavlova, Ltd.
# Raclette Courdavault - Gai pâturage
# Manjimup Dried Apples - G'day, Mate
# Tarte au sucre - Forêts d'érables
# Ipoh Coffee - Leka Trading
# Rössle Sauerkraut - Plutzer Lebensmittelgroßmärkte AG


query = '''
        SELECT Product.ProductName, Category.CategoryName
        FROM Product
        LEFT OUTER JOIN Category 
        ON  Category.ID = Product.CategoryID
        GROUP BY Product.CategoryID
        ORDER BY COUNT(DISTINCT Product.ID);'''

curs.execute(query)
curs.fetchall()