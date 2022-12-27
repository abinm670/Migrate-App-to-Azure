import logging
import azure.functions as func
import psycopg2
import os
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

def main(msg: func.ServiceBusMessage):

    notification_id = int(msg.get_body().decode('utf-8'))
    logging.info('Python ServiceBus queue trigger processed message: %s',notification_id)

    # TODO: Get connection to database
    con=psycopg2.connect(host="postgress1server.postgres.database.azure.com",
                         database='techconfdb',
                         user='abinm670@postgress1server',
                         password='Ahmed1934$'
                         )
    logging.info(f"Connected to Database Successfully")

    
        # TODO: Get notification message and subject from database using the notification_id
    try:
        cor=con.cursor()
        cor.execute("SELECT message, subject from notification WHERE id=%s;",(notification_id,))
        messageContent, subject=cor.fetchone()
        logging.info(f"Message and Subject ID Notfication '{messageContent}':{subject}")
        
        
        
        #     # TODO: Get attendees email and name
        cor.execute("SELECT email, first_name, last_name from attendee;")
        attendees=cor.fetchall()
        # for i in attendees:
            # logging.info(f"list of emails '{i[0]}', and First Name '{i[1]}', last name:'{i[2]}'")
        


        #     # TODO: Loop through each attendee and send an email with a personalized subject
        for x in attendees:
            message= Mail(
                from_email="jeddah_nona_1980@hotmail.com",
                to_emails=x[1],
                subject='User{}:{}'.format(x[2], subject),
                #logging.info(f"Okay '{subject}'")
                plain_text_content=messageContent
                )
            try:
                req=SendGridAPIClient('')
                respond=req.send(message)
                print(respond.body)
                print(respond.status_code)
            except Exception as e:
                print(e)
        
                
        
                
        #     # TODO: Update the notification table by setting the completed date and updating the status with the total number of attendees notified
            total=len(attendees)
            cor.execute("UPDATE notification SET status = %s WHERE id=%s;", (total,notification_id))
            con.commit()
    except (Exception, psycopg2.DatabaseError) as error:
         logging.error(error)
    finally:
    #     # TODO: Close connection`
         con.close()
