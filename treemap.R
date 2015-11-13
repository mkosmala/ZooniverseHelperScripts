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