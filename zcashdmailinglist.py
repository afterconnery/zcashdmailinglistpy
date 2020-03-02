# This python script will open a file named "mailinglist.txt" that has a z-address on every line, and ask the user
# to input a memo. It will then assemble a z_sendmany transaction with a 1 zatoshi output and the memo for each recipient listed in
# mailinglist.txt .

 
file = open("mailinglist.txt")
memotext=input("Input Memo (IN QUOTES): ")
hextext=memotext.encode("hex")
outstring=""
output = open("./sendletter.sh","w")
outstring += './zcash-cli z_sendmany "zxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" '
outstring += '"['
 
for a in file:
    outstring += '{\\"address\\": \\"'+a.replace(',','')+'\\",\\"amount\\": 0.00000001, \\"memo\\":\\"'+hextext+'\\"},'
   
 
outstring=outstring[:-1]
outstring+= ']"'
outstring = outstring.replace('\n', '')
output.write(outstring)

