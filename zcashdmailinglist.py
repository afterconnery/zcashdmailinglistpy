# This python script will open a file named "mailinglist.txt" that has a z-address on every line, and ask the user
# to input a memo. It will then assemble a z_sendmany transaction with a 1 zatoshi output and the memo for each recipient listed in
# mailinglist.txt .

 
file = open("mailinglist1.txt")
memotext=input("Input Memo (IN QUOTES): ")
hextext=memotext.encode("hex")
outstring=""
output = open("./sendletter.sh","w")
outstring += './zcash-cli z_sendmany "zs13kryzzyrfv6fch5y60chw2d07fpwqrt05p0eg5pqy6jfxz0az33t7uh48txrf49u0glx7fxz0dw" '
outstring += '"['
 
for a in file:
    outstring += '{\\"address\\": \\"'+a.replace(',','')+'\\",\\"amount\\": 0.00000001, \\"memo\\":\\"'+hextext+'\\"},'
   
 
outstring=outstring[:-1]
outstring+= ']"'
outstring = outstring.replace('\n', '')
output.write(outstring)

