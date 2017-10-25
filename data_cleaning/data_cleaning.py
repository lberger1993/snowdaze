import names
import sys
import pandas as pd


def randomize_users(data_frame):
    for i, row in data_frame.iterrows():
        x = (names.get_full_name()).lower()
        x = x.split()
        usn = x[0] + '_' + x[1]
        data_frame.loc[i, "username"] = usn.lower()
        data_frame.loc[i, "emails.0.address"] = usn + '@mail.com'
        data_frame.loc[i, "profile.first_name"] = x[0]
        data_frame.loc[i, "profile.last_name"] = x[1]
        data_frame.loc[i, "profile.beneficiary"] = names.get_full_name()
        data_frame.loc[i, "profile.IBAN"] = ""
        data_frame.loc[i, "profile.name_bank"] = ""
        data_frame.loc[i, "profile.swift_bic"] = ""
    data_frame.to_csv('user_randomized.csv', sep=';')

if __name__ == "__main__":
    location = sys.argv[1]
    df = pd.DataFrame.from_csv(location + 'USERS.csv', encoding='latin-1')
    randomize_users(df)