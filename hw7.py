# Вывести количество пользователей, использующих все имеющиеся интерпретаторы-оболочки из /etc/passwd

f=open("/etc/passwd")
#создаем список из интерпретаторов-оболочек (читаем построчно, строку делим по : и берем 7 элемент, удаляем символ переноса строки)
inetrp = [line.split(":")[6].replace("\n","") for line in f.readlines()]
#для каждой уникальной оболочки set(list) считаем вхождение уникального эл-та в список
for i in set(inetrp):
    print(f"{i} - {inetrp.count(i)} ",end="; ")
f.close()


print()
# Вывести UIDы пользователей, для всех групп из /etc/group
#делаем словарь из пар "имя пол-ля:uid пол-ля"  и  "guid группы пол-ля по умолчаниюЖ имя пол-ля"- из /etc/passwd
f=open("/etc/passwd")
users=[line.split(":")[0] for line in f.readlines()]
f.seek(0)
d_uid={k: v for k, v in zip( users,[line.split(":")[2] for line in f.readlines()])}
f.seek(0)
d_guid={k: v for k, v in zip( [line.split(":")[3] for line in f.readlines()], users)}
f.close()

#Для каждой группы печатаем группы: если guid группы есть в словаре из /etc/passwd печатаем uid соответсвущего пол-ля, для каждого пол-ля
# из /etc/group ищем uid по словарю
f=open("/etc/group")
for line in f.readlines():
    line=line.split(":")
    print(line[0],end=":")
    if line[2] in d_guid.keys():
        print(d_uid[d_guid[line[2]]],end=",")
    users=line[3].replace("\n",'').split(",")
    if users[0]!='':
        for i in users:
            print(d_uid[i],end=",")
    if users[0]=='' and line[2] not in d_guid.keys():
        print(end=",")
    print(end=" ")
f.close()
