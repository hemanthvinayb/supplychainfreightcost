

def fun1(data):
    empty_list= []
    for i in data['Freight Cost (USD)']:
        if len(i)>10:
           i= i.split(":")[1][:-1]
           i=int(i)
           new_data=data[data['ID']==i]
           f_=new_data['Freight Cost (USD)']
           f_= float(f_)
           f_= int(f_)
           empty_list.append(f_)
        else:
            i= float(i)
            i= int(i)
            empty_list.append(i)
    data['Freight Cost (USD)']=empty_list
    return data


def fun2(data):
    empty_list= []
    for i in data['Weight (Kilograms)']:
        if len(i)>10:
           i= i.split(":")[1][:-1]
           i=int(i)
           new_data=data[data['ID']==i]
           f_=new_data['Weight (Kilograms)']
           f_= float(f_)
           f_= int(f_)
           empty_list.append(f_)
        else:
           i= float(i)
           i= int(i)
           empty_list.append(i)
    data['Weight (Kilograms)']=empty_list
    return data
            
           
            
           
            