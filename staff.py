def main():
    while 1:
        action=input('输入发起动作：')
        if not action:
            continue
        analy_act(action)

def analy_act(action):
    if action.split()[0] in ('find','add','del','update'):
        if 'where' in action:
            front,behind=action.split('where')
            print(front,behind)
            staff_data=where(behind)
            if front.split()[0] == 'find':
                find(staff_data,front)
            elif front.split()[0] == 'del':
                del_staff(staff_data,front)
            elif front.split()[0] == 'update':
                update_staff(staff_data,front)
        elif action.split()[0] == 'add':
            add_staff(action)
    else:
        print('输入错误')

def option_max(option,goal):
    result=[]
    for index,i in enumerate(li[option]):
        if i > goal:
            prt=[]
            for p in Staff:
                prt.append(li[p][index])
            result.append(prt)
    return result
def option_equle(option,goal):
    result=[]
    for index,i in enumerate(li[option]):
        if i == goal:
            prt=[]
            for p in Staff:
                prt.append(li[p][index])
            result.append(prt)
    return result
def option_min(option,goal):
    result=[]
    for index,i in enumerate(li[option]):
        if i < goal:
            prt=[]
            for p in Staff:
                prt.append(li[p][index])
            result.append(prt)
    return result
def option_like(option,goal):
    result=[]
    for index,i in enumerate(li[option]):
        if goal in i:
            prt=[]
            for p in Staff:
                prt.append(li[p][index])
            result.append(prt)
    return result
def where(ac_behind):
    if '>' in ac_behind:
        option,goal=ac_behind.split('>')
        result=option_max(option.strip(),goal.strip())
        return result
    elif '=' in ac_behind:
        option,goal=ac_behind.split('=')
        result=option_equle(option.strip(),goal.strip())
        return result
    elif '<' in ac_behind:
        option,goal=ac_behind.split('<')
        result=option_min(option.strip(),goal.strip())
        return result
    elif 'like' in ac_behind:
        option,goal=ac_behind.split('like')
        result=option_like(option.strip(),goal.strip())
        return result
    else:
        print('输入误')


def find(staff_data,front):
    filter_front=front.split('from')[0].split()[1:][0].split(',')
    for d in staff_data:
        if '*' in filter_front:
            print(staff_data)
            break
        else:
            for f in filter_front:
                f_index = Staff.index(f)
                print(f,d[f_index])
    print('匹配到%s条数据'%len(staff_data))

def add_staff(action):
    later = action.split('add')[1].split(',')
    # print(later)
    # print(li['staff_id'])
    # print(len(li['staff_id']))
    if later[2] in li['phone']:
        print('输入了重复电话')
    else:
        li['staff_id'].append(len(li['staff_id'])+1)
        li['name'].append(later[0])
        li['age'].append(later[1])
        li['phone'].append(later[2])
        li['dept'].append(later[3])
        li['enroll_date'].append(later[4])
        print(li)
        print('添加了%d次'%(len(later)/5))
        f = open('foods', 'w', encoding='utf-8')
        f.write(str(later))
    # add Alex Li,25,134435344,IT,2015‐10‐29

def del_staff(staff_data,front):
    print(staff_data)
    for i in staff_data:
        id=int(i[0])-1
        print(id)
        li['staff_id'].remove(li['staff_id'][id])
        li['name'].remove(li['name'][id])
        li['age'].remove(li['age'][id])
        li['phone'].remove(li['phone'][id])
        li['dept'].remove(li['dept'][id])
        li['enroll_date'].remove(li['enroll_date'][id])
    print(li)

    #     # print('删除了%d'%action)
    # del from staff where staff_id=3


def update_staff(staff_data,front):
    for_raw=front.split('set')
    print(for_raw)
    print(staff_data)
    if len(for_raw)>=1:
        val,new_val=for_raw[1].strip().split('=')
        for match_n in staff_data:
            staff_id=match_n[0]
            id_index=li['staff_id'].index(staff_id)
            li[val][id_index]=new_val
        print(li)
        print('改变了%d'%len(staff_data))
# update staff_table set age=25 where name = "Alex Li"

f=open('staff_table','r',encoding='UTF-8')
li={}
Staff=['staff_id','name','age','phone','dept','enroll_date']
for i in Staff:
    li[i]=[]
for line in f:
    staff_id,name,age,phone,dept,enroll_date=line.split(',')
    li['staff_id'].append(staff_id)
    li['name'].append(name)
    li['age'].append(age)
    li['phone'].append(phone)
    li['dept'].append(dept)
    li['enroll_date'].append(enroll_date)
print(li)
main()
f.close()
