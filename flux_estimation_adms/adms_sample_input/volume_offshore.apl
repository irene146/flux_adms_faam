&ADMS_HEADER
Comment     = "This is an ADMS parameter file"
Model       = "ADMS"
Version     = 6.0
FileVersion = 9
Complete    = 1
/

&ADMS_PARAMETERS_SUP
SupSiteName                 = "Elgin wellehad"
SupProjectName              = "Elgin wellhead"
SupUseAddInput              = 1
SupAddInputPath             = "C:\adms_runs_b689\adms_runs_correct\wellheadA\cerc_corrections\mbl.AAI"
SupReleaseType              = 0
SupModelBuildings           = 0
SupModelComplexTerrain      = 0
SupModelCoastline           = 0
SupCalcChm                  = 0
SupCalcDryDep               = 0
SupCalcWetDep               = 0
SupCalcPlumeVisibility      = 0
SupModelFluctuations        = 0
SupModelRadioactivity       = 0
SupModelOdours              = 0
SupPaletteType              = 1
SupUseTimeVaryingEmissions  = 0
SupTimeVaryingEmissionsType = 0
SupTimeVaryingVARPath       = " "
SupTimeVaryingFACPath       = " "
SupUseTimeVaryingScreenBySource= "11110010"
SupTimeVaryingEmissionFactorsWeekday =
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
SupTimeVaryingEmissionFactorsSaturday =
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
SupTimeVaryingEmissionFactorsSunday =
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
  1.0e+0 1.0e+0 1.0e+0 1.0e+0
/
&ADMS_PARAMETERS_MET
MetLatitude               = 5.7e+1
MetDataSource             = 0
MetDataFileWellFormedPath = "C:\adms_runs_b689\adms_runs_correct\wellheadA\cerc_corrections\wellheadA_sstemp10.met"
MetWindHeight             = 3.50e+2
MetWindInSectors          = 0
MetWindSectorSizeDegrees  = 1.0e+1
MetDataIsSequential       = 1
MetUseSubset              = 0
MetSubsetHourStart        = 1
MetSubsetDayStart         = 1
MetSubsetMonthStart       = 1
MetSubsetYearStart        = 2023
MetSubsetHourEnd          = 24
MetSubsetDayEnd           = 31
MetSubsetMonthEnd         = 12
MetSubsetYearEnd          = 2023
MetUseVerticalProfile     = 0
MetVerticalProfilePath    = " "
Met_DS_RoughnessMode      = 1
Met_DS_Roughness          = 1.0e-4
Met_DS_UseAdvancedMet     = 0
Met_DS_SurfaceAlbedoMode  = 0
Met_DS_SurfaceAlbedo      = 2.3e-1
Met_DS_PriestlyTaylorMode = 0
Met_DS_PriestlyTaylor     = 1.0e+0
Met_DS_MinLmoMode         = 0
Met_DS_MinLmo             = 1.0e+0
Met_DS_PrecipFactorMode   = 0
Met_DS_PrecipFactor       = 1.0e+0
Met_MS_RoughnessMode      = 3
Met_MS_Roughness          = 1.0e-1
Met_MS_UseAdvancedMet     = 0
Met_MS_SurfaceAlbedoMode  = 3
Met_MS_SurfaceAlbedo      = 2.3e-1
Met_MS_PriestlyTaylorMode = 3
Met_MS_PriestlyTaylor     = 1.0e+0
Met_MS_MinLmoMode         = 3
Met_MS_MinLmo             = 1.0e+0
MetHeatFluxType           = 0
MetInclBoundaryLyrHt      = 1
MetInclSurfaceTemp        = 0
MetInclLateralSpread      = 0
MetInclRelHumidity        = 0
MetHandNumEntries         = 0
/
&ADMS_PARAMETERS_BLD
BldNumBuildings = 0
/
&ADMS_PARAMETERS_HIL
HilGridSize        = 2
HilUseTerFile      = 1
HilUseRoughFile    = 0
HilTerrainPath     = " "
HilRoughPath       = " "
HilCreateFlowField = 0
/
&ADMS_PARAMETERS_CST
CstPoint1X         = 0.0e+0
CstPoint1Y         = 0.0e+0
CstPoint2X         = -1.000e+3
CstPoint2Y         = 1.000e+3
CstLandPointX      = 5.00e+2
CstLandPointY      = 5.00e+2
/
&ADMS_PARAMETERS_FLC
FlcAvgTime         = 9.00e+2
FlcUnitsPollutants = "ug/m3"
FlcUnitsIsotopes   = "Bq/m3"
FlcCalcToxicResponse = 0
FlcToxicExp        = 1.0e+0
FlcCalcPercentiles = 0
FlcNumPercentiles  = 0
FlcCalcPDF         = 0
FlcPDFMode         = 0
FlcNumPDF          = 0
/
&ADMS_PARAMETERS_GRD
GrdSpacingType     = 0
GrdRegularMin      = 
  2.100e+3 1.100e+3 7.5e+1
GrdRegularMax      = 
  1.2500e+4 1.2500e+4 5.95e+2
GrdRegularNumPoints= 
  1040 1140 27
GrdVarSpaceNumPointsX  = 0
GrdVarSpaceNumPointsY  = 0
GrdVarSpaceNumPointsZ  = 0
GrdPtsNumPoints        = 0
GrdPtsUsePointsFile  = 0
GrdPtsPointsFilePath = " "
GrdPtsUsePoints      = 0
GrdUseGrid           = 1
/
&ADMS_PARAMETERS_PUF
PufType         = 0
PufStart        = 1.00e+2
PufStep         = 1.00e+2
PufNumSteps     = 10
/
&ADMS_PARAMETERS_GAM
GamCalcDose     = 0
/
&ADMS_PARAMETERS_OPT
OptNumOutputs               = 1
OptPolName                  =
  "Methane"
OptInclude                  =
  1
OptShortOrLong              =
  0
OptSamplingTime             =
  1.0e+0
OptSamplingTimeUnits        =
  1
OptCondition                =
  0
OptNumPercentiles           =
  0
OptNumExceedences           =
  0
OptPercentiles              =
  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0
OptExceedences              =
  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0  0.0e+0
OptUnits                    =
  "ppb"
OptValidity                 =
  7.5e+1
OptGroupsOrSource           = 1
OptAllSources               = 1
OptNumGroups                = 0
OptIncludedSource           = "Elgin"
OptCreateComprehensiveFile  = 0
OptOutputPerSource          = 0
/
&ADMS_PARAMETERS_CHM
ChmScheme       = 1
/
&ADMS_PARAMETERS_BKG
BkgFilePath     = " "
BkgFixedLevels  = 2
/
&ADMS_COORDINATESYSTEM
ProjectedEPSG               = 0
ProjectedName               = "Unspecified regular Cartesian"
ProjectedWKT                = " "
/
&ADMS_PARAMETERS_ETC
SrcNumSources   = 1
PolNumPollutants= 13
PolNumIsotopes  = 0
/
&ADMS_MAPPERPROJECT
ProjectFilePath             = " "
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "NOx"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 5.2e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "NO2"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 5.2e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "NO"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 8.0e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "O3"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 5.0e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "VOC"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 3.1e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "SO2"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 3.7e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "PM10"
 PolPollutantType         = 1
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-5
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 1.0e+0
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ug/m3"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "PM2.5"
 PolPollutantType         = 1
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  2.5e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 1.0e+0
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ug/m3"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "CO"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 8.6e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "BENZENE"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 3.1e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "BUTADIENE"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 4.5e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "HCl"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 0
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 6.589e-1
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_POLLUTANT_DETAILS
 PolName                  = "Methane"
 PolPollutantType         = 0
 PolGasDepVelocityKnown   = 1
 PolGasDepositionVelocity = 0.0e+0
 PolGasType               = 1
 PolParDepVelocityKnown   = 1
 PolParTermVelocityKnown  = 1
 PolParNumDepositionData  = 1
 PolParDepositionVelocity =
  0.0e+0
 PolParTerminalVelocity =
  0.0e+0
 PolParDiameter =
  1.0e-6
 PolParDensity =
  1.000e+3
 PolParMassFraction =
  1.0e+0
 PolWetWashoutKnown = 1
 PolWetWashout      = 0.0e+0
 PolWetWashoutA     = 1.0e-4
 PolWetWashoutB     = 6.4e-1
 PolConvFactor      = 1.5291e+0
 PolBkgLevel        = 0.0e+0
 PolBkgUnits        = "ppb"
/

&ADMS_SOURCE_DETAILS
SrcName         = "Elgin"
SrcMainBuilding = "(Main)"
SrcHeight       = 1.8e+1
SrcDiameter     = 1.0e+0
SrcVolFlowRate  = 1.1781e+1
SrcVertVeloc    = 1.5e+1
SrcTemperature  = 1.5e+1
SrcMolWeight    = 2.8966e+1
SrcDensity      = 1.225e+0
SrcSpecHeatCap  = 1.012e+3
SrcSourceType   = 2
SrcReleaseAtNTP = 0
SrcEffluxType   = 0
SrcBuoyancyType = 0
SrcPercentNOxAsNO2 = 5.0e+0
SrcX1           = 0.0e+0
SrcY1           = 0.0e+0
SrcL1           = 1.0e+1
SrcL2           = 1.0e+0
SrcFm           = 1.0e+0
SrcFb           = 1.0e+0
SrcMassFlux     = 1.0e+0
SrcAngle1       = 0.0e+0
SrcAngle2       = 0.0e+0
SrcMassH2O      = 0.0e+0
SrcUseVARFile   = 1
SrcNumGroups    = 0
SrcNumVertices        = 8
SrcNumPollutants      = 1
SrcPollutants =
  "Methane"
SrcPolEmissionRate =
  4.58333e-2
SrcPolTotalemission =
  1.0e+0
SrcPolStartTime =
  0.0e+0
SrcPolDuration =
  0.0e+0
SrcNumIsotopes        = 0
/

  &ADMS_SOURCE_VERTEX
  SourceVertexX = -1.4e+1
  SourceVertexY = 2.0e+1
  /

  &ADMS_SOURCE_VERTEX
  SourceVertexX = -1.5e+1
  SourceVertexY = 1.9e+1
  /

  &ADMS_SOURCE_VERTEX
  SourceVertexX = -1.5e+1
  SourceVertexY = -1.9e+1
  /

  &ADMS_SOURCE_VERTEX
  SourceVertexX = -1.4e+1
  SourceVertexY = -2.0e+1
  /

  &ADMS_SOURCE_VERTEX
  SourceVertexX = 1.4e+1
  SourceVertexY = -2.0e+1
  /

  &ADMS_SOURCE_VERTEX
  SourceVertexX = 1.5e+1
  SourceVertexY = -1.9e+1
  /

  &ADMS_SOURCE_VERTEX
  SourceVertexX = 1.5e+1
  SourceVertexY = 1.9e+1
  /

  &ADMS_SOURCE_VERTEX
  SourceVertexX = 1.4e+1
  SourceVertexY = 2.0e+1
  /
