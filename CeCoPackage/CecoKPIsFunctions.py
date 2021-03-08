import math
import numpy as np


def num(x):
   try:
      return float(x)
   except ValueError:
      return np.nan

#IsStageKPIs
def DesignMassFlow ( DesignGasPower, MassFlow,GasPower):
   if DesignGasPower !=  0 : 
      return  GasPower * MassFlow  / DesignGasPower 
   return   0 

def ActualVolFlow( GasDensity, VolFlow, NormalDensity) :
   if GasDensity !=  0 :
      return  ( VolFlow * NormalDensity  * 1000 / GasDensity /3600)  
   else : return 0

def NormalVolFlow( Speed, ActualVolFlow) :
   if Speed !=  0 :
        return ActualVolFlow * 2118.88 / Speed 
   else : return 0
  
def AdiaWorkCoeff( RotorTipSpeed, AdiaHeadM):
    if RotorTipSpeed   !=  0  :
       return AdiaHeadM * 9.80665 / RotorTipSpeed**2
  
def GasPowerRef( RefPower, SpeedRatio, DensityRatio) :
   return  RefPower * SpeedRatio  ** 3 * DensityRatio 

def IsoEfficiency( PolyHead, PolyEfficiency, IsoHead) :
   if PolyHead  !=  0 :
      return  PolyEfficiency  * IsoHead  / PolyHead  
   else : return  0

def MachNumber( GasSpeedOfSound, RotorTipSpeed) :
   if GasSpeedOfSound !=  0 : 
     return  RotorTipSpeed  / GasSpeedOfSound
   else : return  0

def NormalHead( Speed, PolyHead) :
   if Speed !=  0 : 
       return PolyHead / ( ( Speed / 60)  **2)  
   else : return 0

def AdiaEfficiency( PolyHead, AdiaHead, PolyEfficiency) :
   if PolyHead  !=  0 :
     return AdiaHead  * PolyEfficiency  / PolyHead  
   else : return  0

def GasPower( MassFlow, PolyHead, PolyEfficiency) :
   if PolyEfficiency  !=  0 : 
     return  ( 100 * MassFlow * PolyHead )  / ( PolyEfficiency  * 3600) 
   else : return 0

def PolyHead( GasMoleWeight, SuctionTemperature, GasCompressibility, PolyRatio, PressRatio) :
   if GasMoleWeight !=  0 and PolyRatio  !=  0: 
        return ( 8.3145 * (SuctionTemperature + 273.15) * GasCompressibility * PolyRatio / GasMoleWeight) * ( PressRatio  ** ( 1 / PolyRatio ) - 1 ) 
   else : 
        return 0

def MassFlow( VolFlow, NormalDensity) :
   return VolFlow * NormalDensity  * 1000
   
def GasPowerDevnPcn( GasPowerDeviation,DesignGasPower)  :
   if DesignGasPower != 0 :
    return 100 * GasPowerDeviation  / DesignGasPower 

def PressRatio( SuctionPressure, DiscPressure) :
   if SuctionPressure !=  0 :
     return  ( DiscPressure + 1)  / ( SuctionPressure + 1)  
   else :return  0

def SbvPosDeviation(SbvPosTarget1, SbvPosActual1) :
   if SbvPosTarget1 > 0 :
      return ( ( SbvPosTarget1 - SbvPosActual1)  * 100)  / SbvPosTarget1
   else : return 0

def PluggedSuctFilterDetection( S1dPFilterMultistate) :
   if S1dPFilterMultistate  ==  3 or S1dPFilterMultistate  ==  5 :
      return  1 
   else : return  0

def SuctVelocity( AreaInlet, ActualVolFlow) :
   if AreaInlet  !=  0 : 
      return ActualVolFlow  / AreaInlet  
   else : return  0

def TempRatio( SuctionTemperature, DiscTemperature) :
   if SuctionTemperature !=  0 : 
      return (DiscTemperature+ 273.15) / (SuctionTemperature+ 273.15)
   else : return  0

def TempRise( SuctionTemperature, DiscTemperature) :
   return DiscTemperature - SuctionTemperature

def DTemp(HighStageDischargeTemperature,LowStageSuctionTemperature): 
   return  HighStageDischargeTemperature - LowStageSuctionTemperature

def DPress(HighStageDischargePressure,LowStageSuctionPressure): 
   return  HighStageDischargePressure - LowStageSuctionPressure

def VolFlowRef( RefCapacity1, SpeedRatio,  DensityRatio) :
   return  RefCapacity1 * SpeedRatio  * DensityRatio 

def PolyWorkCoeff( RotorTipSpeed, PolyHeadM) :
   if RotorTipSpeed  !=  0 : 
     return  PolyHeadM * 9.80665  / ( RotorTipSpeed  **2) 
   else : return  0

def PolyWorkCoeffRotor( NoRotors1,PolyWorkCoeff) :
   if NoRotors1 !=  0 : 
      return PolyWorkCoeff  / NoRotors1 
   else : return  0
   
def PolyWorkInput( PolyEfficiency, PolyWorkCoeffRotor) :
   if PolyEfficiency !=  0 :
     return 100 *  PolyWorkCoeffRotor    / PolyEfficiency 
   else : return  0 

def MassFlowDeviation( MassFlow, DesignMassFlow):
   return  MassFlow  - DesignMassFlow

def MassFlowDevnPcn( DesignMassFlow, MassFlowDeviation) :
   if DesignMassFlow  !=  0 :
     return 100 * MassFlowDeviation / DesignMassFlow

def GasPowerDeviation( GasPower, DesignGasPower):
   return GasPower  - DesignGasPower

def NormalPower( Speed, GasPower) :
   if Speed !=  0 :
        return GasPower/ ((Speed/60)**3)           
   else : 
        return 0
   
def SpecificPower( MassFlow, GasPower):
    if MassFlow!=  0 :
        return GasPower  / (MassFlow /3600)
    else : 
       return 0

def DesignSpecificPower( MassFlow, DesignGasPower) :
   if MassFlow  !=  0 :
     return DesignGasPower / MassFlow 
   else : return 0

def PolyHeadDeviation( PolyHead, DesignPolyHead) :
   return PolyHead  - DesignPolyHead 

def PolyHeadDevnPcn(  DesignPolyHead, PolyHeadDeviation) :
   if DesignPolyHead !=  0 :
     return 100 * PolyHeadDeviation   

def PolyHeadM(PolyHead) :
   return 1000 * PolyHead  / 9.80665
   
def NormalDensity( GasMoleWeight) :
   return GasMoleWeight * 101325 / ( 8314.5 *  273.15 ) 

def DesignPolyHeadM(DesignPolyHead) :
   return 1000 * DesignPolyHead / 9.80665

def PolyHeadMDeviation( PolyHeadM, DesignPolyHeadM) :
   return PolyHeadM  - DesignPolyHeadM 

def PolyHeadMDevnPcn( DesignPolyHeadM, PolyHeadMDeviation) :
   if DesignPolyHeadM !=  0 :
      return  100 * PolyHeadMDeviation  / DesignPolyHeadM 

def AdiaHead( GasMoleWeight, SuctionTemperature, GasCompressibility, AdiaRatio, PressRatio) :
   if GasMoleWeight !=  0 : 
     douZ= 8.3145  * (SuctionTemperature + 273.15)  * GasCompressibility * AdiaRatio  / GasMoleWeight 
   else : douZ= 0
   if AdiaRatio  !=  0 :
     douY= PressRatio  **( 1 / AdiaRatio )  - 1
   else : douY= 0
   return douZ * douY

def AdiaHeadM( AdiaHead) :
   return 1000 * AdiaHead  / 9.80665    

def GasGamma( SpecificHeatRatio, GammaGain) :
   return SpecificHeatRatio * GammaGain
     
def IsoHead( GasMoleWeight, SuctionTemperature, GasCompressibility, PressRatio) :
   if GasMoleWeight !=  0 :
     Z= ( 8.3145  * (SuctionTemperature + 273.15) * GasCompressibility / GasMoleWeight)  
   else : Z= 0
   if PressRatio  > 0 :
      Y= np.log( PressRatio )  
   else : Y= 0
   return Z * Y

def IsoHeadM( IsoHead) :
   return 1000 * IsoHead  / 9.80665

def NormalHeadM( Speed, PolyHeadM) :
   if Speed !=  0 : 
     return PolyHeadM  /  (Speed/ 60)**2
   else : return  0

def PolyHeadRef( RefHead1, SpeedRatio, DensityRatio) :
   return RefHead1 * ( SpeedRatio  **2)  * DensityRatio 
   
def PolyHeadRefM( PolyHeadRef) :
   return 1000 * PolyHeadRef / 9.80665    

def PressRise( DiscPressure, SuctionPressure) :
   return DiscPressure - SuctionPressure

def AreaExit( DiscDiameter) :
   return math.pi * ( ( DiscDiameter / 2)  **2) 

def AreaInlet( SuctionDiameter) :
   return math.pi * ( ( SuctionDiameter / 2)  **2) 

def DensityRatio( GasDensity,  RefDensity) :
   if GasDensity !=  0 :
      return  RefDensity / GasDensity
   else : return 0

def SpeedRatio( Speed, RefSpeed) :
   if Speed !=  0 :
      return RefSpeed / Speed
   else : return 0

def RotorTipSpeed( RotorDiameter, Speed) :
   return ( Speed / 60)  * math.pi * RotorDiameter
   
def PolyRatio( PressRatio, TempRatio) :
   if PressRatio > 0 and TempRatio >  0 : 
        return np.log(PressRatio) / np.log(TempRatio )
   else :
        return 0 

def DesignGasPower( PolyEfficiencyDesign, MassFlow, PolyHead) :
   if PolyEfficiencyDesign !=  0 : 
      return ( 100 * MassFlow  * PolyHead )  / ( PolyEfficiencyDesign * 3600) 
   else : return 0

def AdiaRatio( GasGamma) :
   if GasGamma !=  1 :
      return GasGamma  / (GasGamma  - 1)  
   else : return 0

def PolyEfficiency(PolyRatio,AdiaRatio) :
   if AdiaRatio  !=  0 : 
      return 100 * PolyRatio  / AdiaRatio  
   else : return 0
   
def PolyEfficiencyDeviation( PolyEfficiency, DesignPolyEfficiency ) :
   return PolyEfficiency - DesignPolyEfficiency

def PolyEfficiencyDevnPcn( PolyEfficiencyDeviation, DesignPolyEfficiency) :
   if DesignPolyEfficiency  !=  0 :
       return 100 * PolyEfficiencyDeviation  / DesignPolyEfficiency

def DesignPolyEfficiency( Speed, VolFlow, EffCurve1Speed, EffCurve2Speed, EffCurve3Speed, EffCurve4Speed, EffCurve5Speed,
                                          x0EffCurve1, x1EffCurve1, x2EffCurve1, x3EffCurve1, x4EffCurve1, x5EffCurve1,
                                          x0EffCurve2, x1EffCurve2, x2EffCurve2, x3EffCurve2, x4EffCurve2, x5EffCurve2,
                                          x0EffCurve3, x1EffCurve3, x2EffCurve3, x3EffCurve3, x4EffCurve3, x5EffCurve3,
                                          x0EffCurve4, x1EffCurve4, x2EffCurve4, x3EffCurve4, x4EffCurve4, x5EffCurve4,
                                          x0EffCurve5, x1EffCurve5, x2EffCurve5, x3EffCurve5, x4EffCurve5, x5EffCurve5):

   EffCurve1Result= EffCurve( x0EffCurve1, x1EffCurve1, x2EffCurve1, x3EffCurve1, x4EffCurve1, x5EffCurve1, VolFlow)
   EffCurve2Result= EffCurve( x0EffCurve2, x1EffCurve2, x2EffCurve2, x3EffCurve2, x4EffCurve2, x5EffCurve2, VolFlow)
   EffCurve3Result= EffCurve( x0EffCurve3, x1EffCurve3, x2EffCurve3, x3EffCurve3, x4EffCurve3, x5EffCurve3, VolFlow)
   EffCurve4Result= EffCurve( x0EffCurve4, x1EffCurve4, x2EffCurve4, x3EffCurve4, x4EffCurve4, x5EffCurve4, VolFlow)
   EffCurve5Result= EffCurve( x0EffCurve5, x1EffCurve5, x2EffCurve5, x3EffCurve5, x4EffCurve5, x5EffCurve5, VolFlow)
   
   EffCurve1ResultDiv = EffCurve1Result
   EffCurve2ResultDiv = EffCurve2Speed - EffCurve1Speed  + EffCurve1Result
   EffCurve3ResultDiv = EffCurve3Speed - EffCurve2Speed  + EffCurve2Result 
   EffCurve4ResultDiv = EffCurve4Speed - EffCurve3Speed  + EffCurve3Result 
   EffCurve5ResultDiv = EffCurve5Speed - EffCurve4Speed  + EffCurve4Result 

   if Speed < EffCurve1Speed and EffCurve1ResultDiv !=0 : 
      return  (EffCurve1Speed - Speed) * EffCurve1Result/ EffCurve1ResultDiv 
   if Speed >=  EffCurve1Speed and Speed < EffCurve2Speed and EffCurve2ResultDiv !=0 : 
      return ( Speed - EffCurve1Speed)  * ( EffCurve2Result - EffCurve1Result) / EffCurve2ResultDiv
   elif  Speed >=  EffCurve2Speed and Speed < EffCurve3Speed and EffCurve3ResultDiv !=0: 
      return ( Speed - EffCurve2Speed)  * ( EffCurve3Result - EffCurve2Result) / EffCurve3ResultDiv
   elif  Speed >=  EffCurve3Speed and Speed < EffCurve4Speed and EffCurve4ResultDiv !=0:
      return ( Speed - EffCurve3Speed)  * ( EffCurve4Result - EffCurve3Result) / EffCurve4ResultDiv
   elif  Speed >=  EffCurve4Speed and EffCurve5ResultDiv !=0:
      return  ( Speed - EffCurve4Speed)  * ( EffCurve5Result - EffCurve4Result) / EffCurve5ResultDiv
   else: return np.nan

def DesignPolyHead( Speed, VolFlow, HeadCurve1Speed, HeadCurve2Speed, HeadCurve3Speed, HeadCurve4Speed, HeadCurve5Speed,
                                          x0HeadCurve1, x1HeadCurve1, x2HeadCurve1, x3HeadCurve1, x4HeadCurve1, x5HeadCurve1,
                                          x0HeadCurve2, x1HeadCurve2, x2HeadCurve2, x3HeadCurve2, x4HeadCurve2, x5HeadCurve2,
                                          x0HeadCurve3, x1HeadCurve3, x2HeadCurve3, x3HeadCurve3, x4HeadCurve3, x5HeadCurve3,
                                          x0HeadCurve4, x1HeadCurve4, x2HeadCurve4, x3HeadCurve4, x4HeadCurve4, x5HeadCurve4,
                                          x0HeadCurve5, x1HeadCurve5, x2HeadCurve5, x3HeadCurve5, x4HeadCurve5, x5HeadCurve5):

   HeadCurve1Result= HeadCurve( x0HeadCurve1, x1HeadCurve1, x2HeadCurve1, x3HeadCurve1, x4HeadCurve1, x5HeadCurve1, VolFlow)
   HeadCurve2Result= HeadCurve( x0HeadCurve2, x1HeadCurve2, x2HeadCurve2, x3HeadCurve2, x4HeadCurve2, x5HeadCurve2, VolFlow)
   HeadCurve3Result= HeadCurve( x0HeadCurve3, x1HeadCurve3, x2HeadCurve3, x3HeadCurve3, x4HeadCurve3, x5HeadCurve3, VolFlow)
   HeadCurve4Result= HeadCurve( x0HeadCurve4, x1HeadCurve4, x2HeadCurve4, x3HeadCurve4, x4HeadCurve4, x5HeadCurve4, VolFlow)
   HeadCurve5Result= HeadCurve( x0HeadCurve5, x1HeadCurve5, x2HeadCurve5, x3HeadCurve5, x4HeadCurve5, x5HeadCurve5, VolFlow)
  
   HeadCurve1ResultDiv = HeadCurve1Result
   HeadCurve2ResultDiv = HeadCurve2Speed - HeadCurve1Speed  + HeadCurve1Result
   HeadCurve3ResultDiv = HeadCurve3Speed - HeadCurve2Speed  + HeadCurve2Result 
   HeadCurve4ResultDiv = HeadCurve4Speed - HeadCurve3Speed  + HeadCurve3Result 
   HeadCurve5ResultDiv = HeadCurve5Speed - HeadCurve4Speed  + HeadCurve4Result 
   if Speed < HeadCurve1Speed and HeadCurve1ResultDiv !=0 : 
      return ( Speed - HeadCurve1Speed)  * ( HeadCurve1Result) / HeadCurve1ResultDiv
   elif Speed >=  HeadCurve1Speed and Speed < HeadCurve2Speed and HeadCurve2ResultDiv !=0 : 
      return ( Speed - HeadCurve1Speed)  * ( HeadCurve2Result - HeadCurve1Result) / HeadCurve2ResultDiv
   elif  Speed >=  HeadCurve2Speed and Speed < HeadCurve3Speed and HeadCurve3ResultDiv !=0: 
      return ( Speed - HeadCurve2Speed)  * ( HeadCurve3Result - HeadCurve2Result) / HeadCurve3ResultDiv
   elif  Speed >=  HeadCurve3Speed and Speed < HeadCurve4Speed and HeadCurve4ResultDiv !=0:
      return ( Speed - HeadCurve3Speed)  * ( HeadCurve4Result - HeadCurve3Result) / HeadCurve4ResultDiv
   elif  Speed >=  HeadCurve4Speed and HeadCurve5ResultDiv !=0:
      return  ( Speed - HeadCurve4Speed)  * ( HeadCurve5Result - HeadCurve4Result) / HeadCurve5ResultDiv
   else: return np.nan
   
 
def HeadCurve( x0, x1, x2, x3, x4, x5, VolFlow) :
   return ( x0 + VolFlow * ( x1 + VolFlow * ( x2 + VolFlow * ( x3 + VolFlow * ( x4 + x5 * VolFlow) ) ) ) ) 

def EffCurve( x0, x1, x2, x3, x4, x5, VolFlow) :
   return ( x0 + VolFlow * ( x1 + VolFlow * ( x2 + VolFlow * ( x3 + VolFlow * ( x4 + x5 * VolFlow) ) ) )  * 100) 



#Non Stage KPIs
def VanePosDev(VanePosActual, VanePosTarget) :
      return VanePosActual - VanePosTarget

def TotalAdiaHead(AdiaHead):
   return sum(AdiaHead)

def TotalAdiaHeadM(TotalAdiaHead):
   return  1000 * TotalAdiaHead/ 9.80665

def TotalIdealPowerAdia(MassFlow,AdiaHead):
   return sum( i/3600*j for i,j in zip(MassFlow,AdiaHead))  

def TotalIdealPowerPoly(MassFlow,PolyHead):
   return  sum( i/3600*j for i,j in zip(MassFlow,PolyHead))

def TotalDesignGasPower(DesignGasPower):
   return sum(DesignGasPower)  

def TotalGasPower(GasPower):
   return sum(GasPower)

def TotalGasPowerDeviaton(TotalDesignGasPower,TotalGasPower):
   return TotalGasPower- TotalDesignGasPower

def TotalGasPowerDevnPcn(TotalDesignGasPower,TotalGasPowerDeviaton):
   return 100 * TotalGasPowerDeviaton / TotalDesignGasPower

def TotalPolyHead(PolyHead):
   return sum(PolyHead)

def TotalDesignPolyHead(DesignPolyHead):
   return sum(DesignPolyHead)

def TotalDesignPolyHeadM(TotalDesignPolyHead):
   return 1000 * TotalDesignPolyHead / 9.80665

def TotalMassFlow(MassFlow):
   return min(MassFlow)

def TotalSpecificPower(TotalMassFlow,TotalPower):
   if TotalMassFlow != 0 :  return TotalPower / (TotalMassFlow/3600)
   else: return 0

def TotalPressRatio(HighStageDischargePressure,LowStageSuctionPressure): 
   EnvironmentBarometricPress=1
   if (LowStageSuctionPressure + EnvironmentBarometricPress) != 0 :  
      return (HighStageDischargePressure + EnvironmentBarometricPress) / (LowStageSuctionPressure  + EnvironmentBarometricPress) 
   else: return 0

def TotalPolyEfficiency( TotalIdealPowerPoly,TotalGasPower):
   return 100 *  TotalIdealPowerPoly /  TotalGasPower

def TotalDesignPolyEfficiency(TotalIdealPowerPoly,TotalDesignGasPower):
   if TotalDesignGasPower != 0 :  return  100 * TotalIdealPowerPoly / TotalDesignGasPower
   else: return 0

def TotalPolyEfficiencyDeviation(TotalPolyEfficiency,TotalDesignPolyEfficiency):
   return TotalPolyEfficiency - TotalDesignPolyEfficiency

def TotalPolyEfficiencyDevnPcn(TotalPolyEfficiencyDeviation,TotalDesignPolyEfficiency):
   return 100 * TotalPolyEfficiencyDeviation / TotalDesignPolyEfficiency

def TotalPower(TotalGasPower,MechEff):
   if MechEff != 0 :  return 100 * TotalGasPower / MechEff
   else: return 0

def TotalPolyHeadM(TotalPolyHead):
   return 1000 * TotalPolyHead / 9.80665

def TotalGasPowerDeviation(TotalGasPower,TotalDesignGasPower):
   return TotalGasPower - TotalDesignGasPower

def TotalPolyHeadMDeviation(TotalPolyHeadDeviation):
   return 1000 * TotalPolyHeadDeviation / 9.80665

def TotalPolyHeadMDevnPcn(TotalPolyHeadDevnPcn):
   return 1000 * TotalPolyHeadDevnPcn / 9.80665

def TotalPolyHeadDeviation(TotalDesignPolyHead,TotalPolyHead):
   return TotalPolyHead - TotalDesignPolyHead

def TotalPolyHeadDevnPcn(TotalPolyHeadDeviation,TotalDesignPolyHead):
   if TotalDesignPolyHead != 0 :return 100 * TotalPolyHeadDeviation / TotalDesignPolyHead

def TotalPressRise(PressRise):
   return sum(PressRise)

def DegradationCost(TotalGasPowerDeviation,PowerCost):
   return TotalGasPowerDeviation * PowerCost * 24

def TotalAdiaEfficiency(TotalIdealPowerAdia, TotalGasPower):
   if TotalGasPower != 0 :  return 100 * TotalIdealPowerAdia / TotalGasPower
   else: return 0

def TotalAdiaEfficiencyDesign(TotalIdealPowerAdia,TotalDesignGasPower):
   if TotalDesignGasPower != 0 :  return 100 * TotalIdealPowerAdia / TotalDesignGasPower
   else: return 0