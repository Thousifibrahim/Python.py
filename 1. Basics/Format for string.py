# FOrmat

key_format = 'Emp no{no},Emp name {name} , Emp sal{sal} , emp address{add} , emp Blood {group}'.format(no=1 ,name ="Shahid" ,sal=1000 , add = "banaglore" ,group = "0+")


print(key_format)


bank_format= "bank name {name} , IFSC code{ifsc}, branch{add}".format(name='canara',ifsc='789',add='yeshwanthpur')
print(bank_format)



#Hybrid -  Combination of Keyword and positional


friends = 'best friends {0} , guide {guide}  , love{status} , age{1}'.format('dayan, azeem , arbaz, shiva,salaman ',21, guide='No',status='single')

print(friends)

