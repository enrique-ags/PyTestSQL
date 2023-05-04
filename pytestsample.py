import pymssql  

def validateTableExist(tableName):

    conn = pymssql.connect(server='DESKTOP-M531GVI\SQLEXPRESS01', user='robot', password='12345', database='AdventureWorks2019')  
    cursor = conn.cursor()  
    cursor.execute("Select count(*) from information_schema.tables where table_name = %s",tableName)
    row =cursor.fetchone()
    while row:
        return row[0]
        row =cursor.fetchone()
    cursor.close()
def validateNotEmptyContactInfo():
    conn = pymssql.connect(server='DESKTOP-M531GVI\SQLEXPRESS01', user='robot', password='12345', database='AdventureWorks2019')  
    cursor = conn.cursor()  
    cursor.execute("Select count(*) FROM [AdventureWorks2019].[Person].[Person]where FirstName is null or LastName is null  or len(FirstName)=0 or len('lastname')=0")
    row =cursor.fetchone()
    while row:
        return row[0]
        row =cursor.fetchone()
    cursor.close()

def validatePhoneType():
    conn = pymssql.connect(server='DESKTOP-M531GVI\SQLEXPRESS01', user='robot', password='12345', database='AdventureWorks2019')  
    cursor = conn.cursor()  
    cursor.execute("SELECT count(*)  FROM [AdventureWorks2019].[Person].[PersonPhone] where PhoneNumberTypeID not in (1,2,3) ")
    row =cursor.fetchone()
    while row:
        return row[0]
        row =cursor.fetchone()
    cursor.close()

def validateNoDuplicatedPhones():
    conn = pymssql.connect(server='DESKTOP-M531GVI\SQLEXPRESS01', user='robot', password='12345', database='AdventureWorks2019')  
    cursor = conn.cursor()  
    cursor.execute("Select sum(ds.countPhones) as duplicatedCounts from (SELECT count([PhoneNumber]) as countPhones FROM [AdventureWorks2019].[Person].[PersonPhone] group by [PhoneNumber] having count ([PhoneNumber]) >1) ds")
    row =cursor.fetchone()
    while row:
        return row[0]
        row =cursor.fetchone()
    cursor.close()

def validateProductSafetyStock():
    conn = pymssql.connect(server='DESKTOP-M531GVI\SQLEXPRESS01', user='robot', password='12345', database='AdventureWorks2019')  
    cursor = conn.cursor()  
    cursor.execute("SELECT count(*) FROM [AdventureWorks2019].[Production].[Product] where SafetyStockLevel <10")
    row =cursor.fetchone()
    while row:
        return row[0]
        row =cursor.fetchone()
    cursor.close()

def validateProductsAreNotEmpty():
    conn = pymssql.connect(server='DESKTOP-M531GVI\SQLEXPRESS01', user='robot', password='12345', database='AdventureWorks2019')  
    cursor = conn.cursor()  
    cursor.execute("SELECT count(*) FROM [AdventureWorks2019].[Production].[Product] where name is null or len(name)=0 or len(name)<=2")
    row =cursor.fetchone()
    while row:
        return row[0]
        row =cursor.fetchone()
    cursor.close()
#validate table exist

def test_tableExist():
    assert validateTableExist('Persons') == 1
#validate table exist
def test_tableExist2():
    assert validateTableExist('Person') == 1

#validate there is no empty data in firstname and lastname
# in table Person
def test_NoEmptyData(): 
    assert validateNotEmptyContactInfo() == 0

#validate only phone types 1,2,3 are present on table phonetype
def test_validPhoneType():
    assert validatePhoneType()==0
#validate no duplicated phones are present on table 
# [Person].[PersonPhone]
def test_NoDuplicatePhones():
    assert  validateNoDuplicatedPhones ==0
#validate safetyProductStock is above 10 producs
def test_validateSafetyStock():
    assert  validateProductSafetyStock()==0
#validate Product Name is not null or len equal zero
def test_validateProductNameNotEmpty():
    assert validateProductsAreNotEmpty()==0







    
     
   
