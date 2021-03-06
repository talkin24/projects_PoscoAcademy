import pandas as pd
def isnan(value):
    try:
        import math
        return math.isnan(float(value))
    except:
        return False
        
def InsertRuntime(df_raw):
    for movie_id in df_raw['movie_id']:
        if movie_id == "tt2382320":
            df_raw[movie_id]['runtime'] = '163.0'
        if movie_id == "tt1745960":
            df_raw[movie_id]['runtime'] = '136.0'
        if movie_id == "tt3089630":
            df_raw[movie_id]['runtime'] = '115.0'
        if movie_id == "tt8356942":
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt1781967":
            # TV Series
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt1346913":
            # Documentary
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt0490087":
            df_raw[movie_id]['runtime'] = '100.0'
        if movie_id == "tt10059518":
            # 2020
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt3492042":
            # N/A
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt8244784":
            # 2020 
            df_raw[movie_id]['runtime'] = '90.0'
        if movie_id == "tt8332922":
            # 2020
            df_raw[movie_id]['runtime'] = '97.0'
        if movie_id == "tt1442286":
            # short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt7798646":
            # 2020
            df_raw[movie_id]['runtime'] = '106.0'
        if movie_id == "tt0360772":
            # Documentary
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt9173418":
            # 2020
            df_raw[movie_id]['runtime'] = '86.0'
        if movie_id == "tt5351480":
            # short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt0102538":
            # Documentary
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt1200853":
            # short
            df_raw[movie_id]['runtime'] = '11.0'
        if movie_id == "tt1717210":
            # N/A
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt2237914":
            df_raw[movie_id]['runtime'] = '90.0'
        if movie_id == "tt2573798":
            # short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt2435500":
            # short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt1145855":
            # animation
            df_raw[movie_id]['runtime'] = '44.0'
        if movie_id == "tt5928532":
            # Tv Series
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt0452999":
            df_raw[movie_id]['runtime'] = '85.0'
        if movie_id == "tt0498879":
            # TV Series
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt2479026":
            # Documentary
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt4590482":
            df_raw[movie_id]['runtime'] = '143.0'
        if movie_id == "tt2763498":
            df_raw[movie_id]['runtime'] = '96.0'
        if movie_id == "tt4355456":
            # short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt3512332":
            # 2020
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt3520844":
            # TV Series
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt4477966":
            # Short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt1383609":
            # Short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt4798386":
            # Short
            df_raw[movie_id]['runtime'] = '.'
        if movie_id == "tt0301503":
            df_raw[movie_id]['runtime'] = '83.0'
            
def InsertImdbScore(df_raw):
    for movie_id in df_raw['movie_id']:
        if movie_id == "tt2382320":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6723592":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6304710":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1745960":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt7504726":
            df_raw[movie_id]["imdb_score"] = '6.8'
        if movie_id == "tt3089630":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1804538":
            df_raw[movie_id]["imdb_score"] = '8.6'
        if movie_id == "tt5649074":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt8356942":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1781967":
            # TV Series
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt10597946":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5280288":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4047068":
            df_raw[movie_id]["imdb_score"] = '6.8'
        if movie_id == "tt5292922":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1346913":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4545300":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5160558":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt10059518":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6807754":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5449004":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt7178988":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt8115904":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1388882":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0485244":
            # Documentary, N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2023631":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3492042":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0485236":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt8244784":
            # 2020
            df_raw[movie_id]["imdb_score"] = '6.4'
        if movie_id == "tt4064028":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5210194":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt8332922":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4380070":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5449860":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1442286":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt7798646":
            df_raw[movie_id]["imdb_score"] = '6.1'
        if movie_id == "tt4229814":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2736560":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1096959":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5916886":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2389374":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1427984":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4982758":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6986684":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt9173418":
            # 2020
            df_raw[movie_id]["imdb_score"] = '4.5'
        if movie_id == "tt10798734":
            # TV Series (News)
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6049430":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5351480":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4994952":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5350540":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6408216":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5648372":
            df_raw[movie_id]["imdb_score"] = '6.2'
        if movie_id == "tt0102538":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2993526":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0367578":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0491144":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1647810":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1649005":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0322956":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt7017420":
            df_raw[movie_id]["imdb_score"] = '8.4'
        if movie_id == "tt4094248":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6042478":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1451684":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4906112":
            df_raw[movie_id]["imdb_score"] = '5.4'
        if movie_id == "tt4255584":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0444480":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1578715":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2911094":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3614128":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5517008":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4509744":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2573798":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt8332674":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1609781":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2435500":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4146338":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4617208":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3239836":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2647116":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6000398":
            df_raw[movie_id]["imdb_score"] = '5.8'
        if movie_id == "tt5923204":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3884512":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2211646":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6047630":
            df_raw[movie_id]["imdb_score"] = '4.7'
        if movie_id == "tt4369142":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3107668":
            # Amnesiac tt2837336
            df_raw[movie_id]["imdb_score"] = '4.3'
        if movie_id == "tt4170078":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2243223":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5637996":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3462264":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2304963":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2734210":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt8248230":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1587396":
            # TV Series
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0452999":
            # TV Series
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3621892":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2424480":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt0400202":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1975161":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5620366":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4403432":
            # TV Series
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5366082":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2768290":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2763498":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt3513086":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2348492":
            # Short
            df_raw[movie_id]["imdb_score"] = '6.2'
        if movie_id == "tt5152156":
            # Short
            df_raw[movie_id]["imdb_score"] = '7.8'
        if movie_id == "tt5274738":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt2402132":
            # N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6051948":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4649072":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt5014406":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt4355456":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6519016":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt6020556":
            # Short
            df_raw[movie_id]["imdb_score"] = '5.8'
        if movie_id == "tt3512332":
            # 2020
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt8151710":
            # Short
            df_raw[movie_id]["imdb_score"] = '.'
        if movie_id == "tt1785302":
            # Documentary N/A
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt0401610":
            # Short
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt4477966":
            # Short
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt1383609":
            # Short
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt5512848":
            # Short
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt4798386":
            # Short
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt3123250":
            # N/A
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt4515364":
            # N/A
            df_raw[movie_id]["imdb_score"] = "."
        if movie_id == "tt1230136":
            df_raw[movie_id]["imdb_score"] = "3.5"
        
def InsertSale(df_raw):
    for movie_id in df_raw['movie_id']:
        if movie_id == "tt0348150":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0499448":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0385752":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120338":
            # titanic in video sales(tab)
            df_raw[movie_id]["dvd_sales"] = "22246589"
            df_raw[movie_id]["blu_sales"] = "8600244"
            df_raw[movie_id]["total_sales"] = "30846833"
        if movie_id == "tt0316654":
            # spider-Man 2 in video sales(tab)
            df_raw[movie_id]["dvd_sales"] = "26538684"
            df_raw[movie_id]["blu_sales"] = "171986"
            df_raw[movie_id]["total_sales"] = "26710670"
        if movie_id == "tt0367882":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4777008":
            # Maleficent: Mistress of Evil
            df_raw[movie_id]["dvd_sales"] = "4993041"
            df_raw[movie_id]["blu_sales"] = "12165327"
            df_raw[movie_id]["total_sales"] = "17158368"
        if movie_id == "tt6450804":
            # Terminator: Dark Fate
            df_raw[movie_id]["dvd_sales"] = "4496174"
            df_raw[movie_id]["blu_sales"] = "8712265"
            df_raw[movie_id]["total_sales"] = "13208439"
        if movie_id == "tt0910970":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0293564":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0859163":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0413099":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0338348":
            # The Polar Express
            df_raw[movie_id]["dvd_sales"] = "115597458"
            df_raw[movie_id]["blu_sales"] = "29882207"
            df_raw[movie_id]["total_sales"] = "145479665"
        if movie_id == "tt0181852":
            # Terminator 3: Rise of the Machines
            df_raw[movie_id]["dvd_sales"] = "620056"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0338526":
            # Van Helsing (only blu-ray)
            df_raw[movie_id]["blu_sales"] = "94645"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0409182":
            # Poseidon
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0372784":
            # Batman Begins
            df_raw[movie_id]["dvd_sales"] = "27885441"
            df_raw[movie_id]["blu_sales"] = "11470789"
            df_raw[movie_id]["total_sales"] = "39356230"
        if movie_id == "tt0367594":
            # Charlie and the Chocolate Factory
            df_raw[movie_id]["dvd_sales"] = "16075473"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0382932":
            # Ratatouille
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0371606":
            # Chicken Little
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0332452":
            # Troy
            df_raw[movie_id]["dvd_sales"] = "17591264"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0397892":
            # Bolt
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0442933":
            # Beowulf
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0424095":
            # Flushed Away
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120855":
            # Tarzan
            df_raw[movie_id]["dvd_sales"] = "62726"
            df_raw[movie_id]["blu_sales"] = "704695"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120591":
            # Armageddon
            df_raw[movie_id]["dvd_sales"] = "700892"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0325710":
            # Fun with Dick and Jane
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1025100":
            # Gemini Man
            df_raw[movie_id]["dvd_sales"] = "2,886,781"
            df_raw[movie_id]["blu_sales"] = "5,039,081"
            df_raw[movie_id]["total_sales"] = "7925862"
        if movie_id == "tt1745960":
            # Top Gun : Maverick
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0145487":
            # Spider-Man
            df_raw[movie_id]["dvd_sales"] = "24544723"
            df_raw[movie_id]["blu_sales"] = "166309"
            df_raw[movie_id]["total_sales"] = "24711032"
        if movie_id == "tt0430357":
            # Miami Vice
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0407304":
            # War of the Worlds
            df_raw[movie_id]["blu_sales"] = "95409"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0304141":
            # Harry Potter and the Prisoner of azkaban
            df_raw[movie_id]["dvd_sales"] = "19887141"
            df_raw[movie_id]["blu_sales"] = "6816774" 
            df_raw[movie_id]["total_sales"] = "26703915"
        if movie_id == "tt0241527":
            # Harry Potter and the Sorcerer's Stone
            df_raw[movie_id]["dvd_sales"] = "16652346"
            df_raw[movie_id]["blu_sales"] = "3553092" 
            df_raw[movie_id]["total_sales"] = "20205438"
        if movie_id == "tt0382625":
            # The Da Vinci Code
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0170016":
            # How the Grinch Stole Christmas
            df_raw[movie_id]["dvd_sales"] = "49807044"
            df_raw[movie_id]["blu_sales"] = "9266910" 
            df_raw[movie_id]["total_sales"] = "59073954"
        if movie_id == "tt0243585":
            # Stuart Little 2
            df_raw[movie_id]["dvd_sales"] = "1312522"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0811080":
            # Speed Racer
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0198781":
            # Monsters, Inc.
            df_raw[movie_id]["dvd_sales"] = "62279413"
            df_raw[movie_id]["blu_sales"] = "46739416" 
            df_raw[movie_id]["total_sales"] = "109018829"
        if movie_id == "tt0477347":
            # Night at the Museum
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0337978":
            # Live Free or Die Hard
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120737":
            # The Lord of the Rings: The Fellowship of the Ring (2001)
            df_raw[movie_id]["blu_sales"] = "4214981" 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0312528":
            # The Cat in the Hat
            df_raw[movie_id]["dvd_sales"] = "10757347"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0343818":
            # I, Robot
            df_raw[movie_id]["dvd_sales"] = "412333"
            df_raw[movie_id]["blu_sales"] = "289230" 
            df_raw[movie_id]["total_sales"] = "701563"
        if movie_id == "tt0164912":
            # Stuart Little
            df_raw[movie_id]["dvd_sales"] = "8381982"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0443649":
            # 10,000 BC
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0172495":
            # Gladiator
            df_raw[movie_id]["dvd_sales"] = "4800213"
            df_raw[movie_id]["blu_sales"] = "11039776" 
            df_raw[movie_id]["total_sales"] = "15839989"
        if movie_id == "tt0181689":
            # Minority Report
            df_raw[movie_id]["blu_sales"] = "164308"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0295297":
            # Harry Potter and the Chamber of Secrets (2002)
            df_raw[movie_id]["dvd_sales"] = "25446422"
            df_raw[movie_id]["blu_sales"] = "1909197" 
            df_raw[movie_id]["total_sales"] = "27355619"
        if movie_id == "tt0103064":
            # Terminator 2: Judgment Day
            df_raw[movie_id]["dvd_sales"] = "977401"
            df_raw[movie_id]["blu_sales"] = "3620629" 
            df_raw[movie_id]["total_sales"] = "4598030"
        if movie_id == "tt0368891":
            # National Treasure
            df_raw[movie_id]["dvd_sales"] = "5268752"
            df_raw[movie_id]["blu_sales"] = "269797" 
            df_raw[movie_id]["total_sales"] = "5538549"
        if movie_id == "tt0449010":
            # Eragon
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0423294":
            # Surf's Up
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0450259":
            # Blood Diamond
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt6924650":
            # Midway(2019)
            df_raw[movie_id]["dvd_sales"] = "2307740"
            df_raw[movie_id]["blu_sales"] = "6163368" 
            df_raw[movie_id]["total_sales"] = "8471108"
        if movie_id == "tt0133240":
            # Treasure Planet (2002)
            df_raw[movie_id]["blu_sales"] = '263364'
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0217505":
            # Gangs of New York (2002)
            df_raw[movie_id]["blu_sales"] = '124636'
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0265086":
            # Black Hawk Down (2001)
            df_raw[movie_id]["dvd_sales"] = "1238211"
            df_raw[movie_id]["blu_sales"] = "285633" 
            df_raw[movie_id]["total_sales"] = "1523844"
        if movie_id == "tt0119116":
            # The Fifth Element (1997)
            df_raw[movie_id]["blu_sales"] = '9311346'
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0266543":
            # Finding Nemo (2003)
            df_raw[movie_id]["dvd_sales"] = "77085742"
            df_raw[movie_id]["blu_sales"] = "36230523" 
            df_raw[movie_id]["total_sales"] = "113316265"
        if movie_id == "tt0167260":
            # The Lord of the Rings: The Return of the King (2003)
            df_raw[movie_id]["dvd_sales"] = "29790451"
            df_raw[movie_id]["blu_sales"] = "4144557" 
            df_raw[movie_id]["total_sales"] = "33935008"
        if movie_id == "tt0167261":
            # The Lord of the Rings: The Two Towers (2002)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0163025":
            # Jurassic Park III (2001)
            df_raw[movie_id]["dvd_sales"] = "2858406"
            df_raw[movie_id]["blu_sales"] = "1808216" 
            df_raw[movie_id]["total_sales"] = "4666622"
        if movie_id == "tt0416236":
            # The Spiderwick Chronicles (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0317705":
            # The Incredibles
            df_raw[movie_id]["dvd_sales"] = "38344728"
            df_raw[movie_id]["blu_sales"] = "16744954" 
            df_raw[movie_id]["total_sales"] = "55089682"
        if movie_id == "tt0119654":
            # Men in Black (1997)
            df_raw[movie_id]["dvd_sales"] = "7238580"
            df_raw[movie_id]["blu_sales"] = "374660" 
            df_raw[movie_id]["total_sales"] = "7613240"
        if movie_id == "tt0120363":
            # Toy Story 2
            df_raw[movie_id]["dvd_sales"] = "42243790"
            df_raw[movie_id]["blu_sales"] = "19752157" 
            df_raw[movie_id]["total_sales"] = "61995947"
        if movie_id == "tt7131622":
            # Once Upon a Time???in Hollywood (2019)
            df_raw[movie_id]["dvd_sales"] = "5542326"
            df_raw[movie_id]["blu_sales"] = "13117458" 
            df_raw[movie_id]["total_sales"] = "18659784"
        if movie_id == "tt0942385":
            # Tropic Thunder (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0960144":
            # You Don't Mess With the Zohan (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0985699":
            # Valkyrie (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0117998":
            # Twister
            df_raw[movie_id]["dvd_sales"] = "10133854"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0352248":
            # Cinderella Man (2005)
            df_raw[movie_id]["dvd_sales"] = "9077396"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120667":
            # Fantastic Four (2005)
            df_raw[movie_id]["dvd_sales"] = "12231710"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0372183":
            # The Bourne Supremacy (2004)
            df_raw[movie_id]["dvd_sales"] = "16239131"
            df_raw[movie_id]["blu_sales"] = "348906" 
            df_raw[movie_id]["total_sales"] = "16588037"
        if movie_id == "tt0461770":
            # Enchanted (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0496806":
            # Ocean's Thirteen (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0400717":
            # Open Season (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0457939":
            # The Holiday (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0397535":
            # Memoirs of a Geisha (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0113492":
            # Judge Dredd (1995)
            df_raw[movie_id]["blu_sales"] = '121773'
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt0443706":
            # Zodiac (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0389860":
            # Click (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0413895":
            # Charlotte's Web (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0489099":
            # Jumper (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0117060":
            # Mission: Impossible (1996)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "5272496" 
            df_raw[movie_id]["total_sales"] = "5272496"
        if movie_id == "tt0327084":
            # Over the Hedge (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0275847":
            # Lilo & Stitch (2002)
            df_raw[movie_id]["dvd_sales"] = "1500269"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0425061":
            # Get Smart (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0358082":
            # Robots (2005)
            df_raw[movie_id]["dvd_sales"] = "23282498"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0960731":
            # Bedtime Stories (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1059786":
            # Eagle Eye (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0117705":
            # Space Jam(1996)
            df_raw[movie_id]["dvd_sales"] = "5502875"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0383216":
            # The Pink Panther (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0970416":
            # The Day the Earth Stood Still (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0118883":
            # Conspiracy Theory (1997)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0244244":
            # Swordfish (2001)
            df_raw[movie_id]["blu_sales"] = "200916"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["blu_sales"]
        if movie_id == "tt5649074":
            # D??j?? Vu (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2935510":
            # Ad Astra (2019)
            df_raw[movie_id]["dvd_sales"] = "3064469"
            df_raw[movie_id]["blu_sales"] = "5930052" 
            df_raw[movie_id]["total_sales"] = "8994521"
        if movie_id == "tt0386140":
            # The Legend of Zorro
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0405469":
            # The Wild (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0146309":
            # Thirteen Days
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "201805" 
            df_raw[movie_id]["total_sales"] = "201805"
        if movie_id == "tt0427392":
            # The Invasion (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0110357":
            # The Lion King (1994)
            df_raw[movie_id]["dvd_sales"] = "116700256"
            df_raw[movie_id]["blu_sales"] = "101774921" 
            df_raw[movie_id]["total_sales"] = "218475177"
        if movie_id == "tt0268978":
            # A Beautiful Mind (2001)
            df_raw[movie_id]["dvd_sales"] = "197201"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0322259":
            # 2 Fast 2 Furious (2003)
            df_raw[movie_id]["dvd_sales"] = "5778575"
            df_raw[movie_id]["blu_sales"] = "181585" 
            df_raw[movie_id]["total_sales"] = "5960160"
        if movie_id == "tt0206634":
            # Children of Men (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0116629":
            # Independence Day (1996)
            df_raw[movie_id]["dvd_sales"] = "14517975"
            df_raw[movie_id]["blu_sales"] = "20996526" 
            df_raw[movie_id]["total_sales"] = "35514501"
        if movie_id == "tt0119567":
            # The Lost World: Jurassic Park (1997)
            df_raw[movie_id]["dvd_sales"] = "2613714"
            df_raw[movie_id]["blu_sales"] = "1916916" 
            df_raw[movie_id]["total_sales"] = "4530630"
        if movie_id == "tt0351283":
            # Madagascar (2005)
            df_raw[movie_id]["dvd_sales"] = "47779452"
            df_raw[movie_id]["blu_sales"] = "1392193" 
            df_raw[movie_id]["total_sales"] = "49171645"
        if movie_id == "tt0307453":
            # Shark Tale (2004)
            df_raw[movie_id]["dvd_sales"] = "1731824"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120903":
            # X-Men (2000)
            df_raw[movie_id]["dvd_sales"] = "5794165"
            df_raw[movie_id]["blu_sales"] = "319329" 
            df_raw[movie_id]["total_sales"] = "6113494"
        if movie_id == "tt0493464":
            # Wanted (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0343660":
            # 50 First Dates (2004)
            df_raw[movie_id]["dvd_sales"] = "7712402"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0427327":
            # Hairspray (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0443489":
            # Dreamgirls (2006)
            df_raw[movie_id]["dvd_sales"] = "49806817"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0362227":
            #The Terminal (2004)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0360486":
            # Constantine (2005)
            df_raw[movie_id]["dvd_sales"] = "570808"
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0472062":
            # Charlie Wilson's War (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt6324278":
            # Abominable (2019)
            df_raw[movie_id]["dvd_sales"] = "7913006"
            df_raw[movie_id]["blu_sales"] = "9999703" 
            df_raw[movie_id]["total_sales"] = "17912709"
        if movie_id == "tt0408306":
            # Munich (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0452637":
            # Lady in the Water (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0462538":
            # The Simpsons Movie (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0770752":
            # Fool's Gold (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1201167":
            # Funny People (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0112573":
            # Braveheart (1995)
            df_raw[movie_id]["blu_sales"] = "7328028" 
            df_raw[movie_id]["total_sales"] = "7328028"
        if movie_id == "tt0418763":
            # Jarhead (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0298148":
            # Shrek 2 (2004)
            df_raw[movie_id]["dvd_sales"] = "7194229" 
            df_raw[movie_id]["total_sales"] = "7194229"
        if movie_id == "tt7349950":
            # It: Chapter Two (2019)
            df_raw[movie_id]["dvd_sales"] = "79781806"
            df_raw[movie_id]["blu_sales"] = "14551209" 
            df_raw[movie_id]["total_sales"] = "22529389"
        if movie_id == "tt0096438":
            # Who Framed Roger Rabbit? (1988)
            df_raw[movie_id]["blu_sales"] = "1198646" 
            df_raw[movie_id]["total_sales"] = "1198646"
        if movie_id == "tt0162661":
            # Sleepy Hollow (1999)
            df_raw[movie_id]["dvd_sales"] = "272848"
            df_raw[movie_id]["total_sales"] = "272848"
        if movie_id == "tt0119282":
            # Hercules (1997)
            df_raw[movie_id]["dvd_sales"] = "1283005"
            df_raw[movie_id]["blu_sales"] = "896523" 
            df_raw[movie_id]["total_sales"] = "2179528"
        if movie_id == "tt0406816":
            # The Guardian (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0398375":
            # Rumor Has It (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0486655":
            # Stardust (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0476964":
            # The Brave One (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0419706":
            # Doom (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0435705":
            # Next (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0430912":
            # Basic Instinct 2 (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0758774":
            # Body of Lies (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120815":
            # Saving Private Ryan (1998)
            df_raw[movie_id]["blu_sales"] = "9403638" 
            df_raw[movie_id]["total_sales"] = "9403638"
        if movie_id == "tt0268380":
            # Ice Age (2002)
            df_raw[movie_id]["dvd_sales"] = "15611651"
            df_raw[movie_id]["blu_sales"] = "293915" 
            df_raw[movie_id]["total_sales"] = "2179528"
        if movie_id == "tt0112384":
            # Apollo 13 (1995)
            df_raw[movie_id]["blu_sales"] = "469423" 
            df_raw[movie_id]["total_sales"] = "469423"
        if movie_id == "tt0133093":
            # The Matrix (1999)
            df_raw[movie_id]["blu_sales"] = "4050617" 
            df_raw[movie_id]["total_sales"] = "4050617"
        if movie_id == "tt0100802":
            # Total Recall (1990)
            df_raw[movie_id]["dvd_sales"] = "239685"
            df_raw[movie_id]["blu_sales"] = "663494" 
            df_raw[movie_id]["total_sales"] = "903179"
        if movie_id == "tt0838283":
            # Step Brothers (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0113497":
            # Jumanji (1995)
            df_raw[movie_id]["dvd_sales"] = "1181164"
            df_raw[movie_id]["blu_sales"] = "376501" 
            df_raw[movie_id]["total_sales"] = "1557665"
        if movie_id == "tt0469641":
            # World Trade Center (2006)
            df_raw[movie_id]["dvd_sales"] = "36986330" 
            df_raw[movie_id]["total_sales"] = "36986330"
        if movie_id == "tt0758794":
            # We Are Marshall (2006)
            df_raw[movie_id]["dvd_sales"] = "28272487" 
            df_raw[movie_id]["total_sales"] = "28272487"
        if movie_id == "tt0137523":
            # Fight Club (1999)
            df_raw[movie_id]["dvd_sales"] = "37030102"
            df_raw[movie_id]["blu_sales"] = "63811448" 
            df_raw[movie_id]["total_sales"] = "100841550"
        if movie_id == "tt0452608":
            # Death Race (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0406375":
            # Zathura (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0430304":
            # Little Man (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0396171":
            # Perfume: The Story of a Murderer (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0107290":
            # Jurassic Park (1993)
            df_raw[movie_id]["dvd_sales"] = "7550139"
            df_raw[movie_id]["blu_sales"] = "9692565"
            df_raw[movie_id]["total_sales"] = "17242704"
        if movie_id == "tt0109444":
            # Clear and Present Danger (1994)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0811138":
            # The Love Guru (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0445934":
            # Blades of Glory (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0486946":
            # Wild Hogs (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0258463":
            # The Bourne Identity (2002)
            df_raw[movie_id]["dvd_sales"] = "10426607"
            df_raw[movie_id]["blu_sales"] = "380059"
            df_raw[movie_id]["total_sales"] = "10806666"
        if movie_id == "tt0452598":
            # Cheaper by the Dozen 2 (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0146838":
            # Any Given Sunday (1999)
            df_raw[movie_id]["blu_sales"] = "192453"
            df_raw[movie_id]["total_sales"] = "192453"
        if movie_id == "tt0949731":
            # The Happening (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0393735":
            # The Shaggy Dog (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0167190":
            # Hellboy (2004)
            df_raw[movie_id]["dvd_sales"] = "379591"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "379591"
        if movie_id == "tt0420238":
            # The Tale of Despereaux (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1034331":
            # Righteous Kill (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0443632":
            # The Sentinel (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0181875":
            # Almost Famous (2000)
            df_raw[movie_id]["blu_sales"] = "537822"
            df_raw[movie_id]["total_sales"] = "537822"
        if movie_id == "tt0455499":
            # Garfield: A Tail of Two Kitties (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0387877":
            # The Black Dahlia (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0831887":
            # The Spirit (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0454824":
            # Flyboys (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0425123":
            # Just Like Heaven (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0379865":
            # Leatherheads (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt7286456":
            # Joker (2019)
            df_raw[movie_id]["dvd_sales"] = "8566745"
            df_raw[movie_id]["blu_sales"] = "24029838"
            df_raw[movie_id]["total_sales"] = "32596583"
        if movie_id == "tt0109830":
            # Forrest Gump (1994) 
            df_raw[movie_id]["blu_sales"] = "2398089"
            df_raw[movie_id]["total_sales"] = "2398089"
        if movie_id == "tt0386588":
            # Hitch (2005)
            df_raw[movie_id]["dvd_sales"] = "16395640"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "16395640"
        if movie_id == "tt0454921":
            # The Pursuit of Happyness (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0112642":
            # Casper (1995)
            df_raw[movie_id]["dvd_sales"] = "74799"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "74799"
        if movie_id == "tt0408790":
            # Flightplan (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120632":
            # City of Angels (1998)
            df_raw[movie_id]["blu_sales"] = "297231"
            df_raw[movie_id]["total_sales"] = "297231"
        if movie_id == "tt0449089":
            # R.V. (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0111282":
            # Stargate (1994)
            df_raw[movie_id]["blu_sales"] = "195486"
            df_raw[movie_id]["total_sales"] = "195486"
        if movie_id == "tt0098439":
            # Kill Bill: Volume 2 (2004)
            df_raw[movie_id]['title'] = "Kill Bill: Volume 2"
            df_raw[movie_id]["blu_sales"] = "934244"
            df_raw[movie_id]["total_sales"] = "934244"
        if movie_id == "tt0824747":
            # Changeling (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0839980":
            # Semi-Pro (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0402022":
            # Aeon Flux (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0414055":
            # Elizabeth: The Golden Age (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0338216":
            # Lucky You (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0463034":
            # You, Me and Dupree (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0814314":
            # Seven Pounds (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0368709":
            # Elizabethtown (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0203009":
            # Moulin Rouge (2001)
            df_raw[movie_id]["blu_sales"] = "213030"
            df_raw[movie_id]["total_sales"] = "213030"
        if movie_id == "tt0418689":
            # Flags of Our Fathers (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0452594":
            # The Break-Up (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0112641":
            # Casino (1995)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1844838"
            df_raw[movie_id]["total_sales"] = "1844838"
        if movie_id == "tt0120863":
            # The Thin Red Line (1998)
            df_raw[movie_id]["blu_sales"] = "221009"
            df_raw[movie_id]["total_sales"] = "221009"
        if movie_id == "tt0790604":
            # Deck the Halls (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0126029":
            # Shrek (2001) 
            df_raw[movie_id]["dvd_sales"] = "13850505"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "13850505"
        if movie_id == "tt0102798":
            # Robin Hood: Prince of Thieves (1991)
            df_raw[movie_id]["blu_sales"] = "337068"
            df_raw[movie_id]["total_sales"] = "337068"
        if movie_id == "tt0110148":
            # Interview with the Vampire: The Vampire Chronicles (1994)
            df_raw[movie_id]["dvd_sales"] = "16737935"
            df_raw[movie_id]["blu_sales"] = "481990"
            df_raw[movie_id]["total_sales"] = "17219925"
        if movie_id == "tt1068680":
            # Yes Man (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0427229":
            # Failure to Launch (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0454848":
            # Inside Man (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120784":
            # Payback (1999)
            df_raw[movie_id]["dvd_sales"] = "896172"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "896172"
        if movie_id == "tt0381971":
            # Curious George (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0365737":
            # Syriana (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0408345":
            # Firewall (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0384537":
            # Silent Hill (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1206885":
            # Rambo: Last Blood (2019)
            df_raw[movie_id]["dvd_sales"] = "8061923"
            df_raw[movie_id]["blu_sales"] = "13999882"
            df_raw[movie_id]["total_sales"] = "22061805"
        if movie_id == "tt1571569":
            # Defiance (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0367959":
            # Hannibal Rising (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0963178":
            # The International (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0362270":
            # The Life Aquatic with Steve Zissou (2004)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "990133"
            df_raw[movie_id]["total_sales"] = "990133"
        if movie_id == "tt0129167":
            # The Iron Giant (1999)
            df_raw[movie_id]["blu_sales"] = "379858"
            df_raw[movie_id]["total_sales"] = "379858"
        if movie_id == "tt0765443":
            # Eastern Promises (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0113010":
            # Fair Game (1995)
            df_raw[movie_id]["dvd_sales"] = "1590574"
            df_raw[movie_id]["blu_sales"] = "284673"
            df_raw[movie_id]["total_sales"] = "1875247"
        if movie_id == "tt0114345":
            # The Scarlet Letter (1995)
            df_raw[movie_id]["blu_sales"] = "6096"
            df_raw[movie_id]["total_sales"] = "6096"
        if movie_id == "tt0421054":
            # Domino (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0891592":
            # Street Fighter: The Legend of Chun-Li (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4426464":
            # Arctic Dogs (2019)
            df_raw[movie_id]["dvd_sales"] = "307001"
            df_raw[movie_id]["blu_sales"] = "432688"
            df_raw[movie_id]["total_sales"] = "739689"
        if movie_id == "tt0097576":
            # Indiana Jones and the Last Crusade (1989)
            df_raw[movie_id]["dvd_sales"] = "13802695"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "13802695"
        if movie_id == "tt1560220":
            # Zombieland: Double Tap (2019)
            df_raw[movie_id]["dvd_sales"] = "4068474"
            df_raw[movie_id]["blu_sales"] = "8050747"
            df_raw[movie_id]["total_sales"] = "12119221"
        if movie_id == "tt0155267":
            # The Thomas Crown Affair (1999)374,086
            df_raw[movie_id]["dvd_sales"] = "374086"
            df_raw[movie_id]["total_sales"] = "374086"
        if movie_id == "tt0109813":
            # The Flintstones (1994)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "340931"
            df_raw[movie_id]["total_sales"] = "340931"
        if movie_id == "tt0825232":
            # Journey to the Center of the Earth (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0401855":
            # Underworld: Evolution (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt3224458":
            # A Beautiful Day in the Neighborhood (2019)
            df_raw[movie_id]["dvd_sales"] = "1672292"
            df_raw[movie_id]["blu_sales"] = "2663060"
            df_raw[movie_id]["total_sales"] = "4335352"
        if movie_id == "tt0314331":
            # Love Actually (2003)
            df_raw[movie_id]["dvd_sales"] = "13308783"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "13308783"
        if movie_id == "tt0408985":
            # Last Holiday (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0450232":
            # 16 Blocks (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt5606664":
            # Doctor Sleep (2019)
            df_raw[movie_id]["dvd_sales"] = "2077992"
            df_raw[movie_id]["blu_sales"] = "4641240"
            df_raw[movie_id]["total_sales"] = "6719232"
        if movie_id == "tt0429589":
            # The Ant Bully (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0445922":
            # Across the Universe (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0959337":
            # Revolutionary Road (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0364970":
            # Babylon A.D. (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0814022":
            # Bangkok Dangerous (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0118956":
            # Deep Rising (1998)
            df_raw[movie_id]["blu_sales"] = "221276"
            df_raw[movie_id]["total_sales"] = "221276"
        if movie_id == "tt1046997":
            # Miracle at St. Anna (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0056937":
            # Cleopatra (1963)
            df_raw[movie_id]["dvd_sales"] = "200620"
            df_raw[movie_id]["blu_sales"] = "2541867"
            df_raw[movie_id]["total_sales"] = "2742487"
        if movie_id == "tt0399295":
            # Lord of War (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt8946378":
            # Knives Out (2019)
            df_raw[movie_id]["blu_sales"] = "2687900"
            df_raw[movie_id]["total_sales"] = "2687900"
        if movie_id == "tt1001508":
            # He's Just Not That Into You (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0362120":
            # Scary Movie 4 (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0134084":
            # Scream 3 (2000)
            df_raw[movie_id]["blu_sales"] = "90453"
            df_raw[movie_id]["total_sales"] = "90453"
        if movie_id == "tt0103874":
            # Bram Stoker's Dracula (1992)
            df_raw[movie_id]["dvd_sales"] = "1667590"
            df_raw[movie_id]["blu_sales"] = "104746"
            df_raw[movie_id]["total_sales"] = "1772336"
        if movie_id == "tt0397313":
            # Eight Below (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0104691":
            # The Last of the Mohicans (1992)
            df_raw[movie_id]["blu_sales"] = "523982"
            df_raw[movie_id]["total_sales"] = "523982"
        if movie_id == "tt0401792":
            # Sin City (2005)
            df_raw[movie_id]["blu_sales"] = "421220"
            df_raw[movie_id]["total_sales"] = "421220"
        if movie_id == "tt0443274":
            # Vantage Point (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0102138":
            # JFK (1991)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "773367"
            df_raw[movie_id]["total_sales"] = "773367"
        if movie_id == "tt0421729":
            # Big Momma's House 2 (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt6189022":
            # Angel Has Fallen (2019)
            df_raw[movie_id]["dvd_sales"] = "7504200"
            df_raw[movie_id]["blu_sales"] = "11442885"
            df_raw[movie_id]["total_sales"] = "18947085"
        if movie_id == "tt0445990":
            # Invincible (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0482571":
            # The Prestige (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0410297":
            # The Lake House (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0472043":
            # Apocalypto (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0758766":
            # Music and Lyrics (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0866439":
            # Made of Honor (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0758730":
            # Aliens vs. Predator - Requiem (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1153702":
            # The Water Horse: Legend of the Deep (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0817538":
            # Drillbit Taylor (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0111143":
            # The Shadow (1994)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1080958"
            df_raw[movie_id]["total_sales"] = "1080958"
        if movie_id == "tt1129442":
            # Transporter 3 (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0430308":
            # Get Rich or Die Tryin' (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0294870":
            # Rent (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0467200":
            # The Other Boleyn Girl (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0444682":
            # The Reaping (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0422720":
            # Marie Antoinette (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0208988":
            # Get Carter (2000)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1111948":
            # Soul Men (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0189192":
            # Just Visiting (2001)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0448134":
            # Sunshine (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0455782":
            # The Hunting Party (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2032572":
            # USS Indianapolis: Men of Courage (2016)
            df_raw[movie_id]["dvd_sales"] = "697328"
            df_raw[movie_id]["blu_sales"] = "279978"
            df_raw[movie_id]["total_sales"] = "977306"
        if movie_id == "tt0490084":
            # Because I Said So (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0379786":
            # Serenity (2005)
            df_raw[movie_id]["dvd_sales"] = "9761947"
            df_raw[movie_id]["blu_sales"] = "157363"
            df_raw[movie_id]["total_sales"] = "9919310"
        if movie_id == "tt0465602":
            # Shoot 'Em Up (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0232500":
            # The Fast and the Furious (2001)
            df_raw[movie_id]["dvd_sales"] = "7229691"
            df_raw[movie_id]["blu_sales"] = "2163100"
            df_raw[movie_id]["total_sales"] = "9392791"
        if movie_id == "tt5822564":
            # The Kitchen (2019)
            df_raw[movie_id]["dvd_sales"] = "598551"
            df_raw[movie_id]["blu_sales"] = "847217"
            df_raw[movie_id]["total_sales"] = "1445768"
        if movie_id == "tt0970411":
            # City of Ember (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0469903":
            # The Express (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0887883":
            # Burn After Reading (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0410377":
            # Nim's Island (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0482603":
            # Space Chimps (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0458352":
            # The Devil Wears Prada (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0478087":
            # 21 (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1033643":
            # What Happens in Vegas... (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0101540":
            # Hotel for Dogs (2009)
            df_raw[movie_id]["dvd_sales"] = "33486352"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "33486352"
        if movie_id == "tt0209958":
            # The Cell (2000)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "168386"
            df_raw[movie_id]["total_sales"] = "168386"
        if movie_id == "tt0437863":
            # The Benchwarmers (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0453556":
            # TMNT (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0417001":
            # Must Love Dogs (2005)
            df_raw[movie_id]["dvd_sales"] = "4869962"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "4869962"
        if movie_id == "tt0762114":
            # License to Wed (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0467197":
            # Max Payne (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0762121":
            # The Nativity Story (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0790686":
            # Mirrors (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0880578":
            # Untraceable (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0426592":
            # Superhero Movie (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0124298":
            # Blast from the Past (1999)
            df_raw[movie_id]["blu_sales"] = "122849"
            df_raw[movie_id]["total_sales"] = "122849"
        if movie_id == "tt0443701":
            # The X-Files: I Want to Believe (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0841046":
            # Walk Hard: The Dewey Cox Story (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0891527":
            # Lions for Lambs (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "":
            # The Tree of Life (2011)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "5535861"
            df_raw[movie_id]["total_sales"] = "5535861"
        if movie_id == "tt1540128":
            # Playing for Keeps (2012)
            df_raw[movie_id]["dvd_sales"] = "2502909"
            df_raw[movie_id]["blu_sales"] = "835135"
            df_raw[movie_id]["total_sales"] = "3338044"
        if movie_id == "tt0383060":
            # Zoom (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0414993":
            # The Fountain (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0401445":
            # A Good Year (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0416496":
            # Bandidas (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0417148":
            # Snakes on a Plane (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "":
            # 21 Bridges (2019)
            df_raw[movie_id]["dvd_sales"] = "562041"
            df_raw[movie_id]["blu_sales"] = "981911"
            df_raw[movie_id]["total_sales"] = "1543952"
        if movie_id == "tt0483607":
            # Doomsday (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1817771":
            # Freaks of Nature (2015)
            df_raw[movie_id]["dvd_sales"] = "147210"
            df_raw[movie_id]["blu_sales"] = "169749"
            df_raw[movie_id]["total_sales"] = "316959"
        if movie_id == "tt0976051":
            # The Reader (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0319343":
            # Elf (2003)
            df_raw[movie_id]["dvd_sales"] = "71280974"
            df_raw[movie_id]["blu_sales"] = "23073433"
            df_raw[movie_id]["total_sales"] = "94354407"
        if movie_id == "tt0457510":
            # Nacho Libre(2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0145531":
            # Stigmata (1999)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "86359"
            df_raw[movie_id]["total_sales"] = "86359"
        if movie_id == "tt0481369":
            # The Number 23 (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0078723":
            # 1941 (1979)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "467070"
            df_raw[movie_id]["total_sales"] = "467070"
        if movie_id == "tt0418647":
            # Dreamer: Inspired by a True Story (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0399146":
            # A History of Violence (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0372873":
            # Dragon Wars: D-War (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0078788":
            # Apocalypse Now (1979)
            df_raw[movie_id]["dvd_sales"] = "606984"
            df_raw[movie_id]["blu_sales"] = "7003869"
            df_raw[movie_id]["total_sales"] = "7610853"
        if movie_id == "tt0087332":
            # Ghostbusters (1984)
            df_raw[movie_id]["dvd_sales"] = "6889446"
            df_raw[movie_id]["blu_sales"] = "4850260"
            df_raw[movie_id]["total_sales"] = "11739706"
        if movie_id == "tt0114709":
            # Toy Story (1995)
            df_raw[movie_id]["dvd_sales"] = "96671201"
            df_raw[movie_id]["blu_sales"] = "22364236"
            df_raw[movie_id]["total_sales"] = "119035437"
        if movie_id == "tt0299658":
            # Chicago (2002)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1188514"
            df_raw[movie_id]["total_sales"] = "1188514"
        if movie_id == "tt0114369":
            # se7en (1995)
            df_raw[movie_id]["dvd_sales"] = "6686191"
            df_raw[movie_id]["blu_sales"] = "332735"
            df_raw[movie_id]["total_sales"] = "7018926"
        if movie_id == "tt0332280":
            # The Notebook (2004)
            df_raw[movie_id]["dvd_sales"] = "84729732"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "84729732"
        if movie_id == "tt0988595":
            # 27 Dresses (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0871426":
            # Baby Mama (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0901476":
            # Bride Wars (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0312004":
            # Wallace & Gromit: The Curse of the Were-Rabbit (2005)
            df_raw[movie_id]["dvd_sales"] = "29224793"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "29224793"
        if movie_id == "tt0431308":
            # P.S. I Love You (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0221027":
            # Blow (2001)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1372898"
            df_raw[movie_id]["total_sales"] = "1372898"
        if movie_id == "tt0139462":
            # Message in a Bottle (1999)
            df_raw[movie_id]["dvd_sales"] = "1951303"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "1951303"
        if movie_id == "tt0110622":
            # Naked Gun 33 1/3: The Final Insult (1994)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "13016"
            df_raw[movie_id]["total_sales"] = "13016"
        if movie_id == "tt0783233":
            # Atonement (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0385726":
            # Glory Road (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0420223":
            # Stranger Than Fiction (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0389722":
            # 30 Days of Night (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0091419":
            # Little Shop of Horrors (1986)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "217376"
            df_raw[movie_id]["total_sales"] = "217376"
        if movie_id == "tt0421206":
            # Gridiron Gang (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1073498":
            # Meet the Spartans (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt8623904":
            # Last Christmas (2019)
            df_raw[movie_id]["dvd_sales"] = "711234"
            df_raw[movie_id]["blu_sales"] = "973688"
            df_raw[movie_id]["total_sales"] = "1684922"
        if movie_id == "tt0446046":
            # Take the Lead (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0114857":
            # Virtuosity (1995)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "75332"
            df_raw[movie_id]["total_sales"] = "75332"
        if movie_id == "tt4463894":
            # Shaft (2019)
            df_raw[movie_id]["dvd_sales"] = "1899764"
            df_raw[movie_id]["blu_sales"] = "1956195"
            df_raw[movie_id]["total_sales"] = "3855959"
        if movie_id == "tt0370032":
            # Ultraviolet (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0395972":
            # North Country (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt5160558":
            # 88 Minutes (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0091225":
            # Howard the Duck (1986)
            df_raw[movie_id]["dvd_sales"] = "1048823"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "1048823"
        if movie_id == "tt0482572":
            # Pride and Glory (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0402901":
            # The Cave (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0350261":
            # An Unfinished Life (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0087843":
            # Once Upon a Time in America (1984)
            df_raw[movie_id]["dvd_sales"] = "71277"
            df_raw[movie_id]["blu_sales"] = "23620144"
            df_raw[movie_id]["total_sales"] = "23691421"
        if movie_id == "tt0087843":
            # Once Upon a Time in America (1984)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0482546":
            # Miss Potter (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2095649":
            # Grace of Monaco (2014)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0358273":
            # Walk the Line (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0870111":
            # Frost/Nixon (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0103639":
            # Aladdin (1992)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "41314769"
            df_raw[movie_id]["total_sales"] = "41314769"
        if movie_id == "tt0087469":
            # Indiana Jones and the Temple of Doom (1984)
            df_raw[movie_id]["dvd_sales"] = "9392247"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "9392247"
        if movie_id == "tt0430922":
            # Role Models (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0265666":
            # The Royal Tenenbaums (2001)
            df_raw[movie_id]["dvd_sales"] = ""
            df_raw[movie_id]["blu_sales"] = "440563"
            df_raw[movie_id]["total_sales"] = "440563"
        if movie_id == "tt0481141":
            # No Reservations (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0107120":
            # Hocus Pocus (1993)
            df_raw[movie_id]["dvd_sales"] = "36182210"
            df_raw[movie_id]["blu_sales"] = "12763891"
            df_raw[movie_id]["total_sales"] = "48946101"
        if movie_id == "tt0414387":
            # Pride & Prejudice (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0083658":
            # Blade Runner
            df_raw[movie_id]["dvd_sales"] = "35434954"
            df_raw[movie_id]["blu_sales"] = "32519996"
            df_raw[movie_id]["total_sales"] = "67954950"
        if movie_id == "tt0498399":
            # We Own the Night (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0397078":
            # Just My Luck (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0478311":
            # Knocked Up (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0494652":
            # Welcome Home Roscoe Jenkins (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0465551":
            # Notes on a Scandal (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0804522":
            # Rendition (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1018785":
            # The Sisterhood of the Traveling Pants 2 (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0139414":
            # Lake Placid (1999)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "762661"
            df_raw[movie_id]["total_sales"] = "762661"
        if movie_id == "tt0425210":
            # Lucky Number Slevin (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0118929":
            # Dark City (1998)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "72012"
            df_raw[movie_id]["total_sales"] = "72012"
        if movie_id == "tt0864761":
            # The Duchess (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0415965":
            # Martian Child (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0405422":
            # The 40 Year-old Virgin (2005)
            df_raw[movie_id]["dvd_sales"] = "27367640"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "27367640"
        if movie_id == "tt0910936":
            # Pineapple Express (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0421239":
            # Red Eye (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0190590":
            # O Brother, Where Art Thou? (2000)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "99482"
            df_raw[movie_id]["total_sales"] = "99482"
        if movie_id == "tt0387131":
            # The Constant Gardener (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1175491":
            # W. (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0335345":
            # The Passion of the Christ (2004)
            df_raw[movie_id]["dvd_sales"] = "8720167"
            df_raw[movie_id]["blu_sales"] = "590215"
            df_raw[movie_id]["total_sales"] = "9310382"
            
        if movie_id == "tt0107614":
            # Mrs. Doubtfire (1993)
            df_raw[movie_id]["dvd_sales"] = "16991310"
            df_raw[movie_id]["blu_sales"] = "1027610"
            df_raw[movie_id]["total_sales"] = "18018920"
        if movie_id == "tt0103855":
            # The Bodyguard (1992)
            df_raw[movie_id]["dvd_sales"] = "5126513"
            df_raw[movie_id]["blu_sales"] = "367204"
            df_raw[movie_id]["total_sales"] = "5493717"
        if movie_id == "tt0108052":
            # Schindler???s List (1993)
            df_raw[movie_id]["dvd_sales"] = "11909494"
            df_raw[movie_id]["blu_sales"] = "510150"
            df_raw[movie_id]["total_sales"] = "12419644"
        if movie_id == "tt0357413":
            # Anchorman: The Legend of Ron Burgundy (2004)
            df_raw[movie_id]["dvd_sales"] = "1099790"
            df_raw[movie_id]["blu_sales"] = "420012"
            df_raw[movie_id]["total_sales"] = "1519802"
        if movie_id == "tt0329101":
            # Freddy vs. Jason (2003)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "97365"
            df_raw[movie_id]["total_sales"] = "97365"
        if movie_id == "tt0398808":
            # Bridge to Terabithia (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1060277":
            # Cloverfield (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0108358":
            # Tombstone (1993)
            df_raw[movie_id]["dvd_sales"] = "27154303"
            df_raw[movie_id]["blu_sales"] = "930814"
            df_raw[movie_id]["total_sales"] = "28085117"
        if movie_id == "tt0466909":
            # The Omen (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0414982":
            # Final Destination 3 (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0308644":
            # Finding Neverland (2004)
            df_raw[movie_id]["dvd_sales"] = "2653204"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "2653204"
        if movie_id == "tt0852713":
            # The House Bunny (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0099685":
            # Goodfellas (1990)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "686215"
            df_raw[movie_id]["total_sales"] = "686215"
        if movie_id == "tt0086250":
            # Scarface (1983)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "5209606"
            df_raw[movie_id]["total_sales"] = "5209606"
        if movie_id == "tt0469494":
            # There Will Be Blood (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0452625":
            # Good Luck Chuck (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0454945":
            # She's the Man (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0453451":
            # Mr. Bean???s Holiday (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0426931":
            # August Rush (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0111161":
            # The Shawshank Redemption (1994)
            df_raw[movie_id]["dvd_sales"] = "2689635"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "2689635"
        if movie_id == "tt0499556":
            # War (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1633356":
            # Shark Night 3D (2011)
            df_raw[movie_id]["dvd_sales"] = "3100212"
            df_raw[movie_id]["blu_sales"] = "899485"
            df_raw[movie_id]["total_sales"] = "3999697"
        if movie_id == "tt0963794":
            # The Ruins (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2461150":
            # Masterminds (2016)
            df_raw[movie_id]["dvd_sales"] = "1643148"
            df_raw[movie_id]["blu_sales"] = "781619"
            df_raw[movie_id]["total_sales"] = "2424767"
        if movie_id == "tt0488658":
            # Unaccompanied Minors (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0388980":
            # The Greatest Game Ever Played (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0787475":
            # Hot Rod (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0090728":
            # Big Trouble in Little China (1986)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "354397"
            df_raw[movie_id]["total_sales"] = "354397"
        if movie_id == "tt0489281":
            # Stop-Loss (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0107007":
            # Gettysburg (1993)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "354397"
            df_raw[movie_id]["total_sales"] = "354397"
        if movie_id == "tt0102984":
            # Stone Cold (1991)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "182388"
            df_raw[movie_id]["total_sales"] = "182388"
        if movie_id == "tt0412080":
            # The World's Fastest Indian (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0800240":
            # Deception (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0120082":
            # Scream 2 (1997)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "100751"
            df_raw[movie_id]["total_sales"] = "100751"
        if movie_id == "tt1620981":
            # The Addams Family (2019)
            df_raw[movie_id]["dvd_sales"] = "2732750"
            df_raw[movie_id]["blu_sales"] = "3174020"
            df_raw[movie_id]["total_sales"] = "5906770"
        if movie_id == "tt0479143":
            # Rocky Balboa (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0101889":
            # The Fisher King (1991)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "251886"
            df_raw[movie_id]["total_sales"] = "251886"
        if movie_id == "tt0465494":
            # Hitman (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0102510":
            # The Naked Gun 2??: The Smell of Fear (1991)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "17469"
            df_raw[movie_id]["total_sales"] = "17469"
        if movie_id == "tt1091751":
            # The Longshots (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0478134":
            # In the Valley of Elah (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1388882":
            # Black Rogue Cops (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0450385":
            # 1408 (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0111070":
            # The Santa Clause (1994)
            df_raw[movie_id]["dvd_sales"] = "22717103"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "22717103"
        if movie_id == "tt0492956":
            # The Game Plan (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0320691":
            # Underworld (2003)
            df_raw[movie_id]["dvd_sales"] = "11383907"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "11383907"
        if movie_id == "tt0398017":
            # Derailed (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0988047":
            # Traitor (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0951216":
            # Mad Money ( 2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0465502":
            # Igor (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0488888":
            # The Libertine (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0076740":
            # Sorcerer (1977)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0465538":
            # Michael Clayton (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1859650":
            # To Rome with Love (2012)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0463998":
            # Freedom Writers (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1023111":
            # Never Back Down (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1027862":
            # Swing Vote (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt3182620":
            # Bitter Harvest (2017)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt5503686":
            # Hustlers (2019)
            df_raw[movie_id]["dvd_sales"] = "3074258"
            df_raw[movie_id]["blu_sales"] = "2331250"
            df_raw[movie_id]["total_sales"] = "5405508"
        if movie_id == "tt0454919":
            # Pulse (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0082971":
            # Raiders of the Lost Ark (1981)
            df_raw[movie_id]["dvd_sales"] = "15960846"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "15960846"
        if movie_id == "tt0101414":
            # Beauty and the Beast (1991)
            df_raw[movie_id]["dvd_sales"] = "126037075"
            df_raw[movie_id]["blu_sales"] = "136052259"
            df_raw[movie_id]["total_sales"] = "262089334"
        if movie_id == "tt0104431":
            # Home Alone 2: Lost in New York (1992)
            df_raw[movie_id]["dvd_sales"] = "1133551"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "1133551"
        if movie_id == "tt0075860":
            # Close Encounters of the Third Kind (1977)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "195138"
            df_raw[movie_id]["total_sales"] = "195138"
        if movie_id == "tt1014775":
            # Beverly Hills Chihuahua (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0486822":
            # Disturbia (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt5325452":
            # Tyler Perry???s Boo! A Madea Halloween (2016)
            df_raw[movie_id]["dvd_sales"] = "10592303"
            df_raw[movie_id]["blu_sales"] = "2449968"
            df_raw[movie_id]["total_sales"] = "13042271"
        if movie_id == "tt0099487":
            # Edward Scissorhands (1990)
            df_raw[movie_id]["dvd_sales"] = "23001913"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "23001913"
        if movie_id == "tt0466342":
            # Date Movie(2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0283426":
            # The Jungle Book 2 (2003)
            df_raw[movie_id]["dvd_sales"] = "1828389"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "1828389"
        if movie_id == "tt0477071":
            # Premonition (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0220099":
            # The Tigger Movie (2000)
            df_raw[movie_id]["dvd_sales"] = "1511028"
            df_raw[movie_id]["blu_sales"] = "483154"
            df_raw[movie_id]["total_sales"] = "3022056"
        if movie_id == "tt1047494":
            # Meet the Browns (2008)
            df_raw[movie_id]["dvd_sales"] = "23007773"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "23007773"
        if movie_id == "tt0799949":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0947802":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0433386":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0483726":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0449467":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0918927":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1013753":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0200465":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0430634":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0479968":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0421073":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0479500":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0475944":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1100119":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0800308":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0089457":
            # Ladyawke (1985)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "707766"
            df_raw[movie_id]["total_sales"] = "3022056"
        if movie_id == "tt0758758":
            # 
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0462519":
            # School for Scoundrels (2006)
            df_raw[movie_id]["dvd_sales"] = "20846315"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "20846315"
        if movie_id == "tt1083456":
            # Fired Up !
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0373074":
            # Kung Fu Hustle (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0455760":
            # Dead Silence (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0419887":
            # The Kite Runner (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1213644":
            # Disaster Movie (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0430431":
            # One Night with the King (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0995039":
            # Ghost Town (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0384680":
            # The Weather Man (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1160368":
            # 12 Rounds (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0799934":
            # Be Kind Rewind (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0413015":
            # Mrs. Henderson Presents (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0804461":
            # Death Sentence (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0780511":
            # Everybody's Fine (2009)
            df_raw[movie_id]["dvd_sales"] = "7440072"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "7440072"
        if movie_id == "tt0399327":
            # The Man (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0462229":
            # Code Name: The Cleaner (2007)
            df_raw[movie_id]["dvd_sales"] = "7629197"
            df_raw[movie_id]["blu_sales"] = "."
            df_raw[movie_id]["total_sales"] = "7629197"
        if movie_id == "tt0763304":
            # Doogal (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0377107":
            # Proof (2005)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0489282":
            # Strange Wilderness (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1034415":
            # Suspiria (2018)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "966509"
            df_raw[movie_id]["total_sales"] = "966509"
        if movie_id == "tt3719896":
            # My All-American(2015)
            df_raw[movie_id]["dvd_sales"] = "2231461"
            df_raw[movie_id]["blu_sales"] = "730910"
            df_raw[movie_id]["total_sales"] = "2962371"
        if movie_id == "tt0446755":
            # The Painted Veil (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1385912":
            # I Can Do Bad All By Myself (2009)
            df_raw[movie_id]["dvd_sales"] = "19657313"
            df_raw[movie_id]["blu_sales"] = "842927"
            df_raw[movie_id]["total_sales"] = "20500240"
        if movie_id == "tt0472198":
            # Notorious (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0452623":
            # Gone Baby Gone
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1135985":
            # Sex Drive
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt6495770":
            # Action Point 
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "216629"
            df_raw[movie_id]["total_sales"] = "216629"
        if movie_id == "tt0443453":
            # Borat
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0094737":
            # Big
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1297695"
            df_raw[movie_id]["total_sales"] = "1297695"
        if movie_id == "tt0356680":
            # The Family Stone
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0926129":
            # Prom Night
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0475276":
            # United 93
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0432291":
            # The Fog
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2357129":
            # Jobs
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2167202":
            # Getaway
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1403241":
            # Wolves
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1085492":
            # The Prince (2014)
            df_raw[movie_id]["dvd_sales"] = "1722069"
            df_raw[movie_id]["blu_sales"] = "325389"
            df_raw[movie_id]["total_sales"] = "2047458"
        if movie_id == "tt5127300":
            # Forsaken (2016)
            df_raw[movie_id]["dvd_sales"] = "1817210"
            df_raw[movie_id]["blu_sales"] = "533542"
            df_raw[movie_id]["total_sales"] = "2350752"
        if movie_id == "tt1023481":
            # Step Up 2 the Streets (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4064028":
            # Hoodwinked (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0395169":
            # Hotel Rwanda (2004)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0486551":
            # Beerfest(2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0058385":
            # My Fair Lady (1964)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0758746":
            # Friday the 13th (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0454841":
            # The Hills Have Eyes
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1148297":
            # Smokin' Aces: The Big Gun
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0979434":
            # Lottery Ticket (2010)
            df_raw[movie_id]["dvd_sales"] = "10422624"
            df_raw[movie_id]["blu_sales"] = "542154"
            df_raw[movie_id]["total_sales"] = "10964778"
        if movie_id == "tt0443543":
            # The Illusionist
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0416508":
            # Becoming Jane
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0815244":
            # Sydney White
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1139668":
            # The Unborn (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0420294":
            # The Texas Chainsaw Massacre: The Beginning (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0425430":
            # The Messengers (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0245686":
            # Joe Dirt
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "203037"
            df_raw[movie_id]["total_sales"] = "203037"
        if movie_id == "tt0430770":
            # The Women (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0497465":
            # Vicky Cristina Barcelona
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0110413":
            # L??on (1994)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1515800"
            df_raw[movie_id]["total_sales"] = "1515800"
        if movie_id == "tt0469623":
            # Things We Lost in the Fire
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4380070":
            # The Immigrant
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "19401"
            df_raw[movie_id]["total_sales"] = "19401"
        if movie_id == "tt0439815":
            # Slither
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0373883":
            # Halloween
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0436697":
            # The Queen (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0906108":
            # Why Did I Get Married?
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0455857":
            # When a Stranger Calls
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0056172":
            # Lawrence of Arabia (1962)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "11791531"
            df_raw[movie_id]["total_sales"] = "11791531"
        if movie_id == "tt0881891":
            # All About Steve (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0427309":
            # The Great Debaters (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0416320":
            # Match Point
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0434215":
            # Flicka
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0419946":
            # The Marine (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0829459":
            # A Mighty Heart
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0453494":
            # Hoot (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0780536":
            # In Bruges (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1031969":
            # The Rocker (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1142433":
            # Post Grad (2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0373469":
            # Kiss Kiss Bang Bang
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0397044":
            # Blood and Chocolate (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2503954":
            # Broken Horses(2015)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2584018":
            # Freedom (2014)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0775539":
            #  Stomp the Yard(2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1179891":
            # My Bloody Valentine(2009)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0971209":
            # A Perfect Getaway
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0770772":
            # I Think I Love My Wife
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0308055":
            # Bobby
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0404203":
            # Little Children
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0388795":
            #Brokeback Mountain
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0937375":
            # This Christmas
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0884328":
            # The Mist
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0498380":
            # Letters from Iwo Jima
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0416185":
            # Resurrecting the Champ (2007)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4939066":
            # Battle for Incheon: Operation Chromite
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0083722":
            # Cat People
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "449390"
            df_raw[movie_id]["total_sales"] = "449390"
        if movie_id == "tt0805564":
            # Lars and the Real Girl
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0073195":
            # Jaws
            df_raw[movie_id]["dvd_sales"] = "5659274"
            df_raw[movie_id]["blu_sales"] = "1693707"
            df_raw[movie_id]["total_sales"] = "7352981"
        if movie_id == "tt0084726":
            # Star Trek II: The Wrath of Khan
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "248171"
            df_raw[movie_id]["total_sales"] = "248171"
        if movie_id == "tt0462590":
            # Step Up
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0481536":
            # Harold & Kumar Escape from Guantanamo Bay
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1082868":
            # Quarantine
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0406759":
            # The Eye
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0479884":
            # Crank (2006)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0429591":
            # Aquamarine
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1084950":
            # Rachel Getting Married
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1042877":
            # Cadillac Records
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0439289":
            # Running with Scissors
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0091276":
            # Invaders from Mars
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "55273"
            df_raw[movie_id]["total_sales"] = "55273"
        if movie_id == "tt2968804":
            # Drive Hard
            df_raw[movie_id]["dvd_sales"] = "31805"
            df_raw[movie_id]["blu_sales"] = "19489"
            df_raw[movie_id]["total_sales"] = "51294"
        if movie_id == "tt0493430":
            # Jackass Number Two
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0416212":
            # The Secret Life of Bees
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0419843":
            # In the Land of Women
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0489270":
            # Saw III
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0204946":
            # Bring It On
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "311139"
            df_raw[movie_id]["total_sales"] = "311139"
        if movie_id == "tt0890870":
            # Saw IV
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0455612":
            # Madea's Family Reunion
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1314655":
            # Devil
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0981227":
            # Nick and Norah's Infinite Playlist (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0424993":
            # Employee of the Month
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4669186":
            # Kevin Hart: What Now?
            df_raw[movie_id]["dvd_sales"] = "1165190"
            df_raw[movie_id]["blu_sales"] = "549854"
            df_raw[movie_id]["total_sales"] = "1715044"
        if movie_id == "tt0420087":
            # A Prairie Home Companion
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0499554":
            # Reno 911!: Miami
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0365485":
            # The Matador
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0785007":
            # Over Her Dead Body
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0454970":
            # Turistas
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1156320":
            # Making of a True Story: Rescue Dawn
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0884224":
            # War Inc
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2556874":
            # Plastic
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0057193":
            # It's a Mad Mad Mad Mad World
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1492246"
            df_raw[movie_id]["total_sales"] = "1492246"
        if movie_id == "tt0482606":
            # The Strangers
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0386032":
            # Sicko
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2950418":
            # Greater
            df_raw[movie_id]["dvd_sales"] = "2046765"
            df_raw[movie_id]["blu_sales"] = "185871"
            df_raw[movie_id]["total_sales"] = "2232636"
        if movie_id == "tt5350540":
            # Skin Trade: Behind the Action, Fighting You Can Believe
            df_raw[movie_id]["dvd_sales"] = "967286"
            df_raw[movie_id]["blu_sales"] = "260732"
            df_raw[movie_id]["total_sales"] = "1228018"
        if movie_id == "tt0211933":
            # Awake
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1185834":
            # Star Wars: The Clone Wars (2008)
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0126886":
            # Election
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "69778"
            df_raw[movie_id]["total_sales"] = "69778"
        if movie_id == "tt0449059":
            # Little Miss Sunshine
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0104454":
            # Howards End
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "173095"
            df_raw[movie_id]["total_sales"] = "173095"
        if movie_id == "tt0482599":
            # Shutter
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0437800":
            # Akeelah and the Bee
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1095174":
            # New in Town
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0437179":
            # The Good Girl
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0437179":
            # See No Evil
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4196848":
            # Mr. Church
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4060866":
            # Code of Honor
            df_raw[movie_id]["dvd_sales"] = "240632"
            df_raw[movie_id]["blu_sales"] = "33688"
            df_raw[movie_id]["total_sales"] = "274320"
        if movie_id == "tt0498353":
            # Hostel: Part II
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1174732":
            # An Education
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0338427":
            # shopgirl
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1772422":
            # Outside Bet
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt3488328":
            # Pound of Flesh
            df_raw[movie_id]["dvd_sales"] = "86236"
            df_raw[movie_id]["blu_sales"] = "51023"
            df_raw[movie_id]["total_sales"] = "137259"
        if movie_id == "tt0467406":
            # Juno
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0832266":
            # Definitely, Maybe
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0433383":
            # Good Night, and Good Luck.
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0379725":
            # Capote
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1611176":
            # The Descent'
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt3125324":
            # Beyond the Lights
            df_raw[movie_id]["dvd_sales"] = "2161645"
            df_raw[movie_id]["blu_sales"] = "529637"
            df_raw[movie_id]["total_sales"] = "2691282"
        if movie_id == "tt1220628":
            # I Hope They Serve Beer in Hell
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2402105":
            # Dom Hemingway
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt1723811":
            # Shame
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1408234"
            df_raw[movie_id]["total_sales"] = "1408234"
        if movie_id == "tt0790712":
            # The Messenger (2009)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "487218"
            df_raw[movie_id]["total_sales"] = "487218"
        if movie_id == "tt2800038":
            # Atlas Shrugged: Who Is John Galt? (2014)
            df_raw[movie_id]["dvd_sales"] = "1038167"
            df_raw[movie_id]["blu_sales"] = "434301"
            df_raw[movie_id]["total_sales"] = "1472468"
        if movie_id == "tt1798243":
            # Rudderless
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0959306":
            # Reach Me (2014)
            df_raw[movie_id]["dvd_sales"] = "61256"
            df_raw[movie_id]["blu_sales"] = "25037"
            df_raw[movie_id]["total_sales"] = "86293"
        if movie_id == "tt0115736":
            # Bound
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "234777"
            df_raw[movie_id]["total_sales"] = "234777"
        if movie_id == "tt2118624":
            # The Final Girls
            df_raw[movie_id]["dvd_sales"] = "417314"
            df_raw[movie_id]["blu_sales"] = "927103"
            df_raw[movie_id]["total_sales"] = "1344417"
        if movie_id == "tt3075362":
            # Anna
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt0057115":
            # The Great Escape
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "745517"
            df_raw[movie_id]["total_sales"] = "745517"
        if movie_id == "tt3614128":
            # Joe
            df_raw[movie_id]["dvd_sales"] = "2229245"
            df_raw[movie_id]["blu_sales"] = "532582"
            df_raw[movie_id]["total_sales"] = "2761827"
        if movie_id == "tt2414822":
            # The Perfect wave (2014)
            df_raw[movie_id]["dvd_sales"] = "823749"
            df_raw[movie_id]["blu_sales"] = "44383"
            df_raw[movie_id]["total_sales"] = "868132"
        if movie_id == "tt4340720":
            # Chain of Command
            df_raw[movie_id]["dvd_sales"] = "993651"
            df_raw[movie_id]["blu_sales"] = "70666"
            df_raw[movie_id]["total_sales"] = "1064317"
        if movie_id == "tt8332674":
            # Truth or Dare
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt4103724":
            # Forever My Girl (2018)
            df_raw[movie_id]["dvd_sales"] = "3270852"
            df_raw[movie_id]["blu_sales"] = "1250955"
            df_raw[movie_id]["total_sales"] = "4521807"
        if movie_id == "tt0088993":
            # Day of the Dead
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "335973"
            df_raw[movie_id]["total_sales"] = "335973"
        if movie_id == "tt4700756":
            # Believe(2016)
            df_raw[movie_id]["dvd_sales"] = "71963"
            df_raw[movie_id]["blu_sales"] = "27582"
            df_raw[movie_id]["total_sales"] = "99545"
        if movie_id == "tt2166834":
            # Batman: The Dark Knight Returns, Part 2
            df_raw[movie_id]["dvd_sales"] = "1931762"
            df_raw[movie_id]["blu_sales"] = "2334439"
            df_raw[movie_id]["total_sales"] = "4266201"
        if movie_id == "tt2761578":
            # Wicked Blood
            df_raw[movie_id]["dvd_sales"] = "60970"
            df_raw[movie_id]["blu_sales"] = "16245"
            df_raw[movie_id]["total_sales"] = "77215"
        if movie_id == "tt0038650":
            # it's a wonderful life
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "3627421"
            df_raw[movie_id]["total_sales"] = "3627421"
        if movie_id == "tt5923204":
            # Frances Ha
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "492026"
            df_raw[movie_id]["total_sales"] = "492026"
        if movie_id == "tt0093512":
            # Maurice
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "138299"
            df_raw[movie_id]["total_sales"] = "138299"
        if movie_id == "tt0815241":
            # Religulous
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if movie_id == "tt2510028":
            # Frontera
            df_raw[movie_id]["dvd_sales"] = "146331"
            df_raw[movie_id]["blu_sales"] = "73648"
            df_raw[movie_id]["total_sales"] = "219979"
        if movie_id == "tt2215673":
            # the Timber
            df_raw[movie_id]["dvd_sales"] = "51007"
            df_raw[movie_id]["blu_sales"] = "14459"
            df_raw[movie_id]["total_sales"] = "65466"
        if movie_id == "tt0038787":
            # Notorious
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "979560"
            df_raw[movie_id]["total_sales"] = "979560"
        if movie_id == "tt0061811":
            # In the Heat of the Night
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "546518"
            df_raw[movie_id]["total_sales"] = "546518"
        if movie_id == "tt1462758":
            # buried
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "1357092"
            df_raw[movie_id]["total_sales"] = "1357092"
        if movie_id == "tt3528666":
            # The Marine 4: Moving Target
            df_raw[movie_id]["dvd_sales"] = "1553531"
            df_raw[movie_id]["blu_sales"] = "346531"
            df_raw[movie_id]["total_sales"] = "1900062"
        if movie_id == "tt3621892":
            # the lunchbox (2014)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "512957"
            df_raw[movie_id]["total_sales"] = "512957"
        if movie_id == "":
            # Grace Unplugged 
            df_raw[movie_id]["dvd_sales"] = "3980659"
            df_raw[movie_id]["blu_sales"] = "536454"
            df_raw[movie_id]["total_sales"] = "4517113"
        if movie_id == "tt2051894":
            # Home Run
            df_raw[movie_id]["dvd_sales"] = "2260989"
            df_raw[movie_id]["blu_sales"] = "300960"
            df_raw[movie_id]["total_sales"] = "2561949"
        if movie_id == "tt2884206":
            # I Origins (2014)
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "398957"
            df_raw[movie_id]["total_sales"] = "398957"
        if movie_id == "tt5620366":
            # the invitation
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "176264"
            df_raw[movie_id]["total_sales"] = "176264"
        if movie_id == "tt4191580":
            # Meet the blacks(2016)
            df_raw[movie_id]["dvd_sales"] = "1098990"
            df_raw[movie_id]["blu_sales"] = "105672"
            df_raw[movie_id]["total_sales"] = "1204662"
        if movie_id == "tt0110057":
            # Hoop Dreams
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "155265"
            df_raw[movie_id]["total_sales"] = "155265"
        if movie_id == "tt0058182":
            # A Hard Day's Night
            df_raw[movie_id]["dvd_sales"] = "."
            df_raw[movie_id]["blu_sales"] = "172840"
            df_raw[movie_id]["total_sales"] = "172840"
        if movie_id == "tt4162992":
            # Rotor DR1
            df_raw[movie_id]["dvd_sales"] = "16113"
            df_raw[movie_id]["blu_sales"] = "17809"
            df_raw[movie_id]["total_sales"] = "33922"
#         if movie_id == "":
#             # 
#             df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
#         if movie_id == "":
#             # 
#             df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
#         if movie_id == "":
#             # 
#             df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
#         if movie_id == "":
#             # 
#             df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
#         if movie_id == "":
#             # 
#             df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        if df_raw[movie_id]["blu_sales"] == ".":
            df_raw[movie_id]["total_sales"] = df_raw[movie_id]["dvd_sales"]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            

