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
                                not_compres_file=0
                                size_data3=""
                                size_data4=""
                                save_03=""
                                save_04=""
                                cout_compress2=""
                            
                                size_data4=size_data2
                                while count_times_stop!=1:
                                    cout_compress+=1
                                    Stop_compress=0
                                   
                                    long_Start=len(size_data2)
                                    size_data3=size_data2
                                    #print(cout_compress)
                                  
                                 
                                    size_data12=""
                                    Times=""

                                    size_data11=""

                                    block=0
                                    blocks=10
                                    Calculus=""
                                    
                                    
                                    
                                    while block<long:
                                        long=len(size_data2)
                                        Calculus=size_data2[block:block+blocks]
                                        Zero_one_divide=0
                                        Zero_one_divide_result=0
                                        Zero_one_divide_result_second=0
                                        Zero_one_divide_result_second_back=0
                                        save_00=""
                                        save_01=""
                                        save_02=""
                                        
                                        
                                        block+=blocks

                                        
                                        Zero_one_divide=int(Calculus,2)
                                        Zero_one_divide_result=Zero_one_divide//32
                                        Zero_one_divide_result_second=Zero_one_divide_result*32
                                        Zero_one_divide_result_second_back=Zero_one_divide_result_second+1
                                          
                                        if Zero_one_divide_result_second_back==Zero_one_divide and Zero_one_divide_result<2**2 and len(Calculus)==10:
                                            
                                              save_00=format(Zero_one_divide_result,'02b')
                                             
                                              size_data12=size_data12+"0"+save_00+save_00
                                              save_03=save_00
                                              save_04+="0"+save_00
                                              
                                             
                                        
                                        
                                        else:
                                            if   Calculus[0:1]=="0" and Calculus[1:3]==Calculus[3:5] and save_03==Calculus[1:3] and len(Calculus)==10:
                                            	    save_04+="1"
                                            	    
                                            	    save_03=""
                                            	    
                                            	    
                                            	    
                                                 
                                                  
                                                    
                                            save_01=Calculus
                                            
                                            size_data12=size_data12+save_01
                                            #print(Zero_one_divide_result_second_back)
                                            #print(Zero_one_divide)
                                             

                                        
                                    size_data2=size_data12[::-1]
                                    cout_compress_long1=len(save_04) 
                                    #print(len(size_data2))
                                    
                                    long_Stop=len(size_data12)
                                    if long_Stop>=long_Start or cout_compress==(2**16)-1 or long_Stop<=22:
                                        
                                        not_compres_file=0
                                        count_times_stop=1
                                    if cout_compress_long1>2**30:
                                        not_compres_file=1
                                        count_times_stop=1
                                        
                                        
                                        
                                   
                                    
                                    
                                cout_compress_long=len(save_04) 
                                cout_compress2=format(cout_compress_long,'032b') 
                                cout_compress3=format(cout_compress_long,'048b') 
                                cout_compress1=format(cout_compress,'016b')
                                if not_compres_file==0:
                                	size_data11="10"+cout_compress2+save_04+size_data12
                                elif not_compres_file==1:
                                	size_data11="11"+cout_compress3+save_04+size_data12
                          
                                #print(cout_compress1)
                                
                                lenf=len(size_data11)
                                            
                                add_bits118=""
                                count_bits=8-lenf%8
                                z=0
                                        
                                if count_bits!=8:
                                    while z<count_bits:
                                        add_bits118="0"+add_bits118
                                        z=z+1
                                                                        
                                                                        
                                size_data11=cout_compress1+add_bits118+size_data11
                                
                                
                                
                                
                                
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

                                    cout_compress1=int(size_data2[0:16],2) 
                                    size_data2=size_data2[16:] 
                                    size_data7=""
                                    size_data7=size_data2
                                    size_data2=size_data2
                                    
                                    if size_data7[0:9]=="000000001":
                                        size_data2=size_data2[9:]
                                    elif size_data7[0:8]=="00000001":
                                        size_data2=size_data2[8:]
                                    elif size_data7[0:7]=="0000001":
                                        size_data2=size_data2[7:]
                                    elif size_data7[0:6]=="000001":
                                        size_data2=size_data2[6:]
                                    elif size_data7[0:5]=="00001":
                                        size_data2=size_data2[5:]
                                    elif size_data7[0:4]=="0001":
                                        size_data2=size_data2[4:]
                                    elif size_data7[0:3]=="001":
                                        size_data2=size_data2[3:]
                                    elif size_data7[0:2]=="01":
                                        size_data2=size_data2[2:]
                                    elif size_data7[0:1]=="1":
                                        size_data2=size_data2[1:]


                                    lenf2=len(size_data2)
                                    #print(lenf2)
                                    cout_compress=0
                                    opssite_equal=1
                                    count_times_stop=0
                                    not_compres_file=0
                                    size_data3=""
                                    size_data4=""
                                    save_03=""
                                    save_04=""
                                    save_06=""
                                    save_07="" 
                                    cout_compress2=""
                                    Calculus2=""
                                    size_data6=""
                                    
                                    block2=0
                                    blocks2=5
                                    size_data6=size_data2[:1]
                                    if size_data6[0:1]=="0":
                                        size_data2=size_data2[1:]
                                        cout_compress2=int(size_data2[0:32],2)
                                        size_data2=size_data2[32:]

                                    elif size_data6[0:1]=="1":
                                        size_data2=size_data2[1:]
                                        cout_compress2=int(size_data2[0:48],2)
                                        size_data2=size_data2[48:]
                                        
                                    
                                    save_04=size_data2[:cout_compress2]
                                 
                                    size_data2=size_data2[cout_compress2:]
                                
                                    size_data4=size_data2
                                    while cout_compress1!=cout_compress:
                                        cout_compress+=1
                                        Stop_compress=0
                                       
                                        long_Start=len(size_data2)
                                        size_data3=size_data2
                                        size_data2=size_data2
                                        #print(cout_compress)
                                      
                                     
                                        size_data12=""
                                        Times=""

                                        size_data11=""

                                        block=0
                                        blocks=5
                                        Calculus=""
                                        
                                        
                                        
                                        while block<long:
                                            long=len(size_data2)
                                            Calculus=size_data2[block:block+blocks]
                                            Zero_one_divide=0
                                            Zero_one_divide_result=0
                                            Zero_one_divide_result_second=0
                                            Zero_one_divide_result_second_back=0
                                            save_00=""
                                            save_01=""
                                            save_02=""
                                           
                                            
                                            
                                            block+=blocks

                                            
                                            

                                            save_06=save_04[block2:block2+1]
                                            save_07=save_04[block2+1:block2+3]
                                            #print(save_06+save_07)
                                            
                                            
                                            
                                            
                                            
                                            
                                            
                                           
                                           
                                              
                                            if   Calculus[0:1]=="0" and Calculus[1:3]==Calculus[3:5] and save_06=="0" and save_07==Calculus[1:3]:

                                                  Zero_one_divide=int(Calculus[1:3],2)
                                                  Zero_one_divide_result_second=Zero_one_divide*32
                                                  Zero_one_divide_result_second_back=Zero_one_divide_result_second+1
                                                
                                                  save_00=format(Zero_one_divide_result_second_back,'010b')
                                                 
                                                  size_data12=size_data12+save_00
                                                  save_03=save_07
                                                  
                                                 
                                                  block2+=3
                                                
                                                  
                                                  
                                                  
                                                  
                                                 
                                            
                                            
                                            else:
                                                if   Calculus[0:1]=="0" and Calculus[1:3]==Calculus[3:5] and save_03==Calculus[1:3] and save_06=="1":
                                                        
                                                        
                                                        block2+=1
                                                        
                                                       
                                                        
                                                        
                                                     
                                                Calculus2=size_data2[block:block+blocks]      
                                                        
                                                save_01=Calculus+Calculus2
                                                
                                                
                                                size_data12=size_data12+save_01
                                                block+=blocks
                                                #print(Zero_one_divide_result_second_back)
                                                #print(Zero_one_divide)
                                                 

                                            
                                        size_data2=size_data12[::-1]
                                        cout_compress_long1=len(save_04) 
                                        #print(len(size_data2))
                                        
                                        long_Stop=len(size_data12)
                                        
                                            
                                            
                                            
                                       
                                        
                                        
                                    
                                    size_data11=size_data12
                                    
                              
                                    #print(cout_compress1)
                                    
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
                                 
self=""                                
d=encypthion_class()
    
xw=d.encypthion1()
print(xw)

xw1=d.encypthion2()
print(xw1)
