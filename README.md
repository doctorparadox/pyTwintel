## Howdy, stranger!

This humble toolkit gives a quick and dirty view of a Twitter user's recent timeline history, including basic account info, a Top 20 list of (mostly noncommon) the words they've used, and a list of the named entities (i.e. proper nouns including people, places, organizations, and so on) they've mentioned in their last 100 tweets.

### How to use

Easy peasy. Just invoke "python intel.py" at the command line and it'll prompt you for the screenname to investigate.

### Easy tweaks to be made

* Add more "blacklist" words to filter out by editing common_words.txt (for my own purposes I've left "RT" in there for now, but there are better ways to get a sense of how much an account is retweeting vs. tweeting which I hope to add in a later version)
* Change the number of tweets to fetch from the user timeline in intel.py, or make this a parameter you can pass in like the screenname
* Change the display layout to consolidate the view or remove parts of the user account info you're not interested in, etc.
* Add another "blacklist" to filter out specific entities from the 3rd part of the display, or add a "whitelist" to specifically look for tracked entities
* Store the data for later parsing (coming in a future version -- for now, keeping things simple...)

### Fun things to look for

* Some users show a mismatch between their location as stated in their profile, and the time zone set privately in their settings (the former is displayed publicly while the latter is not) -- this is useful for sniffing out trolls and/or bots masquerading as citizens of someplace else.
* If the 'contributors' flag is set to True (rare), then multiple individuals are expressly allowed to manage this account.
