import twutilities as tw
import text_analysis as ta
import json
import pandas as pd
import re

sname = raw_input("Right on! Whose tweets do you want to get? (no @ symbol) > ")

timeline = tw.getTimeline(sname, 100)
userdata = tw.getUserData(timeline)

print("\nInfo about this user:")
print(userdata)

# Get the full text of the user's tweets back as a List
usertweets = tw.returnUserTweets(timeline)

# Print the top 20 words in this user's last X tweets, in order
print("\nTop words this user uses:")
topwords = ta.getTopWords(usertweets)
topwordsdisplay = pd.DataFrame(topwords.items()).sort_values([1], ascending=False)
print(topwordsdisplay)

# Print the named entities in these tweets
print("\nTop named entities mentioned by this user:")

# Returns a Set
propernouns = ta.getNamedEntities(usertweets)

# Sort it, turn it into a list, and use the fmtcols utility to show it all pretty-like
pnounslist = sorted(list(propernouns))
ta.fmtcols(pnounslist, 5)
