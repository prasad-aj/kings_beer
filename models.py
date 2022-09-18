from app import app

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class hot_sell_daily_record(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    OP_mode = db.Column(db.String(10))
    Date = db.Column(db.Date)
    Blenders_Pride = db.Column(db.Integer)
    Breezer = db.Column(db.Integer)
    DSP_Balck_180 = db.Column(db.Integer)
    DSP_Balck_90 = db.Column(db.Integer)
    IB_180 = db.Column(db.Integer)
    IB_90 = db.Column(db.Integer)
    Mcd_Rum_180 = db.Column(db.Integer)
    Mcd_Rum_90 = db.Column(db.Integer)
    MCDowells_180 = db.Column(db.Integer)
    MCDowells_90 = db.Column(db.Integer)
    Oak_Smith_Gold_180 = db.Column(db.Integer)
    Oak_Smith_Gold_90 = db.Column(db.Integer)
    Oak_Smith_Silver_180 = db.Column(db.Integer)
    Oak_Smith_Silver_90 = db.Column(db.Integer)
    OC_180 = db.Column(db.Integer)
    OC_90 = db.Column(db.Integer)
    Old_Monk_180 = db.Column(db.Integer)
    Old_Monk_90 = db.Column(db.Integer)
    RC_180 = db.Column(db.Integer)
    RC_90 = db.Column(db.Integer)
    Royal_Stag_180 = db.Column(db.Integer)
    Royal_Stag_90 = db.Column(db.Integer)
    Royal_Stag_Barel_180 = db.Column(db.Integer)
    Royal_Stag_Barel_90 = db.Column(db.Integer)
    Signature_180 = db.Column(db.Integer)
    other1 = db.Column(db.Integer)
    other2 = db.Column(db.Integer)
    Remark = db.Column(db.String(50))
    Day_Sell = db.Column(db.Integer)
    MRP_profit = db.Column(db.Float)
    Actual_profit = db.Column(db.Float)

    def __init__(self, OP_mode, Date, item_scounts, Remark, Day_Sell, MRP_profit, Actual_profit):

        Blenders_Pride, Breezer, DSP_Balck_180, DSP_Balck_90, IB_180, IB_90, Mcd_Rum_180, Mcd_Rum_90, MCDowells_180, MCDowells_90, Oak_Smith_Gold_180, Oak_Smith_Gold_90, Oak_Smith_Silver_180, Oak_Smith_Silver_90, OC_180, OC_90, Old_Monk_180, Old_Monk_90, RC_180, RC_90, Royal_Stag_180, Royal_Stag_90, Royal_Stag_Barel_180, Royal_Stag_Barel_90, Signature_180, other1, other2 = item_scounts


        self.OP_mode = OP_mode
        self.Date  =  Date
        self.Blenders_Pride  =  Blenders_Pride
        self.Breezer  =  Breezer
        self.DSP_Balck_180  =  DSP_Balck_180
        self.DSP_Balck_90  =  DSP_Balck_90
        self.IB_180  =  IB_180
        self.IB_90  =  IB_90
        self.Mcd_Rum_180  =  Mcd_Rum_180
        self.Mcd_Rum_90  =  Mcd_Rum_90
        self.MCDowells_180  =  MCDowells_180
        self.MCDowells_90  =  MCDowells_90
        self.Oak_Smith_Gold_180  =  Oak_Smith_Gold_180
        self.Oak_Smith_Gold_90  =  Oak_Smith_Gold_90
        self.Oak_Smith_Silver_180  =  Oak_Smith_Silver_180
        self.Oak_Smith_Silver_90  =  Oak_Smith_Silver_90
        self.OC_180  =  OC_180
        self.OC_90  =  OC_90
        self.Old_Monk_180  =  Old_Monk_180
        self.Old_Monk_90  =  Old_Monk_90
        self.RC_180  =  RC_180
        self.RC_90  =  RC_90
        self.Royal_Stag_180  =  Royal_Stag_180
        self.Royal_Stag_90  =  Royal_Stag_90
        self.Royal_Stag_Barel_180  =  Royal_Stag_Barel_180
        self.Royal_Stag_Barel_90  =  Royal_Stag_Barel_90
        self.Signature_180  =  Signature_180
        self.other1  =  other1
        self.other2  =  other2
        self.Remark  =  Remark
        self.Day_Sell  =  Day_Sell
        self.MRP_profit  =  MRP_profit
        self.Actual_profit  =  Actual_profit

class hot_stock(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    OP_mode = db.Column(db.String(10))
    Blenders_Pride = db.Column(db.Integer)
    Breezer = db.Column(db.Integer)
    DSP_Balck_180 = db.Column(db.Integer)
    DSP_Balck_90 = db.Column(db.Integer)
    IB_180 = db.Column(db.Integer)
    IB_90 = db.Column(db.Integer)
    Mcd_Rum_180 = db.Column(db.Integer)
    Mcd_Rum_90 = db.Column(db.Integer)
    MCDowells_180 = db.Column(db.Integer)
    MCDowells_90 = db.Column(db.Integer)
    Oak_Smith_Gold_180 = db.Column(db.Integer)
    Oak_Smith_Gold_90 = db.Column(db.Integer)
    Oak_Smith_Silver_180 = db.Column(db.Integer)
    Oak_Smith_Silver_90 = db.Column(db.Integer)
    OC_180 = db.Column(db.Integer)
    OC_90 = db.Column(db.Integer)
    Old_Monk_180 = db.Column(db.Integer)
    Old_Monk_90 = db.Column(db.Integer)
    RC_180 = db.Column(db.Integer)
    RC_90 = db.Column(db.Integer)
    Royal_Stag_180 = db.Column(db.Integer)
    Royal_Stag_90 = db.Column(db.Integer)
    Royal_Stag_Barel_180 = db.Column(db.Integer)
    Royal_Stag_Barel_90 = db.Column(db.Integer)
    Signature_180 = db.Column(db.Integer)
    other1 = db.Column(db.Integer)
    other2 = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self, OP_mode, Blenders_Pride, Breezer, DSP_Balck_180, DSP_Balck_90, IB_180, IB_90, Mcd_Rum_180, Mcd_Rum_90, MCDowells_180, MCDowells_90, Oak_Smith_Gold_180, Oak_Smith_Gold_90, Oak_Smith_Silver_180, Oak_Smith_Silver_90, OC_180, OC_90, Old_Monk_180, Old_Monk_90, RC_180, RC_90, Royal_Stag_180, Royal_Stag_90, Royal_Stag_Barel_180, Royal_Stag_Barel_90, Signature_180, other1, other2, total ):
        self.OP_mode = OP_mode
        self.Blenders_Pride  =  Blenders_Pride
        self.Breezer  =  Breezer
        self.DSP_Balck_180  =  DSP_Balck_180
        self.DSP_Balck_90  =  DSP_Balck_90
        self.IB_180  =  IB_180
        self.IB_90  =  IB_90
        self.Mcd_Rum_180  =  Mcd_Rum_180
        self.Mcd_Rum_90  =  Mcd_Rum_90
        self.MCDowells_180  =  MCDowells_180
        self.MCDowells_90  =  MCDowells_90
        self.Oak_Smith_Gold_180  =  Oak_Smith_Gold_180
        self.Oak_Smith_Gold_90  =  Oak_Smith_Gold_90
        self.Oak_Smith_Silver_180  =  Oak_Smith_Silver_180
        self.Oak_Smith_Silver_90  =  Oak_Smith_Silver_90
        self.OC_180  =  OC_180
        self.OC_90  =  OC_90
        self.Old_Monk_180  =  Old_Monk_180
        self.Old_Monk_90  =  Old_Monk_90
        self.RC_180  =  RC_180
        self.RC_90  =  RC_90
        self.Royal_Stag_180  =  Royal_Stag_180
        self.Royal_Stag_90  =  Royal_Stag_90
        self.Royal_Stag_Barel_180  =  Royal_Stag_Barel_180
        self.Royal_Stag_Barel_90  =  Royal_Stag_Barel_90
        self.Signature_180  =  Signature_180
        self.other1  =  other1
        self.other2  =  other2
        self.total  = total


db.create_all()


