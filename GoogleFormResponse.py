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
import pandas as pd

def main():
    print('Checking..')
    #Variables  
    locale.setlocale( locale.LC_ALL, 'en_US')
    scope = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    print('Singing in to Gspread..')
    client = gspread.authorize(creds)
    print('Log in successful')
    sheet = client.open('Return On Investment (Responses)').sheet1
    data = sheet.get_all_values()
    del data[0] #Delete header                                                       
    seenData = []#Trigger

    #Open seenResponse.csv which holds all past responses
    with open('seenResponse.csv') as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            seenData.append(row)
            
    def sendEmail():
        #data variables explained on top
        noData = False
        for i in data:
            #Send ROI Email if data is not in seenData
            if i not in seenData:
                #Append New Data to seenResponse.csv
                newData = [i]
                my_df = pd.DataFrame(newData)
                my_df.to_csv('seenResponse.csv', index=False, mode='a', header=False)
                #Error Catcher if form was filled out with all zerps
                if int(i[6]) == 0 and int(i[7]) == 0 and int(i[8]) == 0 and int(i[9]) == 0 and int(i[10]) == 0 and int(i[11]) == 0 and int(i[13]) == 0 and int(i[14]) == 0 and int(i[15]) == 0 and int(i[16]) == 0 and int(i[17]) == 0:
                        msg = MIMEMultipart()
                        msg['From'] = 'hugo@marijuanadoctors.com'
                        msg['To'] = i[18]
                        msg['Subject'] = i[2] + ' ' + i[3] + "'s Return on Investment" 
                        body = "<body><h3 style='color:rgb(0,54,79);'>Hello, " + i[2] + ' ' + i[3] +"</h3>\n<p style='color:rgb(0,54,79);'> Unfortunatley we could not process your return on investment, due to our minimum purchase order is $1,000. Your total was $0.00 </p>\n<p>Please, Fill out the <a href='https://docs.google.com/forms/d/e/1FAIpQLSdZk4GoC312XBTCC8sYyCIy6HUbDYayojoSF0b2I6M2wyL8Qw/viewform'> form</a> again. </p>\n<p><a href='https://docs.google.com/forms/d/e/1FAIpQLSfL7ZZciHqxwAS7nqK-7cDjC-k3HWZJpUtISpDyU1CGAPvckw/viewform?usp=sf_link'>Click here</a> to schedule a CBD appointment.</p><footer><small><a href='https://www.marijuanadoctors.com'>MarijuanaDoctors.com</a></br> A new kind of heal<span style='color:#20AABD;'>thc</span>are</small></footer></body>"  
                        #attach the body to the message as html
                        msg.attach(MIMEText(body, 'html'))
                        print(msg)
                        #initilize the sever
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('hugo@marijuanadoctors.com', '1sugaray')
                        #send the email
                        server.sendmail(msg['from'], msg['To'], msg.as_string())
                        #close the server
                        server.quit()
                        print('Email sent to ' + i[18]) 
                else:# All other requestes that arent all zeros
                    #CALCULATIONS HERE TO LINE 457
                    #TOTAL COST FOR 1x PURCHASE
                    a = int(i[6]) * 30.00
                    b = int(i[7]) * 37.50
                    c = int(i[8]) * 150.00
                    d = int(i[9]) * 186.00
                    e = int(i[10]) * 22.50
                    f = int(i[11]) * 30.00
                    g = int(i[13]) * 30.00
                    h = int(i[14]) * 39.00
                    j = int(i[15]) * 39.00
                    k = int(i[16]) * 27.59
                    l = int(i[17]) * 14.99
                    total = a + b + c + d + e + f + g + h + j + k + l

                    #TOTAL COST FOR 1 YEAR CONTRACT $1,000 BUT UNDER $2,500
                    aaa = int(i[6]) * 28.80
                    bbb = int(i[7]) * 36.00
                    ccc = int(i[8]) * 144.00
                    ddd = int(i[9]) * 178.56
                    eee = int(i[10]) * 21.60
                    fff = int(i[11]) * 28.80
                    ggg = int(i[13]) * 28.80
                    hhh = int(i[14]) * 37.44
                    jjj = int(i[15]) * 37.44
                    kkk = int(i[16]) * 26.49
                    lll = int(i[17]) * 14.39          
                    x1000 = aaa + bbb + ccc + ddd + eee + fff + ggg + hhh + jjj + kkk + lll

                    #TOTAL COST FOR 1 YEAR CONTRACT $2,500 BUT UNDER $5,000
                    aaaa = int(i[6]) * 27.60
                    bbbb = int(i[7]) * 34.50
                    cccc = int(i[8]) * 138.00
                    dddd = int(i[9]) * 171.12
                    eeee = int(i[10]) * 20.70
                    ffff = int(i[11]) * 27.60
                    gggg = int(i[13]) * 27.60
                    hhhh = int(i[14]) * 35.88
                    jjjj = int(i[15]) * 35.88
                    kkkk = int(i[16]) * 25.38
                    llll = int(i[17]) * 13.79          
                    x2500 = aaaa + bbbb + cccc + dddd + eeee + ffff + gggg + hhhh + jjjj + kkkk + llll

                    #TOTAL COST FOR 1 YEAR CONTRACT $5,000 BUT UNDER $10,000
                    aaaaa = int(i[6]) * 26.40
                    bbbbb = int(i[7]) * 33.00
                    ccccc = int(i[8]) * 132.00
                    ddddd = int(i[9]) * 163.68
                    eeeee = int(i[10]) * 19.80
                    fffff = int(i[11]) * 26.40
                    ggggg = int(i[13]) * 26.40
                    hhhhh = int(i[14]) * 34.32
                    jjjjj = int(i[15]) * 34.32
                    kkkkk = int(i[16]) * 24.28
                    lllll = int(i[17]) * 13.19          
                    x5000 = aaaaa + bbbbb + ccccc + ddddd + eeeee + fffff + ggggg + hhhhh + jjjjj + kkkkk + lllll            

                    #TOTAL COST FOR 1 YEAR CONTRACT OVER $10,000
                    aaaaaa = int(i[6]) * 25.20
                    bbbbbb = int(i[7]) * 31.50
                    cccccc = int(i[8]) * 126.00
                    dddddd = int(i[9]) * 156.24
                    eeeeee = int(i[10]) * 18.90
                    ffffff = int(i[11]) * 25.20
                    gggggg = int(i[13]) * 25.20
                    hhhhhh = int(i[14]) * 32.76
                    jjjjjj = int(i[15]) * 32.76
                    kkkkkk = int(i[16]) * 23.18
                    llllll = int(i[17]) * 12.59          
                    x10000 = aaaaaa + bbbbbb + cccccc + dddddd + eeeeee + ffffff + gggggg + hhhhhh + jjjjjj + kkkkkk + llllll

                    #TOTAL RETURN BASED ON SRP 
                    aa = int(i[6]) * 50.00
                    bb = int(i[7]) * 62.50
                    cc = int(i[8]) * 249.00
                    dd = int(i[9]) * 309.00
                    ee = int(i[10]) * 37.50
                    ff = int(i[11]) * 50.00
                    gg = int(i[13]) * 50.00
                    hh = int(i[14]) * 65.00
                    jj = int(i[15]) * 65.00
                    kk = int(i[16]) * 45.99
                    ll = int(i[17]) * 24.99            
                    totalReturn = aa + bb + cc + dd + ee + ff + gg + hh + jj + kk + ll

                    #Normal 1x Purchase total formatted
                    formattedTotal = '${:,.2f}'.format(total)

                    #ROI FOR 1x PURCHASE COST
                    roi = totalReturn - total
                    formattedRoi = '${:,.2f}'.format(roi)

                    x1000total = '${:,.2f}'.format(x1000)
                    x1000roi = totalReturn - x1000

                    x2500Total = '${:,.2f}'.format(x2500)
                    x2500roi = totalReturn - x2500

                    x5000Total = '${:,.2f}'.format(x5000)
                    x5000roi = totalReturn - x5000

                    x10000Total = '${:,.2f}'.format(x10000)
                    x10000roi = totalReturn - x10000
                    #TRY STATEMENTS TO HANDLE ZERO DIVISION ERRORS
                    #INDIVIDUAL MARGINS
                    #1TIME PURCHASE INDIVIDUAL MARGINS
                    #T500mg = (aa - a) / aa
                    try:
                        T500mg = (aa - a) / a
                    except ZeroDivisionError as ex:
                        T500mg = 0
                    try:
                        T1000mg = (bb - b) / b
                    except ZeroDivisionError as ex:
                        T1000mg = 0
                    try:
                        T4500mg = (cc - c) / c
                    except ZeroDivisionError as ex:
                        T4500mg = 0
                    try: 
                        T6000mg = (dd - d) / d 
                    except ZeroDivisionError as ex:
                        T6000mg = 0
                    try:
                        T250mg = (ee - e) / e
                    except ZeroDivisionError as ex:
                        T250mg = 0
                    try:               
                        C4oz = (ff - f) / f 
                    except ZeroDivisionError as ex:
                        C4oz = 0
                    try:
                        Capsules = (gg - g) / g
                    except ZeroDivisionError as ex:
                        Capsules = 0
                    try:
                        CapsulesM = (hh - h) / h
                    except ZeroDivisionError as ex:
                        CapsulesM = 0
                    try:
                        CapsulesC = (jj - j) / j
                    except ZeroDivisionError as ex:
                        CapsulesC = 0
                    try:
                        Gummies = (kk - k) / k
                    except ZeroDivisionError as ex:
                        Gummies = 0
                    try:
                        TopCream = (ll - l) / l
                    except ZeroDivisionError as ex:
                        TopCream = 0

                    #1,000 Year Contract Margins
                    try:
                        T500mg1 = (aa - aaa) / aaa
                    except ZeroDivisionError as ex:
                        T500mg1 = 0
                    try:
                        T1000mg1 = (bb - bbb) / bbb
                    except ZeroDivisionError as ex:
                        T1000mg1 = 0
                    try:
                        T4500mg1 = (cc - ccc) / ccc
                    except ZeroDivisionError as ex:
                        T4500mg1 = 0
                    try:
                        T6000mg1 = (dd - ddd) / ddd
                    except ZeroDivisionError as ex:
                        T6000mg1 = 0
                    try:
                        T250mg1 = (ee - eee) / eee             
                    except ZeroDivisionError as ex:
                        T250mg1 = 0
                    try:
                        C4oz1 = (ff - fff) / fff
                    except ZeroDivisionError as ex:
                        C4oz1 = 0
                    try:                 
                        Capsules1 = (gg - ggg) / ggg
                    except ZeroDivisionError as ex:
                        Capsules1 = 0
                    try:
                        CapsulesM1 = (hh - hhh) / hhh 
                    except ZeroDivisionError as ex:
                        CapsulesM1 = 0
                    try:
                        CapsulesC1 = (jj - jjj) / jjj
                    except ZeroDivisionError as ex:
                        CapsulesC1 = 0
                    try:
                        Gummies1 = (kk - kkk) / kkk
                    except ZeroDivisionError as ex:
                        Gummies1 = 0
                    try:
                        TopCream1 = (ll - lll) / lll
                    except ZeroDivisionError as ex:
                        TopCream1 = 0

                    #2,500 Year Contract Margins
                    try:
                        T500mg2 = (aa - aaaa) / aaaa
                    except ZeroDivisionError as ex:
                        T500mg2 = 0
                    try:
                        T1000mg2 = (bb - bbbb) / bbbb
                    except ZeroDivisionError as ex:
                        T1000mg2 = 0
                    try:
                        T4500mg2 = (cc - cccc) / cccc
                    except ZeroDivisionError as ex:
                        T4500mg2 = 0
                    try:
                        T6000mg2 = (dd - dddd) / dddd
                    except ZeroDivisionError as ex:
                        T6000mg2 = 0
                    try:
                        T250mg2 = (ee - eeee) / eeee
                    except ZeroDivisionError as ex:
                        T250mg2 = 0
                    try:          
                        C4oz2 = (ff - ffff) / ffff
                    except ZeroDivisionError as ex:
                        C4oz2 = 0
                    try:
                        Capsules2 = (gg - gggg) / gggg
                    except ZeroDivisionError as ex:
                        Capsules2 = 0
                    try:
                        CapsulesM2 = (hh - hhhh) / hhhh
                    except ZeroDivisionError as ex:
                        CapsulesM2 = 0
                    try:
                        CapsulesC2 = (jj - jjjj) / jjjj
                    except ZeroDivisionError as ex:
                        CapsulesC2 = 0
                    try: 
                        Gummies2 = (kk - kkkk) / kkkk
                    except ZeroDivisionError as ex:
                        Gummies2 = 0
                    try:
                        TopCream2 = (ll - llll) / llll
                    except ZeroDivisionError as ex:
                        TopCream2 = 0
                    
                    #5,000 Year Contract Margins
                    try:
                        T500mg3 = (aa - aaaaa) / aaaaa
                    except ZeroDivisionError as ex:
                        T500mg3 = 0
                    try:
                        T1000mg3 = (bb - bbbbb) / bbbbb
                    except ZeroDivisionError as ex:
                        T1000mg3 = 0
                    try:
                        T4500mg3 = (cc - ccccc) / ccccc
                    except ZeroDivisionError as ex:
                        T4500mg3 = 0
                    try: 
                        T6000mg3 = (dd - ddddd) / ddddd
                    except ZeroDivisionError as ex:
                        T6000mg3 = 0
                    try:
                        T250mg3 = (ee - eeeee) / eeeee
                    except ZeroDivisionError as ex:
                        T250mg3 = 0
                    try:             
                        C4oz3 = (ff - fffff) / fffff
                    except ZeroDivisionError as ex:
                        C4oz3 = 0
                    try: 
                        Capsules3 = (gg - ggggg) / ggggg
                    except ZeroDivisionError as ex:
                        Capsules3 = 0
                    try:
                        CapsulesM3 = (hh - hhhhh) / hhhhh
                    except ZeroDivisionError as ex:
                        CapsulesM3 = 0
                    try:
                        CapsulesC3 = (jj - jjjjj) / jjjjj
                    except ZeroDivisionError as ex:
                        CapsulesC3 = 0
                    try:
                        Gummies3 = (kk - kkkkk) / kkkkk
                    except ZeroDivisionError as ex:
                        Gummies3 = 0
                    try:
                        TopCream3 = (ll - lllll) / lllll
                    except ZeroDivisionError as ex:
                        TopCream3 = 0

                    #5,000 Year Contract Margins
                    try:
                        T500mg4 = (aa - aaaaaa) / aaaaaa
                    except ZeroDivisionError as ex:
                        T500mg4 = 0
                    try:             
                        T1000mg4 = (bb - bbbbbb) / bbbbbb
                    except ZeroDivisionError as ex:
                        T1000mg4 = 0
                    try:
                        T4500mg4 = (cc - cccccc) / cccccc 
                    except ZeroDivisionError as ex:
                        T4500mg4 = 0
                    try:
                        T6000mg4 = (dd - dddddd) / dddddd 
                    except ZeroDivisionError as ex:
                        T6000mg4 = 0
                    try:
                        T250mg4 = (ee - eeeeee) / eeeeee             
                    except ZeroDivisionError as ex:
                        T250mg4 = 0
                    try:
                        C4oz4 = (ff - ffffff) / ffffff 
                    except ZeroDivisionError as ex:
                        C4oz4 = 0
                    try:
                        Capsules4 = (gg - gggggg) / gggggg
                    except ZeroDivisionError as ex:
                        Capsules4 = 0
                    try:
                        CapsulesM4 = (hh - hhhhhh) / hhhhhh 
                    except ZeroDivisionError as ex:
                        CapsulesM4 = 0
                    try:
                        CapsulesC4 = (jj - jjjjjj) / jjjjjj 
                    except ZeroDivisionError as ex:
                        CapsulesC4 = 0
                    try:
                        Gummies4 = (kk - kkkkkk) / kkkkkk 
                    except ZeroDivisionError as ex:
                        Gummies4 = 0
                    try:
                        TopCream4 = (ll - llllll) / llllll
                    except ZeroDivisionError as ex:
                        TopCream4 = 0

                    #MARGIN TOTAl
                    margins = roi / total
                    x1000M = x1000roi / x1000
                    x2500M = x2500roi / x2500
                    x5000M = x5000roi / x5000
                    x10000M = x10000roi / x10000

                    #Savings 1K
                    savingsAAAA = a - aaa
                    savingsBBBB = b - bbb
                    savingsCCCC = c - ccc
                    savingsDDDD = d - ddd
                    savingsEEEE = e - eee
                    savingsFFFF = f - fff
                    savingsGGGG = g - ggg
                    savingsHHHH = h - hhh
                    savingsJJJJ = j - jjj
                    savingsKKKK = k - kkk
                    savingsLLLL = l - lll
                    totalSavings1k = savingsAAAA + savingsBBBB + savingsCCCC + savingsDDDD + savingsEEEE + savingsFFFF + savingsGGGG + savingsHHHH + savingsJJJJ + savingsKKKK + savingsLLLL            
                    #Savings 2500 but less than 5K
                    savingsAAA = a - aaaa
                    savingsBBB = b - bbbb
                    savingsCCC = c - cccc
                    savingsDDD = d - dddd
                    savingsEEE = e - eeee
                    savingsFFF = f - ffff
                    savingsGGG = g - gggg
                    savingsHHH = h - hhhh 
                    savingsJJJ = j - jjjj
                    savingsKKK = k - kkkk
                    savingsLLL = l - llll
                    totalSavings2k = savingsAAA + savingsBBB + savingsCCC + savingsDDD + savingsEEE + savingsFFF + savingsGGG + savingsHHH + savingsJJJ + savingsKKK + savingsLLL            
                    #Savings 5K but less than 10k
                    savingsAA = a - aaaaa
                    savingsBB = b - bbbbb
                    savingsCC = c - ccccc
                    savingsDD = d - ddddd
                    savingsEE = e - eeeee
                    savingsFF = f - fffff 
                    savingsGG = g - ggggg
                    savingsHH = h - hhhhh 
                    savingsJJ = j - jjjjj
                    savingsKK = k - kkkkk
                    savingsLL = l - lllll
                    totalSavings5k = savingsAA + savingsBB + savingsCC + savingsDD + savingsEE + savingsFF + savingsGG + savingsHH + savingsJJ + savingsKK + savingsLL            
                    #SAVINGS OVER $10,000
                    savingsA = a - aaaaaa
                    savingsB = b - bbbbbb
                    savingsC = c - cccccc
                    savingsD = d - dddddd
                    savingsE = e - eeeeee 
                    savingsF = f - ffffff 
                    savingsG = g - gggggg
                    savingsH = h - hhhhhh 
                    savingsJ = j - jjjjjj
                    savingsK = k - kkkkkk
                    savingsL = l - llllll
                    totalSavings10k = savingsA + savingsB + savingsC + savingsD + savingsE + savingsF + savingsG + savingsH + savingsJ + savingsK + savingsL

                    #If statements to properly output discounts according to total
                    if total < 1000:
                        msg = MIMEMultipart()
                        msg['From'] = 'hugo@marijuanadoctors.com'
                        msg['To'] = i[18]
                        msg['Subject'] = i[2] + ' ' + i[3] + "'s Return on Investment" 
                        body = "<body><h3 style='color:rgb(0,54,79);'>Hello, " + i[2] + ' ' + i[3] +"</h3>\n<p style='color:rgb(0,54,79);'> Unfortunatley we could not process your return on investment, due to our minimum purchase order is $1,000. Your total was " + formattedTotal + " </p>\n<p>Please, Fill out the <a href='https://docs.google.com/forms/d/e/1FAIpQLSdZk4GoC312XBTCC8sYyCIy6HUbDYayojoSF0b2I6M2wyL8Qw/viewform'> form</a> again. </p>\n<p><a href='https://docs.google.com/forms/d/e/1FAIpQLSfL7ZZciHqxwAS7nqK-7cDjC-k3HWZJpUtISpDyU1CGAPvckw/viewform?usp=sf_link'>Click here</a> to schedule a CBD appointment.</p><footer><small><a href='https://www.marijuanadoctors.com'>MarijuanaDoctors.com</a></br> A new kind of heal<span style='color:#20AABD;'>thc</span>are</small></footer></body>"  
                        #attach the body to the message as html
                        msg.attach(MIMEText(body, 'html'))
                        print(msg)
                        #initilize the sever
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('hugo@marijuanadoctors.com', '1sugaray')
                        #send the email
                        server.sendmail(msg['from'], msg['To'], msg.as_string())
                        #close the server
                        server.quit()
                        print('Email sent to ' + i[18]) 
                    if total > 999.99 and total < 2500.00:
                        msg = MIMEMultipart()
                        msg['From'] = 'hugo@marijuanadoctors.com'
                        msg['To'] = i[18]
                        msg['Subject'] = i[2] + ' ' + i[3] + "'s Return on Investment" 
                        msg['Cc'] = 'zena@marijuanadoctors.com'
                        body = "<body></br><h3 style='color:rgb(0,54,79);'>Hello, " + i[2] + ' ' + i[3] +"</h3><table style='border: 1px solid black;border-collapse: collapse;margin-left: auto;margin-right: auto;'><tr><th style='text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;border: 1px solid black;border-collapse: collapse;'>Quantity</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Product</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Time Purchase Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Year Contract Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Savings</th><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[6] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE CBD™ Tincture 500mg (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(a,2),grouping=True)) + "</br><span style='text-align:right;'> /ROI: "+ "{0:.0%}".format(T500mg) +"</span></td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(aaa,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T500mg1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsAAAA,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[7] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tincture 1000mg (SRP $62.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(b,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T1000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(bbb,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T1000mg1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsBBBB,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[8] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 4500mg (SRP $249.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(c,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ccc,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsCCCC,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[9] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 6000mg (SRP $309.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(d,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ddd,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsDDDD,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[10] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Pet Line 250mg Tincture K-9 (Pets) (SRP $37.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(e,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(eee,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsEEEE,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[11] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ Muscle Cream 4oz (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(f,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(fff,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsFFFF,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[13] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Capsules (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(g,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ggg,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsGGGG,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[14] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Melatonin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(h,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(hhh,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM1) + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsHHHH,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[15] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Curcumin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(j,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(jjj,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsJJJJ,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[16] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum THC-Free™ CBD Gummies (250mg) (SRP $45.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(k,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(kkk,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsKKKK,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[17] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum CBD Topical Cream (2 oz) (SRP $24.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(l,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(lll,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream1) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsLLLL,2),grouping=True)) + "</td></tr><tr style='border-left: none; border-right: none;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total Investment: " + formattedTotal + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total Investment: " + x1000total + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;'><mark>1 Year Contract Savings Per Month: "+ '${:,.2f}'.format(totalSavings1k) +"</mark></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'><a href='https://docs.google.com/spreadsheets/d/1vWimQ9xRF51BiBLouxPSAPBMxjZAU81qlVrxo716QBk/edit?usp=sharing'>click here to see a SRP breakdown.</a></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>ROI: "+ formattedRoi +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>ROI: "+ '${:,.2f}'.format(x1000roi) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'>Margin: "+  "{0:.0%}".format(margins) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Margin: "+  "{0:.0%}".format(x1000M) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr></table><small>*Return on investment is based on SRP</small></br>\n<div style='background-color:#00364F;'><p style='color:white; padding:20px;text-align:center;'>We appreciate you taking the time to consider significantly increasing the revenue in your business. We take great pride at bringing our clients great medical grade products with extremely competitive pricing. With all clients that invest in their business with our 1-year contract, we offer guidance and training for you and your staff to achieve the best results.</br>Please <a href='https://docs.google.com/forms/d/1a1SsAw5nBPqzlQP7ln_mqqVzt7oX7ucEZlGpIqTNiBw/'>Click Here</a> to to schedule an appointment with one of our dedicated staff members.</p></div>\n</body><footer><small><a href='https://www.marijuanadoctors.com'>MarijuanaDoctors.com</a></br> A new kind of heal<span style='color:#20AABD;'>thc</span>are</small></footer></body>"
                        #attach the body to the message as html
                        msg.attach(MIMEText(body, 'html'))
                        print(msg)
                        #initilize the sever
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('hugo@marijuanadoctors.com', '1sugaray')
                        #send the email
                        server.sendmail(msg['from'], msg['To'], msg.as_string())
                        #close the server
                        server.quit()
                        print('Email sent to ' + i[18])
                    if total > 2499.99 and total < 5000.00:
                        msg = MIMEMultipart()
                        msg['From'] = 'hugo@marijuanadoctors.com'
                        msg['To'] = i[18]
                        msg['Subject'] = i[2] + ' ' + i[3] + "'s Return on Investment" 
                        msg['Cc'] = 'zena@marijuanadoctors.com'
                        body = "<body></br><h3 style='color:rgb(0,54,79);'>Hello, " + i[2] + ' ' + i[3] +"</h3><table style='border: 1px solid black;border-collapse: collapse;margin-left: auto;margin-right: auto;'><tr><th style='text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;border: 1px solid black;border-collapse: collapse;'>Quantity</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Product</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Time Purchase Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Year Contract Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Savings</th><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[6] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE CBD™ Tincture 500mg (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(a,2),grouping=True)) + "</br><span style='text-align:right;'> /ROI: "+ "{0:.0%}".format(T500mg) +"</span></td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(aaaa,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T500mg2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsAAA,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[7] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tincture 1000mg (SRP $62.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(b,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T1000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(bbbb,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T1000mg2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsBBB,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[8] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 4500mg (SRP $249.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(c,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(cccc,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsCCC,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[9] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 6000mg (SRP $309.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(d,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(dddd,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsDDD,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[10] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Pet Line 250mg Tincture K-9 (Pets) (SRP $37.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(e,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(eeee,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsEEE,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[11] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ Muscle Cream 4oz (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(f,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ffff,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsFFF,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[13] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Capsules (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(g,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(gggg,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsGGG,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[14] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Melatonin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(h,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(hhhh,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM2) + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsHHH,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[15] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Curcumin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(j,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(jjjj,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsJJJ,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[16] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum THC-Free™ CBD Gummies (250mg) (SRP $45.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(k,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(kkkk,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsKKK,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[17] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum CBD Topical Cream (2 oz) (SRP $24.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(l,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(llll,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream2) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsLLL,2),grouping=True)) + "</td></tr><tr style='border-left: none; border-right: none;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total Investment: " + formattedTotal + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total Investment: " + x2500Total  + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;'><mark>1 Year Contract Savings Per Month: "+ '${:,.2f}'.format(totalSavings2k) +"</mark></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'><a href='https://docs.google.com/spreadsheets/d/1vWimQ9xRF51BiBLouxPSAPBMxjZAU81qlVrxo716QBk/edit?usp=sharing'>click here to see a SRP breakdown.</a></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>ROI: "+ formattedRoi +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>ROI: "+ '${:,.2f}'.format(x2500roi) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'>Margin: "+  "{0:.0%}".format(margins) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Margin: "+ "{0:.0%}".format(x2500M) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr></table><small>*Return on investment is based on SRP</small></br>\n<div style='background-color:#00364F;'><p style='color:white; padding:20px;text-align:center;'>We appreciate you taking the time to consider significantly increasing the revenue in your business. We take great pride at bringing our clients great medical grade products with extremely competitive pricing. With all clients that invest in their business with our 1-year contract, we offer guidance and training for you and your staff to achieve the best results.</br>Please <a href='https://docs.google.com/forms/d/1a1SsAw5nBPqzlQP7ln_mqqVzt7oX7ucEZlGpIqTNiBw/'>Click Here</a> to to schedule an appointment with one of our dedicated staff members.</p></div>\n</body><footer><small><a href='https://www.marijuanadoctors.com'>MarijuanaDoctors.com</a></br> A new kind of heal<span style='color:#20AABD;'>thc</span>are</small></footer></body>"
                        #attach the body to the message as html
                        msg.attach(MIMEText(body, 'html'))
                        print(msg)
                        #initilize the sever
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('hugo@marijuanadoctors.com', '1sugaray')
                        #send the email
                        server.sendmail(msg['from'], msg['To'], msg.as_string())
                        #close the server
                        server.quit()
                        print('Email sent to ' + i[18])
                    if total > 4999.99 and total < 10000.00:
                        msg = MIMEMultipart()
                        msg['From'] = 'hugo@marijuanadoctors.com'
                        msg['To'] = i[18]
                        msg['Subject'] = i[2] + ' ' + i[3] + "'s Return on Investment" 
                        msg['Cc'] = 'zena@marijuanadoctors.com'
                        body = "<body></br><h3 style='color:rgb(0,54,79);'>Hello, " + i[2] + ' ' + i[3] +"</h3><table style='border: 1px solid black;border-collapse: collapse;margin-left: auto;margin-right: auto;'><tr><th style='text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;border: 1px solid black;border-collapse: collapse;'>Quantity</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Product</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Time Purchase Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Year Contract Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Savings</th><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[6] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE CBD™ Tincture 500mg (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(a,2),grouping=True)) + "</br><span style='text-align:right;'> /ROI: "+ "{0:.0%}".format(T500mg) +"</span></td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(aaaaa,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T500mg3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsAA,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[7] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tincture 1000mg (SRP $62.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(b,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T1000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(bbbbb,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T1000mg3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsBB,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[8] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 4500mg (SRP $249.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(c,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ccccc,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsCC,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[9] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 6000mg (SRP $309.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(d,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ddddd,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsDD,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[10] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Pet Line 250mg Tincture K-9 (Pets) (SRP $37.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(e,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(eeeee,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsEE,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[11] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ Muscle Cream 4oz (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(f,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(fffff,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsFF,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[13] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Capsules (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(g,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ggggg,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsGG,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[14] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Melatonin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(h,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(hhhhh,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM3) + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsHH,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[15] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Curcumin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(j,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(jjjjj,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsJJ,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[16] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum THC-Free™ CBD Gummies (250mg) (SRP $45.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(k,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(kkkkk,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsKK,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[17] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum CBD Topical Cream (2 oz) (SRP $24.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(l,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(lllll,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream3) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsLL,2),grouping=True)) + "</td></tr><tr style='border-left: none; border-right: none;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total Investment: " + formattedTotal + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total Investment: " + x5000Total  + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;'><mark>1 Year Contract Savings Per Month: "+ '${:,.2f}'.format(totalSavings5k) +"</mark></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'><a href='https://docs.google.com/spreadsheets/d/1vWimQ9xRF51BiBLouxPSAPBMxjZAU81qlVrxo716QBk/edit?usp=sharing'>click here to see a SRP breakdown.</a></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>ROI: "+ formattedRoi +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>ROI: "+ '${:,.2f}'.format(x5000roi) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'>Margin: "+  "{0:.0%}".format(margins) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Margin: "+ "{0:.0%}".format(x5000M) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr></table><small>*Return on investment is based on SRP</small></br>\n<div style='background-color:#00364F;'><p style='color:white; padding:20px;text-align:center;'>We appreciate you taking the time to consider significantly increasing the revenue in your business. We take great pride at bringing our clients great medical grade products with extremely competitive pricing. With all clients that invest in their business with our 1-year contract, we offer guidance and training for you and your staff to achieve the best results.</br>Please <a href='https://docs.google.com/forms/d/1a1SsAw5nBPqzlQP7ln_mqqVzt7oX7ucEZlGpIqTNiBw/'>Click Here</a> to to schedule an appointment with one of our dedicated staff members.</p></div>\n</body><footer><small><a href='https://www.marijuanadoctors.com'>MarijuanaDoctors.com</a></br> A new kind of heal<span style='color:#20AABD;'>thc</span>are</small></footer></body>"
                        #attach the body to the message as html
                        msg.attach(MIMEText(body, 'html'))
                        print(msg)
                        #initilize the sever
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('hugo@marijuanadoctors.com', '1sugaray')
                        #send the email
                        server.sendmail(msg['from'], msg['To'], msg.as_string())
                        #close the server
                        server.quit()
                        print('Email sent to ' + i[18])                
                    if total > 9999.99:
                        msg = MIMEMultipart()
                        msg['From'] = 'hugo@marijuanadoctors.com'
                        msg['To'] = i[18]
                        msg['Subject'] = i[2] + ' ' + i[3] + "'s Return on Investment" 
                        msg['Cc'] = 'zena@marijuanadoctors.com'
                        body = "<body></br><h3 style='color:rgb(0,54,79);'>Hello, " + i[2] + ' ' + i[3] +"</h3><table style='border: 1px solid black;border-collapse: collapse;margin-left: auto;margin-right: auto;'><tr><th style='text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;border: 1px solid black;border-collapse: collapse;'>Quantity</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Product</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Time Purchase Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>One Year Contract Cost & Margin</th><th style='border: 1px solid black;border-collapse: collapse;text-align: center;background-color: #00364F;color: white;padding: 25px;font-family: Arial Black;font-size: 15px;'>Savings</th><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[6] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE CBD™ Tincture 500mg (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(a,2),grouping=True)) + "</br><span style='text-align:right;'> /ROI: "+ "{0:.0%}".format(T500mg) +"</span></td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(aaaaaa,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T500mg4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsA,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[7] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tincture 1000mg (SRP $62.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(b,2),grouping=True)) + "/ROI: "+ "{0:.0%}".format(T1000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(bbbbbb,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T1000mg4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsB,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[8] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 4500mg (SRP $249.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(c,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(cccccc,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T4500mg4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsC,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[9] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Tinture 6000mg (SRP $309.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(d,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(dddddd,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T6000mg4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsD,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[10] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ CBD Pet Line 250mg Tincture K-9 (Pets) (SRP $37.50)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(e,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(eeeeee,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(T250mg4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsE,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[11] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-FREE™ Muscle Cream 4oz (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(f,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(ffffff,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(C4oz4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsF,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[13] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Capsules (SRP $50.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(g,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(gggggg,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Capsules4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsG,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[14] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Melatonin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(h,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(hhhhhh,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesM4) + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsH,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[15] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>THC-Free™ CBD Soft Gel Capsules with Curcumin (500mg) (SRP $65.00)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(j,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(jjjjjj,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(CapsulesC4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsJ,2),grouping=True)) + "</td></tr><tr><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[16] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum THC-Free™ CBD Gummies (250mg) (SRP $45.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(k,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(kkkkkk,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(Gummies4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsK,2),grouping=True)) + "</td></tr><tr style='background-color: #f2f2f2;'><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + i[17] + "</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Full Spectrum CBD Topical Cream (2 oz) (SRP $24.99)</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(l,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Cost: " + str(locale.currency(round(llllll,2),grouping=True)) + " /ROI: "+ "{0:.0%}".format(TopCream4) +"</td><td style='border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>" + str(locale.currency(round(savingsL,2),grouping=True)) + "</td></tr><tr style='border-left: none; border-right: none;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total Investment: " + formattedTotal + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total Investment: " + x10000Total + "</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;'><mark>1 Year Contract Savings Per Month: "+ '${:,.2f}'.format(totalSavings10k) +"</mark></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'><a href='https://docs.google.com/spreadsheets/d/1vWimQ9xRF51BiBLouxPSAPBMxjZAU81qlVrxo716QBk/edit?usp=sharing'>click here to see a SRP breakdown.</a></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>Total: "+ '${:,.2f}'.format(totalReturn) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'><mark>ROI: "+ formattedRoi +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'><mark>ROI: "+ '${:,.2f}'.format(x10000roi) +"</mark></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr><tr style='border-left: none; border-right: none;;'><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-right: none;'>Margin: "+  "{0:.0%}".format(margins) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;'>Margin: "+ "{0:.0%}".format(x10000M) +"</td><td style = 'border: 1px solid black;border-collapse: collapse;text-align: center;padding: 15px;font-family: Lucida Sans Unicode;border-left: none;border-right: none;'></td></tr></table><small>*Return on investment is based on SRP</small></br>\n<div style='background-color:#00364F;'><p style='color:white; padding:20px;text-align:center;'>We appreciate you taking the time to consider significantly increasing the revenue in your business. We take great pride at bringing our clients great medical grade products with extremely competitive pricing. With all clients that invest in their business with our 1-year contract, we offer guidance and training for you and your staff to achieve the best results.</br>Please <a href='https://docs.google.com/forms/d/1a1SsAw5nBPqzlQP7ln_mqqVzt7oX7ucEZlGpIqTNiBw/'>Click Here</a> to to schedule an appointment with one of our dedicated staff members.</p></div>\n</body><footer><small><a href='https://www.marijuanadoctors.com'>MarijuanaDoctors.com</a></br> A new kind of heal<span style='color:#20AABD;'>thc</span>are</small></footer></body>"
                        #attach the body to the message as html
                        msg.attach(MIMEText(body, 'html'))
                        print(msg)
                        #initilize the sever
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login('hugo@marijuanadoctors.com', '1sugaray')
                        #send the email
                        server.sendmail(msg['from'], msg['To'], msg.as_string())
                        #close the server
                        server.quit()
                        print('Email sent to ' + i[18])
                
            else:#Else to no new data that outputs No New Data only once
                noData = True
        if noData == True:
            print('No New Data')
            noData = False
    sendEmail()
    print('Checking again in 3 minutes..')
    print('')

#Schedule to execute every 3 minutes
schedule.every(3).minutes.do(main)

#While loop that runs the pending schedule
while 1:
    schedule.run_pending()
    time.sleep(1)