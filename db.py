import pymysql

# Open database connection
db = pymysql.connect("localhost","root","rat","build_flats" )
print("connection successfull")