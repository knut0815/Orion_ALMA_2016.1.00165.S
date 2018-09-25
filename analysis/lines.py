from astropy import units as u
unknown_map = {'Unknown_4': 'NaClv=1_18-17',
               'Unknown_3': 'Na37Cl_18-17',
               'Unknown_5': 'NaClv=2_17-16',
               'Unknown_6': 'Na37Clv=7_18-17',
               'Unknown_7': '41KCl_29-28',
               'Unknown_8': 'NaClv=4_17-16',
               'Unknown_9': 'Na37Clv=1_17-16',
               'Unknown_10': 'KCl_28-27',
               'Unknown_11': 'KClv=6_29-28',
               'Unknown_14': 'Na37Clv=5_19-18',
               'Unknown_15': 'KClv=3_31-30',
               'Unknown_16': 'KClv=4_31-30',
               'Unknown_B3_1': 'Na37Clv=3-7-6',
               'Unknown_B3_2': 'NaClv=6_7-6',
               'Unknown_B3_3': 'Na37Cl_7-6', #89.2210022*u.GHz,
               'Unknown_B3_4': 'NaClv=3_7-6', #89.1509141*u.GHz,
               'Unknown_B3_6': 'Na37Clv=4_8-7',
               'Unknown_B3_8': 'KClv=3_13-12',
               'Unknown_B3_9': 'Na37Clv=1_8-7',
               'Unknown_B3_10': 'NaClv=4_8-7',
               'Unknown_B3_11': 'NaClv=5_8-7',
               'Unknown_B3_12': 'KCl_13-12',
               'Unknown_B3_13': 'Na37Clv=3_8-7',
               'Unknown_B3_14': 'NaClv=6_8-7',
               'Unknown_B3_15': 'Na37Clv=5_7-6',
               'Unknown_B3_16': 'NaClv=4_7-6',
               'Unknown_B3_17': 'NaClv=5_7-6',
              }

disk_lines = {'Si34S_13-12':229.5008677*u.GHz,
              #'CH3OCHO_19(3,17)-18(2,16)E':229.590456*u.GHz,
              'KCl_30-29':230.32056*u.GHz, # Unknown_1
              #'KCl 30-29': 230.32056*u.GHz,
              'NaClv=2_18-17':230.7791504*u.GHz, # NaCl v=2 18-17 Unknown_2
              'Na37Cl_18-17':229.245887*u.GHz, # Na37Cl v=0 18-17 Unknown_3
              #'NaClv=2 18-17': 230.778872*u.GHz,
              'Na37Clv=2_7-6': 87.912201*u.GHz,
              #'NaClv=2_27-26': 345.7563678473489*u.GHz*(1+4/3e5),
              #'CH3OH24(4)-25(1)': 347.918109*u.GHz, # questionable.
              'NaClv=6_28-27': 347.9041709541925*u.GHz,#*(1+4/3e5),
              'U232.634': 232.634*u.GHz,
              'KClv=4_29-28': 217.21510511183442*u.GHz,#*(1+17/3e5),
              'KClv=3_29-28': 218.56558019739168*u.GHz,#*(1+17/3e5),
              'KClv=7_47-46': 344.6947427950654*u.GHz,#*(1+17/3e5),
              'KClv=6_47-46': 346.8536682021295*u.GHz,#*(1+17/3e5),
              #'RbClv=1 42-41': 218.55158*u.GHz,
              '41KClv=2_31-30': 229.682294*u.GHz, # 41KCl v=2 31-30 # U229.682
              'K37Clv=1_31-30': 229.818833*u.GHz, # K37Cl v=1 31-30 # U229.819
              'KClv=5 31-30': 230.726*u.GHz, # KCl v=5 31-30 # U230.726
              'U230.966': 230.966*u.GHz,
              'U229.550': 229.550*u.GHz,
              'H2Ov2=1_5(5,0)-6(4,3)': 232.6867*u.GHz,
              'NaClv=1_18-17': 232.50995*u.GHz, # NaCl v=1 18-17
              'NaClv=2_17-16': 217.979967*u.GHz, # NaCl v=2 17-16
              'SiS_12-11': 217.817644*u.GHz,
              'Na37Clv=7_18-17': 217.65469079300237*u.GHz*(1+4/3e5),
              '41KCl_29-28': 217.543178*u.GHz, # 41KCl 29-28
              'HC3N_24-23': 218.324788*u.GHz, #nearby: 'SOv=1 6(5)-5(4)': 218.32455*u.GHz,
              'NaClv=4_17-16': 214.7423125*u.GHz, # NaCl v=4 17-16
              'Na37Clv=1_17-16': 214.938601*u.GHz, # Na37Cl v=1 17-16 214.9396309*u.GHz,
              'KCl_28-27': 215.008301*u.GHz, # CNHCO?  KCl 28-27
              '29SiOv=0_5-4': 214.3857577*u.GHz,
              'KClv=6_29-28': 214.53238232216245*u.GHz*(1+17/3e5),
              'Unknown_12': 214.637167*u.GHz, # SiSv=3 12-11?
              #'Unknown_13': 215.88712*u.GHz,
              'KClv=5_29-28': 215.87071581317286*u.GHz*(1+17/3e5),
              'Na37Clv=5_19-18': 233.170797*u.GHz*(1+4/3e5),
              'KClv=3_31-30': 233.6083343*u.GHz, # KCl v=3 31-30
              'KClv=4_31-30': 232.16300227817646*u.GHz, # KCl v=4 31-30
              'KClv=6_31-30': 229.2793232274198*u.GHz + 17*u.MHz,
              '29SiOv=0_2-1': 85.759199*u.GHz,
              '29SiOv=2_2-1': 85.640452*u.GHz,
              'SiOv=1_2-1': 86.24343*u.GHz,
              'SiOv=0_2-1': 86.84696*u.GHz,
              #'Unknown_B3_1': 87.2662137*u.GHz,
              'Na37Clv=3-7-6': 87.26292913122961*u.GHz, #Na37Clv=3_7-6
              'Na37Clv=4_7-6': 86.61885501446523*u.GHz,
              'NaClv=6_7-6': 87.16579637482937*u.GHz,
              #'Unknown_B3_2': 87.16579637482937*u.GHz, # NaCl v=6 J=7-6
              'Na37Cl_7-6': 89.220081*u.GHz, #Na37Cl 7-6
              #'Na37Clv=0_7-6': 89.220081*u.GHz,
              'NaClv=3_7-6': 89.1500999*u.GHz, #'NaClv=3 7-6':
              'Unknown_B3_5': 88.5912644*u.GHz,
              'Na37Clv=4_8-7': 98.98871154098742*u.GHz, # Na37Cl v=4 J=8-7
              #'Unknown_B3_7': 98.26060141133333*u.GHz, # 33SO2 2_20-3_13
              'KClv=3_13-12': 98.09799843033333*u.GHz, # KCl v=3 13-12
              'Na37Clv=1_8-7': 101.2118805*u.GHz, # NaCl v=1 8-7
              'NaClv=4_8-7': 101.1218267*u.GHz,
              'NaClv=5_8-7': 100.36400944205525*u.GHz,
              'KCl_13-12': 99.929581*u.GHz, # KCl 13-12
              'Na37Clv=3_8-7': 99.72479196311542*u.GHz,
              #'Unknown_B3_14': 99.61752628783333*u.GHz,
              'NaClv=6_8-7': 99.6136888781839*u.GHz, # NaCl v=6 J=8-7
              'Na37Clv=5_7-6': 85.9818763055*u.GHz,
              'NaClv=4_7-6': 88.4854845*u.GHz, #88.48522219933332*u.GHz,
              #'Unknown_B3_17': 87.82511009749999*u.GHz,
              'NaClv=5_7-6': 87.8224018163528*u.GHz, # NaCl v=5 J=7-6
              'SiOv=0_5-4': 217.10498*u.GHz,
              'SiOv=1_5-4': 215.59595*u.GHz,
              'H30a': 231.900928*u.GHz, # not actually detected
              'SO2_2-1_1': 86.09395*u.GHz,
              'SO3_2-2_1': 99.299905*u.GHz,
              'SOv=1_3_2-2_1': 98.758192*u.GHz,
              'SO8_8-7_7': 344.310612*u.GHz,
              'SO9_8-8_7': 346.528481*u.GHz,
              'U346.3': 346.3708*u.GHz,
              'U344.4': 344.4537*u.GHz,
              'U335.0': 335.0508032*u.GHz,
              'NaClv=1_26-25': 335.5028961780772*u.GHz,#*(1+4/3e5), # NaCl v=1 26-25
              'KClv=1_44-43': 335.13404*u.GHz, # KCl v=1 44-43
              'U333.0': 333.006652*u.GHz,
              'SiOv=5_8-7': 335.28198*u.GHz, # traces higher-velocity inner region
              '29SiOv=0_8-7': 342.9808425*u.GHz,
              '29SiOv=1_8-7': 340.6118623*u.GHz,
              '29SiOv=2_8-7': 338.2451561*u.GHz,
              'SiOv=0_8-7': 347.330824*u.GHz,
              'SiOv=1_8-7': 344.916247*u.GHz,
              'SiOv=2_8-7': 342.504607*u.GHz,
              '30SiOv=0_8-7': 338.9300437*u.GHz,
              '30SiOv=1_8-7': 336.6029763*u.GHz,
              '30SiOv=2_8-7': 334.2781299*u.GHz,
              'SiS19-18': 344.779481*u.GHz,
              'H13CN1-0': 86.3401764*u.GHz,
              'HC15N1-0': 86.0549664*u.GHz,
              'HCN1-0': 88.6318473*u.GHz,
              'HC3N11-10': 100.076386*u.GHz,
              'HC3Nv7=1_11-10': 100.3224109*u.GHz,
              #'33SO2_2(2,0)-3(1,3)': 98.261864*u.GHz,
              'Na37Clv=5_8-7': 98.25733786046476*u.GHz,
              'Na37Clv=6_8-7': 97.53067092151468*u.GHz,
              'CS2-1': 97.980953*u.GHz,
              #'Si34S_19-18': 335.34203*u.GHz, # questionable?
              'SO4_5-4_4': 100.029565*u.GHz,
              'K37Clv=2_12-11': 88.543115*u.GHz,
              'K37Clv=1_12-11': 89.082847*u.GHz,
              '41KClv=2_12-11': 89.031339*u.GHz,
              'Na37Clv=1_7-6': 88.564135*u.GHz,
              'KClv=2 13-12': 98.706013*u.GHz,
              'KClv=1 13-12': 99.31644*u.GHz,
              '41KClv=0_13-12': 97.628122*u.GHz,
              'SOv=1_4_5-4_4': 98.317606*u.GHz,
              '34SO 3(2)-2(1)': 97.71531*u.GHz,
              '41KClv=0 31-30': 232.49984*u.GHz,
              'KClv=0 45-44': 344.820535*u.GHz,
              'NaClv=2 27-26': 345.761343*u.GHz,
              'KClv=2 44-43': 333.067637*u.GHz,
              'K37Clv=1 29-28': 215.034661*u.GHz,
              '41KClv=2 29-28': 214.907409*u.GHz,
              '41KClv=0 46-45': 344.3381157*u.GHz, # nondetection; absorbed in fg
              'Na37Clv=2 8-7': 100.46681*u.GHz,
              'K37Clv=1 47-46': 347.7131124*u.GHz,
              '41KClv=1 45-44': 334.8543603*u.GHz,
              'Na37Clv=4_27-26': 333.4595595*u.GHz, # Na37Cl v=4 27-26 333.4494677370167
              #'NaClv=6_27-26': 335.53383475975716*u.GHz*(1+4/3e5),
              'NaClv=6_27-26': 335.53383475975716*u.GHz,#*(1+10/3e5),
              'KClv=8_46-45': 335.31315753141826*u.GHz,#*(1+17/3e5), # Si34S 19-18?
              'KClv=4_13-12': 97.48597186602274*u.GHz,#*(1+17/3e5), # ExoMol freqs wrong!
              'K37Clv=4_46-45': 334.16516227198736*u.GHz,#*(1+17/3e5),
              'K37Clv=6_32-31': 230.056385278549*u.GHz,#*(1+17/3e5),
              '41K37Clv=2_32-31': 230.20574188113096*u.GHz,#*(1+17/3e5),
              '41K37Clv=1_30-29': 217.16381062227083*u.GHz,#*(1+17/3e5),
              'K37Clv=3_12-11': 88.00456925402997*u.GHz, # already shifted by 17kms
              'NaClv=8_8-7': 98.12862959892306*u.GHz, # already shifted by 4kms
              'NaClv=7_8-7': 98.8671926968896*u.GHz, # already shifted by 4kms
              'K37Clv=6_30-29': 215.73679432678762*u.GHz, # already shifted by 17 kms
              'K37Clv=4_J=32-31': 232.90755269258102*u.GHz, # already shifted by 17 kms
             }

outflow_lines = {'Si34S_13-12': 229.499086*u.GHz,
                 'H2Ov2=1_5(5,0)-6(4,3)': 232.6867*u.GHz,
                 'SiOv=1_5-4': 215.59595*u.GHz,
                 'SiOv=0_5-4': 217.10498*u.GHz,
                 '29SiOv=0_5-4': 214.3857577*u.GHz,
                 '29SiOv=0_8-7': 342.9808425*u.GHz,
                 '29SiOv=1_8-7': 340.6118623*u.GHz,
                 '29SiOv=2_8-7': 338.2451561*u.GHz,
                 'SiOv=0_8-7': 347.330824*u.GHz,
                 'SiOv=1_8-7': 344.916247*u.GHz,
                 'SiOv=2_8-7': 342.504607*u.GHz,
                 '30SiOv=0_8-7': 338.9300437*u.GHz,
                 '30SiOv=1_8-7': 336.6029763*u.GHz,
                 '30SiOv=2_8-7': 334.2781299*u.GHz,
                 'SO8_8-7_7': 344.310612*u.GHz,
                 'SO9_8-8_7': 346.528481*u.GHz,
                 'SiS19-18': 344.779481*u.GHz,
                 'SO2_8(3,5)-9(2,8)': 86.639095*u.GHz,
                 '29Si34S5-4': 86.617742*u.GHz,
                 'S2O10(2,8)-8(2,7)': 85.9826741*u.GHz,
                 'SO2v1=1_8(3,5)-9(2,8)': 87.825785*u.GHz,
                 'SO2v2=2_4(3,1)-3(2,2)': 344.461808*u.GHz,
                 #'SO2v2=1_19(1,19)-18(0,18)': 346.379186*u.GHz,
                 'SOv=0 7(8)-7(7)': 214.35703*u.GHz,
                 'SOv=0 5(5)-4(4)': 215.22065*u.GHz,
                 '34SO 6(5)-5(4)': 215.83992*u.GHz,
                }

absorbers = {'12CO2-1': 230.538*u.GHz,
             '12CO3-2': 345.7959899*u.GHz,
            }

texnames = {'Si34S_13-12': 'Si$^{34}$S 13-12',
            #'CH3OCHO_19(3,17)-18(2,16)E':229.590456*u.GHz,
            'KCl_30-29':'KCl 30-29', #230.321535*u.GHz,
            'NaClv=2_18-17':'NaCl v=2 18-17', #230.780241*u.GHz,
            'Na37Cl_18-17':'Na$^{37}$Cl 18-17', #229.2474253*u.GHz, # maybe acetone?
            'NaClv=2 18-17': 'NaCl v=2 18-17',
            'U232.634': 'U232.634',
            'U229.550': 'U229.550',
            '41KClv=2_31-30': '$^{41}$KCl v=2 31-30', # SLAIM only
            'K37Clv=1_31-30': 'K$^{37}$Cl v=1 31-30',
            'KClv=5 31-30': 'KCl v=5 31-30',
            'U230.966': 'U230.966',
            'KClv=3_29-28': 'KCl v=3 J=29-28',
            'KClv=4_29-28': 'KCl v=4 J=29-28',
            'H2Ov2=1_5(5,0)-6(4,3)': 'H$_2$O v$_2$=1 $5_{5,0}-6_{4,3}$',
            'NaClv=1_18-17': 'NaCl v=1 18-17', #232.5105*u.GHz,
            'NaClv=2_17-16': 'NaCl v=2 17-16', #217.9795*u.GHz,
            'SiS_12-11': 'SiS 12-11',
            'Na37Clv=7_18-17': 'Na$^{37}$Cl v=7 J=18-17', #217.6660212*u.GHz,
            '41KCl_29-28': '$^{41}$KCl 29-28', #217.5473*u.GHz, # deuterated formic acid?
            'HC3N_24-23': 'HC$_3$N 24-23',
            'NaClv=4_17-16': 'NaCl v=4 17-16', #214.7417*u.GHz, # Si33S?
            'Na37Clv=1_17-16': 'Na$^{37}$Cl v=1 17-16', #'U214.940', #214.9396309*u.GHz,
            'KCl_28-27': 'KCl 28-27', #215.0092408*u.GHz, # CNHCO?  KCl?
            '29SiOv=0_5-4': '$^{29}$SiO v=0 J=5-4', #214.3857577*u.GHz,
            'KClv=6_29-28': 'KCl v=6 J=29-28', #214.54879*u.GHz,
            'Unknown_12': 'U214.637', #214.637167*u.GHz, # SiSv=3 12-11?
            #'Unknown_13': 215.88712*u.GHz,
            'KClv=5_29-28': 'KCl v=5 J=29=28', # '$^{13}$CH$_3$OH $4_{2,2}-3_{1,2}$',
            'Na37Clv=5_19-18': 'Na$^{37}$Cl v=5 J=19-18', #233.170797*u.GHz,
            'KClv=3_31-30': 'KCl v=3 31-30', #233.6083343*u.GHz,
            'KClv=4_31-30': 'KCl v=4 31-30', #232.16300227817646*u.GHz,
            'KClv=6_31-30': 'KCl v=6 31-30',
            '29SiOv=0_2-1': '$^{29}$SiO v=0 J=2-1',
            '29SiOv=2_2-1': '$^{29}$SiO v=2 J=2-1',
            'SiOv=1_2-1': 'SiO v=1 J=2-1',
            'SiOv=0_2-1': 'SiO v=0 J=2-1',
            'Na37Clv=3-7-6': 'Na$^{37}$Cl v=3 7-6', #87.2662137*u.GHz,
            'NaClv=6_7-6': 'NaCl v=6 7-6', #87.1707681*u.GHz,
            'Na37Cl_7-6': 'Na$^{37}$Cl 7-6', #89.2210022*u.GHz,
            'NaClv=3_7-6': 'NaCl v=3 7-6', #89.1509141*u.GHz,
            'Unknown_B3_5': 'U88.591', #88.5912644*u.GHz,
            'NaClv=4_8-7': 'NaCl v=4 8-7',
            'NaClv=4_7-6': 'NaCl v=4 7-6', #88.5912644*u.GHz,
            'SiOv=0_5-4': 'SiO v=0 J=5-4',
            'SiOv=1_5-4': 'SiO v=1 J=5-4',
            'H30a': 'H30$\\alpha$', #231.900928*u.GHz, # not actually detected
            'U346.3': 'U346.371', #346.3708*u.GHz,
            'U344.4': 'U344.454', #344.4537*u.GHz,
            'U335.0': 'K$^{37}$Cl 45-44', #335.0523*u.GHz,
            #'K37Clv=0 45-44': 335.0508032*u.GHz,
            'NaClv=1_26-25': 'NaCl v=1 26-25', #335.5057*u.GHz,
            'KClv=1_44-43': 'KCl v=1 44-43', #335.1307*u.GHz,
            'U333.0': 'NaCl v=2 26-25', #333.0126*u.GHz,
            '29SiOv=0_8-7': '$^{29}$SiO v=0 J=8-7',
            '29SiOv=1_8-7': '$^{29}$SiO v=1 J=8-7',
            '29SiOv=2_8-7': '$^{29}$SiO v=2 J=8-7',
            'SiOv=0_8-7': 'SiO v=0 J=8-7',
            'SiOv=1_8-7': 'SiO v=1 J=8-7',
            'SiOv=2_8-7': 'SiO v=2 J=8-7',
            '30SiOv=0_8-7': '$^{30}$SiO v=0 J=8-7',
            '30SiOv=1_8-7': '$^{30}$SiO v=1 J=8-7',
            '30SiOv=2_8-7': '$^{30}$SiO v=2 J=8-7',
            '12CO2-1': '$^{12}$CO 2-1',
            'SO2_2-1_1': 'SO $2_2-1_1$',
            'SO8_8-7_7': 'SO $8_8-7_7$',
            'SO9_8-8_7': 'SO $9_8-8_7$',
            'H13CN1-0': 'H$^{13}$CN 1-0',
            'HC15N1-0': 'HC$^{15}$N 1-0',
            'SO2_8(3,5)-9(2,8)': 'SO2 8(3,5)-9(2,8)',
            'KCl_13-12': 'KCl 13-12',
            'Na37Clv=2_7-6': 'Na$^{37}$Cl v=2 7-6',
            'K37Clv=2_12-11':'K$^{37}$Cl v=2 12-11',
            'K37Clv=1_12-11':'K$^{37}$Cl v=1 12-11',
            '41KClv=2_12-11':'$^{41}$KCl v=2 12-11',
            'Na37Clv=1_7-6': 'Na$^{37}$Cl v=1 7-6',
            'Na37Clv=0_7-6': 'Na$^{37}$Cl v=0 7-6',
            'SOv=1_4_5-4_4': 'SO v=1 $4_5-4_4$',
            '41KClv=0 31-30': '$^{41}$KCl 31-30',
            'KClv=0 45-44': 'KCl J=45-44',
            'NaClv=2 27-26': 'NaCl v=2 27-26',
            'Na37Clv=1_8-7': 'Na$^{37}$Cl v=1 8-7',
            'Na37Clv=2 8-7': 'Na$^{37}$Cl v=2 8-7',
            '41KClv=0 46-45': '$^{41}$KCl 46-45',
            '41KClv=1 45-44': '$^{41}$KCl v=1 45-44',
            'K37Clv=1_47-46':'K$^{37}$Cl v=1 47-46',
            'NaClv=5_7-6': 'NaCl v=5 7-6',
            'NaClv=6_8-7': 'NaCl v=6 8-7',
            'Na37Clv=5_7-6': 'Na$^{37}$Cl v=5 7-6',
            'Na37Clv=4_7-6': 'Na$^{37}$Cl v=4 7-6',
            'NaClv=5_8-7': 'NaCl v=5 8-7',
            'Na37Clv=3_8-7': 'Na$^{37}$Cl v=3 8-7',
            'Na37Clv=4_8-7': 'Na$^{37}$Cl v=4 8-7',
            'KClv=3_13-12': 'KCl v=3 13-12',
            'KClv=4_13-12': 'KCl v=4 13-12',
            'Na37Clv=4_27-26': 'Na$^{37}$Cl v=4 27-26',
            'KClv=7_47-46': 'KCl v=7 J=47-46',
            'KClv=6_47-46': 'KCl v=6 J=47-46',
            'NaClv=2_27-26': 'NaCl v=2 J=27-26',
            'NaClv=6_28-27': 'NaCl v=6 J=28-27',
            'NaClv=6_27-26': 'NaCl v=6 J=27-26',
            'KClv=8_46-45': 'KCl v=8 J=46-45',
            'K37Clv=4_46-45': 'K$^{37}$Cl v=4 J=46-45',
            'K37Clv=6_32-31': 'K$^{37}$Cl v=6 J=32-31',
            'K37Clv=3_12-11': 'K$^{37}$Cl v=3 J=12-11',
            '41K37Clv=2_32-31': '$^{41}$K$^{37}$Cl v=2 J=32-31',
            '41K37Clv=1_30-29': '$^{41}$K$^{37}$Cl v=1 J=30-29',
            '41KClv=0_13-12': '$^{41}$KCl v=0 J=13-12',
            'NaClv=8_8-7': 'NaCl v=8 J=8-7',
            'NaClv=7_8-7': 'NaCl v=7 J=8-7',
            'K37Clv=6_30-29': 'K$^{37}$Cl v=6 J=30-29',
            'K37Clv=4_J=32-31': 'K$^{37}$Cl v=4 J=32-31',
            }
