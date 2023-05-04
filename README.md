# PyTest and SQL server
This code is to validate tables using pytest and SSQL server

# install pytest using pip

1. pip install -U pytest

# Create a SQL user and enable SQL authentication mode for this new user

verify if system has installed the following packages:

Type:

pip list 

as shown below:

![image](https://user-images.githubusercontent.com/12807393/235483581-0794039d-6435-47ed-a7af-14e36e629385.png)

In case packages below are not installed please type the commands below:

# to verify pip it's installed type:

pip --version
C:\Users\riotb>pip --version
pip 23.0.1 from C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.3056.0_x64__qbz5n2kfra8p0\lib\site-packages\pip (python 3.10)


# to install  pymssql:

pip install pymssql

# Installing SQL server developer edition:

go to:

https://www.microsoft.com/en-us/sql-server/sql-server-downloads

Once installed, follow the wizzard

Important configurations:

look for SQL server configuration manager:

![image](https://user-images.githubusercontent.com/12807393/235489389-dde946ce-8e2f-4518-b3a0-c090e377a0da.png)

Look for the pipes are enabled:

![image](https://user-images.githubusercontent.com/12807393/235489997-e4a93751-07d0-444d-97d2-a9c31dc45d52.png)

TCP is enabled


![image](https://user-images.githubusercontent.com/12807393/235490278-5ca815f3-e63a-4dfb-8a93-33cdb9408236.png)

# Getting the Port and Host Name:

to get the host name, create a new SQL query and type sentence below:

Select Host_name()

![image](https://user-images.githubusercontent.com/12807393/235496425-500c328f-63f3-4051-bbd2-287dc02185ab.png)


to get the port create a new SQL Query :

```sql
USE MASTER

GO

xp_readerrorlog 0, 1, N'Server is listening on'

GO 
```


![image](https://user-images.githubusercontent.com/12807393/235497027-1bab83ea-b7a6-4d1d-864a-ddea6ea2a81d.png)



# To configure SQL authentication and create a new user:

go to properties in SQL server as shown below:

![image](https://user-images.githubusercontent.com/12807393/235498613-48a35f84-60d3-4aa9-9e85-8e5a2ae7ed11.png)

# Executing pytest

write your methods to validate

![image](https://user-images.githubusercontent.com/12807393/236122799-9ad409a9-66ab-4478-82d6-c44fb33e2a16.png)

write your asserst method

![image](https://user-images.githubusercontent.com/12807393/236122910-a0762259-dea9-4c53-a778-eb2a99777365.png)

save your file

# Execute pytest

execute  using: pytest testing.py where testing.py is the file that contain assert methods
you will see a summary results as shown below:
![image](https://user-images.githubusercontent.com/12807393/236123221-2cf944f1-6cd0-4e04-bc2b-612cd2f89991.png)

# Test report

a file executionReport.txt its included. Contains the output from the execution of pytest. Contains a section for fails and also the number of successful checks

doubts: enrique.davila@gmail.com
