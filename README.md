# Python Zcash Memo Mailer
## To be used with zcashd (full node) on **LINUX**

IMPORTANT: You MUST update the "from" address in the python code to be the z-address you wish to send from. It is a placeholder by default, "zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

All files need to be in the `/zcash/src/` folder. The python script will open a file in the same directory 
named "mailinglist.txt" that has a z-address on every line (example provided), and ask the user to input a memo. 
It will then assemble a z_sendmany transaction with a 1 zatoshi output and the memo for each recipient listed in mailinglist.txt . 

Change the mode of the `zcashdmailinglist.sh` so it can be executed. `sudo chmod u+x zcashdmailinglist.sh`
Hopefully within the `zcashdmailinglist.sh` the program will have you enter your password to change the mode of `sendletter.sh`.
If it doesn not then you will then need to change the mode of the `sendletter.sh` script so you can execute it. 
`sudo chmod u+x sendletter.sh`. 

The `sendletted.sh` file will be overwritten each time you run the python script.

To check and make sure your memo transaction went through you type: </br>
`zcash-cli z_getoperationresult (["operationid", "OPID NUMBER THAT WAS LISTED AFTER YOU TYPED IN YOUR MEMO"])`

Thanks to [Michael Harms](https://github.com/michaelharms6010) for starting this project and making [Zecmailer](https://www.zecmailer.com/)!

Thoughts or questions you can hit me up on [Twitter](https://twitter.com/shonondray) or send me a #z2z memo </br>
zs13kryzzyrfv6fch5y60chw2d07fpwqrt05p0eg5pqy6jfxz0az33t7uh48txrf49u0glx7fxz0dw
