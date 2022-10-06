#get year user is born 
og=int(input('what year were you born ')) 

#boolean 
bdy=(input("did you celebrate your birthday this year ")) 

#if Boolean is no will add 0 if Boolean is yes will add 1 
ny=bdy=="no" 

age = (2022-og-ny) 

#end Boolean 
#print age 
# 
print(str("you are"),age, str("years old"))