from django.shortcuts import render
from inputs.forms import Reg_Case
from inputs.models import filldetails , Document
# Create your views here.
import os
import re
from django.core.files.storage import default_storage
import pandas as pd
import numpy as np
from django.http import HttpResponse

def process1(data1):
    """
    for i in range(0,len(data)):
        try:
            a_datetime = datetime.strptime(data.iloc[i,0],"%Y-%m-%d %H:%M:%S")
            #print(a_datetime.time())
            timer.append(int(str(a_datetime.time()).split(':')[0])/24)
        except:
            timer.append(12)

    data['date_time']=timer

    from sklearn.preprocessing import LabelEncoder , OneHotEncoder
    onehotencoder = OneHotEncoder(categorical_features=[0,1,2])

    data1 = onehotencoder.fit_transform(data1).toarray()
    data1 = onehotencoder.fit_transform(data1).toarray()
    """

    row2=[]

    for i in range(0,len(data1)):
        if(int(data1.iloc[i][2])<0 or int(data1.iloc[i][2])>90):
            row2.append(0)
        else:
            row2.append(int(data1.iloc[i][2]))
    data1.iloc[:,2]=row2


    row3=[]

    for i in range(0,len(data1)):
        try:
            if(data1.iloc[i][3][0]=='F'):
                row3.append(1)
            else:
                row3.append(0)
        except:
            row2.append(0)
    data1.iloc[:,3]=row3



    row6=[]

    for i in range(0,len(data1)):
        if(data1.iloc[i][6]=="Yes"):
            row6.append(1)
        else:
            row6.append(0)
    data1.iloc[:,6]=row6

    row6=[]


    row8=[]

    for i in range(0,len(data1)):
        if(data1.iloc[i][8]=="Yes"):
            row8.append(1)
        else:
            row8.append(0)
    data1.iloc[:,8]=row8

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X1 = LabelEncoder()
    labelencoder_X2 = LabelEncoder()
    for i in range(3,data1.shape[1]-1):
        if i==5 or i==10 or i==6 or i==8 or i==26:
            continue
        if i<8:
            data1.iloc[:,i]=labelencoder_X1.fit_transform(data1.iloc[:,i])
        else:
            data1.iloc[:,i]=labelencoder_X1.fit_transform(data1.iloc[:,i])
    print(i)

    row27=[]

    for i in range(0,len(data1)):
        try:
            if(data1.iloc[i][27]=='-1'):
                row27.append(0)
            else:
                row27.append(1)
        except:
            row2.append(0)
    data1.iloc[:,27]=row27

    return data1, labelencoder_X1

def process2(data2,labelencoder_X1):
    """
    for i in range(0,len(data)):
        try:
            a_datetime = datetime.strptime(data.iloc[i,0],"%Y-%m-%d %H:%M:%S")
            #print(a_datetime.time())
            timer.append(int(str(a_datetime.time()).split(':')[0])/24)
        except:
            timer.append(12)

    data['date_time']=timer

    from sklearn.preprocessing import LabelEncoder , OneHotEncoder
    onehotencoder = OneHotEncoder(categorical_features=[0,1,2])

    data1 = onehotencoder.fit_transform(data1).toarray()
    data1 = onehotencoder.fit_transform(data1).toarray()
    """


    row2=0
    for i in range(0,len(data2)):
        if(int(data2.iloc[0][2])<0 or int(data2.iloc[0][2])>90):
            row2=0
        else:
            row2  = (int(data2.iloc[0][2]))
    data2.iloc[2]=row2


    row3=0
    for i in range(0,len(data2)):
        try:
            if(data2.iloc[0][3][0]=='F'):
                row3 =1
            else:
                row3=0
        except:
            row2=0
    data2.iloc[0][3]=row3



    row6=0

    if(data2.iloc[0][6][0]== 'Y' or data2.iloc[6][0]== 'y'):
        row6=1
    else:
        row6=0
    data2.iloc[0][6]=row6


    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    #labelencoder_X1 = LabelEncoder()
    #labelencoder_X2 = LabelEncoder()
    for i in range(3,data2.shape[1]-1):
        if i==5 or i==10 or i==6 or i==8 or i==26:
            continue
        if i<8:
            data2.iloc[0][i]=labelencoder_X1.fit_transform(data2.iloc[0][i])
            print(data2.iloc[0][i])
        else:
            data2.iloc[0][i-1]=labelencoder_X1.fit_transform(data2.iloc[0][i-1])
        print(i)

    row27=[]

    row26=0
    for i in range(0,len(data2)):
        try:
            if(data2.iloc[0][26]=='-1'):
                row26=0
            else:
                row26=1
        except:
            row26=0
    data2.iloc[0][26]=row26

    return data2



def processboth(data1,data2):
    """
    for i in range(0,len(data)):
        try:
            a_datetime = datetime.strptime(data.iloc[i,0],"%Y-%m-%d %H:%M:%S")
            #print(a_datetime.time())
            timer.append(int(str(a_datetime.time()).split(':')[0])/24)
        except:
            timer.append(12)

    data['date_time']=timer

    from sklearn.preprocessing import LabelEncoder , OneHotEncoder
    onehotencoder = OneHotEncoder(categorical_features=[0,1,2])

    data1 = onehotencoder.fit_transform(data1).toarray()
    data1 = onehotencoder.fit_transform(data1).toarray()
    """

    row2=[]

    for i in range(0,len(data1)):
        if(data1.iloc[i][2]<0 or data1.iloc[i][2]>90):
            row2.append(0)
        else:
            row2.append(data1.iloc[i][2])
    data1['Age']=row2

    row2=[]
    for i in range(0,len(data2)):
        if(data2.iloc[i][2]<0 or data2.iloc[i][2]>90):
            row2.append(0)
        else:
            row2.append(data2.iloc[i][2])
    data2['Age']=row2



    row3=[]

    for i in range(0,len(data1)):
        try:
            if(data1.iloc[i][3][0]=='F'):
                row3.append(1)
            else:
                row3.append(0)
        except:
            row2.append(0)
    data1['Gender']=row3

    row3=[]
    for i in range(0,len(data2)):
        try:
            if(data2.iloc[i][3][0]=='F'):
                row3.append(1)
            else:
                row3.append(0)
        except:
            row2.append(0)
    data2['Gender']=row3





    row6=[]

    for i in range(0,len(data1)):
        if(data1.iloc[i][6]=="Yes"):
            row6.append(1)
        else:
            row6.append(0)
    data1['self_employed']=row6

    row6=[]

    for i in range(0,len(data2)):
        if(data2.iloc[i][6]=="Yes"):
            row6.append(1)
        else:
            row6.append(0)
    data2['self_employed']=row6


    row8=[]

    for i in range(0,len(data1)):
        if(data1.iloc[i][8]=="Yes"):
            row8.append(1)
        else:
            row8.append(0)
    data1['treatment']=row8

    from sklearn.preprocessing import LabelEncoder, OneHotEncoder
    labelencoder_X1 = LabelEncoder()
    labelencoder_X2 = LabelEncoder()
    for i in range(3,data1.shape[1]-1):
        if i==5 or i==10 or i==6 or i==8 or i==26:
            continue
        if i<8:
            data1.iloc[:,i]=labelencoder_X1.fit_transform(data1.iloc[:,i])
            data2.iloc[:,i]=labelencoder_X1.fit_transform(data2.iloc[:,i])
        else:
            data1.iloc[:,i]=labelencoder_X1.fit_transform(data1.iloc[:,i])
            data2.iloc[:,i-1]=labelencoder_X1.fit_transform(data2.iloc[:,i-1])
        print(i)

    row27=[]

    for i in range(0,len(data1)):
        try:
            if(data1.iloc[i][27]=='-1'):
                row27.append(0)
            else:
                row27.append(1)
        except:
            row2.append(0)
    data1['comments']=row27

    row26=[]
    for i in range(0,len(data2)):
        try:
            if(data2.iloc[i][26]=='-1'):
                row26.append(0)
            else:
                row26.append(1)
        except:
            row26.append(0)
    data2['comments']=row26

    return data1,data2


def ml(csvv):
    data1 = pd.DataFrame(csvv)

    data1 = data1.fillna(str(-1))
    print(data1.shape)

    data1 = process1_data1()



def takeinput(request):
    form = Reg_Case(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.save(commit=True)

            test = []
            test.append(0)
            test.append(0)
            unique_HR =  form.cleaned_data.get('unique_HR')
            unique123 = form.cleaned_data.get('uniq')
            age = form.cleaned_data.get('age')
            test.append(age)
            gender = form.cleaned_data.get('gender')
            test.append(gender)
            country = form.cleaned_data.get('country')
            test.append(country)
            state = form.cleaned_data.get('state')
            test.append(state)
            self_employed = form.cleaned_data.get('self_employed')
            test.append(self_employed)
            family_history = form.cleaned_data.get('family_history')
            test.append(family_history)
            work_interfere = form.cleaned_data.get('work_interfere')
            test.append(work_interfere)
            no_employees = form.cleaned_data.get('no_employees')
            test.append(no_employees)
            remote_work = form.cleaned_data.get('remote_work')
            test.append(remote_work)
            tech_company = form.cleaned_data.get('tech_company')
            test.append(tech_company)
            benefits = form.cleaned_data.get('benefits')
            test.append(benefits)
            care_options = form.cleaned_data.get('care_options')
            test.append(care_options)
            wellness_program = form.cleaned_data.get('wellness_program')
            test.append(wellness_program)
            seek_help = form.cleaned_data.get('seek_help')
            test.append(help)
            anonimity = form.cleaned_data.get('anonimity')
            test.append(anonimity)
            leave = form.cleaned_data.get('leave')
            test.append(leave)
            mental_health_consequence = form.cleaned_data.get('mental_health_consequence')
            test.append(mental_health_consequence)
            phys_health_consequence = form.cleaned_data.get('phys_health_consequence')
            test.append(phys_health_consequence)
            coworkers =form.cleaned_data.get('coworkers')
            test.append(coworkers)
            supervisor =form.cleaned_data.get('supervisor')
            test.append(supervisor)
            mental_health_interview = form.cleaned_data.get('mental_health_interview')
            test.append(mental_health_interview)
            phys_health_interview = form.cleaned_data.get('phys_health_interview')
            test.append(phys_health_interview)
            mental_vs_physical = form.cleaned_data.get('mental_vs_physical')
            test.append(mental_vs_physical)
            obs_consequence = form.cleaned_data.get('obs_consequence')
            test.append(obs_consequence)
            comments =form.cleaned_data.get('comments')
            test.append(comments)

            k = Document.objects.filter()
            print(k[0])
            raw_data = default_storage.open(os.path.join('', str(k[0].csvfile1)), 'r')
            data = raw_data.read().splitlines()
            #print(data)
            csvv = []
            rt=0
            for i in data:
                if rt==0:
                    rt=rt+1
                    continue
                else:
                    csvv.append(i.split(','))
                rt=rt+1
            print(comments)
            data1 = pd.DataFrame(csvv)
            #data2 = np.array(test)
            #data2 = data2.reshape(-1)
            data2 = pd.DataFrame(test)

            data1 = data1.fillna(str(-1))
            data2 = data2.fillna(str(-1))


            data2 = pd.DataFrame(data2)
            print(data2.shape)
            data1 , labelencoder_X1 = process1(data1)

            print(data1.shape)

            X_train = data1.iloc[:,[6,7,9,23,27]]#,13,14,15,16,17,18,19,20,21,22,23,24,25]]
            Y_train = data1.iloc[:,8]

            #print(X_train)
            from sklearn.neural_network import MLPClassifier
            clf = MLPClassifier(hidden_layer_sizes=(1024,512), activation="relu", solver='adam', alpha=0.0001, batch_size='auto', learning_rate="constant", learning_rate_init=0.001, power_t=0.5, max_iter=16000, shuffle=True, random_state=None, tol=1e-4, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-8)
            clf.fit(X_train,Y_train)
            print(data2)
            print(data2.shape)
            tester=[]
            klr=np.zeros((1, 5))
            tester.append(data2.iloc[6])
            tester.append(data2.iloc[7])
            tester.append(data2.iloc[8])
            tester.append(data2.iloc[22])
            tester.append(data2.iloc[26])
            print(tester[0][0])
            if tester[0][0]=="Yes":
                klr[0][0]=1
            else:
                klr[0][0]=0

            if tester[1][0]=="Yes":
                klr[0][1]=1
            else:
                klr[0][1]=0

            if tester[2][0]=="Yes":
                klr[0][2]=1
            else:
                klr[0][2]=0

            if tester[3][0]=="Yes":
                klr[0][3]=1
            else:
                klr[0][3]=0

            if(tester[4][0][0]!="N"):
                klr[0][4]=1
            else:
                klr[0][4]=0

            print(tester)
            Y_pred1 = clf.predict(klr)
            klr = klr.reshape(-1, 1)
            print("value ",Y_pred1)
            ans="no"
            print(klr)
            if(Y_pred1[0]==1):
                return HttpResponse("should go for treatment")
            else:
                return HttpResponse("should not go for treatment")
    return render(request,'inputs/forms_index.html',{'form':form})
