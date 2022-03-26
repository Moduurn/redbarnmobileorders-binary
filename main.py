# Author: Rajeev M C
# Date :  200-03-24
# program to extract the daily mobile orders for Redbarn stores
# Command arguments : --searchdate get the mobile orders for a given date
#                     --savefolder to specify the  destination folder to keep the extracted files

import requests
import argparse
from datetime import datetime, timedelta, date
import os
import sys
import traceback

def get_dailymobileorder_extract(p_date=None):
    ret_val = None
    apiURL = 'https://dashboard.moduurn.com/getRedBarnsDailyData/'
    try:
        start_date = p_date
        if not p_date:
            start_date = (date.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        # api_headers = {'Authorization': f'Passcode %s' % (merchant['passcode'])}
        # resp = requests.get(cfg.apiURL, json=transaction_search_data, headers=api_headers)
        resp = requests.get(f'{apiURL}{start_date}')
        if resp.status_code == 200:
            ret_val = resp.json()
    except:
        exp = sys.exc_info()
        trce = traceback.format_exc()
        print(trce)
        print(exp)
    return ret_val

def save_mobileorders(p_order_summary, p_target_folder = None):
    try:
        if not p_order_summary:
            return
        if p_target_folder:
            if not os.path.isdir(p_target_folder):
                os.mkdir(p_target_folder)
        for summary in p_order_summary:
            report_date     = summary[0]
            loc_name        = summary[1]
            order_summary   = summary[2]
            store_nbr       = summary[3]
            report_date = (datetime.strptime(report_date, '%Y-%m-%d')).strftime("%m%d%y")
            file_name = f'{report_date}.{store_nbr}'
            if p_target_folder:
                p_target_folder = p_target_folder.strip('\\')
                file_name = f'{p_target_folder}\{file_name}'
            with open(file_name,"w") as file:
                file.write("\n".join( str(plu_summary)  for plu_summary in  order_summary ))
    except:
        exp = sys.exc_info()
        trce = traceback.format_exc()
        print(trce)
        print(exp)

if __name__ == '__main__':
    order_summary   = None
    save_folder     = None
    parser = argparse.ArgumentParser()
    parser.add_argument('--searchdate', type=str,
                        help=' Optional Parameter the specific date for which the mobile order summary is needed in ISO Date format  eg. searchdate=2022-03-22')
    parser.add_argument('--savefolder', type=str,
                        help=' Optional Parameter Folder where the extracted files to be sored.  savefolder=C:\Moduurn')
    args = parser.parse_args()
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Initiated Fetching Moduurn Mobile Orders...')
    if args.searchdate:
        order_summary = get_dailymobileorder_extract(args.searchdate)
    else:
        order_summary = get_dailymobileorder_extract(args.searchdate)
    if not order_summary:
        print('Failed to retrieve the mobile orders summary for the day. Please try after sometime or contact Moduurn team')
    if args.savefolder:
        save_folder = args.savefolder
    else:
        save_folder = '.\\'
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Initiated Saving Moduurn Mobile Orders in {save_folder}')
    save_mobileorders(order_summary, save_folder)
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Saved  Moduurn Mobile Orders in {save_folder}')




