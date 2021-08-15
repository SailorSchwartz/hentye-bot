# hentye-bot
Hentye is a discord bot I created which specialises in mass uploading files.

Put all the files you want into the images folder.

"Pruning" is the act of deleting all files either 0 Bytes or greater than 8 Megabytes.

"Renaming" is the act of renaming all files from 00000 to 99999, which i find is useful for if the bot ever breaks.

The code is currently messy and probably buggy, I'll update it at a later date

It's also fully public domain.


# known issues

"aiohttp.client_exceptions.ClientOSError: [WinError 64] The specified network name is no longer available"
idk how to fix this yet but it sometimes comes up when youve been uploading for quite a long time, best fix i can think of is to just restart the program, delete all the files in /images/ that youve uploaded and try again
