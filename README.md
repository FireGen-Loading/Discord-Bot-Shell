# Discord Bot Shell
simple *kinda* of shell thing to use bots through command line.

pretty bare bones.

## Commands:
* `i <path>` posts a image at the path
* `m <message>` `<path>` posts a message with a optional path fields
* `r <message id> <message>` `<path>` replies to a message
* `cd` a normal cd command

## Setup:

1. make a folder name ``Profiles``
2. add a `{profile name}.json` file in the folder you just made with the settings of the bot. e.g `sample.json`
3. run `controller.py` in `Discord-Bot-Shell` folder
4. enter the name of the profile into the login. following step 2 example you'd need to enter `sample` as the username

## Settings file:
```json
{
    "Channel id" : 0,
    "Token" : "Bot token"
}
```

replace the 0 near `"Channel id"` with the id of the channel

and replace `"Bot token"` with the token of your bot

### general guide:
this script is made for simple image posting really.
any you will need to either use a file manager and/or discord on the side with this.

but yea it *kind* of acts if tho it a normal command shell, tho it does lack 90% of the features of one.
it's just meant to be a quick way to send custom messages and stuff using bots.
it does also help do know how to use the command line to have this thing work.

yea it does have bugs.
it was just a thing i made in a few hours
