import pandas as pd

#Read in files
qb_df = pd.read_csv("C:\\Users\\jibso\\Downloads\\qb_fantasy_top_24.csv")
rb_df = pd.read_csv("C:\\Users\\jibso\\Downloads\\rb_fantasy_top_36.csv")
wr_df = pd.read_csv("C:\\Users\\jibso\\Downloads\\wr_fantasy_top_36.csv")
te_df = pd.read_csv("C:\\Users\\jibso\\Downloads\\te_fantasy_top_36.csv")

#Clean QB df
def clean_qb_df(qb_df):
    #Drop unnecessary columns
    qb_df= qb_df.drop(['Pos', 'G', 'GS', 'TD%', 'Int%', 'Pass Y/A', 'AY/A', 'Y/C', 'Rate', 'QBR', 'Sk', 
                       'Sk%', 'NY/A', 'ANY/A', '4QC', 'GWD', 'Rush Y/A', 'Rush Y/G', 'Pass Y/G'], axis=1)

    #Rename columns 
    qb_df.rename(columns={'Tm': 'Team', 'Fantasy Points': '2023 Fantasy Points'}, inplace=True)

    #Change data types
    qb_df[['Rush Att', 'Rush Yds', 'Rush TD', 'Fmb']] = qb_df[['Rush Att', 'Rush Yds', 'Rush TD', 'Fmb']].astype(int)

    #Create my rankings
    player_rows = []
    players = ['Lamar Jackson', 'Josh Allen', 'Patrick Mahomes', 'C.J. Stroud', 'Jalen Hurts', 'Brock Purdy', 'Joe Burrow', 
            'Jordan Love', 'Justin Herbert', 'Dak Prescott', 'Trevor Lawrence', 'Tua Tagovailoa']

    for player in players:
        row = qb_df[qb_df['Player'] == player]
        player_rows.append(row)
        my_qb_rankings = pd.DataFrame()
        my_qb_rankings = pd.concat(player_rows, ignore_index=True)

    return my_qb_rankings

#Clean rb_df
def clean_rb_df(rb_df):
    #Drop columns
    rb_df= rb_df.drop(['Pos', 'G', 'GS', 'Rush Y/A', 'Rush Y/G', 'Ctch%', 'Y/R', 'Y/Tgt', 'R/G', 'Rec Y/G'], axis=1)

    #Rename columns 
    rb_df.rename(columns={'Tm': 'Team', 'Fantasy Points': '2023 Fantasy Points'}, inplace=True)

    #Create my rankings
    player_rows = []
    players = ['Breece Hall', 'Jahmyr Gibbs', 'Bijan Robinson', 'Christian McCaffrey', 'Saquon Barkley', 'Travis Etienne', 'De\'Von Achane', 
            'Isiah Pacheco', 'James Cook', 'Kenneth Walker III', 'Rachaad White', 'Kyren Williams']

    for player in players:
        row = rb_df[rb_df['Player'] == player]
        player_rows.append(row)
        my_rb_rankings = pd.DataFrame()
        my_rb_rankings = pd.concat(player_rows, ignore_index=True)

    return my_rb_rankings

#Clean wr_df
def clean_wr_df(wr_df):
    #Drop columns
    wr_df= wr_df.drop(['Pos', 'G', 'GS', 'Rush Y/A', 'Rush Y/G', 'Ctch%', 'Y/R', 'Y/Tgt', 'R/G', 'Rec Y/G', 'Rush Y/A', 'Rush Y/G'], axis=1)

    #Rename columns 
    wr_df.rename(columns={'Tm': 'Team', 'Fantasy Points': '2023 Fantasy Points'}, inplace=True)

    #Create my rankings
    player_rows = []
    players = ['CeeDee Lamb', 'Ja\'Marr Chase', 'Justin Jefferson', 'Amon-Ra St. Brown', 'Tyreek Hill', 'Puka Nacua', 'Garrett Wilson', 
            'D.J. Moore', 'Rashee Rice', 'Nico Collins', 'Jaylen Waddle', 'Zay Flowers']

    for player in players:
        row = wr_df[wr_df['Player'] == player]
        player_rows.append(row)
        my_wr_rankings = pd.DataFrame()
        my_wr_rankings = pd.concat(player_rows, ignore_index=True)

    return my_wr_rankings

#Clean te_df
def clean_te_df(te_df):
    #Drop columns
    te_df= te_df.drop(['Pos', 'G', 'GS', 'Ctch%', 'Y/R', 'Y/Tgt', 'R/G', 'Rec Y/G'], axis=1)

    #Rename columns 
    te_df.rename(columns={'Tm': 'Team', 'Fantasy Points': '2023 Fantasy Points'}, inplace=True)

    #Create my rankings
    player_rows = []
    players = ['Sam LaPorta', 'Trey McBride', 'Dalton Kincaid', 'Mark Andrews', 'Kyle Pitts', 'T.J. Hockenson', 'George Kittle', 
            'Travis Kelce', 'Cole Kmet', 'David Njoku', 'Evan Engram', 'Dalton Schultz']

    for player in players:
        row = te_df[te_df['Player'] == player]
        player_rows.append(row)
        my_te_rankings = pd.DataFrame()
        my_te_rankings = pd.concat(player_rows, ignore_index=True)

    return my_te_rankings

my_qb_rankings = clean_qb_df(qb_df)
my_rb_rankings = clean_rb_df(rb_df)
my_wr_rankings = clean_wr_df(wr_df)
my_te_rankings = clean_te_df(te_df)

my_qb_rankings.to_csv('C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\qb_data\\qb_rankings.csv', index=False)
my_rb_rankings.to_csv('C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\rb_data\\rb_rankings.csv', index=False)
my_wr_rankings.to_csv('C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\wr_data\\wr_rankings.csv', index=False)
my_te_rankings.to_csv('C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\te_data\\te_rankings.csv', index=False)