def fin():
    import time
    time.sleep(5)
    quit()

def mc():
    Lst=[input('Q= '), input('m= '), input('c= '), input('ΔΘ= ')]
    if Lst[0]=='x'or Lst[0]=='?':
        try:
            Lst[1]= float(Lst[1])
            Lst[2]= float(Lst[2])
            Lst[3]= float(Lst[3])
            Q= Lst[1]*Lst[2]*Lst[3]
            return Q            
        except ValueError:
            print('ERROR. Invalid input.')
            fin()
    else:
        try:
            Lst.remove('x')
        except ValueError:
            try:
                Lst.remove('?')
            except ValueError:
                try:
                    Lst[0]=float(Lst[0])
                    Lst[1]=float(Lst[1])
                    Lst[2]=float(Lst[2])
                    Lst[3]=float(Lst[3])
                    print('ERROR. Problem is already solved')
                    if float(Lst[0])!=float(Lst[1])*float(Lst[2])*float(Lst[3]):
                        print('Also The Numbers are wrong.\nQ=mcΔΘ\n{0}*{1}*{2}≠{3}'.format(Lst[1],Lst[2],Lst[3],Lst[0]))
                    fin()
                except ValueError:
                    print('ERROR. Invalid Input.')
                    fin()
        pass
        try:
            Lst[0]=float(Lst[0])
            Lst[1]=float(Lst[1])
            Lst[2]=float(Lst[2])
            Z= Lst[1]*Lst[2]
            return Lst[0]/Z
        except ValueError:
            print('Error. Invalid input.')

######################
######################
######################
######################
            
def PRA(x,u=None,q=None,v=None,I=None,R=None,t=None,PR=None):
    if x=='u':
        try:
            q=float(q)
            v=float(v)
            return q*v
        except:
            try:
                I=float(I)
                t=float(t)
                v=float(v)
                return I*t*v
            except:
                try:
                    t=float(t)
                    PR=float(PR)
                    return PR*t
                except:
                    try:
                        q= float(q)
                        PR= float(PR)
                        I= float(I)
                        return q*PR/I
                    except:
                        try:
                            v= float(v)
                            t= float(t)
                            R= float(R)
                            return v*v*t/R
                        except:
                            try:
                                R= float(R)
                                I= float(I)
                                t= float(t)
                                return R*I*I*t
                            except:
                                print('INVALID or NOT ENOUGH information.')

    elif x=='q':
        try:
            u= float(u)
            v= float(v)
            return u/v
        except:
            try:
                I= float(I)
                t= float(t)
                return I*t
            except:
                try:
                    u=float(u)
                    I=float(I)
                    R=float(R)
                    return u/(I*R)
                except:
                    print('INVALID or NOT ENOUGH information.')

    elif x=='v':
        try:
            I=float(I)
            R=float(R)
            return I*R
        except:
            try:
                u=float(u)
                q=float(q)
                return u/q
            except:
                try:
                    t=float(t)
                    PR=float(PR)
                    q=float(q)
                    return PR*t/q
                except:
                    try:
                        u= float(u)
                        t= float(t)
                        I= float(I)
                        return u/(I*t)
                    except:
                        try:
                            PR= float(PR)
                            I= float(I)
                            return PR/I
                        except:
                            try:
                                PR=float(PR)
                                R=float(R)
                                from math import sqrt
                                return sqrt(PR*R)
                            except:
                                print('INVALID or NOT ENOUGH information.')

    elif x=='I':
        try:
            R= float(R)
            v= float(v)
            return v/R
        except:
            try:
                PR= float(PR)
                v= float(v)
                return PR/v
            except:
                try:
                    u=float(u)
                    t=float(t)
                    v=float(v)
                    return u/(t*v)
                except:
                    from math import sqrt
                    R=float(R)
                    PR=float(PR)
                    sqrt(PR/R)
                    print('INVALID or NOT ENOUGH information.')

    elif x=='R':
        try:
            I=float(I)
            v=float(v)
            return v/I
        except:
            try:
                u=float(u)
                q=float(q)
                I=float(I)
                return u/(q*I)
            except:
                try:
                    I=float(I)
                    PR=float(PR)
                    return PR/(I*I)
                except:
                    try:
                        u= float(u)
                        t= float(t)
                        v= float(v)
                        return v*v*t/u
                    except:
                        try:
                            t= float(t)
                            u= float(u)
                            I= float(I)
                            return u/(I*I*t)
                        except:
                            try:
                                v= float(v)
                                PR= float(PR)
                                return v*v/PR
                            except:                            
                                print('INVALID or NOT ENOUGH information.')

    elif x=='t':
        try:
            I=float(I)
            q=float(q)
            return q/I
        except:
            try:
                u=float(u)
                PR=float(PR)
                return u/PR
            except:
                try:
                    q=float(q)
                    v=float(v)
                    PR=float(PR)
                    return q*v/PR
                except:
                    try:
                        u= float(u)
                        R= float(R)
                        I= float(I)
                        return u/(R*I*I)
                    except:
                        try:
                            q= float(q)
                            R= float(R)
                            v= float(v)
                            return q*R/v
                        except:
                            try:
                                q= float(q)
                                R= float(R)
                                u= float(u)
                                return q*q*R/u
                            except:
                                print('INVALID or NOT ENOUGH information.')

    elif x=='P':
        try:
            I=float(I)
            v=float(v)
            return v/I
        except:
            try:
                R=float(R)
                I=float(I)
                return R*I*I
            except:
                try:
                    v=float(v)
                    R=float(R)
                    return v*v/R
                except:
                    try:
                        u= float(u)
                        I= float(I)
                        q= float(q)
                        return u/(q*I)
                    except:
                        try:
                            q= float(q)
                            t= float(t)
                            v= float(v)
                            return v*t/q
                        except:
                                print('INVALID or NOT ENOUGH information.')








a=PRA('v',R=10,PR=15)
print(a)



import time
time.sleep(5)