#Imports
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import locale
import schedule
import time

def runIt():
    locale.setlocale( locale.LC_ALL, 'en_US')
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('CCC ROI-5b90b2563c40.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('CCC ROI Responses').sheet1
    data = sheet.get_all_values()
    del data[0] #Delete header    

    seenTime = []#Trigger
    seenName = []
    seenEmail = []
    secondEmail = []

    with open('C:/Users/Henry/Desktop/CCC Return on Investment/seenResponse.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            seenEmail.append(row[0])
            seenName.append(row[1] + ' ' + row[2])
            seenTime.append(row[5])
            secondEmail.append(row[4])

    def sendEmail():
        for i in data:
            if i[0] not in seenTime:
                newData = i    
                with open('seenResponse.csv', 'a', newline='') as f: #append to seenResponse.csv with new data from recent form submission
                    fieldNames = ['Email','First','Last','Phone','Second Email', 'Time Stamp']
                    thewriter = csv.DictWriter(f, fieldnames = fieldNames)
                    thewriter.writeheader()
                    thewriter.writerow({'Email': newData[1], 'First' : newData[2], 'Last' : newData[3], 'Phone' : newData[4], 'Second Email' : newData[5], 'Time Stamp' : newData[0]})
                #Total Cost
                aa = int(i[6]) * 30.00
                bb = int(i[7]) * 30.00
                cc = int(i[8]) * 37.50
                dd = int(i[9]) * 149.40
                ee = int(i[10]) * 185.40
                ff = int(i[11]) * 39.00
                gg = int(i[12]) * 27.59
                hh = int(i[13]) * 14.99
                jj = int(i[14]) * 30.00
                kk = int(i[15]) * 22.50
                ll = int(i[16]) * 39.00
                total = aa + bb + cc + dd + ee + ff + gg + hh + jj + kk + ll
                formatedTotal = '${:,.2f}'.format(total)                     
                #ROI Total          
                a = int(i[6]) * 50.00
                b = int(i[7]) * 50.00
                c = int(i[8]) * 62.50
                d = int(i[9]) * 249.00
                e = int(i[10]) * 309.00
                f = int(i[11]) * 65.00
                g = int(i[12]) * 45.99
                h = int(i[13]) * 24.99
                j = int(i[14]) * 49.99
                k = int(i[15]) * 37.50
                l = int(i[16]) * 65
                ROItotal = a + b + c + d + e + f + g + h + j + k + l

                roi = ROItotal - total
                formatedRoi = '${:,.2f}'.format(roi)

                msg = MIMEMultipart()
                msg['From'] = 'hugo@marijuanadoctors.com'
                msg['To'] = i[5]
                msg['Subject'] = i[2] + ' ' + i[3] + "'s Return on Investment"    
                body = "<table style='margin: auto; border: solid 1px black; border-collapse: collapse; text-align: center; font-family: Source Sans Pro;' > <tr style='background-color:  #006927; padding:20px; color:white;'> <th style='padding: 20px;'>Quantity</th> <th>Product</th> <th>Cost</th> </tr> <tr style='border: solid 1px black;background-color:#f2f2f2;'> <td style='border: solid 1px black; padding:20px;'>" + i[6] + "</td> <td style='border: solid 1px black; padding:20px;'>THC-Free CBD Tincture (500mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(aa,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;'> <td style='border: solid 1px black; padding:20px;'>" + i[7] + "</td> <td style='border: solid 1px black; padding:20px;'>THC-Free CBD Capsules (750mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(bb,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;background-color:#f2f2f2;'> <td style='border: solid 1px black; padding:20px;'>" + i[8] + "</td> <td style='border: solid 1px black; padding:20px;'>THC-Free CBD Tincture (1000mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(cc,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;'> <td style='border: solid 1px black; padding:20px;'>" + i[9] + "</td> <td style='border: solid 1px black; padding:20px;'>THC-Free CBD Tincture (4500mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(dd,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;background-color:#f2f2f2;'> <td style='border: solid 1px black; padding:20px;'>" + i[10] + "</td> <td style='border: solid 1px black; padding:20px;'>THC-Free CBD Tincture (6000mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(ee,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;'> <td style='border: solid 1px black; padding:20px;'>" + i[11] + "</td> <td style='border: solid 1px black; padding:20px;'>THC-Free CBD Soft Gel Capsules with Melatonin (750mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(ff,2),grouping=True)) + "</td><tr style='border: solid 1px black;'> <td style='border: solid 1px black; padding:20px;'>" + i[16] + "</td> <td style='border: solid 1px black; padding:20px;'>THC-Free CBD Soft Gel Capsules with Curucmin (750mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(ll,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;background-color:#f2f2f2;'> <td style='border: solid 1px black; padding:20px;'>" + i[12] + "</td> <td style='border: solid 1px black; padding:20px;'>Full Spectrum THC-Free CBD Gummies (250mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(gg,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;'> <td style='border: solid 1px black; padding:20px;'>" + i[13] + "</td> <td style='border: solid 1px black; padding:20px;'>Full Spectrum CBD Topical Cream (2 oz)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(hh,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;background-color:#f2f2f2;'> <td style='border: solid 1px black; padding:20px;'>" + i[14] + "</td> <td style='border: solid 1px black; padding:20px;'>Full Spectrum CBD Topical Cream (4 oz)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(jj,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;'> <td style='border: solid 1px black; padding:20px;'>" + i[15] + "</td> <td style='border: solid 1px black; padding:20px;'>Broad Spectrum CBD Oil for Pets (250mg)</td> <td style='border: solid 1px black; padding:20px;'>"+ str(locale.currency(round(kk,2),grouping=True)) + "</td> </tr> <tr style='border: solid 1px black;background-color:#f2f2f2;'> <td style='border: solid 1px black; padding:25px;border-left:none;border-right:none;'>Total Cost</td> <td style='border: solid 1px black; padding:20px; border-left:none;border-right:none;'><mark style='padding:5px;'>"+ formatedTotal + "</mark></td> <td style='border: solid 1px black; padding:20px; border-left:none;border-right:none;'></td> </tr><tr style='border: solid 1px black;background-color:#f2f2f2;'> <td style='border: solid 1px black; padding:25px;border-left:none;border-right:none;'>Return on Investment</td> <td style='border: solid 1px black; padding:20px; border-left:none;border-right:none;'><mark style='padding:5px;'>"+ formatedRoi + "</mark></td> <td style='border: solid 1px black; padding:20px; border-left:none;border-right:none;'></td> </tr> </table></br>\n<small>*Return on investment is based on SRP"

                #attach the body to the message as html
                msg.attach(MIMEText(body, 'html'))
                print(msg)
                #initilize the sever
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.login('hugo@marijuanadoctors.com', ******)
                #send the email
                server.sendmail(msg['from'], msg['To'], msg.as_string())
                #close the server
                server.quit()
                print('Email Sent to ' + i[5])   

    sendEmail()


schedule.every(1).minutes.do(runIt)

while 1:
    schedule.run_pending()
    time.sleep(1)