#!/bin/python
import sys
import os
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler
import random
import glob
random.seed(42)


PATH_DIR= Path.cwd()

#if len(sys.argv) < 2:
#    print ('Usage: ' + sys.argv[0] + ' <filename>')
#    sys.exit(1)

#print ('pre-processed PRS scores are available at:              ' + sys.argv[1])


all_files = glob.glob(str(PATH_DIR)+ "/*.best")

frames = []

for filename in all_files:
    df = pd.read_csv(filename, index_col="IID", header= 0, sep= '\t')
    frames.append(df)


PRS_primary = pd.concat(frames, axis=1, ignore_index=True)

col_names = []

for i in range(len(all_files)):

		col = str(all_files[i]).split("/")[-1].strip(".best")
		col_names.append(col)

reduced_pPRS = PRS_primary[PRS_primary.columns[2::3]]
reduced_pPRS.columns = col_names


scaler = MinMaxScaler()
scaled_pPRS = pd.DataFrame(scaler.fit_transform(reduced_pPRS), columns = reduced_pPRS.columns)


scaled_pPRS['Composit_score_polyElastic']= ((scaled_pPRS['trait_29']*scaled_pPRS['trait_12']*58.849280)+
                     (scaled_pPRS['trait_15']*scaled_pPRS['trait_4']*52.796841)+
                     (scaled_pPRS['trait_11']*scaled_pPRS['trait_20']*45.154075)+
                     (scaled_pPRS['trait_58']*scaled_pPRS['trait_62']*43.978632)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_37']*43.390765)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_69']*42.206775)+
                     (scaled_pPRS['trait_34']*scaled_pPRS['trait_68']*42.136056)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_55']*41.167585)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_33']*38.403183)+
                     (scaled_pPRS['trait_26']*scaled_pPRS['trait_52']*37.537678)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_33']*36.493028)+
                     (scaled_pPRS['trait_26']*scaled_pPRS['trait_23']*34.505337)+
                     (scaled_pPRS['trait_54']*scaled_pPRS['trait_39']*33.673372)+
                     (scaled_pPRS['trait_26']*scaled_pPRS['trait_9']*33.594732)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_76']*33.381145)+
                     (scaled_pPRS['trait_45']*scaled_pPRS['trait_39']*32.942218)+
                     (scaled_pPRS['trait_25']*scaled_pPRS['trait_55']*32.759231)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['trait_71']*32.435932)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_62']*31.744399)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_62']*31.002598)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_65']*30.689279)+
                     (scaled_pPRS['trait_67']*scaled_pPRS['trait_69']*30.659355)+
                     (scaled_pPRS['trait_30']*scaled_pPRS['trait_40']*30.159317)+
                     (scaled_pPRS['trait_75']*scaled_pPRS['trait_61']*30.047132)+
                     (scaled_pPRS['trait_29']*scaled_pPRS['trait_21']*29.900928)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_70']*29.878248)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_66']*29.819145)+
                     (scaled_pPRS['trait_75']*scaled_pPRS['trait_20']*29.662408)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_35']*29.521778)+
                     (scaled_pPRS['trait_63']*scaled_pPRS['trait_72']*29.372132)+
                     (scaled_pPRS['trait_20']*scaled_pPRS['trait_63']*28.963688)+
                     (scaled_pPRS['trait_24']*scaled_pPRS['trait_53']*28.957166)+
                     (scaled_pPRS['trait_29']*scaled_pPRS['trait_23']*28.789449)+
                     (scaled_pPRS['trait_11']*scaled_pPRS['trait_55']*28.307654)+
                     (scaled_pPRS['trait_5']*scaled_pPRS['trait_12']*28.174806)+
                     (scaled_pPRS['trait_59']*scaled_pPRS['trait_72']*27.992889)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_16']*27.294122)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_45']*27.033197)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['trait_10']*26.895401)+
                     (scaled_pPRS['trait_50']*scaled_pPRS['trait_32']*26.675411)+
                     (scaled_pPRS['trait_12']*scaled_pPRS['trait_58']*26.631133)+
                     (scaled_pPRS['trait_60']*scaled_pPRS['trait_50']*26.576569)+
                     (scaled_pPRS['trait_20']*scaled_pPRS['trait_74']*26.088453)+
                     (scaled_pPRS['trait_41']*scaled_pPRS['trait_22']*25.538069)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['trait_58']*25.385504)+
                     (scaled_pPRS['trait_24']*scaled_pPRS['trait_3']*25.378142)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_53']*25.314398)+
                     (scaled_pPRS['trait_16']*scaled_pPRS['trait_66']*25.190139)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_67']* 25.087081)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_55']*24.837369)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_70']*24.818119)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_71']*24.537498)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_32']*24.536254)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_66']*24.145611)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_59']*24.075781)+
                     (scaled_pPRS['trait_13']*scaled_pPRS['trait_1']*23.926094)+
                     (scaled_pPRS['trait_4']*scaled_pPRS['trait_39']*23.891014)+
                     (scaled_pPRS['trait_3']*scaled_pPRS['trait_20']*23.628005)+
                     (scaled_pPRS['trait_52']*scaled_pPRS['trait_62']*23.563474)+
                     (scaled_pPRS['trait_40']*scaled_pPRS['trait_31']*23.304426)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_11']*22.912737)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_50']*22.849949)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_23']*22.793267)+
                     (scaled_pPRS['trait_76']*scaled_pPRS['trait_73']*22.752081)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_74']*22.691942)+
                     (scaled_pPRS['trait_28']*scaled_pPRS['trait_71']*22.690993)+
                     (scaled_pPRS['trait_39']*scaled_pPRS['trait_62']*22.667241)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_11']*22.618959)+
                     (scaled_pPRS['trait_23']*scaled_pPRS['trait_63']*21.939939)+
                     (scaled_pPRS['trait_37']*scaled_pPRS['trait_39']*21.869644)+
                     (scaled_pPRS['trait_76']*scaled_pPRS['trait_31']*21.404001)+
                     (scaled_pPRS['trait_30']*scaled_pPRS['trait_69']*21.292904)+
                     (scaled_pPRS['trait_22']*scaled_pPRS['trait_69']*21.228948)+
                     (scaled_pPRS['trait_21']*scaled_pPRS['trait_34']*20.797492)+
                     (scaled_pPRS['trait_5']*scaled_pPRS['trait_53']*20.766513)+
                     (scaled_pPRS['trait_59']*scaled_pPRS['trait_67']*20.378205)+
                     (scaled_pPRS['trait_49']*scaled_pPRS['trait_16']*20.371289)+
                     (scaled_pPRS['trait_53']*scaled_pPRS['trait_71']*20.329814)+
                     (scaled_pPRS['trait_35']*scaled_pPRS['trait_52']*20.153764)+
                     (scaled_pPRS['trait_17']*scaled_pPRS['trait_63']*19.997026)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_12']*19.657728)+
                     (scaled_pPRS['trait_50']*scaled_pPRS['trait_68']*19.579645)+
                     (scaled_pPRS['trait_24']*scaled_pPRS['trait_12']*19.225711)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_46']*19.162823)+
                     (scaled_pPRS['trait_40']*scaled_pPRS['trait_21']*18.959201)+
                     (scaled_pPRS['trait_15']*scaled_pPRS['trait_9']*18.865165)+
                     (scaled_pPRS['trait_33']*scaled_pPRS['trait_59']*18.625337)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_55']*18.452113)+
                     (scaled_pPRS['trait_34']*scaled_pPRS['trait_71']*17.895777)+
                     (scaled_pPRS['trait_68']*scaled_pPRS['trait_67']*17.819361)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_55']*17.730311)+
                     (scaled_pPRS['trait_30']*scaled_pPRS['trait_32']*17.657299)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_67']*17.651424)+
                     (scaled_pPRS['trait_17']*scaled_pPRS['trait_68']*17.651424)+
                     (scaled_pPRS['trait_28']*scaled_pPRS['trait_8']*17.473049)+
                     (scaled_pPRS['trait_16']*scaled_pPRS['trait_69']*17.408130)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_40']*17.298142)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_52']*17.249759)+
                     (scaled_pPRS['trait_10']*scaled_pPRS['trait_62']*17.064498)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_10']*16.671809)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_6']*16.639492)+
                     (scaled_pPRS['trait_35']*scaled_pPRS['trait_74']*16.364199)+
                     (scaled_pPRS['trait_17']*scaled_pPRS['trait_51']*16.168816)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_34']*15.896041)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_47']*15.799451)+
                     (scaled_pPRS['trait_16']*scaled_pPRS['trait_35']*15.729063)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_63']*15.654522)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_10']*15.146254)+
                     (scaled_pPRS['trait_46']*scaled_pPRS['trait_39']*15.120552)+
                     (scaled_pPRS['trait_60']*scaled_pPRS['trait_69']*15.077016)+
                     (scaled_pPRS['trait_14']*scaled_pPRS['trait_68']*15.042262)+
                     (scaled_pPRS['trait_39']*scaled_pPRS['trait_68']*15.016950)+
                     (scaled_pPRS['trait_25']*scaled_pPRS['trait_8']*14.957253)+
                     (scaled_pPRS['trait_25']*scaled_pPRS['trait_34']*14.950703)+
                     (scaled_pPRS['trait_17']*scaled_pPRS['trait_53']*14.935972)+
                     (scaled_pPRS['trait_39']*scaled_pPRS['trait_55']*14.925196)+
                     (scaled_pPRS['trait_43']*scaled_pPRS['trait_22']*14.863926)+
                     (scaled_pPRS['trait_13']*scaled_pPRS['trait_53']*14.380162)+
                     (scaled_pPRS['trait_26']*scaled_pPRS['trait_62']*14.236891)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_33']*14.224283)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_5']*13.966136)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_71']*13.918862)+
                     (scaled_pPRS['trait_76']*scaled_pPRS['trait_8']*13.823901)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_21']*12.248667)+
                     (scaled_pPRS['trait_52']*scaled_pPRS['trait_63']*12.067506)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['trait_74']*11.994375)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_35']*11.750018)+
                     (scaled_pPRS['trait_33']*scaled_pPRS['trait_72']*10.883662)+
                     (scaled_pPRS['trait_39']*scaled_pPRS['trait_72']*10.602185)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_50']*10.221849)+
                     (scaled_pPRS['trait_17']*scaled_pPRS['trait_32']*10.049902)+
                     (scaled_pPRS['trait_54']*scaled_pPRS['trait_59']*10.001024)+
                     (scaled_pPRS['trait_16']*scaled_pPRS['trait_21']*9.679859)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_69']*9.650015)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_34']*9.190492)+
                     (scaled_pPRS['trait_34']*scaled_pPRS['trait_72']*9.116918)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_66']*9.093719)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_3']*8.734591)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_20']*8.337458)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_28']*8.100907)+
                     (scaled_pPRS['trait_5']*scaled_pPRS['trait_52']*7.509962)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_60']*7.460217)+
                     (scaled_pPRS['trait_29']*scaled_pPRS['trait_24']*7.237351)+
                     (scaled_pPRS['trait_3']*scaled_pPRS['trait_23']*5.110316)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['trait_9']*4.702611)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_73']*4.141403)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_45']*2.532982)+
                     (scaled_pPRS['trait_39']*scaled_pPRS['trait_66']*1.708154)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_54']*-1.437933)+
                     (scaled_pPRS['trait_52']*scaled_pPRS['trait_58']*-2.919382)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_11']*-3.961119)+
                     (scaled_pPRS['trait_13']*scaled_pPRS['trait_8']*-4.604911)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_77']*-5.588485)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['trait_34']*-7.402449)+
                     (scaled_pPRS['trait_7']*scaled_pPRS['trait_53']*-8.210830)+
                     (scaled_pPRS['trait_33']*scaled_pPRS['trait_66']*-8.627072)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_71']*-9.376341)+
                     (scaled_pPRS['trait_28']*scaled_pPRS['trait_22']*-9.538595)+
                     (scaled_pPRS['trait_54']*scaled_pPRS['trait_16']*-9.606158)+
                     (scaled_pPRS['trait_20']*scaled_pPRS['trait_33']*-9.916618)+
                     (scaled_pPRS['trait_10']*scaled_pPRS['trait_71']*-10.010519)+
                     (scaled_pPRS['trait_54']*scaled_pPRS['trait_12']*-10.427662)+
                     (scaled_pPRS['trait_28']*scaled_pPRS['trait_74']*-10.563598)+
                     (scaled_pPRS['trait_59']*scaled_pPRS['trait_69']*-10.715941)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_67']*-10.875840)+
                     (scaled_pPRS['trait_40']*scaled_pPRS['trait_11']*-10.940913)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_12']*-10.980798)+
                     (scaled_pPRS['trait_30']*scaled_pPRS['trait_53']*-11.115192)+
                     (scaled_pPRS['trait_37']*scaled_pPRS['trait_66']*-11.199638)+
                     (scaled_pPRS['trait_28']*scaled_pPRS['trait_23']*-11.250697)+
                     (scaled_pPRS['trait_60']*scaled_pPRS['trait_16']*-11.266255)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['Total_trait_12']*-11.545864)+
                     (scaled_pPRS['trait_30']*scaled_pPRS['trait_11']*-11.697771)+
                     (scaled_pPRS['trait_32']*scaled_pPRS['trait_33']*-12.012224)+
                     (scaled_pPRS['trait_30']*scaled_pPRS['trait_24']*-12.151675)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_70']*-12.180552)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_60']*-12.226281)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_32']*-12.314022)+
                     (scaled_pPRS['trait_47']*scaled_pPRS['trait_34']*-12.370783)+
                     (scaled_pPRS['trait_11']*scaled_pPRS['trait_59']*-12.767196)+
                     (scaled_pPRS['trait_29']*scaled_pPRS['trait_17']*-12.816469)+
                     (scaled_pPRS['trait_53']*scaled_pPRS['trait_58']*-13.121160)+
                     (scaled_pPRS['trait_60']*scaled_pPRS['trait_59']*-13.139942)+
                     (scaled_pPRS['trait_25']*scaled_pPRS['Total_trait_12']*-13.338520)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_37']*-13.454048)+
                     (scaled_pPRS['trait_75']*scaled_pPRS['trait_12']*-13.557144)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['Total_trait_12']*-13.576208)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_58']*-13.587007)+
                     (scaled_pPRS['trait_21']*scaled_pPRS['trait_12']*-13.747057)+
                     (scaled_pPRS['trait_53']*scaled_pPRS['trait_63']*-13.845102)+
                     (scaled_pPRS['trait_17']*scaled_pPRS['trait_22']*-13.894520)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_54']*-14.111731)+
                     (scaled_pPRS['trait_40']*scaled_pPRS['trait_72']*-14.351706)+
                     (scaled_pPRS['trait_62']*scaled_pPRS['trait_72']*-14.451938)+
                     (scaled_pPRS['trait_45']*scaled_pPRS['trait_63']*-14.780071)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_74']*-14.994771)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_56']*-15.004392)+
                     (scaled_pPRS['trait_31']*scaled_pPRS['trait_72']*-15.124746)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_72']*-15.161795)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_50']*-15.225889)+
                     (scaled_pPRS['trait_61']*scaled_pPRS['trait_6']*-15.236913)+
                     (scaled_pPRS['trait_50']*scaled_pPRS['trait_39']*-15.365775)+
                     (scaled_pPRS['trait_75']*scaled_pPRS['trait_11']*-15.612835)+
                     (scaled_pPRS['trait_29']*scaled_pPRS['trait_55']*-15.701273)+
                     (scaled_pPRS['trait_58']*scaled_pPRS['trait_63']*-15.888249)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_71']*-15.969955)+
                     (scaled_pPRS['trait_20']*scaled_pPRS['trait_69']*-16.269286)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_61']*-16.343809)+
                     (scaled_pPRS['trait_21']*scaled_pPRS['trait_51']*-16.463471)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_11']*-16.467428)+
                     (scaled_pPRS['trait_35']*scaled_pPRS['trait_55']*-16.751638)+
                     (scaled_pPRS['trait_76']*scaled_pPRS['trait_71']*-16.762511)+
                     (scaled_pPRS['trait_12']*scaled_pPRS['trait_51']*-17.042099)+
                     (scaled_pPRS['trait_37']*scaled_pPRS['trait_35']*-17.087925)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_66']*-17.406241)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_62']*-17.451712)+
                     (scaled_pPRS['trait_52']*scaled_pPRS['trait_53']*-18.033422)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_8']*-18.205805)+
                     (scaled_pPRS['trait_21']*scaled_pPRS['trait_74']*-18.236924)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_39']*-18.422479)+
                     (scaled_pPRS['trait_23']*scaled_pPRS['trait_33']*-18.903259)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_62']*-18.914102)+
                     (scaled_pPRS['trait_13']*scaled_pPRS['trait_5']*-19.020970)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_23']*-19.090658)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_50']*-19.215279)+
                     (scaled_pPRS['trait_17']*scaled_pPRS['trait_39']*-19.241486)+
                     (scaled_pPRS['trait_11']*scaled_pPRS['trait_22']*-19.381896)+
                     (scaled_pPRS['trait_59']*scaled_pPRS['trait_71']*-19.444752)+
                     (scaled_pPRS['trait_59']*scaled_pPRS['trait_62']*-19.616271)+
                     (scaled_pPRS['trait_62']*scaled_pPRS['trait_66']*-19.682622)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_35']*-19.759254)+
                     (scaled_pPRS['trait_30']*scaled_pPRS['trait_70']*-20.260942)+
                     (scaled_pPRS['trait_45']*scaled_pPRS['trait_21']*-20.332468)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_23']*-20.389411)+
                     (scaled_pPRS['trait_54']*scaled_pPRS['trait_66']*-20.474728)+
                     (scaled_pPRS['trait_3']*scaled_pPRS['trait_55']*-20.487787)+
                     (scaled_pPRS['trait_6']*scaled_pPRS['trait_67']*-20.507025)+
                     (scaled_pPRS['trait_11']*scaled_pPRS['trait_21']*-20.559676)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_63']*-20.585477)+
                     (scaled_pPRS['trait_38']*scaled_pPRS['trait_62']*-20.987571)+
                     (scaled_pPRS['trait_56']*scaled_pPRS['trait_29']*-21.112712)+
                     (scaled_pPRS['trait_5']*scaled_pPRS['trait_20']*-21.401252)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_34']*-21.418327)+
                     (scaled_pPRS['trait_40']*scaled_pPRS['trait_67']*-21.429963)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_62']*-21.688526)+
                     (scaled_pPRS['trait_8']*scaled_pPRS['trait_74']*-21.758489)+
                     (scaled_pPRS['trait_32']*scaled_pPRS['Total_trait_12']*-21.875365)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_37']*-22.273096)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_69']*-23.003030)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_9']*-23.177700)+
                     (scaled_pPRS['trait_37']*scaled_pPRS['trait_72']*-23.484152)+
                     (scaled_pPRS['trait_26']*scaled_pPRS['trait_20']*-23.503367)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_6']*-23.797295)+
                     (scaled_pPRS['trait_31']*scaled_pPRS['trait_35']*-24.161424)+
                     (scaled_pPRS['trait_32']*scaled_pPRS['trait_55']*-24.461037)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_32']*-24.786957)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_77']*-25.145800)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_66']*-25.200187)+
                     (scaled_pPRS['trait_33']*scaled_pPRS['trait_67']*-25.249025)+
                     (scaled_pPRS['trait_75']*scaled_pPRS['trait_55']*-25.252948)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_73']*-25.624458)+
                     (scaled_pPRS['trait_55']*scaled_pPRS['Total_trait_12']*-26.152108)+
                     (scaled_pPRS['trait_77']*scaled_pPRS['trait_63']*-26.193278)+
                     (scaled_pPRS['trait_19']*scaled_pPRS['trait_58']*-26.464080)+
                     (scaled_pPRS['trait_29']*scaled_pPRS['trait_31']*-27.005286)+
                     (scaled_pPRS['trait_62']*scaled_pPRS['Total_trait_12']*-27.069799)+
                     (scaled_pPRS['trait_45']*scaled_pPRS['trait_3']*-27.498880)+
                     (scaled_pPRS['trait_70']*scaled_pPRS['trait_23']*-27.547237)+
                     (scaled_pPRS['trait_57']*scaled_pPRS['trait_53']*-28.006892)+
                     (scaled_pPRS['trait_40']*scaled_pPRS['trait_23']*-28.775709)+
                     (scaled_pPRS['trait_50']*scaled_pPRS['trait_10']*-29.333872)+
                     (scaled_pPRS['trait_63']*scaled_pPRS['trait_69']*-29.773721)+
                     (scaled_pPRS['trait_20']*scaled_pPRS['trait_39']*-30.087469)+
                     (scaled_pPRS['trait_15']*scaled_pPRS['trait_57']*-30.093207)+
                     (scaled_pPRS['trait_20']*scaled_pPRS['trait_52']*-30.093933)+
                     (scaled_pPRS['trait_3']*scaled_pPRS['trait_52']*-30.506332)+
                     (scaled_pPRS['trait_39']*scaled_pPRS['trait_71']*-31.327492)+
                     (scaled_pPRS['trait_25']*scaled_pPRS['trait_12']*-31.447526)+
                     (scaled_pPRS['trait_48']*scaled_pPRS['trait_59']*-32.674248)+
                     (scaled_pPRS['trait_24']*scaled_pPRS['trait_39']*-32.980134)+
                     (scaled_pPRS['trait_26']*scaled_pPRS['trait_69']*-34.348760)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_5']*-34.504481)+
                     (scaled_pPRS['trait_18']*scaled_pPRS['trait_6']*-34.907608)+
                     (scaled_pPRS['trait_65']*scaled_pPRS['trait_31']*-35.136146)+
                     (scaled_pPRS['trait_36']*scaled_pPRS['trait_1']*-35.321193)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_29']*-35.461532)+
                     (scaled_pPRS['trait_4']*scaled_pPRS['trait_25']*-36.300460)+
                     (scaled_pPRS['trait_73']*scaled_pPRS['trait_21']*-36.926717)+
                     (scaled_pPRS['trait_76']*scaled_pPRS['trait_69']*-37.481648)+
                     (scaled_pPRS['trait_9']*scaled_pPRS['trait_34']*-37.583541)+
                     (scaled_pPRS['trait_26']*scaled_pPRS['trait_33']*-38.779077)+
                     (scaled_pPRS['trait_40']*scaled_pPRS['trait_61']*-39.503308)+
                     (scaled_pPRS['trait_28']*scaled_pPRS['trait_16']*-40.861247)+
                     (scaled_pPRS['trait_16']*scaled_pPRS['trait_52']*-41.740528)+
                     (scaled_pPRS['trait_1']*scaled_pPRS['trait_24']*-42.129703)+
                     (scaled_pPRS['trait_20']*scaled_pPRS['trait_55']*-46.053929)+
                     (scaled_pPRS['trait_12']*scaled_pPRS['trait_39']*-64.387492)+
                     
                     ## Add non-interaction terms:               
                     (scaled_pPRS['trait_51']*20.546074)+
                     (scaled_pPRS['trait_28']*19.954692)+
                     (scaled_pPRS['trait_31']*19.135018)+
                     (scaled_pPRS['trait_27']*19.129389)+
                     (scaled_pPRS['trait_21']*17.089466)+
                     (scaled_pPRS['trait_44']*14.528990)+
                     (scaled_pPRS['trait_33']*13.243266)+
                     (scaled_pPRS['trait_65']*12.541073)+
                     (scaled_pPRS['trait_8']*12.472665)+
                     (scaled_pPRS['trait_23']*12.455628)+
                     (scaled_pPRS['trait_11']*12.074841)+
                     (scaled_pPRS['trait_54']*11.519012)+
                     (scaled_pPRS['trait_20']*10.498940)+
                     (scaled_pPRS['trait_37']*10.333866)+
                     (scaled_pPRS['trait_40']*9.953368)+
                     (scaled_pPRS['trait_1']*9.832423)+
                     (scaled_pPRS['trait_43']*8.395807)+
                     (scaled_pPRS['trait_5']*7.064639)+
                     (scaled_pPRS['trait_66']*7.046030)+
                     (scaled_pPRS['trait_38']*6.847831)+
                     (scaled_pPRS['trait_52']*5.512873)+
                     (scaled_pPRS['trait_19']*5.369968)+
                     (scaled_pPRS['trait_60']*5.279056)+
                     (scaled_pPRS['trait_2']*4.960010)+
                     (scaled_pPRS['trait_73']*3.978966)+
                     (scaled_pPRS['trait_59']*3.917082)+
                     (scaled_pPRS['trait_45']*3.441207)+
                     (scaled_pPRS['trait_14']*3.363107)+
                     (scaled_pPRS['trait_4']*2.992133)+
                     (scaled_pPRS['trait_3']*2.377275)+
                     (scaled_pPRS['trait_64']*1.283975)+
                     (scaled_pPRS['trait_74']*1.060336)+
                     #(scaled_pPRS['gender']*0.825914)+
                     (scaled_pPRS['trait_9']*0.420984)+
                     (scaled_pPRS['trait_62']*-0.206954)+
                     (scaled_pPRS['trait_58']*-0.383374)+
                     (scaled_pPRS['trait_32']*-0.862345)+
                     (scaled_pPRS['trait_49']*-0.911806)+
                     (scaled_pPRS['trait_42']*-1.053575)+
                     (scaled_pPRS['trait_26']*-1.079834)+
                     (scaled_pPRS['trait_63']*-1.259695)+
                     (scaled_pPRS['trait_30']*-1.399643)+
                     (scaled_pPRS['trait_47']*-1.855062)+
                     (scaled_pPRS['trait_6']*-2.350011)+
                     (scaled_pPRS['trait_56']*-4.048538)+
                     (scaled_pPRS['trait_68']*-4.796173)+
                     (scaled_pPRS['trait_12']*-5.062406)+
                     (scaled_pPRS['trait_16']*-5.275871)+
                     (scaled_pPRS['trait_46']*5.404438)+
                     (scaled_pPRS['trait_55']*-6.086167)+
                     (scaled_pPRS['trait_18']*-6.462152)+
                     (scaled_pPRS['trait_41']*-6.772785)+
                     (scaled_pPRS['trait_7']*-7.313569)+
                     (scaled_pPRS['trait_57']*-7.601046)+
                     (scaled_pPRS['trait_24']*-8.027098)+
                     (scaled_pPRS['trait_72']*-8.506355)+
                     (scaled_pPRS['trait_29']*-10.161404)+
                     (scaled_pPRS['trait_39']*-10.624280)+
                     (scaled_pPRS['trait_71']*-12.196588)+
                     (scaled_pPRS['trait_17']*-12.515968)+
                     (scaled_pPRS['trait_76']*-13.925610)+
                     (scaled_pPRS['trait_50']*-14.117372)+
                     (scaled_pPRS['trait_48']*-14.117525)+
                     (scaled_pPRS['trait_70']*-14.135657)+
                     (scaled_pPRS['trait_67']*-16.389537)+
                     (scaled_pPRS['trait_53']*-16.560934)+
                     (scaled_pPRS['trait_75']*-18.352214)+
                     (scaled_pPRS['trait_35']*-18.484809)+
                     (scaled_pPRS['trait_61']*-20.316712)+
                     (scaled_pPRS['trait_22']*-24.234385)+
                     (scaled_pPRS['trait_13']*-26.965932)+
                     (scaled_pPRS['trait_10']*-27.049515)+
                     (scaled_pPRS['trait_34']*-33.430666) 
                                   )
