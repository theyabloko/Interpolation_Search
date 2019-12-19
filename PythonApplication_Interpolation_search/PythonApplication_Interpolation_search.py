
import threading

def search(list_numbers, search_number, start_list, end_list, flag):
  while(start_list<=end_list and search_number>=list_numbers[start_list] and search_number<=list_numbers[end_list]):
    if(start_list==end_list):
        if list_numbers[start_list] == search_number:
            print("Позиция в списке: ",str(start_list))
            flag=1
        else:
            print("Число не найдено")
    random= start_list + int(((float(end_list-start_list)/(list_numbers[end_list]-list_numbers[start_list]))*(search_number-list_numbers[start_list]))) #random - номер элемента
    if list_numbers[random]==search_number:
        print("Позиция в списке: ",str(random))
        flag=1

    if list_numbers[random]<search_number:
        start_list= random+1
    else:
        end_list= random-1
  if(flag==0):
    print("Число не найдено")



list_numbers=list(map(int ,input("Введите список чисел через пробел: ").split()))
search_number=int(input("Искомое число: "))
start_list=0 #левая часть искомой области
end_list=len(list_numbers)-1 #правая часть искомой области
flag=0 #переменная флаг, 1 - значение найдено, 0 - не найдено

t=threading.Thread(target=search, args=(list_numbers, search_number, start_list, end_list, flag))
t.start()


