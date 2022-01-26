import pickle

acc_list=[]#{NO., Name, Type, Ammount}
def intro():
    print ("\n\n\tBANK")
    print ("\n\tMANAGEMENT")
    print ("\n\n\nMADE BY : Enter your name")
    print ("\nSCHOOL : Enter your school name")
def db_creation():
    f1=open('account.dat','wb')
    acc_list=[]
    pickle.dump(acc_list,f1)
    f1.close()
def db_load():
    f2=open('account.dat','rb')
    a=pickle.load(f2)
    f2.close()
    return a
def db_save(a):
    f3=open('account.dat','wb')
    pickle.dump(a,f3)
    f3.close()
def create_account(a):
    if len(a)==0:
        new_account_number=1
    else:
        z=a[-1]
        y=z[0]
        new_account_number=y+1
    while True:
        name=input('Enter the name of the account holder:- ')
        if len(name)==0:
            print('Enter a valid name!')
            continue
        name=name.upper()
        break
    while True:
        ty=input('Enter type of the account (C/S):- ')
        if len(ty)!=1:
            print('Enter ether C or S')
            continue
        ty=ty.upper()
        break
    while True:
        ammt=input('Enter initial amount(>=500 for Saving and >=1000 for Current):- ')
        if not ammt.isdigit():
            print('Enter a valid ammount')
            continue
        ammt=int(ammt)
        if (ty=='C' and ammt<1000)or(ty=='S'and ammt<500):
           print('Enter a valid ammount')
           continue
        break
    new=[new_account_number,name,ty,ammt]
    a.append(new)
    print ("Account Created Successfully")
    print ("YOUR ACCOUNT NUMBER IS: ",new_account_number)
    return a
def deposit_withdraw(a,b,c):
    index=0
    for i in a:
        if i[0]==b:
            z=i
            break
        index+=1
    else:
        print('Account Not Found')
    if c==1:
        while True:
            ammt=input("Enter Amount To Be Deposited:- ")
            if not ammt.isdigit():
                print('Enter a valid amount!')
                continue
            ammt=int(ammt)
            break
    elif c==2:
        while True:
            if z[-1]==0:
                print('No Balance Left')
                break
            else:
                bal=z[-1]
            ammt=input("Enter Amount To Be Withdrawn:- ")
            if not ammt.isdigit():
                print('Enter a valid amount!')
                continue
            ammt=-(int(ammt))
            if (-(ammt))>bal:
                print('Not enough balance')
                break
            break
    else:
        pass
    z[-1]+=ammt
    a[index]=z
    print('The ammount has been updated')
    print('The new balance is',z[-1])
    return a
def display_sp(a,b):
    flag=0
    for i in a:
        if i[0]==b:
            z=i
            flag=1
            break
    if flag==0:
        print('No account found')
    else:
        print('Balance of the account number',z[0],'is',z[-1])
def display_all(a):
    if len(a)==0:
        print('No Accounts Found')
    else:
        print('[Account No., Holder Name, Type, Balance]')
        for i in a:
            print(i)
def delete_account(a,b):
    flag=0
    index=0
    for i in a:
        if i[0]==b:
            z=i
            flag=1
            break
        index+=1
    if flag==0:
        print('No account found')
    else:
        print('The account number',z[0], 'has been deleted')
        del a[index]
    return a
def modify_account(a,b):
    
    index=0
    for i in a:
        if i[0]==b:
            z=i
        
            while True:
                name=input('Enter the name of the account holder:- ')
                if len(name)==0:
                    print('Enter a valid name!')
                    continue
                name=name.upper()
                break
            while True:
                ty=input('Enter type of the account (C/S):- ')
                if len(ty)!=1:
                    print('Enter ether C or S')
                    continue
                ty=ty.upper()
                break
            while True:
                ammt=input('Enter initial amount(>=500 for Saving and >=1000 for Current):- ')
                if not ammt.isdigit():
                    print('Enter a valid ammount')
                    continue
                ammt=int(ammt)
                if (ty=='C' and ammt<1000)or(ty=='S'and ammt<500):
                    print('Enter a valid ammount')
                    continue
                break
            break
        index+=1
    else:
        print('Account not found')
    a[index]=[z[0],name,ty,ammt]
    return a
    
    
    
intro()
while True:
    print(3*"\n",60*"=",'\nStartup\n')
    b=input("Is this the first time running this program?(Y/N):- ")
    if b=='y'or b=='Y':
        db_creation()
        break
    elif b=='n'or b=='N':
        acc_list=db_load()
        break
    else:
        print('Enter a valid input')
    print('\n\n\n')
while True:
    print (3*"\n",60*"=")
    print ("""MAIN MENU
    1. New Account
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. All Account Holder List
    6. Close An Account
    7. Modify An Account
    8. Exit
    """)

    
    ch=input("Enter Your Choice(1~8):- ")
    if ch=='1':
        acc_list=create_account(acc_list)
        db_save(acc_list)
    
    elif ch=='2':
        while True:
            num=input("\n\nEnter Account Number:- ")
            if not num.isdigit():
                print('Enter a valid Account number!')
                continue
            num=int(num)
            break
        acc_list=deposit_withdraw(acc_list,num,1)
        db_save(acc_list)
    elif ch=='3':
            while True:
                num=input("\n\nEnter Account Number:- ")
                if not num.isdigit():
                    print('Enter a valid Account number!')
                    continue
                num=int(num)
                break
            acc_list=deposit_withdraw(acc_list,num,2)
            db_save(acc_list)

    elif ch=='4':
            while True:
                num=input("\n\nEnter Account Number:- ")
                if not num.isdigit():
                    print('Enter a valid Account number!')
                    continue
                num=int(num)
                break
            display_sp(acc_list,num)

    elif ch=='5':
            display_all(acc_list)

    elif ch=='6':
            while True:
                num=input("\n\nEnter Account Number:- ")
                if not num.isdigit():
                    print('Enter a valid Account number!')
                    continue
                num=int(num)
                break
            acc_list=delete_account(acc_list,num)
            db_save(acc_list)
        
    elif ch=='7':
            while True:
                num=input("\n\nEnter Account Number:- ")
                if not num.isdigit():
                    print('Enter a valid Account number!')
                    continue
                num=int(num)
                break
            acc_list=modify_account(acc_list,num)
            db_save(acc_list)

    elif ch=='8':
            db_save(acc_list)
            break
        
    else:
            print ("Input correcr choice...(1-8)")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            

    
