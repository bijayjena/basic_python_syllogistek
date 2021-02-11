#Join two sorted lists such that the final list is also sorted

list1=[int(ele) for ele in input("Enter a list 1: ").split(" ")]
list2=[int(ele) for ele in input("Enter a list 2: ").split(" ")]
list1.sort()
list2.sort()
final_list=list1+list2
final_list.sort()
print(final_list)












# final_list=[]
# ci=cj=i=j=0
# while i<len(list1) and j<len(list2):
#   if(list1[i]<list2[j]):
#       final_list.append(list1[i])
#       ci+=1
#   else:
#       final_list.append(list2[j])
#       c+=1
#       break
# final_list=final_list+list1[i:]+list2[j:]
# print(final_list)