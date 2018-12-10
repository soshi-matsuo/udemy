import csv
import os

from termcolor import colored


class Robot:
    def __init__(self):
        self.name = 'Roboter'
        # init csv file
        if os.path.exists('roboter/ranking.csv') is False:
            with open('roboter/ranking.csv', 'w') as csv_file:
                field_names = ['Name', 'Votes']
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()

    def ask_name(self):
        human_name = input(colored(
            'Hello! My name is {}.\nWhat\'s your name?\n'.format(self.name), 'green'))
        return human_name

    def recommend(self):
        # convert csv into list to sort it
        with open('roboter/ranking.csv', 'r') as csv_r:
            reader = csv.reader(csv_r)
            sort_list = []
            for row in reader:
                sort_list.append(row)

        # sort data by number of votes
        sort_list.sort(key=lambda row: row[1], reverse=True)

        # recommend restaurant in ranking untill user input 'yes' or 'y'
        for i in range(len(sort_list)):
            try:
                print(sort_list[1 + i])
                ans = input(colored('My recommendation is {}, do you like this? [yes/no]\n'
                            .format(sort_list[1 + i][0]), 'green'))
                ans = ans.lower()
                if ans == 'yes' or ans == 'y':
                    break
                else:
                    continue
            except IndexError:
                break

    def ask_restaurant(self, human_name):
        # ask user's favor
        liked_res = input(colored(
            '{}, what restaurant do you like?\n'.format(human_name), 'green'))
        res_data = liked_res.lower().capitalize()

        # convert csv into list to edit
        with open('roboter/ranking.csv', 'r') as csv_r:
            reader = csv.reader(csv_r)
            new_csv = []
            for row in reader:
                new_csv.append(row)

        # edit list and overwrite to csv
        with open('roboter/ranking.csv', 'w', newline='') as csv_w:
            writer = csv.writer(csv_w)
            res_exist = False
            for line in new_csv[1:]:
                # if user's favor is in list, increase number of votes 
                if line[0] == res_data:
                    line[1] = int(line[1])
                    line[1] += 1
                    res_exist = True
            # if it is not in list, append it newly
            if res_exist is False:
                new_csv.append([res_data, 1])
            # overwrite to csv
            writer.writerows(new_csv)

        print(colored('Thank you {}, Have a nice day!'.format(human_name), 'green'))