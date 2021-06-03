import pandas
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Setting up tables
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.expand_frame_repr', False)
pandas.set_option('display.max_colwidth', None)

# Reading CSV files into program
rohit_df = pandas.read_csv(r'D:\Python Cricket Projects\Rohit_Sharma_data.csv')
sehwag_df = pandas.read_csv(r'D:\Python Cricket Projects\Sehwag_data.csv')
sachin_df = pandas.read_csv(r'D:\Python Cricket Projects\Sachin_data.csv')

# Converting date into readable form for the IDE
rohit_df['Date'] = pandas.to_datetime(rohit_df['Date'])
sehwag_df['Date'] = pandas.to_datetime(sehwag_df['Date'])
sachin_df['Date'] = pandas.to_datetime(sachin_df['Date'])

rohit_df['Player Name'] = rohit_df['Player Name'].astype('string')
rohit_df['Runs'] = rohit_df['Runs'].astype('string')
sehwag_df['Player Name'] = sehwag_df['Player Name'].astype('string')
sehwag_df['Runs'] = sehwag_df['Runs'].astype('string')
sachin_df['Player Name'] = sachin_df['Player Name'].astype('string')
sachin_df['Runs'] = sachin_df['Runs'].astype('string')

# Converting runs to a string to remove the '*' character
rohit_df['Runs Absolute Value'] = rohit_df.Runs.str.replace('*', '', regex=True)
rohit_df['Runs Absolute Value'] = rohit_df['Runs Absolute Value'].astype('int')
sehwag_df['Runs Absolute Value'] = sehwag_df.Runs.str.replace('*', '', regex=True)
sehwag_df['Runs Absolute Value'] = sehwag_df['Runs Absolute Value'].astype('int')
sachin_df['Runs Absolute Value'] = sachin_df.Runs.str.replace('*', '', regex=True)
sachin_df['Runs Absolute Value'] = sachin_df['Runs Absolute Value'].astype('int')

rohit_runs_df = rohit_df[rohit_df['Player Name'] == "RG Sharma"]
sehwag_runs_df = sehwag_df[sehwag_df['Player Name'] == "V Sehwag"]
sachin_runs_df = sachin_df[sachin_df['Player Name'] == "SR Tendulkar"]

rohitNotOutCount, sehwagNotOutCount, sachinNotOutCount = 0, 0, 0

# Looping through the database and counting each time a batsman has remained not out
# This helps with the cumulative average count
for i in range(len(rohit_runs_df)):
    if rohit_runs_df.iloc[i][1][len(rohit_runs_df.iloc[i][1]) - 1] == '*':
        rohitNotOutCount += 1

for i in range(len(sehwag_runs_df)):
    if sehwag_runs_df.iloc[i][1][len(sehwag_runs_df.iloc[i][1]) - 1] == '*':
        sehwagNotOutCount += 1

for i in range(len(sachin_runs_df)):
    if sachin_runs_df.iloc[i][1][len(sachin_runs_df.iloc[i][1]) - 1] == '*':
        sachinNotOutCount += 1

# Calculating each batsman's respective cumulative average
rohitAverage = sum(rohit_runs_df['Runs Absolute Value']) / (len(rohit_runs_df) - rohitNotOutCount)
sehwagAverage = sum(sehwag_runs_df['Runs Absolute Value']) / (len(sehwag_runs_df) - sehwagNotOutCount)
sachinAverage = sum(sachin_runs_df['Runs Absolute Value']) / (len(sachin_runs_df) - sachinNotOutCount)

# Rounding the averages up to two decimal places for better presentation
rohitAverage = round(rohitAverage, 2)
sehwagAverage = round(sehwagAverage, 2)
sachinAverage = round(sachinAverage, 2)

# Calculating each batsman's respective cumulative strike rate
rohitStrikeRate = sum(rohit_runs_df['Runs Absolute Value']) / sum(rohit_runs_df['Balls Faced']) * 100
sehwagStrikeRate = sum(sehwag_runs_df['Runs Absolute Value']) / sum(sehwag_runs_df['Balls Faced']) * 100
sachinStrikeRate = sum(sachin_runs_df['Runs Absolute Value']) / sum(sachin_runs_df['Balls Faced']) * 100

# Rounding off the strike rates to two decimal places for better presentation
rohitStrikeRate = round(rohitStrikeRate, 2)
sehwagStrikeRate = round(sehwagStrikeRate, 2)
sachinStrikeRate = round(sachinStrikeRate, 2)

rohit_250s, sehwag_250s, sachin_250s = 0, 0, 0
rohit_200s, sehwag_200s, sachin_200s = 0, 0, 0
rohit_150s, sehwag_150s, sachin_150s = 0, 0, 0
rohit_100s, sehwag_100s, sachin_100s = 0, 0, 0
rohit_50s, sehwag_50s, sachin_50s = 0, 0, 0

# Looping through the database and checking for milestones
for i in range(len(rohit_runs_df)):
    if rohit_runs_df['Runs Absolute Value'].iloc[i] >= 50:
        rohit_50s += 1
    if rohit_runs_df['Runs Absolute Value'].iloc[i] >= 100:
        rohit_100s += 1
    if rohit_runs_df['Runs Absolute Value'].iloc[i] >= 150:
        rohit_150s += 1
    if rohit_runs_df['Runs Absolute Value'].iloc[i] >= 200:
        rohit_200s += 1
    if rohit_runs_df['Runs Absolute Value'].iloc[i] >= 250:
        rohit_250s += 1

for i in range(len(sehwag_runs_df)):
    if sehwag_runs_df['Runs Absolute Value'].iloc[i] >= 50:
        sehwag_50s += 1
    if sehwag_runs_df['Runs Absolute Value'].iloc[i] >= 100:
        sehwag_100s += 1
    if sehwag_runs_df['Runs Absolute Value'].iloc[i] >= 150:
        sehwag_150s += 1
    if sehwag_runs_df['Runs Absolute Value'].iloc[i] >= 200:
        sehwag_200s += 1
    if sehwag_runs_df['Runs Absolute Value'].iloc[i] >= 250:
        sehwag_250s += 1

for i in range(len(sachin_runs_df)):
    if sachin_runs_df['Runs Absolute Value'].iloc[i] >= 50:
        sachin_50s += 1
    if sachin_runs_df['Runs Absolute Value'].iloc[i] >= 100:
        sachin_100s += 1
    if sachin_runs_df['Runs Absolute Value'].iloc[i] >= 150:
        sachin_150s += 1
    if sachin_runs_df['Runs Absolute Value'].iloc[i] >= 200:
        sachin_200s += 1
    if sachin_runs_df['Runs Absolute Value'].iloc[i] >= 250:
        sachin_250s += 1

# Creating a table to present each batsman's milestones and chance of reaching a particular milestone in a match
milestones = PrettyTable()
milestones.field_names = ["Batsman Name", "Total Matches", "250+", "Chance (250+)", "200+", "Chance (200+)", "150+",
                          "Chance (150+)", "100+", "Chance (100+)", "50+", "Chance (50+)"]
milestones.add_row(
    ["Rohit Sharma", len(rohit_runs_df), rohit_250s, '{:.1%}'.format(rohit_250s / len(rohit_runs_df)), rohit_200s,
     '{:.1%}'.format(rohit_200s / len(rohit_runs_df)), rohit_150s, '{:.1%}'.format(rohit_150s / len(rohit_runs_df)),
     rohit_100s, '{:.1%}'.format(rohit_100s / len(rohit_runs_df)), rohit_50s,
     '{:.1%}'.format(rohit_50s / len(rohit_runs_df))])
milestones.add_row(
    ["Virender Sehwag", len(sehwag_runs_df), sehwag_250s, '{:.1%}'.format(sehwag_250s / len(sehwag_runs_df)),
     sehwag_200s, '{:.1%}'.format(sehwag_200s / len(sehwag_runs_df)), sehwag_150s,
     '{:.1%}'.format(sehwag_150s / len(sehwag_runs_df)), sehwag_100s,
     '{:.1%}'.format(sehwag_100s / len(sehwag_runs_df)), sehwag_50s, '{:.1%}'.format(sehwag_50s / len(sehwag_runs_df))])
milestones.add_row(
    ["Sachin Tendulkar", len(sachin_runs_df), sachin_250s, '{:.1%}'.format(sachin_250s / len(sachin_runs_df)),
     sachin_200s, '{:.1%}'.format(sachin_200s / len(sachin_runs_df)), sachin_150s,
     '{:.1%}'.format(sachin_150s / len(sachin_runs_df)), sachin_100s,
     '{:.1%}'.format(sachin_100s / len(sachin_runs_df)), sachin_50s, '{:.1%}'.format(sachin_50s / len(sachin_runs_df))])

# Calculating how many runs each batsman has cumulatively contributed to in each match
rohitContribution = sum(rohit_runs_df['Runs Absolute Value']) / sum(rohit_df['Runs Absolute Value'])
sehwagContribution = sum(sehwag_runs_df['Runs Absolute Value']) / sum(sehwag_df['Runs Absolute Value'])
sachinContribution = sum(sachin_runs_df['Runs Absolute Value']) / sum(sachin_df['Runs Absolute Value'])

# Converting values to percentages for better presentation
rohitContribution = '{:.1%}'.format(rohitContribution)
sehwagContribution = '{:.1%}'.format(sehwagContribution)
sachinContribution = '{:.1%}'.format(sachinContribution)

# Plotting bar graphs to compare runs scored by each respective batsman to other batsmen in the same games
sachin_df.groupby(['Player Name'])['Runs Absolute Value'].sum().sort_values(ascending=False).head(7).plot(kind='bar',
                                                                                                          color='mediumseagreen')
plt.title('Sachin', fontsize=25)
plt.xlabel('Batsmen', fontsize=16)
plt.xticks(rotation=360, fontsize=7.8)
plt.ylabel('Cumulative Runs', fontsize=13)
plt.show()

sehwag_df.groupby(['Player Name'])['Runs Absolute Value'].sum().sort_values(ascending=False).head(7).plot(kind='bar',
                                                                                                          color='xkcd:scarlet')
plt.title('Sehwag', fontsize=25)
plt.xlabel('Batsmen', fontsize=16)
plt.xticks(rotation=360, fontsize=8)
plt.ylabel('Cumulative Runs', fontsize=15)
plt.show()

rohit_df.groupby(['Player Name'])['Runs Absolute Value'].sum().sort_values(ascending=False).head(7).plot(kind='bar',
                                                                                                         color='xkcd:sky blue')
plt.title('Rohit', fontsize=25)
plt.xlabel('Batsmen', fontsize=16)
plt.xticks(rotation=360, fontsize=9.1)
plt.ylabel('Cumulative Runs', fontsize=15)
plt.show()

# Creating data frames for all Indian players other than the respective batsmen for comparison purposes
non_rohit_df = rohit_df[rohit_df['Player Name'] != 'RG Sharma']
non_sehwag_df = sehwag_df[sehwag_df['Player Name'] != 'V Sehwag']
non_sachin_df = sachin_df[sachin_df['Player Name'] != 'SR Tendulkar']

# Comparing each batsman's total runs to other batsmen in the matches they've played
rohitRunsComparison = (sum(rohit_runs_df['Runs Absolute Value']) / len(rohit_runs_df)) / (
            sum(non_rohit_df['Runs Absolute Value']) / len(non_rohit_df))
sehwagRunsComparison = (sum(sehwag_runs_df['Runs Absolute Value']) / len(sehwag_runs_df)) / (
            sum(non_sehwag_df['Runs Absolute Value']) / len(non_sehwag_df))
sachinRunsComparison = (sum(sachin_runs_df['Runs Absolute Value']) / len(sachin_runs_df)) / (
            sum(non_sachin_df['Runs Absolute Value']) / len(non_sachin_df))

# Rounding all values up to three decimal points for better presentation
rohitRunsComparison = str(round(rohitRunsComparison, 3)) + 'x'
sehwagRunsComparison = str(round(sehwagRunsComparison, 3)) + 'x'
sachinRunsComparison = str(round(sachinRunsComparison, 3)) + 'x'

maxAverage = max(rohitAverage, sehwagAverage, sachinAverage)


def winnerAverage():
    if maxAverage == rohitAverage \
            and maxAverage != sehwagAverage and maxAverage != sachinAverage:
        return "Rohit Sharma"
    elif maxAverage == sehwagAverage \
            and maxAverage != rohitAverage and maxAverage != sachinAverage:
        return "Virender Sehwag"
    elif maxAverage == sachinAverage \
            and maxAverage != rohitAverage and maxAverage != sehwagAverage:
        return "Sachin Tendulkar"
    else:
        return "Tied"


maxStrikeRate = max(rohitStrikeRate, sehwagStrikeRate, sachinStrikeRate)


def winnerStrikeRate():
    if maxStrikeRate == rohitStrikeRate \
            and maxStrikeRate != sehwagStrikeRate and maxStrikeRate != sachinStrikeRate:
        return "Rohit Sharma"
    elif maxStrikeRate == sehwagStrikeRate \
            and maxStrikeRate != rohitStrikeRate and maxStrikeRate != sachinStrikeRate:
        return "Virender Sehwag"
    elif maxStrikeRate == sachinStrikeRate \
            and maxStrikeRate != rohitStrikeRate and maxStrikeRate != sehwagStrikeRate:
        return "Sachin Tendulkar"
    else:
        return "Tied"


maxContribution = max(float(rohitContribution.strip('%')), float(sehwagContribution.strip('%')),
                      float(sachinContribution.strip('%')))


def winnerContribution():
    if maxContribution == float(rohitContribution.strip('%')) \
            and maxContribution != float(sehwagContribution.strip('%')) \
            and maxContribution != float(sachinContribution.strip('%')):
        return "Rohit Sharma"
    elif maxContribution == float(sehwagContribution.strip('%')) \
            and maxContribution != float(rohitContribution.strip('%')) \
            and maxContribution != float(sachinContribution.strip('%')):
        return "Virender Sehwag"
    elif maxContribution == float(sachinContribution.strip('%')) \
            and maxContribution != float(sehwagContribution.strip('%')) \
            and maxContribution != float(rohitContribution.strip('%')):
        return "Sachin Tendulkar"
    else:
        return "Tied"


maxRunsComparison = max(rohitRunsComparison.strip('x'), sehwagRunsComparison.strip('x'), sachinRunsComparison.strip('x'))


def winnerRunsComparison():
    if maxRunsComparison == rohitRunsComparison.strip('x') and maxRunsComparison != sehwagRunsComparison.strip(
            'x') and maxRunsComparison != sachinRunsComparison.strip('x'):
        return "Rohit Sharma"
    elif maxRunsComparison == sehwagRunsComparison.strip('x') and maxRunsComparison != rohitRunsComparison.strip(
            'x') and maxRunsComparison != sachinRunsComparison.strip('x'):
        return "Virender Sehwag"
    elif maxRunsComparison == sachinRunsComparison.strip('x') and maxRunsComparison != sehwagRunsComparison.strip(
            'x') and maxRunsComparison != rohitRunsComparison.strip('x'):
        return "Sachin Tendulkar"
    else:
        return "Tied"


# Creating a table to present all the data we have gathered thus far
finalTable = PrettyTable()
finalTable.add_column("Parameter", ["Average", "Strike Rate", "Team Contribution", "Runs Comparison"])
finalTable.add_column("Rohit Sharma", [rohitAverage, rohitStrikeRate, rohitContribution, rohitRunsComparison])
finalTable.add_column("Virender Sehwag", [sehwagAverage, sehwagStrikeRate, sehwagContribution, sehwagRunsComparison])
finalTable.add_column("Sachin Tendulkar", [sachinAverage, sachinStrikeRate, sachinContribution, sachinRunsComparison])
finalTable.add_column("Winner", [winnerAverage(), winnerStrikeRate(), winnerContribution(), winnerRunsComparison()])

print(milestones)
print(finalTable)
