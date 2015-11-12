#!/usr/bin/env python

# written by Margaret Kosmala <mkosmala@gmail.com> 2015-11-12

# This script will take classification export files from Zooniverse projects 
# and count the number of classifications done by each user for an arbitrary 
# number of input files. It calculates the total number of classifications 
# across input files and sorts the results by number of classifications from 
# large to small. Useful for single project / input files, as well as when
# managing multiple projects.

import csv
import sys

if len(sys.argv) < 3:
    print "Format: user_classifications.py <output file> <input file1> ... <input fileN>"
    exit(1)

outfilename = sys.argv[1]
infiles = sys.argv[2:]

# number of files
num_files = len(infiles)

# the dictionary is keyed on user id and has a list of N+2 elements,
# one for each file, plus one for the user name, and one for the total count
users = {}

# count classifications for all files
counter = 1
for eachfile in infiles:
    
    # go through the file
    with open(eachfile,'rb') as afile:
    
        areader = csv.reader(afile)
    
        # ignore the header
        areader.next()

        # read each line (classification) and record the user
        # with 0 for users without names
        for row in areader:
        
            # read in the user ID and assign 0 if not logged in
            try:
                user_id = int(row[1])
                user_name = row[0]
            except ValueError:
                user_id = 0
                user_name = "not-logged-in"
        
            # add the user to the dictionary if necessary
            if user_id not in users:
                # +2 is one for the user name, one for the total
                users[user_id] = [0] * (num_files + 2)
                users[user_id][0] = user_name
        
            # tally 
            users[user_id][counter] = users[user_id][counter] + 1

    # increment for the next file        
    counter = counter + 1

# calculate the total for each user
for user_id in users:
    total = sum(users[user_id][1:])
    users[user_id][counter] = total

# print to output file
# sort by total contributions
with open(outfilename,'wb') as ofile:
    
    owriter = csv.writer(ofile)
    
    # header
    headerrow = infiles
    headerrow.insert(0,"user_name")
    headerrow.insert(0,"user_id")
    headerrow.append("total")
    owriter.writerow(headerrow)
    
    # data
    for pairs in sorted(users.items(), key=lambda x: x[1][counter], reverse=True):
        user_id = pairs[0]
        datarow = users[user_id]
        datarow.insert(0,user_id)
        owriter.writerow(datarow)        
   