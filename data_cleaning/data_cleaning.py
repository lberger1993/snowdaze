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
    data_frame.to_csv('user_randomized.csv', sep=';')


if __name__ == "__main__":
    location = sys.argv[1]
    df = pd.DataFrame.from_csv(location + 'USERS.csv', encoding='latin-1')
    randomize_users(df)








#"_id"	username	emails.0.address	emails.0.verified	profile.settings.enrolled	profile.settings.role	profile.settings.accepted	profile.settings.creator	profile.settings.number	profile.settings.participants	profile.settings.enrolledAt	profile.has_picture	profile.first_name	profile.last_name	profile.temp_id	profile.t_shirt	profile.birth.date	profile.birth.place	profile.birth.country	profile.info.address	profile.info.city	profile.info.zip	profile.info.province	profile.info.country	profile.thursday_activity	profile.friday_activity	profile.course	profile.phone	profile.team_volley	profile.thursday_rental	profile.race	profile.friday_rental	profile.university	profile.food_allergies	profile.beneficiary	profile.IBAN	profile.name_bank	profile.swift_bic

#df = pd.read_csv(location + 'USERS.csv', index_col=["username"], names=["emails.0.address"], encoding='latin-1')
#print(df)