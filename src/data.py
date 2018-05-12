import csv

home_wins = 0
draw = 0
away_wins = 0
row_num = 0

outfile = open("full_final.csv", "a")
csv_writer = csv.writer(outfile, quoting=csv.QUOTE_NONE)

with open('full.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            if (row_num != 0):
                mRow = row
                home_goal = int(row[34])
                away_goal = int(row[35])
                if home_goal > away_goal:
                    home_wins = 1
                    draw = 0
                    away_wins = 0
                elif home_goal == away_goal:
                    home_wins = 0
                    draw = 1
                    away_wins = 0
                else:
                    home_wins = 0
                    draw = 0
                    away_wins = 1
                del mRow[-1]
                del mRow[-1]
                mRow = map(lambda x: float(x), mRow)
                mRow.append(home_wins)
                mRow.append(draw)
                mRow.append(away_wins)
                csv_writer.writerow(mRow)
        except:
            print(row_num)
        row_num += 1
