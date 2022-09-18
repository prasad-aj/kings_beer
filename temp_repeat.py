
data = ["Blenders_Pride", "Breezer", "DSP_Balck_180", "DSP_Balck_90", "IB_180", "IB_90", "Mcd_Rum_180", "Mcd_Rum_90", "MCDowells_180", "MCDowells_90", "Oak_Smith_Gold_180", "Oak_Smith_Gold_90", "Oak_Smith_Silver_180", "Oak_Smith_Silver_90", "OC_180", "OC_90", "Old_Monk_180", "Old_Monk_90", "RC_180", "RC_90", "Royal_Stag_180", "Royal_Stag_90", "Royal_Stag_Barel_180", "Royal_Stag_Barel_90", "Signature_180", "other1", "other2"]
data = [ "AMSTEL 500", "AMSTEL 650", "BECKS ICE 500", "BECKS ICE 650", "BIRA BLONDE 650", "BIRA BOOM 500", "BIRA BOOM 650", "BIRA GOLD 650", "BUDWISER MILD 500", "BUDWISER MILD 650", "CARLSBERG SMTH 500", "CARLSBERG SMTH 650", "CARSLBERG 500", "CARSLBERG 650", "CORONA 330", "HAYWARDS 2000 500", "HAYWARDS 2000 650", "HEINEKEN 330", "HOGRADAN 330", "KF 650ML", "KF MILD 330", "KF MILD 500", "KF MILD 650", "KF STORM", "KF ULTRA 650", "KF ULTRA MAX 650", "KF330ML", "KF500ML", "LP 500", "LP 650", "LP MILD", "LP MILD 500 ML", "MAGNUM 500", "MAGNUM 650", "TUBORG 330", "TUBORG 500", "TUBORG 650", "TUBORG MILD"]
for item in data:

    print(f'''"{item}": [
            9,
            9,
            9
        ],''')



    # print(f'''    if '{item}' in entry_data:
    #     if mode=="set":
    #         entry.{item} = entry_data['{item}']
    #     elif mode=="add":
    #         entry.{item} += entry_data['{item}']
    #     elif mode=="sub":
    #         entry.{item} = max( 0, entry.{item} - entry_data['{item}'] )
    # tntry.{item} = entry.{item} + sntry.{item}
    # tcount += entry.{item}
    #         ''')