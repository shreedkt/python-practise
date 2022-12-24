#Write a program to find out whether a student is pass or fail 
# if it requires total 40% and at least 33% in each subject to pass. 
# Assume 3 subjects and take makes as an input from the user.

sub1 = int(input('Enter First Subject Marks\n'))
sub2 = int(input('Enter Second Subject Marks\n'))
sub3 = int(input('Enter Third Subject Marks\n'))
# total = sub1+sub2+sub3
# per = total/3
# print(per)
# if(per>40):
#     print('Pass')
# else:
#     print('Not Pass')
if(sub1<33 or sub2<33 or sub3<33):
    print("You'r fail due to less than 33 marks in a Subject")
elif(sub1+sub2+sub3)/3 <40:
    print("You'r fail becouse your overall percenage is less than 40%")
else:
    print("Congratulation! You'r Pass The Exam")