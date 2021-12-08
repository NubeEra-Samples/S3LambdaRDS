import json
import mysql.connector
import boto3


def lambda_handler(event, context):
    print("*************************************")
    print(event)   

    # mydb = mysql.connector.connect(
    # host="localhost",
    # user="yourusername",
    # password="yourpassword",
    # database="mydatabase"
    # )

    # mycursor = mydb.cursor()

    # sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # val = ("John", "Highway 21")
    # mycursor.execute(sql, val)

    # mydb.commit()

    # print(mycursor.rowcount, "record inserted.")
    print("*************************************")
    return {
        'statusCode': 200,
        'body': json.dumps('Welcome from Lambda!')
    }