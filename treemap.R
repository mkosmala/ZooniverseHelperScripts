# Written by Margaret Kosmala <mkosmala@gmail.com> 2015-11-12
# Adapted from Philip Brohan's code posted 2013-05-01 to 
#    Zooniverse science team group blog
# This version updates Philip's code to use the newer version
#    of the treemap package
#
# This code will create a "treemap" visualization. It is useful
# for showing the relative contributions of your users to your
# Zooniverse project. Each square represents a user and the
# size of the square is proportional to the number of 
# classifications that user has done. 
#
# The input is a csv file containing one column that has unique
# identifiers for each user (either an ID or username) and 
# another column that indicates how many classifications each
# user has done. 


# run this once
#install.packages('treemap')

# run this all the time
library(treemap)

# ------------------
# fill this part out
# ------------------

# input file
data_filename = 'questions_by_user_mod.csv'

# put your column names here
unique_ids = 'user_name'
num_of_classifications = 'classifications'

# output file
out_filename = 'questions_treemap.png'
out_title = 'Season Spotter Questions - Nov 12, 2015'

# ----------------------------
# now you are ready to run all
# ----------------------------

# read in file
ts = read.csv(data_filename,header=TRUE)

# create the output file
# default is PNG; change to suit your needs
png(file=out_filename,width=960,height=800)

# create the visualization
treemap(ts,
        index=unique_ids,
        vSize=num_of_classifications,
        fontsize.labels=20,
        title=out_title,
        fontsize.title=25)

# close the output file
dev.off()