
from flask import redirect, url_for, request, render_template, flash, send_file
from app import app
from utilities import export_to_excel, get_price_info
from read_database import get_hot_data, check_if_exits, get_stock, update_hot_stock
from models import db, hot_sell_daily_record, hot_stock
import datetime

price_data = get_price_info()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock')
def stock():
    hstock, htitle = get_stock(hot_stock)
    print(htitle)
    print(hstock)
    return render_template('stock.html',
        len=len,
        htitle=htitle, hstock=hstock   )


@app.route('/hrecord', methods =["GET", "POST"])
def hrecord():

    if request.method == "POST":
        en_opmod = request.form['OP_mode']
        en_date = datetime.datetime.strptime(request.form['Date'], '%Y-%m-%d').date()

        already_ids = check_if_exits(hot_sell_daily_record, en_opmod, en_date)

        if already_ids == []:
            entry_data = []
            entry_dict = {}

            price_dict = {"tsell":0, 'p_mrp':0, 'p_actual':0}

            for item_name in ["Blenders_Pride", "Breezer", "DSP_Balck_180", "DSP_Balck_90", "IB_180", "IB_90", "Mcd_Rum_180", "Mcd_Rum_90", "MCDowells_180", "MCDowells_90", "Oak_Smith_Gold_180", "Oak_Smith_Gold_90", "Oak_Smith_Silver_180", "Oak_Smith_Silver_90", "OC_180", "OC_90", "Old_Monk_180", "Old_Monk_90", "RC_180", "RC_90", "Royal_Stag_180", "Royal_Stag_90", "Royal_Stag_Barel_180", "Royal_Stag_Barel_90", "Signature_180", "other1", "other2"]:
                try:
                    value = int(request.form[item_name])
                except:
                    value = 0
                entry_data.append(value)
                entry_dict[item_name] = value

                if en_opmod == "Daily Sell":
                    if item_name in price_data["hot_drinks"]:
                        try:
                            price_dict["tsell"] += value * price_data["hot_drinks"][item_name][2]
                            price_dict["p_mrp"] += value * ( price_data["hot_drinks"][item_name][2] - price_data["hot_drinks"][item_name][1] )
                            price_dict["p_actual"] += value * ( price_data["hot_drinks"][item_name][2] - price_data["hot_drinks"][item_name][0] )
                        except:
                            pass
            remark = request.form['Remark']

            sell_record = hot_sell_daily_record( en_opmod, en_date, entry_data,   remark, price_dict["tsell"], price_dict["p_mrp"] , price_dict["p_actual"] )
            db.session.add( sell_record )
            db.session.commit()

            if en_opmod == "Daily Sell":
                pass
            elif en_opmod == "New Stock":
                update_hot_stock(db, hot_stock, 'stock', entry_dict, 'add')

            flash(en_opmod+ " entry of "+ str(en_date) +" is added!")  
        else:
            flash("ERROR: "+en_opmod+ " entry of "+ str(en_date) +" is already provided!")  

    return render_template('h_record.html')


@app.route('/export', methods =["GET", "POST"])
def export():

    if request.method == "POST":
        en_opmod = request.form['OP_mode']
        sdate = datetime.datetime.strptime(request.form['SDate'], '%Y-%m-%d').date()
        edate = datetime.datetime.strptime(request.form['EDate'], '%Y-%m-%d').date()
         
        date_ref = str(sdate) +' to ' + str(edate)
        hot_edata, htitle = get_hot_data(en_opmod, sdate, edate)
        
        if hot_edata != []:
            ef_obj = export_to_excel(hot_edata, htitle)

            #flash(en_opmod +' Data of '+ str(sdate) +' to ' + str(edate) +' is exported! ['+str(len(hot_edata))+"]") 
            
            return send_file(ef_obj, download_name="Export "+date_ref+".xls", as_attachment=True)
        else:
            flash("ERROR: "+en_opmod +' Data of '+ date_ref +' is not found') 


    return render_template('export.html')


@app.route('/create_default')
def declare_database():

    for op_mode in ['Stock', 'In Use', 'Total']:
        entry = hot_stock(op_mode, 0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        db.session.add( entry )


    db.session.commit()
    return redirect(url_for('index'))



