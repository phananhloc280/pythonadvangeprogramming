import pyodbc
connection = pyodbc.connect('DRIVER = {ODBC Driver 18 for SQL Server}; SERVER=PAL; DATABASE=InventorySaleManagement; DSN=InventorySaleManagement; Trusted_Connection=yes; encrypt=yes; TrustServerCertificate=yes')
db=connection.cursor()

db.execute('Select * from Role')
rows = db.fetchall()

raw_supplier = db.execute("SELECT id FROM Suplier")
supplier = raw_supplier.fetchall()
print(len(supplier))
db.close()
