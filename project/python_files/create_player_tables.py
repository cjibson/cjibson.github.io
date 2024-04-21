import pandas as pd

#Read in table data
qb_rankings = pd.read_csv("C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\qb_data\\qb_rankings.csv")
rb_rankings = pd.read_csv("C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\rb_data\\rb_rankings.csv")
wr_rankings = pd.read_csv("C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\wr_data\\wr_rankings.csv")
te_rankings = pd.read_csv("C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\te_data\\te_rankings.csv")


def create_qb_files(qb_rankings):
    #Loop through rows and create a df for each
    rank = 1
    for index, row in qb_rankings.iterrows():
        player_df = pd.DataFrame(row).transpose()

        #Send to csv
        filepath = f"C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\qb_data\\qb_{rank}.csv"
        player_df.to_csv(filepath, index=False)
        rank += 1

def create_rb_files(rb_rankings):
    #Loop through rows and create a df for each
    rank = 1
    for index, row in rb_rankings.iterrows():
        player_df = pd.DataFrame(row).transpose()

        #Send to csv
        filepath = f"C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\rb_data\\rb_{rank}.csv"
        player_df.to_csv(filepath, index=False)
        rank += 1

def create_wr_files(wr_rankings):
    #Loop through rows and create a df for each
    rank = 1
    for index, row in wr_rankings.iterrows():
        player_df = pd.DataFrame(row).transpose()

        #Send to csv
        filepath = f"C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\wr_data\\wr_{rank}.csv"
        player_df.to_csv(filepath, index=False)
        rank += 1

def create_te_files(te_rankings):
    #Loop through rows and create a df for each
    rank = 1
    for index, row in te_rankings.iterrows():
        player_df = pd.DataFrame(row).transpose()

        #Send to csv
        filepath = f"C:\\Users\\jibso\\OneDrive\\Desktop\\Websites\\https---cjibson.github.io-\\project\\data\\te_data\\te_{rank}.csv"
        player_df.to_csv(filepath, index=False)
        rank += 1
        
create_qb_files(qb_rankings)
create_rb_files(rb_rankings)
create_wr_files(wr_rankings)
create_te_files(te_rankings)