from models import hot_sell_daily_record

def get_hot_data(en_opmod, sdate, edate):
    og_titles = [ title for title in hot_sell_daily_record.__table__.columns.keys() ]
    titles =[ title.replace("_", " ") for title in og_titles ]

    #data_entries = hot_sell_daily_record.query.filter_by(OP_mode=en_opmod).all()
    if en_opmod != "All":
        filter = ( (hot_sell_daily_record.OP_mode == en_opmod) & (hot_sell_daily_record.Date >= sdate) & (hot_sell_daily_record.Date <= edate) )
    else:
        filter = ( (hot_sell_daily_record.Date >= sdate) & (hot_sell_daily_record.Date <= edate) )
    
    data_entries = hot_sell_daily_record.query.filter( filter ).order_by(hot_sell_daily_record.Date).all()


    out_data = []
    for entry in data_entries:
        entry_dict = entry.__dict__
        row_data = [ entry_dict[title] for title in og_titles]
        out_data.append(row_data)

    return out_data, titles


def get_stock(table_obj):
    og_titles = [ title for title in table_obj.__table__.columns.keys() ][1:]
    titles = [ title.replace("_", " ") for title in og_titles ]

    filter = ( (table_obj.id == 1) | (table_obj.id >= 2) | (table_obj.id <= 3) )

    
    data_entries = table_obj.query.filter( filter ).order_by(table_obj.id).all()


    out_data = []
    for entry in data_entries:
        entry_dict = entry.__dict__
        row_data = [ entry_dict[title] for title in og_titles]
        out_data.append(row_data)

    return out_data, titles



def check_if_exits(table_obj, en_opmod, en_date):
    filter = ( (table_obj.OP_mode == en_opmod) & (hot_sell_daily_record.Date == en_date) )
    
    ids = []
    data_entries = hot_sell_daily_record.query.filter( filter ).all()
    for entry in data_entries:
        entry_dict = entry.__dict__
        ids.append( entry_dict["id"] )

        #table_obj.query.filter_by(id=entry_dict["id"]).delete()

    return ids


def update_hot_stock(db, table_obj, op_mod, entry_data, mode):
    if op_mod=='stock':
        entry = table_obj.query.filter_by(id=1).first()
        sntry = table_obj.query.filter_by(id=2).first()
    elif op_mod=='in_use':
        entry = table_obj.query.filter_by(id=2).first()
        sntry = table_obj.query.filter_by(id=1).first()
    tntry = table_obj.query.filter_by(id=3).first()

    tcount = 0
    if 'Blenders_Pride' in entry_data:
        if mode=="set":
            entry.Blenders_Pride = entry_data['Blenders_Pride']
        elif mode=="add":
            entry.Blenders_Pride += entry_data['Blenders_Pride']
        elif mode=="sub":
            entry.Blenders_Pride = max( 0, entry.Blenders_Pride - entry_data['Blenders_Pride'] )
    tntry.Blenders_Pride = entry.Blenders_Pride + sntry.Blenders_Pride
    tcount += entry.Blenders_Pride

    if 'Breezer' in entry_data:
        if mode=="set":
            entry.Breezer = entry_data['Breezer']
        elif mode=="add":
            entry.Breezer += entry_data['Breezer']
        elif mode=="sub":
            entry.Breezer = max( 0, entry.Breezer - entry_data['Breezer'] )
    tntry.Breezer = entry.Breezer + sntry.Breezer
    tcount += entry.Breezer

    if 'DSP_Balck_180' in entry_data:
        if mode=="set":
            entry.DSP_Balck_180 = entry_data['DSP_Balck_180']
        elif mode=="add":
            entry.DSP_Balck_180 += entry_data['DSP_Balck_180']
        elif mode=="sub":
            entry.DSP_Balck_180 = max( 0, entry.DSP_Balck_180 - entry_data['DSP_Balck_180'] )
    tntry.DSP_Balck_180 = entry.DSP_Balck_180 + sntry.DSP_Balck_180
    tcount += entry.DSP_Balck_180

    if 'DSP_Balck_90' in entry_data:
        if mode=="set":
            entry.DSP_Balck_90 = entry_data['DSP_Balck_90']
        elif mode=="add":
            entry.DSP_Balck_90 += entry_data['DSP_Balck_90']
        elif mode=="sub":
            entry.DSP_Balck_90 = max( 0, entry.DSP_Balck_90 - entry_data['DSP_Balck_90'] )
    tntry.DSP_Balck_90 = entry.DSP_Balck_90 + sntry.DSP_Balck_90
    tcount += entry.DSP_Balck_90

    if 'IB_180' in entry_data:
        if mode=="set":
            entry.IB_180 = entry_data['IB_180']
        elif mode=="add":
            entry.IB_180 += entry_data['IB_180']
        elif mode=="sub":
            entry.IB_180 = max( 0, entry.IB_180 - entry_data['IB_180'] )
    tntry.IB_180 = entry.IB_180 + sntry.IB_180
    tcount += entry.IB_180

    if 'IB_90' in entry_data:
        if mode=="set":
            entry.IB_90 = entry_data['IB_90']
        elif mode=="add":
            entry.IB_90 += entry_data['IB_90']
        elif mode=="sub":
            entry.IB_90 = max( 0, entry.IB_90 - entry_data['IB_90'] )
    tntry.IB_90 = entry.IB_90 + sntry.IB_90
    tcount += entry.IB_90

    if 'Mcd_Rum_180' in entry_data:
        if mode=="set":
            entry.Mcd_Rum_180 = entry_data['Mcd_Rum_180']
        elif mode=="add":
            entry.Mcd_Rum_180 += entry_data['Mcd_Rum_180']
        elif mode=="sub":
            entry.Mcd_Rum_180 = max( 0, entry.Mcd_Rum_180 - entry_data['Mcd_Rum_180'] )
    tntry.Mcd_Rum_180 = entry.Mcd_Rum_180 + sntry.Mcd_Rum_180
    tcount += entry.Mcd_Rum_180

    if 'Mcd_Rum_90' in entry_data:
        if mode=="set":
            entry.Mcd_Rum_90 = entry_data['Mcd_Rum_90']
        elif mode=="add":
            entry.Mcd_Rum_90 += entry_data['Mcd_Rum_90']
        elif mode=="sub":
            entry.Mcd_Rum_90 = max( 0, entry.Mcd_Rum_90 - entry_data['Mcd_Rum_90'] )
    tntry.Mcd_Rum_90 = entry.Mcd_Rum_90 + sntry.Mcd_Rum_90
    tcount += entry.Mcd_Rum_90

    if 'MCDowells_180' in entry_data:
        if mode=="set":
            entry.MCDowells_180 = entry_data['MCDowells_180']
        elif mode=="add":
            entry.MCDowells_180 += entry_data['MCDowells_180']
        elif mode=="sub":
            entry.MCDowells_180 = max( 0, entry.MCDowells_180 - entry_data['MCDowells_180'] )
    tntry.MCDowells_180 = entry.MCDowells_180 + sntry.MCDowells_180
    tcount += entry.MCDowells_180

    if 'MCDowells_90' in entry_data:
        if mode=="set":
            entry.MCDowells_90 = entry_data['MCDowells_90']
        elif mode=="add":
            entry.MCDowells_90 += entry_data['MCDowells_90']
        elif mode=="sub":
            entry.MCDowells_90 = max( 0, entry.MCDowells_90 - entry_data['MCDowells_90'] )
    tntry.MCDowells_90 = entry.MCDowells_90 + sntry.MCDowells_90
    tcount += entry.MCDowells_90

    if 'Oak_Smith_Gold_180' in entry_data:
        if mode=="set":
            entry.Oak_Smith_Gold_180 = entry_data['Oak_Smith_Gold_180']
        elif mode=="add":
            entry.Oak_Smith_Gold_180 += entry_data['Oak_Smith_Gold_180']
        elif mode=="sub":
            entry.Oak_Smith_Gold_180 = max( 0, entry.Oak_Smith_Gold_180 - entry_data['Oak_Smith_Gold_180'] )
    tntry.Oak_Smith_Gold_180 = entry.Oak_Smith_Gold_180 + sntry.Oak_Smith_Gold_180
    tcount += entry.Oak_Smith_Gold_180

    if 'Oak_Smith_Gold_90' in entry_data:
        if mode=="set":
            entry.Oak_Smith_Gold_90 = entry_data['Oak_Smith_Gold_90']
        elif mode=="add":
            entry.Oak_Smith_Gold_90 += entry_data['Oak_Smith_Gold_90']
        elif mode=="sub":
            entry.Oak_Smith_Gold_90 = max( 0, entry.Oak_Smith_Gold_90 - entry_data['Oak_Smith_Gold_90'] )
    tntry.Oak_Smith_Gold_90 = entry.Oak_Smith_Gold_90 + sntry.Oak_Smith_Gold_90
    tcount += entry.Oak_Smith_Gold_90

    if 'Oak_Smith_Silver_180' in entry_data:
        if mode=="set":
            entry.Oak_Smith_Silver_180 = entry_data['Oak_Smith_Silver_180']
        elif mode=="add":
            entry.Oak_Smith_Silver_180 += entry_data['Oak_Smith_Silver_180']
        elif mode=="sub":
            entry.Oak_Smith_Silver_180 = max( 0, entry.Oak_Smith_Silver_180 - entry_data['Oak_Smith_Silver_180'] )
    tntry.Oak_Smith_Silver_180 = entry.Oak_Smith_Silver_180 + sntry.Oak_Smith_Silver_180
    tcount += entry.Oak_Smith_Silver_180

    if 'Oak_Smith_Silver_90' in entry_data:
        if mode=="set":
            entry.Oak_Smith_Silver_90 = entry_data['Oak_Smith_Silver_90']
        elif mode=="add":
            entry.Oak_Smith_Silver_90 += entry_data['Oak_Smith_Silver_90']
        elif mode=="sub":
            entry.Oak_Smith_Silver_90 = max( 0, entry.Oak_Smith_Silver_90 - entry_data['Oak_Smith_Silver_90'] )
    tntry.Oak_Smith_Silver_90 = entry.Oak_Smith_Silver_90 + sntry.Oak_Smith_Silver_90
    tcount += entry.Oak_Smith_Silver_90

    if 'OC_180' in entry_data:
        if mode=="set":
            entry.OC_180 = entry_data['OC_180']
        elif mode=="add":
            entry.OC_180 += entry_data['OC_180']
        elif mode=="sub":
            entry.OC_180 = max( 0, entry.OC_180 - entry_data['OC_180'] )
    tntry.OC_180 = entry.OC_180 + sntry.OC_180
    tcount += entry.OC_180

    if 'OC_90' in entry_data:
        if mode=="set":
            entry.OC_90 = entry_data['OC_90']
        elif mode=="add":
            entry.OC_90 += entry_data['OC_90']
        elif mode=="sub":
            entry.OC_90 = max( 0, entry.OC_90 - entry_data['OC_90'] )
    tntry.OC_90 = entry.OC_90 + sntry.OC_90
    tcount += entry.OC_90

    if 'Old_Monk_180' in entry_data:
        if mode=="set":
            entry.Old_Monk_180 = entry_data['Old_Monk_180']
        elif mode=="add":
            entry.Old_Monk_180 += entry_data['Old_Monk_180']
        elif mode=="sub":
            entry.Old_Monk_180 = max( 0, entry.Old_Monk_180 - entry_data['Old_Monk_180'] )
    tntry.Old_Monk_180 = entry.Old_Monk_180 + sntry.Old_Monk_180
    tcount += entry.Old_Monk_180

    if 'Old_Monk_90' in entry_data:
        if mode=="set":
            entry.Old_Monk_90 = entry_data['Old_Monk_90']
        elif mode=="add":
            entry.Old_Monk_90 += entry_data['Old_Monk_90']
        elif mode=="sub":
            entry.Old_Monk_90 = max( 0, entry.Old_Monk_90 - entry_data['Old_Monk_90'] )
    tntry.Old_Monk_90 = entry.Old_Monk_90 + sntry.Old_Monk_90
    tcount += entry.Old_Monk_90

    if 'RC_180' in entry_data:
        if mode=="set":
            entry.RC_180 = entry_data['RC_180']
        elif mode=="add":
            entry.RC_180 += entry_data['RC_180']
        elif mode=="sub":
            entry.RC_180 = max( 0, entry.RC_180 - entry_data['RC_180'] )
    tntry.RC_180 = entry.RC_180 + sntry.RC_180
    tcount += entry.RC_180

    if 'RC_90' in entry_data:
        if mode=="set":
            entry.RC_90 = entry_data['RC_90']
        elif mode=="add":
            entry.RC_90 += entry_data['RC_90']
        elif mode=="sub":
            entry.RC_90 = max( 0, entry.RC_90 - entry_data['RC_90'] )
    tntry.RC_90 = entry.RC_90 + sntry.RC_90
    tcount += entry.RC_90

    if 'Royal_Stag_180' in entry_data:
        if mode=="set":
            entry.Royal_Stag_180 = entry_data['Royal_Stag_180']
        elif mode=="add":
            entry.Royal_Stag_180 += entry_data['Royal_Stag_180']
        elif mode=="sub":
            entry.Royal_Stag_180 = max( 0, entry.Royal_Stag_180 - entry_data['Royal_Stag_180'] )
    tntry.Royal_Stag_180 = entry.Royal_Stag_180 + sntry.Royal_Stag_180
    tcount += entry.Royal_Stag_180

    if 'Royal_Stag_90' in entry_data:
        if mode=="set":
            entry.Royal_Stag_90 = entry_data['Royal_Stag_90']
        elif mode=="add":
            entry.Royal_Stag_90 += entry_data['Royal_Stag_90']
        elif mode=="sub":
            entry.Royal_Stag_90 = max( 0, entry.Royal_Stag_90 - entry_data['Royal_Stag_90'] )
    tntry.Royal_Stag_90 = entry.Royal_Stag_90 + sntry.Royal_Stag_90
    tcount += entry.Royal_Stag_90

    if 'Royal_Stag_Barel_180' in entry_data:
        if mode=="set":
            entry.Royal_Stag_Barel_180 = entry_data['Royal_Stag_Barel_180']
        elif mode=="add":
            entry.Royal_Stag_Barel_180 += entry_data['Royal_Stag_Barel_180']
        elif mode=="sub":
            entry.Royal_Stag_Barel_180 = max( 0, entry.Royal_Stag_Barel_180 - entry_data['Royal_Stag_Barel_180'] )
    tntry.Royal_Stag_Barel_180 = entry.Royal_Stag_Barel_180 + sntry.Royal_Stag_Barel_180
    tcount += entry.Royal_Stag_Barel_180

    if 'Royal_Stag_Barel_90' in entry_data:
        if mode=="set":
            entry.Royal_Stag_Barel_90 = entry_data['Royal_Stag_Barel_90']
        elif mode=="add":
            entry.Royal_Stag_Barel_90 += entry_data['Royal_Stag_Barel_90']
        elif mode=="sub":
            entry.Royal_Stag_Barel_90 = max( 0, entry.Royal_Stag_Barel_90 - entry_data['Royal_Stag_Barel_90'] )
    tntry.Royal_Stag_Barel_90 = entry.Royal_Stag_Barel_90 + sntry.Royal_Stag_Barel_90
    tcount += entry.Royal_Stag_Barel_90

    if 'Signature_180' in entry_data:
        if mode=="set":
            entry.Signature_180 = entry_data['Signature_180']
        elif mode=="add":
            entry.Signature_180 += entry_data['Signature_180']
        elif mode=="sub":
            entry.Signature_180 = max( 0, entry.Signature_180 - entry_data['Signature_180'] )
    tntry.Signature_180 = entry.Signature_180 + sntry.Signature_180
    tcount += entry.Signature_180

    if 'other1' in entry_data:
        if mode=="set":
            entry.other1 = entry_data['other1']
        elif mode=="add":
            entry.other1 += entry_data['other1']
        elif mode=="sub":
            entry.other1 = max( 0, entry.other1 - entry_data['other1'] )
    tntry.other1 = entry.other1 + sntry.other1
    tcount += entry.other1

    if 'other2' in entry_data:
        if mode=="set":
            entry.other2 = entry_data['other2']
        elif mode=="add":
            entry.other2 += entry_data['other2']
        elif mode=="sub":
            entry.other2 = max( 0, entry.other2 - entry_data['other2'] )
    tntry.other2 = entry.other2 + sntry.other2
    tcount += entry.other2

    entry.total = tcount

    db.session.commit()