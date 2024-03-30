// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © GuruprasadMeduri
//@version=4

//***************GUIDE***********************************
//CPR - Applicable only for daily pivots
//CPR - All 3 lines display enabled by default
//CPR - Central Pivot line display cannot changed
//CPR - Central Pivot is a blue line by default and can be changed from settings
//CPR - Top Range & Bottom Ranage display can be changed from settings
//CPR - Top Range & Bottom Ranage are  Yellow lines by default and can be chaned from settings
//Daily pivots - Pivot line and CPR Central line are same
//Daily pivots - level 1 & 2 (S1, R1, S2  R2) display enabled by default and can be changed from settings
//Daily pivots - level 3 (S3 & R3) is availale and can be seleted from settings
//Daily pivots - Resistance(R) lines are Red lines and can be changed from settings
//Daily pivots - Support(S) lines are Green lines and can be changed from settings
//Weekly pivots - Pivot is a blue line by default and can be changed from settings
//Weekly pivots - 3 levels (S1, R1, S2, R2, S3 & R3) availale and can be seleted from settings
//Weekly pivots - Resistance(R) lines are crossed (+) Red lines and can be changed from settings
//Weekly pivots - Support(S) lines are crossed (+) Green lines and can be changed from settings
//Monthly pivots - Pivot is a blue line by default and can be changed from settings
//Monthly pivots - 3 levels (S1, R1, S2, R2, S3 & R3) availale and can be seleted from settings
//Monthly pivots - Resistance(R) lines are circled (o) Red lines and can be changed from settings
//Monthly pivots - Support(S) lines are circled (o) Green lines and can be changed from settings


study("CPR with MAs, Super Trend & VWAP by GuruprasadMeduri", overlay = true, shorttitle="Magic",precision=1)
//******************LOGICS**************************

//cenral pivot range

pivot = (high + low + close) /3 //Central Povit
BC = (high + low) / 2 //Below Central povit
TC = (pivot - BC) + pivot //Top Central povot

//3  support levels
S1 = (pivot * 2) - high
S2 = pivot - (high - low)
S3 = low - 2 * (high - pivot)

//3  resistance levels
R1 = (pivot * 2) - low
R2 = pivot + (high - low)
R3 = high + 2 * (pivot-low)

//Checkbox inputs
CPRPlot = input(title = "Plot CPR?", type=input.bool, defval=true)
DayS1R1 = input(title = "Plot Daiy S1/R1?", type=input.bool, defval=true)
DayS2R2 = input(title = "Plot Daiy S2/R2?", type=input.bool, defval=false)
DayS3R3 = input(title = "Plot Daiy S3/R3?", type=input.bool, defval=false)
WeeklyPivotInclude = input(title = "Plot Weekly Pivot?", type=input.bool, defval=false)
WeeklyS1R1 = input(title = "Plot weekly S1/R1?", type=input.bool, defval=false)
WeeklyS2R2 = input(title = "Plot weekly S2/R2?", type=input.bool, defval=false)
WeeklyS3R3 = input(title = "Plot weekly S3/R3?", type=input.bool, defval=false)
MonthlyPivotInclude = input(title = "Plot Montly Pivot?", type=input.bool, defval=false)
MonthlyS1R1 = input(title = "Plot Monthly S1/R1?", type=input.bool, defval=false)
MonthlyS2R2 = input(title = "Plot Monthly S2/R2?", type=input.bool, defval=false)
MonthlyS3R3 = input(title = "Plot Montly S3/R3?", type=input.bool, defval=false)

//******************DAYWISE CPR & PIVOTS**************************
// Getting daywise CPR
DayPivot = security(syminfo.tickerid, "D", pivot[1], barmerge.gaps_off, barmerge.lookahead_on)
DayBC = security(syminfo.tickerid, "D", BC[1], barmerge.gaps_off, barmerge.lookahead_on)
DayTC = security(syminfo.tickerid, "D", TC[1], barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks daywse for CPR
CPColour = DayPivot != DayPivot[1] ? na : color.blue
BCColour = DayBC != DayBC[1] ? na : color.blue
TCColour = DayTC != DayTC[1] ? na : color.blue

//Plotting daywise CPR
plot(DayPivot, title = "CP" , color = CPColour, style = plot.style_linebr, linewidth =2)
plot(CPRPlot ? DayBC : na , title = "BC" , color = BCColour, style = plot.style_line, linewidth =1)
plot(CPRPlot ? DayTC : na , title = "TC" , color = TCColour, style = plot.style_line, linewidth =1)

// Getting daywise Support levels
DayS1 = security(syminfo.tickerid, "D", S1[1], barmerge.gaps_off, barmerge.lookahead_on)
DayS2 = security(syminfo.tickerid, "D", S2[1], barmerge.gaps_off, barmerge.lookahead_on)
DayS3 = security(syminfo.tickerid, "D", S3[1], barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks for daywise Support levels 
DayS1Color =DayS1 != DayS1[1] ? na : color.green
DayS2Color =DayS2 != DayS2[1] ? na : color.green
DayS3Color =DayS3 != DayS3[1] ? na : color.green

//Plotting daywise Support levels
plot(DayS1R1 ? DayS1 : na, title = "D-S1" , color = DayS1Color, style = plot.style_line, linewidth =1)
plot(DayS2R2 ? DayS2 : na, title = "D-S2" , color = DayS2Color, style = plot.style_line, linewidth =1)
plot(DayS3R3 ? DayS3 : na, title = "D-S3" , color = DayS3Color, style = plot.style_line, linewidth =1)

// Getting daywise Resistance levels
DayR1 = security(syminfo.tickerid, "D", R1[1], barmerge.gaps_off, barmerge.lookahead_on)
DayR2 = security(syminfo.tickerid, "D", R2[1], barmerge.gaps_off, barmerge.lookahead_on)
DayR3 = security(syminfo.tickerid, "D", R3[1], barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks for daywise Support levels
DayR1Color =DayR1 != DayR1[1] ? na : color.red
DayR2Color =DayR2 != DayR2[1] ? na : color.red
DayR3Color =DayR3 != DayR3[1] ? na : color.red

//Plotting daywise Resistance levels
plot(DayS1R1 ? DayR1 : na, title = "D-R1" , color = DayR1Color, style = plot.style_line, linewidth =1)
plot(DayS2R2 ? DayR2 : na, title = "D-R2" , color = DayR2Color, style = plot.style_line, linewidth =1)
plot(DayS3R3 ? DayR3 : na, title = "D-R3" , color = DayR3Color, style = plot.style_line, linewidth =1)

//******************WEEKLY PIVOTS**************************

// Getting Weely Pivot
WPivot = security(syminfo.tickerid, "W", pivot[1], barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks for Weely Pivot 
WeeklyPivotColor =WPivot != WPivot[1] ? na : color.blue

//Plotting Weely Pivot
plot(WeeklyPivotInclude ? WPivot:na, title = "W-P" , color = WeeklyPivotColor, style = plot.style_circles, linewidth =1)


// Getting Weely Support levels
WS1 = security(syminfo.tickerid, "W", S1[1],barmerge.gaps_off, barmerge.lookahead_on)
WS2 = security(syminfo.tickerid, "W", S2[1],barmerge.gaps_off, barmerge.lookahead_on)
WS3 = security(syminfo.tickerid, "W", S3[1],barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks for weekly Support levels
WS1Color =WS1 != WS1[1] ? na : color.green
WS2Color =WS2 != WS2[1] ? na : color.green
WS3Color =WS3 != WS3[1] ? na : color.green

//Plotting Weely Support levels
plot(WeeklyS1R1 ? WS1 : na, title = "W-S1" , color = WS1Color, style = plot.style_cross, linewidth =1)
plot(WeeklyS2R2 ? WS2 : na, title = "W-S2" , color = WS2Color, style = plot.style_cross, linewidth =1)
plot(WeeklyS3R3 ? WS3 : na, title = "W-S3" , color = WS3Color, style = plot.style_cross, linewidth =1)

// Getting Weely Resistance levels
WR1 = security(syminfo.tickerid, "W", R1[1], barmerge.gaps_off, barmerge.lookahead_on)
WR2 = security(syminfo.tickerid, "W", R2[1], barmerge.gaps_off, barmerge.lookahead_on)
WR3 = security(syminfo.tickerid, "W", R3[1], barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks for weekly Resistance levels
WR1Color = WR1 != WR1[1] ? na : color.red
WR2Color = WR2 != WR2[1] ? na : color.red
WR3Color = WR3 != WR3[1] ? na : color.red

//Plotting Weely Resistance levels
plot(WeeklyS1R1 ? WR1 : na , title = "W-R1" , color = WR1Color, style = plot.style_cross, linewidth =1)
plot(WeeklyS2R2 ? WR2 : na , title = "W-R2" , color = WR2Color, style = plot.style_cross, linewidth =1)
plot(WeeklyS3R3 ? WR3 : na , title = "W-R3" , color = WR3Color, style = plot.style_cross, linewidth =1)

//******************MONTHLY PIVOTS**************************

// Getting Monhly Pivot
MPivot = security(syminfo.tickerid, "M", pivot[1],barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks for Monthly Support levels 
MonthlyPivotColor =MPivot != MPivot[1] ? na : color.blue

//Plotting  Monhly Pivot
plot(MonthlyPivotInclude? MPivot:na, title = " M-P" , color = MonthlyPivotColor, style = plot.style_line, linewidth =1)

// Getting  Monhly Support levels
MS1 = security(syminfo.tickerid, "M", S1[1],barmerge.gaps_off, barmerge.lookahead_on)
MS2 = security(syminfo.tickerid, "M", S2[1],barmerge.gaps_off, barmerge.lookahead_on)
MS3 = security(syminfo.tickerid, "M", S3[1],barmerge.gaps_off, barmerge.lookahead_on)

//Adding linebreaks for Montly Support levels
MS1Color =MS1 != MS1[1] ? na : color.green
MS2Color =MS2 != MS2[1] ? na : color.green
MS3Color =MS3 != MS3[1] ? na : color.green

//Plotting  Monhly Support levels
plot(MonthlyS1R1 ? MS1 : na, title = "M-S1" , color = MS1Color, style = plot.style_circles, linewidth =1)
plot(MonthlyS2R2 ? MS2 : na, title = "M-S2" , color = MS2Color, style = plot.style_circles, linewidth =1)
plot(MonthlyS3R3 ? MS3 : na, title = "M-S3" , color = MS3Color, style = plot.style_circles, linewidth =1)

// Getting  Monhly Resistance levels
MR1 = security(syminfo.tickerid, "M", R1[1],barmerge.gaps_off, barmerge.lookahead_on)
MR2 = security(syminfo.tickerid, "M", R2[1],barmerge.gaps_off, barmerge.lookahead_on)
MR3 = security(syminfo.tickerid, "M", R3[1],barmerge.gaps_off, barmerge.lookahead_on)

MR1Color =MR1 != MR1[1] ? na : color.red
MR2Color =MR2 != MR2[1] ? na : color.red
MR3Color =MR3 != MR3[1] ? na : color.red

//Plotting  Monhly Resistance levels
plot(MonthlyS1R1 ? MR1 : na , title = "M-R1", color = MR1Color, style = plot.style_circles , linewidth =1)
plot(MonthlyS2R2 ? MR2 : na , title = "M-R2" , color = MR2Color, style = plot.style_circles, linewidth =1)
plot(MonthlyS3R3 ? MR3 : na, title = "M-R3" , color = MR3Color, style = plot.style_circles, linewidth =1)

//*****************************INDICATORs**************************

//SMA
PlotSMA = input(title = "Plot SMA?", type=input.bool, defval=true)
SMALength = input(title="SMA Length", type=input.integer, defval=50)
SMASource = input(title="SMA Source", type=input.source, defval=close)
SMAvg = sma (SMASource, SMALength)
plot(PlotSMA ? SMAvg : na,  color= color.orange, title="SMA")

//EMA
PlotEMA = input(title = "Plot EMA?", type=input.bool, defval=true)
EMALength = input(title="EMA Length", type=input.integer, defval=62)
EMASource = input(title="EMA Source", type=input.source, defval=close)
EMAvg = ema (EMASource, EMALength)
plot(PlotEMA ? EMAvg : na,  color= color.red, title="EMA")

PlotEMA2 = input(title = "Plot EMA?", type=input.bool, defval=true)
EMALength2 = input(title="EMA Length", type=input.integer, defval=38)
EMASource2 = input(title="EMA Source", type=input.source, defval=close)
EMAvg2 = ema (EMASource2, EMALength2)
plot(PlotEMA2 ? EMAvg2 : na,  color= color.red, title="EMA")

//MULTI TIME FRAME EMA
PlotMTFEMA2 = input(title = "MTF EMA?", type=input.bool, defval=true)
mtf2= input(title="MTF", type=input.resolution, defval="1D")
MTFEMALength2 = input(title="EMA Length", type=input.integer, defval=38)
MTFEMASource2 = input(title="EMA Source", type=input.source, defval=close)
MTFEMAvg2 = ema (MTFEMASource2, MTFEMALength2)
ma2 =security(syminfo.tickerid, mtf2, MTFEMAvg2)
plot(PlotMTFEMA2 ? ma2 : na,  color= color.red, title="EMA")

PlotMTFEMA = input(title = "MTF EMA?", type=input.bool, defval=true)
mtf= input(title="MTF", type=input.resolution, defval="1D")
MTFEMALength = input(title="EMA Length", type=input.integer, defval=62)
MTFEMASource = input(title="EMA Source", type=input.source, defval=close)
MTFEMAvg = ema (MTFEMASource, MTFEMALength)
ma =security(syminfo.tickerid, mtf, MTFEMAvg)
plot(PlotMTFEMA2 ? ma : na,  color= color.rgb(82, 82, 255), title="EMA")



//EMA block ploting usind default 62 and 38
PlotBand = input(title = "Plot BAND?", type=input.bool, defval=true)
col = EMAvg > EMAvg2 ? color.red : EMAvg < EMAvg2 ? color.lime : color.yellow
p1 = plot(EMAvg, title="Slow MA", linewidth=2,  color=col)
p2 = plot(EMAvg2, title="Slow MA",  linewidth=2,color=col)
fill(p1, p2, color=color.silver, transp=50)


//VWAP
PlotVWAP = input(title = "Plot VWAP?", type=input.bool, defval=true)
VWAPSource = input(title="VWAP Source", type=input.source, defval=close)
VWAPrice = vwap (VWAPSource)
plot(PlotVWAP ? VWAPrice : na,  color= color.teal, title="VWAP")
//SuperTrend
PlotSTrend = input(title = "Plot Super Trend?", type=input.bool, defval=true)
InputFactor=input(3, minval=1,maxval = 100, title="Factor")
InputLength=input(10, minval=1,maxval = 100, title="Lenght")
BasicUpperBand=hl2-(InputFactor*atr(InputLength))
BasicLowerBand=hl2+(InputFactor*atr(InputLength))
FinalUpperBand=0.0
FinalLowerBand=0.0
FinalUpperBand:=close[1]>FinalUpperBand[1]? max(BasicUpperBand,FinalUpperBand[1]) : BasicUpperBand
FinalLowerBand:=close[1]<FinalLowerBand[1]? min(BasicLowerBand,FinalLowerBand[1]) : BasicLowerBand
IsTrend=0.0
IsTrend:= close > FinalLowerBand[1] ? 1: close< FinalUpperBand[1]? -1: nz(IsTrend[1],1)
STrendline = IsTrend==1? FinalUpperBand: FinalLowerBand
linecolor = IsTrend == 1 ? color.green : color.red
Plotline = (PlotSTrend? STrendline: na)
plot(Plotline, color = linecolor , style = plot.style_line , linewidth = 1,title = "SuperTrend")
PlotShapeUp = cross(close,STrendline) and close>STrendline
PlotShapeDown = cross(STrendline,close) and close<STrendline
plotshape(PlotSTrend?  PlotShapeUp: na, "Up Arrow", shape.triangleup,location.belowbar,color.green,0,0)
plotshape(PlotSTrend?  PlotShapeDown: na , "Down Arrow", shape.triangledown , location.abovebar, color.red,0,0)


R1break = IsTrend==1 and open[0]<DayR1 and close[0]>DayR1  ? 1 : 0
R1break2 = IsTrend!=1 and open[0]>DayR1 and close[0]<DayR1  ? 1 : 0
R2break = IsTrend==1 and open[0]<DayR2 and close[0]>DayR2  ? 1 : 0
R2break2 = IsTrend!=1 and open[0]>DayR2 and close[0]<DayR2  ? 1 : 0
// TCbreak = IsTrend==1 and open[1]<DayTc and close[1]>DayTC  ? 1 : 0
S1break2 = IsTrend!=1 and open[0]>DayS1 and close[0]<DayS1  ? 1 : 0
S1break = IsTrend==1 and open[0]<DayS1 and close[0]>DayS1  ? 1 : 0
S2break2 = IsTrend!=1 and open[0]>DayS2 and close[0]<DayS2  ? 1 : 0
S2break = IsTrend==1 and open[0]<DayS2 and close[0]>DayS2  ? 1 : 0
// BCbreak = IsTrend!=1 and open[1]>DayBC and close[1]<DayBC  ? 1 : 0
Pbreak = IsTrend==1 and open[0]<DayPivot and close[0]>DayPivot  ? 1 : 0
Pbreak2 = IsTrend!=1 and open[0]>DayPivot and close[0]<DayPivot  ? 1 : 0
temp  = R1break or R2break or S1break or S2break or R1break2 or R2break2 or S1break2 or S2break2 or Pbreak or Pbreak2 ? 1 : 0
// pricee = 17119
// count9 = IsTrend!=1 and close[1]>pricee
buy_condition = R1break or R2break or S1break or S2break or Pbreak ? 1 : 0
sell_condition =  R1break2 or R2break2 or S1break2 or S2break2 or Pbreak2 ? 1 : 0 
plotshape(series=buy_condition, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=sell_condition, title="Sell Signal", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

alertcondition(temp	, title="System Found Alert", message="Trade Entry get Ready")

greencandle = open[0]<close[0] ? 1 : 0
alertcondition(greencandle	, title="Green candle Alert", message="Trade Entry")

