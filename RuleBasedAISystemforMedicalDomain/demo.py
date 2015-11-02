import string
import itertools

global wm
wm=['has-symptom fever Ed very-high', 
    'has-symptom cough Ed positive', 
    'has-disease poison-ivy Alice negative', 
    'Max says Alice has-disease poison-ivy',  
    'Grace says Don is-healthy', 
    'Grace is-doctor', 
    'Whoopingcough is-contagious', 
    'Ed contacts Alice']



rules= [('0',
                ['has-symptom fever ?patient very-high'],
                ['has-symptom fever ?patient high']),
        ('1',
                ['has-disease whooping-cough ?patient positive'],
                ['has-symptom cough ?patient positive']),
        ('2',
                ['has-disease poison-ivy ?patient positive'],
                ['has-symptom rash ?patient positive']),
        ('3',
                ['has-symptom fever ?patient very-high','has-symptom congestion ?patient positive'],
                ['has-symptom flu ?patient positive']),
        ('4',
                ['has-symptom rash ?patient positive','has-symptom fever ?patient not-high'],
                ['has-disease poison-ivy ?patient positive']),
        ('5',
                ['has-symptom cough ?patient positive','has-symptom fever ?patient very-high'],
                ['has-disease whooping-cough ?patient positive']),
        ('6',
                ['has-symptom fever ?patient negative', 'has-symptom cough ?patient negative','has-symptom rash ?patient negative'],
                ['is-healthy ?patient positive']),
        ('7',
                ['?disease is-contagious', 'has-disease contagious ?patient1 positive','?patient2 contacts ?patient1'],
                ['has-disease contagious ?patient2 positive']),
        ('8',
                ['?doctor is-doctor', '?doctor says ?patient has-disease poison-ivy','?doctor says ?patient has-disease whooping-cough', '?doctor says ?patient is-healthy'],
                ['?doctor says ?patient true'])]
        

def subt(theta,pattern):
  for item in theta:
    position=item.find("/")
    variable=item[:position]
    literal=item[(position+1):]
    if variable in pattern:
        pattern=string.replace(pattern,variable,literal)
        #print pattern
        
    return pattern

def var (obj):
      if (obj[0] == '?'):
                  return True
      return False 
  
  

def unify(P,Q,theta):
   
    if P==Q:
        return 1
    else:
     a=P.split()
     b=Q.split()   
     for x,y in itertools.izip(a,b):
       if x!=y:
         if var(x):
          t= str(x)+"/"+str(y)
          if t not in theta:
           theta.append(t);
          return unify(subt(theta,P),subt(theta,Q),theta) 
         elif var(y):
           t= str(y)+"/"+str(x)
           if t not in theta:
            theta.append(t);
           return unify(subt(theta,P),subt(theta,Q),theta)
         else:
              return 0
              
def checkEqual3(flag):
    return flag[1:] == flag[:-1]              
             
        
#global theta1


#P="has-symptom cough ?doctor positive ?patient"
#Q="has-symptom cough John positive Ed "
#A="shambhavi is wearing white"
#B="shambhavi is wearing white"
#B="Namrata is sitting"
#C="Raj is friend of Sham"
#D="sha is friend of ?friend2"
#w=unify(A,B,theta1);
#r=subt(['?z/doc','?y/?z'],"?y is human")

#theta1=['?patient/Ed','?doctor/John']
#Pattern=subt(P,theta1);

global lhs
global rhs
lhs=[]
rhs=[]
for rule in rules:
    #for x in rule[1]:
     lhs.append(rule[1])
     
for rule in rules:     
     rhs.append(rule[2])
 
 
theta1=[] 

counter=0     
#for fact in wm:      #for each fact in the wm
for count, fact in enumerate(wm):
    #print fact
    #print "Counter"+str(count)
    for ind,i in enumerate(lhs):     #
        lhslen=len(i)
        #print "length"
        #print lhslen
        if lhslen==1:
            l="".join(i)
            print "if theta1"
            print theta1
            assign=unify(l,str(wm[count]),theta1)
            #print "Assign value"+str(assign)
            if assign==1:
                
                
                rhsrule="".join(rhs[ind])
                mwnew=subt(theta1,rhsrule)
                if mwnew not in wm:                   
                   wm.append(mwnew)
                
            #print wm
            
        elif lhslen>1:
            flag=[]
            for subi in i:               #populating the flag    
                l="".join(subi)
                assign=unify(l,str(wm[count]),theta1)
                                
                flag.extend(str(assign))
                
            
            for index in range(len(flag)):   #updating the flag according to the match in wm
                
                if flag[index]=='0':
                    
                    for facts1 in wm:
                        l="".join(i[index])
                        #print l
                        assign=unify(l,str(facts1),theta1)
                        #print assign
                        if assign==1:
                         flag[index]=1
                         
                
   
            if checkEqual3(flag) and 1 in flag:    
                      #print "matched with rule "+str(ind) 
                rhsrule="".join(rhs[ind])                
                mwnew=subt(theta1,rhsrule)
                if mwnew not in wm:                                         
                         wm.append(mwnew)
                
                
            else:
                        
                        for ind2, subrule2 in enumerate(i):
                            print subrule2
                            print ind2
                            print theta1
                            if flag[ind2] == 0:
                                
                                print theta1
                                askuser=subt(theta1,subrule)
                                uservalue==raw_input(askuser+"True / False / Unknown / End")
                                if uservalue == "True":
                                    if askuser not in wm:
                                        wm.append(askuser)
                                        flag[ind2]=1
                                if uservalue == "End":
                                    break;
                                else:
                                    pass;
                                        
                            
                        
                        
    counter=counter+1 
    theta1=[]                
                
                
                
            
            
                        
   
       
       
       
               
               
            
#print str(wm)
print wm    
          