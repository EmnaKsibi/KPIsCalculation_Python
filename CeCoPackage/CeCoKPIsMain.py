DEBUG=False #Set to true to see details if error occurs
from CeCoPackage.CeCoKPIsDictionaries import CeCoKPIsDictionary
from CeCoPackage.CeCoKPIsDictionaries import GetKPIsRelatedInputs  
from CeCoPackage.CeCoKPIsDictionaries import  CeCoUnitsDictionary
from CeCoPackage.CentrifugalCompressor import CentrifugalCompressor
from csv import DictReader
import pandas as pd
import ctypes
import sys 
import csv
import os


#Check For Input errors 
def CeCo_InputCheCkErrors(**kwargs) :
   if (DEBUG): print("In CeCo_InputCheCkErrors")
   test=False
   Message=""
   if ("TestOP0" in kwargs and os.path.isfile(kwargs['TestOP0'])==False):    
      if (DEBUG): print( "In CeCo_InputCheCkErrors: Exception: FileNotFoundError: "+str(kwargs['TestOP0']))
      test=True
      Message+=  "\nFileNotFoundError: "+ kwargs['TestOP0']
   if ("TestOP1" in kwargs and isinstance(kwargs['TestOP1'], int)==False or kwargs['TestOP1'] < 0):    
         test=True
         Message+=  "\nNumber of stages should be integer:"+str(kwargs['TestOP1'])
   if ("TestOP2" in kwargs):    
      for listWantedKPIsItem in kwargs['TestOP2']:
         if GetKPIsRelatedInputs(listWantedKPIsItem) ==None:
            test=True
            Message+=  "\nKPI Name is unknown: "+str(listWantedKPIsItem)
   if ("TestOP3" in kwargs and os.path.isfile(kwargs['TestOP3'])==False):    
      if (DEBUG): print( "In CeCo_InputCheCkErrors: Exception: FileNotFoundError: "+str(kwargs['TestOP3']))
      test=True
      Message+=  "\nFileNotFoundError: "+ kwargs['TestOP3']
   if ("TestOP3" in kwargs and "TestOP4" in kwargs and os.path.isfile(kwargs['TestOP3']) ):    
      try:
         dialect= csv.Sniffer().sniff(open(kwargs['TestOP3'], "r").readline(),kwargs['TestOP4'])
         if (DEBUG): print("In CeCo_InputCheCkErrors: The Data File Delimiter is "+str(dialect.delimiter))
         if ( kwargs['TestOP4']=="."):    
            test=True
            Message+=  "\nDataSeperator '.' Might be Confused with Data Float delimiter"
      except Exception as e: 
         print( "In CeCo_InputCheCkErrors: Exception: "+str(e))
         test=True
         Message+=  "\nWrong DataSeperator '"+ kwargs['TestOP4']+ "'"
   if (test):
      ctypes.windll.user32.MessageBoxW(0,  Message,"Failed!", 0)
      sys.exit()


# Creating a standard List of Tag name and constant values
def CeCo_GetDataInputModel(path,InputFileName,listWantedKPIs,nbStage):
   if (DEBUG): print("In CeCo_GetDataInputModel")
   pathInput=path +'\\'+  InputFileName+'.csv'
   CeCo_InputCheCkErrors(TestOP1=nbStage,TestOP2=listWantedKPIs)
   dfInputs= pd.DataFrame( columns =['RelatedInput','TagOrValue'])
   dfInputs = dfInputs.append({'RelatedInput': 'Timestamp','TagOrValue':'ToBeFilled'}, ignore_index= True)
   for listKPIsItem in listWantedKPIs :
      for KPIsRelatedInputsItem in GetKPIsRelatedInputs(listKPIsItem)['RelatedIsStageInputs']:
         for stage in range(1,nbStage+1):
            KPIsRelatedInputsItemName=KPIsRelatedInputsItem+str(stage)
            if KPIsRelatedInputsItemName not in dfInputs.values :  
               dfInputs = dfInputs.append({'RelatedInput': KPIsRelatedInputsItemName,'TagOrValue':'ToBeFilledIn['+CeCoUnitsDictionary[KPIsRelatedInputsItem]+"]"}, ignore_index= True)
      for KPIsRelatedInputsItem in GetKPIsRelatedInputs(listKPIsItem)['RelatedNonStageInputs']:
         if KPIsRelatedInputsItem not in dfInputs.values: 
            dfInputs = dfInputs.append({'RelatedInput': KPIsRelatedInputsItem,'TagOrValue':'ToBeFilledIn['+CeCoUnitsDictionary[KPIsRelatedInputsItem]+"]"}, ignore_index= True)
   try:
      dfInputs.to_csv( pathInput, ",", index = False)
      if (DEBUG): print( "In CeCo_GetDataInputModel: Input File created:\n"+str(dfInputs))
      ctypes.windll.user32.MessageBoxW(0, "Fill the Created Input File with Tags or Values.\nPath: "+pathInput, "Instructions", 0)
   except Exception as e:
      print( "In CeCo_GetDataInputModel: Exception: "+str(e))



# Importing data and calculate wanted KPIs
def CeCo_GetKPIsCalculationResult(path,InputMappingFileName,DataFileName,ResultFileName,DataSeperator,listWantedKPIs,nbStage) :
   if (DEBUG): print( "In CeCo_GetKPIsCalculationResult")
   pathInput=path +'\\'+  InputMappingFileName+'.csv'
   pathData=path+'\\'+  DataFileName+'.csv'
   pathResult=path+'\\'+  ResultFileName+'.csv'
   CeCo_InputCheCkErrors(TestOP0=pathInput,TestOP1=nbStage,TestOP2=listWantedKPIs,TestOP3=pathData,TestOP4=DataSeperator)
   dfInputs= pd.read_csv(pathInput,",").to_dict(orient='list')
   DataInitialisation=dfInputs['TagOrValue']
   ColumnInitialisation=dfInputs['RelatedInput']
   dictOutputs =dict({0: dict(zip(ColumnInitialisation,DataInitialisation))})

   try :
      with open( pathData , 'r' ) as read_obj:
         csv_dict_reader = DictReader(read_obj, delimiter =DataSeperator)
         DataTags=csv_dict_reader.fieldnames      
         index=0
         print("In CeCo_GetKPIsCalculationResult: Calculation In Progress...")
         for row in csv_dict_reader: 
            dictOutputs.update({index: dict(zip(ColumnInitialisation,DataInitialisation))})
            for item in dictOutputs[index].keys() :
              if dictOutputs[index][item] in DataTags :
                  dictOutputs[index][item]=row[dictOutputs[index][item]]
            CeCo=CentrifugalCompressor(nbStage,**dictOutputs[index]) 
            for KPI in listWantedKPIs:
              if(KPI in CeCoKPIsDictionary['IsStageKPI']):
                  for stage in range(1,nbStage+1):
                    dictOutputs[index][KPI+str(stage)] = CeCo.getattr(KPI)(stage)
              elif(KPI in CeCoKPIsDictionary['NonStageKPI']):
                  dictOutputs[index][KPI] =CeCo.getattr(KPI)()
            if (DEBUG): print("In CeCo_GetKPIsCalculationResult: *Row "+str(index)+" Calculated:\n"+str(dictOutputs[index]))
            index+=1
      dfOutputs= pd.DataFrame(dictOutputs.values())
      if  dfOutputs.isnull().values.any() and DEBUG:
         print("In CeCo_GetKPIsCalculationResult: Completed With missing input values (NaN)!\n"+str(dfOutputs[dfOutputs.isnull().any(axis=1)]))
      dfOutputs.to_csv( pathResult, ",", index = False)
      print("In CeCo_GetKPIsCalculationResult: Calculation done!")
      ctypes.windll.user32.MessageBoxW(0, "ResultFile: "+pathResult, "Completed", 0)
   except Exception as e:
      print( "In CeCo_GetKPIsCalculationResult: Exception: "+str(e) )
