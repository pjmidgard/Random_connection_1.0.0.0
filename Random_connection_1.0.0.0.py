                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)
                                cout_compress=0
                                opssite_equal=1
                                while cout_compress!=1000:
                                    cout_compress+=1
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
                                                    Number_Times=((Times//4)-(Times2//4))-1
                                                    Change=Calculus[Times:Times+4]
                                                    Equal_Not_compress=format(Number_Times,'04b')
                                                    if opssite_equal==1 and Calculus[Times2:Times2+4]==Equal_Not_compress and Calculus[Times2+4:Times2+5]==Equal_Not_compress[3:4] or opssite_equal==2 and Calculus[Times2:Times2+4]==Equal_Not_compress and Calculus[Times2+4:Times4+5]!=Equal_Not_compress[3:4]:

                                                        compress4=1
                                                    if opssite_equal==2 and Calculus[Times2:Times2+4]==Equal_Not_compress and Calculus[Times2+4:Times2+5]==Equal_Not_compress[3:4] or opssite_equal==1 and Calculus[Times2:Times2+4]==Equal_Not_compress and Calculus[Times2+4:Times4+5]!=Equal_Not_compress[3:4]:
                                                        
                                                        compress4=1
                                                        compress6=1
                                                if Times>=0 and Times2>=0 and Calculus[Times:Times+4]==Calculus[Times2:Times2+4] and Times2!=Times:
                                                    Number_Times=((Times//4)-(Times-Times2//4))-1
                                                    if Number_Times>=0 and Number_Times<=7 and compress_start==0:
                                                        save_01=Calculus[:Times2+3]+Calculus[Times2+4:80]
                                                        Equal_Not_compress=format(Number_Times,'03b')
                                                        save_05=Calculus2[:Times2+3]+Calculus2[Times2+4:80]
                                                        if len(save_05)==79:
                                                            compress2=1
                                                            compress_start=1
                                                        
                                                            
                                        

                                            Times3=76
                                            Times4=76
                                            while Times3!=156:
                                                Times3+=4
                                                Times4=76
                                                    
                                                while Times4!=156:
                                                    Times4+=4
                                                    if Times3>=80 and Times4>=80 and Calculus[Times3:Times3+4]!=Calculus[Times4:Times4+4] and Times4!=Times3:
                                                        Number_Times=((Times3//4)-(Times4//4))-1
                                                        Change=Calculus[Times3:Times3+4]
                                                        Equal_Not_compress=format(Number_Times,'04b')

                                                        if opssite_equal==1 and Calculus[Times4:Times4+4]==Equal_Not_compress and Calculus[Times4+4:Times4+5]==Equal_Not_compress[3:4] or opssite_equal==2 and Calculus[Times4:Times4+4]==Equal_Not_compress and Calculus[Times4+4:Times4+5]!=Equal_Not_compress[3:4]:
                                                            
                                                            compress5=1
                                                        if opssite_equal==2 and Calculus[Times4:Times4+4]==Equal_Not_compress and Calculus[Times4+4:Times4+5]==Equal_Not_compress[3:4] or opssite_equal==1 and Calculus[Times4:Times4+4]==Equal_Not_compress and Calculus[Times4+4:Times4+5]!=Equal_Not_compress[3:4]:
                                                            
                                                            compress5=1
                                                            compress7=1
                                                    if Times3>=80 and Times4>=80 and Calculus[Times3:Times3+4]==Calculus[Times4:Times4+4] and Times4!=Times3:
                                                        Number_Times2=((Times3//4)-(Times4//4))-1
                                                        if Number_Times2>=0 and Number_Times2<=7 and compress_start2==0 and compress2==1:
                                                            save_03=Calculus[80:Times4+3]+Calculus[Times4+4:]
                                                            Equal_Not_compress=format(Number_Times2,'03b')
                                                            save_03=save_05+Calculus2[80:Times4+3]+Calculus2[Times4+4:]
                                                            if len(save_03)==158:
                                                                compress=1
                                                                compress3=1
                                                                compress_start2=1
                                                                
                                                                
                                                        
                                        if compress3==1 and compress4==1 and compress5==1 and compress6==0 and compress7==0:
                                            save_04="1"+Calculus2
	                                                    

                                        elif compress3==1 and compress4==1 and compress6==1 and compress7==1 and compress7==1:

                                            save_04="0"+save_03
                                            #print(save)
                                            size_data12=size_data12+save_04
                                        else:
                                            save_04="1"+Calculus2
                                            size_data12=size_data12+save_04
                                            #print(save_04)

                                    size_data2=size_data12[::-1]
                                    opssite_equal+=1
                                    if opssite_equal==3:
                                    	opssite_equal=1
                                    #print(len(size_data2))
                                   
                                    
                                    
                                
                                size_data11="1"+size_data12
                                
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
