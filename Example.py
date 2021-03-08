from CeCoPackage import CeCoKPIsMain

path =r'C:\Users\E100026\Desktop\KPIs Calculation_Centrifugal Compressor_Python'
InputMappingFileName = 'CeCo_DataInputsMappingTest'
DataFileName = 'CeCo_DataTest'
DataSeperator=','    
ResultFileName ='CeCo_KPIsResultTest'
nbStage=2

listWantedKPIs=['ActualVolFlow' ]

#step1: Generate the Input file to choose the 'Value' or the 'TagName' (column name) as provided in the "DataFileName"
#CeCoKPIsMain.CeCo_GetDataInputModel(path,InputMappingFileName,listWantedKPIs,nbStage)

#step2: Generete the result File "CeCo_KPIsResult" with list WantedKPIs Calculated and the input related 
CeCoKPIsMain.CeCo_GetKPIsCalculationResult(path,InputMappingFileName,DataFileName,ResultFileName,DataSeperator,listWantedKPIs,nbStage)



#Additional Things Can be done without creating csv for immediate results
from CeCoPackage import CeCoKPIsDictionaries
from CeCoPackage import CecoKPIsFunctions
InputOrKPIToCheck='ActualVolFlow'

# # Tool 1: To check The unit of KPIs or Input
# print("Tool 1: "+ str(CeCoKPIsDictionaries.CeCoUnitsDictionary[InputOrKPIToCheck]))

# # Tool 2: To check The Get All Related Inputs for a Particular KPI
# print("Tool 2: "+ str(CeCoKPIsDictionaries.GetKPIsRelatedInputs(InputOrKPIToCheck)))

# # Tool 3: To check The Get Non Stage Related Inputs for a Particular KPI
# print("Tool 3: "+ str(CeCoKPIsDictionaries.GetKPIsRelatedInputs(InputOrKPIToCheck)['RelatedNonStageInputs']))

# # Tool 4: To check The Get Is Stage Related Inputs for a Particular KPI
# print( "Tool 4: "+str(CeCoKPIsDictionaries.GetKPIsRelatedInputs(InputOrKPIToCheck)['RelatedIsStageInputs']))

# # Tool 5: To check the list of all Available KPIs
# print( "Tool 5: "+str(CeCoKPIsDictionaries.listAllAvailableKPIs))

# # Tool 6: To check the Value of a Particular KPI with values: It can be used to check before launching the whole rows in the Data csv
# print("Tool 6: "+str(CecoKPIsFunctions.ActualVolFlow( GasDensity=203.3506281, VolFlow=380.0322266, NormalDensity=CecoKPIsFunctions.NormalDensity(GasMoleWeight=19.94000946))))
