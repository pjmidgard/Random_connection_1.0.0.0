from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compression c or e for extract: ")
#@Author Jurijus pacalovas
class encypthion_class:

    def encypthion1(self):

                 
                long3=0
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="c" and namez!="e":
                    print("Your enter incorrect letter")
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    
                        
                    namea=""
                    namem=""
                    namema="?"
                    
                    assxw=0
                    
                    nameas=name
                    nac=len(nameas)

                    long=len(name)
                   
                    name_cut=len(".bin")
                    
                    nameas=name+".bin"
                    name_bofore=len(nameas)
                    
                    
                    

                    	 
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        
                
                        size_after2=len(data)
                        #print(size_after2)  
                        
                        if len(data)==0 or len(data)>2**40:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        
                        lenf1=len(data)
                          
                    
                            
  
                            
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)
                                #print(lenf2)
                                cout_compress=0
                                opssite_equal=1
                                count_times_stop=0
                                compress_stop=0
                                while count_times_stop!=1:
                                    cout_compress+=1
                                    compress_stop=0
                                    long_Start=len(size_data2)
                                    size_data3=size_data2
                                    #print(cout_compress)
                                  
                                 
                                    size_data12=""
                                    Times=""

                                    size_data11=""

                                    block=0
                                    blocks=160
                                    Calculus=""
                                    not_compres_file=0
                                    while block<long:
                                        long=len(size_data2)
                                        Calculus=size_data2[block:block+blocks]
                                        Calculus2=size_data2[block:block+blocks]
                                        block+=blocks
                                        Times=-4
                                        Times2=-4
                                        Times3=76
                                        Times4=76
                                        compress=0
                                        compress2=0
                                        compress3=0
                                        compress4=0
                                        compress5=0
                                        compress6=0
                                        compress7=0
                                        compress_start=0
                                        compress_start2=0
                                        save_00=""
                                        save_01=""
                                        save_03=""
                                        save_04=""
                                        save_05=""
                                        Check=0
                                        Number_Times2=-1

                                        while Times!=76:
                                            Times+=4
                                            Times2=-4
                                            while Times2!=76:
                                                Times2+=4
                                                if Times>=0 and Times2>=0 and Calculus[Times:Times+4]!=Calculus[Times2:Times2+4] and Times2!=Times:
                                                    Number_Times=-((Times//4)-(Times2//4))-1
                                                    #print(Number_Times)
                                                    Change=Calculus[Times:Times+4]
                                                    Equal_Not_compress=format(Number_Times,'04b')
                                                    Number_TimesE=format(Number_Times,'04b')
                                                    if opssite_equal==1 and Calculus[Times:Times+3]=="111" and Calculus[Times+4:Times+5]==Equal_Not_compress[3:4] and Calculus[Times2:Times2+3]=="000" and Number_Times>-1 and Number_Times<16  and Times//4>1 and Times//4<16 :

                            
                                                        save_05=Equal_Not_compress[:3]+Number_TimesE[:3]+Calculus2[:Times]+Calculus2[Times+4:Times2]+Calculus2[Times2+4:Times2+5]+Calculus2[Times2+5:80]
                                                        if len(save_05)==78:
                                                            compress4=1
                                                            
                                                    elif opssite_equal==1 and Calculus[Times:Times+3]=="000" and Calculus[Times+4:Times+5]==Equal_Not_compress[3:4] and Calculus[Times2:Times2+3]=="111" and Calculus[Times2+4:Times2+5]==Equal_Not_compress[3:4] and Number_Times>-1 and Number_Times<16 and Times//4>1 and Times//4<16:
                                                        
                                                        


                                                        
                                                           
                                                      
                                                        save_05=Equal_Not_compress[:3]+Number_TimesE[:3]+Calculus2[:Times]+Calculus2[Times+4:Times2]+Calculus2[Times2+4:Times2+5]+Calculus2[Times2+5:80]

                                                        
                                                        if len(save_05)==78:   
                                                            compress2=1
                                                            compress_start=1
                                                            compress4=1
                                                            compress6=1
                                                            #print(len(save_05)) 
                                                        
                                                    
                                        

                                            Times3=76
                                            Times4=76
                                            while Times3!=156:
                                                Times3+=4
                                                Times4=76
                                                    
                                                while Times4!=156:
                                                    Times4+=4
                                                    if Times3>=80 and Times4>=80 and Calculus[Times3:Times3+4]!=Calculus[Times4:Times4+4] and Times4!=Times3:
                                                        Number_Times=-((Times3//4)-(Times4//4))-1
                                                        Change=Calculus[Times3:Times3+4]
                                                        Equal_Not_compress=format(Number_Times,'04b')
                                                        Number_TimesE=format(Number_Times,'04b')

                                                        if opssite_equal==1 and Calculus[Times3:Times3+3]=="111" and Calculus[Times3+4:Times3+5]==Equal_Not_compress[3:4] and Calculus[Times4:Times4+3]=="000" and Calculus[Times4+4:Times4+5]==Equal_Not_compress[3:4] and Number_Times>-1 and Number_Times<16  and Times//4>1 and Times//4<16 or opssite_equal==2 and Calculus[Times:Times+3]=="000" and Calculus[Times+4:Times+5]==Equal_Not_compress[3:4] and Calculus[Times2:Times2+3]=="000" and Calculus[Times2+4:Times2+5]==Equal_Not_compress[3:4] and Number_Times>-1 and Number_Times<16 and Times//4>1 and Times//4<16:
                                                            
                                                            
                                                            
                                                                
                                                            save_03=save_05+Equal_Not_compress[:3]+Number_TimesE[:3]+Calculus2[80:Times2]+Calculus2[Times3+4:Times4]+Calculus2[Times4+4:Times4+5]+Calculus2[Times4+5:]
                                                            if len(save_03)==156:
                                                                compress5=1
                                                                
                                                        elif opssite_equal==1 and Calculus[Times3:Times3+3]=="000" and Calculus[Times3+4:Times3+5]==Equal_Not_compress[3:4] and Calculus[Times4:Times4+3]=="111" and Calculus[Times4+4:Times4+5]==Equal_Not_compress[3:4] and Number_Times>-1 and Number_Times<16 and Times//4>1 and Times//4<16:
                                                            
                                                           
                                                            
                                                               
                                                            
                                                            save_03=save_05+Equal_Not_compress[:3]+Number_TimesE[:3]+Calculus2[80:Times2]+Calculus2[Times3+4:Times4]+Calculus2[Times4+4:Times4+5]+Calculus2[Times4+5:]
                                                            
                                                            
                                                            if len(save_03)==156:
                                                                compress5=1
                                                                compress7=1

                                                                compress=1
                                                                compress3=1
                                                                compress_start2=1
                                                                #print(len(save_03))
                                                                
                                                        
                                                        
                                        if compress4==1 and compress5==1 and compress6==1 and compress7==0 and compress_stop==0:
                                            save_04="10"+save_03
                                
                                            size_data12=size_data12+save_04
                                            #print(len(save_04))
                                        
	                                                    

                                        elif compress4==1 and compress5==1 and compress6==1 and compress7==1 and compress_stop==0:

                                            save_04="0"+save_03
                                            #print(len(save_03))
                                            size_data12=size_data12+save_04
                                            
                                        
                                        else:
                                            not_compress=""
                                            if compress_stop==0:
                                                not_compress="11"
                                                
                                            save_04=not_compress+Calculus2
                                            #print(len(save_04))
                                            size_data12=size_data12+save_04

                                        
                                    size_data2=size_data12[::-1]
                                    #print(len(size_data2))
                                    
                                    long_Stop=len(size_data12)
                                    if long_Start<long_Stop or cout_compress==15 or long_Stop<=320:
                                        count_times_stop=1
                                        
                                   
                                    
                                    
                                cout_compress=format(cout_compress,'04b')
                                size_data11=cout_compress+"1"+size_data3
                                
                                lenf=len(size_data11)
                                            
                                add_bits118=""
                                count_bits=8-lenf%8
                                z=0
                                        
                                if count_bits!=8:
                                    while z<count_bits:
                                        add_bits118="0"+add_bits118
                                        z=z+1
                                                                        
                                                                        
                                size_data11=add_bits118+size_data11
                                
                                
                                
                                
                                
                                #print(size_data11)
                                  
                               
             
                                                                                
                                n = int(size_data11, 2)
                                
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                             
                                jl=binascii.unhexlify(qqwslenf % n)
                                
                                size_after=len(jl)
                                
                                   
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                            
                                assxw=assxw+1
                                if assxw==1:
                                    assx=10
                                    if assx==10:

                                        f2.write(jl)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)

    def encypthion2(self):

                 
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    namea=""
                    namem=""
                    namema="?"
                   
                 
                    assxw=0
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                  
                    
                    long=len(nameas)

                    nac=len(nameas)
                   
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data = binary_file.read()
                      
                      
                        

                        

                    
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    Count_add_block=0

                                    

                                    size_data3=size_data2
                                    
                                    if size_data3[0:9]=="000000001":
                                        size_data3=size_data3[9:]
                                    elif size_data3[0:8]=="00000001":
                                        size_data3=size_data3[8:]
                                    elif size_data3[0:7]=="0000001":
                                        size_data3=size_data3[7:]
                                    elif size_data3[0:6]=="000001":
                                        size_data3=size_data3[6:]
                                    elif size_data3[0:5]=="00001":
                                        size_data3=size_data3[5:]
                                    elif size_data3[0:4]=="0001":
                                        size_data3=size_data3[4:]
                                    elif size_data3[0:3]=="001":
                                        size_data3=size_data3[3:]
                                    elif size_data3[0:2]=="01":
                                        size_data3=size_data3[2:]
                                    elif size_data3[0:1]=="1":
                                        size_data3=size_data3[1:]
                                    
                                    
                                    
                                    size_data11=""
                                    size_data12=""
                                    size_data11=size_data12
                                    
                                    
                                
                                
                                                                                
                                    n = int(size_data11, 2)
                                
                                    qqwslenf=len(size_data11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                
                                    size_after=len(jl)

                                    size_after=len(jl)
                                
                                   
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                       assx=10
                                       if assx==10:

                                          f2.write(jl)
                                          x2 = time()
                                          x3=x2-x
                                          return print(x3)
self=""                                
d=encypthion_class()
    
xw=d.encypthion1()
print(xw)

xw1=d.encypthion2()
print(xw1)
