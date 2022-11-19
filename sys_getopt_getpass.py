import sys
import getopt
import getpass

# Username = getpass.getuser()
# Paasword = getpass.getpass("Enter The Paasword :-> ")
# print(getpass.getuser()) # Directory name
# if Username== input("Enter The Email :-> ") and Paasword=="Mahendrakar":
#     print("Welcome To Lobby Guru")


# var = sys.argv[1:]
# print(var)
# print(sys.argv)
#terminal me aise likana hai brother : -----> # python (filename) Guru Mahendrakar

# output :-> sys.argv[0] -> ['filename return ']
# output : -> sys.argv[1: ] -> ["Guru","Mahendrakar"]


a ,b = getopt.getopt(sys.argv[1:],"f:m:s:sea:")
print(a,b)

"f:m:s:sea" # means -f -s -m -sea  hoga to : -> (first tuple me ayenge) OR ( nahi hoga to dusre tuple me )
#output = [('-f', 'Guru')] ['Mahendrakar']



#-----------------------------------------------memoryview------------------------------------------------------------------

list = [1,2,3,4,5,6]

