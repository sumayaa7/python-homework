import pandas as pd

df = pd.read_csv("task\\stackoverflow_qa.csv")

df["creationdate"] = pd.to_datetime(df["creationdate"])
before_2014 = df[df["creationdate"].dt.year < 2014]

score_gt_50 = df[df["score"] > 50]

score_50_100 = df[(df["score"] >= 50) & (df["score"] <= 100)]

answered_by_scott = df[df["ans_name"] == "Scott Boston"]

users = ["Unutbu", "Mike Pennington", "Scott Boston", "Demitri", "DarkAnt"]
answered_by_5 = df[df["ans_name"].isin(users)]

march = pd.Timestamp("2014-03-01")
october = pd.Timestamp("2014-10-31")
unutbu_low_score = df[
    (df["creationdate"].between(march, october))
    & (df["ans_name"] == "Unutbu")
    & (df["score"] < 5)
]

score_or_views = df[(df["score"].between(5, 10)) | (df["viewcount"] > 10000)]

not_scott = df[df["ans_name"] != "Scott Boston"]

print("✅ Questions before 2014:", len(before_2014))
print("✅ Score > 50:", len(score_gt_50))
print("✅ Score 50–100:", len(score_50_100))
print("✅ Answered by Scott Boston:", len(answered_by_scott))
print("✅ Answered by 5 users:", len(answered_by_5))
print("✅ Unutbu (Mar–Oct 2014, score < 5):", len(unutbu_low_score))
print("✅ Score 5–10 or view > 10000:", len(score_or_views))
print("✅ Not answered by Scott Boston:", len(not_scott))




import pandas as pd

titanic_df = pd.read_csv("task\\titanic.csv")
female_class1_20_30 = titanic_df[
    (titanic_df["Sex"] == "female")
    & (titanic_df["Pclass"] == 1)
    & (titanic_df["Age"].between(20, 30))
]
fare_over_100 = titanic_df[titanic_df["Fare"] > 100]

survived_alone = titanic_df[
    (titanic_df["Survived"] == 1)
    & (titanic_df["SibSp"] == 0)
    & (titanic_df["Parch"] == 0)
]
embarked_c_fare_50 = titanic_df[
    (titanic_df["Embarked"] == "C") & (titanic_df["Fare"] > 50)
]
siblings_parents = titanic_df[
    (titanic_df["SibSp"] > 0) & (titanic_df["Parch"] > 0)
]
child_not_survived = titanic_df[
    (titanic_df["Age"] <= 15) & (titanic_df["Survived"] == 0)
]
cabin_fare_200 = titanic_df[
    titanic_df["Cabin"].notna() & (titanic_df["Fare"] > 200)
]

odd_passengerid = titanic_df[titanic_df["PassengerId"] % 2 != 0]
unique_tickets = titanic_df[titanic_df["Ticket"].duplicated(keep=False) == False]

miss_class1 = titanic_df[
    (titanic_df["Name"].str.contains("Miss", case=False, na=False))
    & (titanic_df["Pclass"] == 1)
    & (titanic_df["Sex"] == "female")
]
print("✅ Female Class 1 Age 20–30:", len(female_class1_20_30))
print("✅ Fare > 100:", len(fare_over_100))
print("✅ Survived & Alone:", len(survived_alone))
print("✅ Embarked C & Fare > 50:", len(embarked_c_fare_50))
print("✅ SibSp and Parch > 0:", len(siblings_parents))
print("✅ Age ≤ 15 & not survived:", len(child_not_survived))
print("✅ Cabin & Fare > 200:", len(cabin_fare_200))
print("✅ Odd PassengerId:", len(odd_passengerid))
print("✅ Unique Tickets:", len(unique_tickets))
print("✅ Miss in name & Class 1:", len(miss_class1))

