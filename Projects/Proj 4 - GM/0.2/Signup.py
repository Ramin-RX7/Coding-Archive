SU_Nickname= input('Type you Nickname:')

op_inf= open('.\\GM_Info.py',mode='w')
op_inf.write('Nickname= \'' + SU_Nickname + '\'\n'
             'Credit= 0\n'
             'Crash_Wins= 0\n'
             'Crash_Loses= 0\n'
             'BJ_Wins= 0\n'
             'BJ_Loses= 0'
            )
op_inf.close()


def CardINFO():
    CardNom= input('Type your card number: ')
    if len(CardNom) == 16:
        CardPass= input('Type your password: ')
        if len(CardPass)>=8 and len(CardPass)<=12:
            CardCVV= input('Type CVV2: ') 
            if len(CardCVV) == 3 or len(CardCVV) == 4:
                CardMonth= input('Expiration month: ')
                if len(CardMonth)==2 or len(CardMonth)==1:
                    if CardMonth == '01' or CardMonth == '02' or CardMonth == '03' or CardMonth == '04' or CardMonth == '05' or CardMonth == '06' or CardMonth == '07' or CardMonth == '08' or CardMonth == '09' or CardMonth == '1' or CardMonth == '2' or CardMonth == '3' or CardMonth == '4' or CardMonth == '5' or CardMonth == '6' or CardMonth == '7' or CardMonth == '8' or CardMonth == '9' or CardMonth == '10' or CardMonth == '11' or CardMonth == '12':
                        CardYear= input('Expiration year: ')
                        if len(CardYear)==2 :
                            if CardYear == '00' or CardYear == '98' or CardYear == '99' or CardYear == '00' or CardYear == '01' or CardYear == '02':
                            
                                op_inf= open('.\\Card_Info.py',mode='w')
                                op_inf.write('CardNom= \''  + CardNom  + '\'\n' +
                                            'CardPass= \'' + CardPass + '\'\n' +
                                            'CardCVV= \''  + CardCVV  + '\'\n' +
                                            'CardMonth= \''+ CardMonth+ '\'\n' +
                                            'CardYear= \'' + CardYear + '\'\n'
                                            )
                                op_inf.close()
                                print('Card has been added.')
                                print('Your account has been created completly.')
                                import time
                                time.sleep(4)
                                
                            else:
                                print('Invalid Year Number.\n')
                                CardINFO()
                        else:
                            print('Invalid Year Number.\n')
                            CardINFO()
                    else:
                        print('Invalid Month Number.\n')
                        CardINFO()
                else:
                    print('Invalid Month Number.\n')
                    CardINFO()
            else:
                print('Invalid CVV2 Number.\n')
                CardINFO()
        else:
            print('Invalid Password.\n')
            CardINFO()
    else:
        print('Invalid Card Number.\n')
        CardINFO()

CardINFO()
