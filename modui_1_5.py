immutable_var = tuple([1,2,3,'string',False])
print(immutable_var)
#immutable_var[0] = 500 # кортеж неизменяемый обьект, поэтому нельзя изменить значения элементов
#print(immutable_var)
mutable_list = [5,10,15,20,25, 'вторник']
print(mutable_list)
mutable_list[0]=8
mutable_list[5]='среда'
print(mutable_list)