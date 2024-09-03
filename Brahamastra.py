
//@version=4
study("Pivot Points Standard", "Magic Indicator 2", overlay=true, max_lines_count=500,  max_labels_count=500)

AUTO = "Auto"
DAILY = "Daily"
WEEKLY = "Weekly"
MONTHLY = "Monthly"
QUARTERLY = "Quarterly"
YEARLY = "Yearly"
BIYEARLY = "Biyearly"
TRIYEARLY = "Triyearly"
QUINQUENNIALLY = "Quinquennially"
DECENNIALLY = "Decennially"

TRADITIONAL = "Traditional"
FIBONACCI = "Fibonacci"
WOODIE = "Woodie"
CLASSIC = "Classic"
DEMARK = "DM"
CAMARILLA = "Camarilla"

kind = input(title="Type", defval="Traditional", options=[TRADITIONAL, FIBONACCI, WOODIE, CLASSIC, DEMARK, CAMARILLA])
pivot_time_frame = input(title="Pivots Timeframe", defval=AUTO, options=[AUTO, DAILY, WEEKLY, MONTHLY, QUARTERLY, YEARLY, BIYEARLY, TRIYEARLY, QUINQUENNIALLY, DECENNIALLY])
look_back = input(title="Number of Pivots Back", type=input.integer, defval=15, minval=1, maxval=5000)
is_daily_based = input(title="Use Daily-based Values", type=input.bool, defval=true, tooltip = "When this option is unchecked, Pivot Points will use intraday data while calculating on intraday charts. If Extended Hours are displayed on the chart, they will be taken into account during the pivot level calculation. If intraday OHLC values are different from daily-based values (normal for stocks), the pivot levels will also differ.")
show_labels = input(title="Show Labels", type=input.bool, defval=true, inline = "labels")
position_labels = input("Left", "", options = ["Left", "Right"], inline = "labels")

var DEF_COLOR = #FB8C00
var arr_time = array.new_int()
var p = array.new_float()
p_show = input(true, "P‏  ‏  ‏  ‏  ‏  ‏  ‏  ‏", inline = "P")
p_color = input(DEF_COLOR, "", inline = "P")

var r1 = array.new_float()
var s1 = array.new_float()
s1r1_show = input(true, "S1/R1", inline = "S1/R1")
s1r1_color = input(DEF_COLOR, "", inline = "S1/R1")

var r2 = array.new_float()
var s2 = array.new_float()
s2r2_show = input(true, "S2/R2", inline = "S2/R2")
s2r2_color = input(DEF_COLOR, "", inline = "S2/R2")

var r3 = array.new_float()
var s3 = array.new_float()
s3r3_show = input(true, "S3/R3", inline = "S3/R3")
s3r3_color = input(DEF_COLOR, "", inline = "S3/R3")

var r4 = array.new_float()
var s4 = array.new_float()
s4r4_show = input(true, "S4/R4", inline = "S4/R4")
s4r4_color = input(DEF_COLOR, "", inline = "S4/R4")

var r5 = array.new_float()
var s5 = array.new_float()
s5r5_show = input(true, "S5/R5", inline = "S5/R5")
s5r5_color = input(DEF_COLOR, "", inline = "S5/R5")


pivotX_open = float(na)
pivotX_open := nz(pivotX_open[1],open)
pivotX_high = float(na)
pivotX_high := nz(pivotX_high[1],high)
pivotX_low = float(na)
pivotX_low := nz(pivotX_low[1],low)
pivotX_prev_open = float(na)
pivotX_prev_open := nz(pivotX_prev_open[1])
pivotX_prev_high = float(na)
pivotX_prev_high := nz(pivotX_prev_high[1])
pivotX_prev_low = float(na)
pivotX_prev_low := nz(pivotX_prev_low[1])
pivotX_prev_close = float(na)
pivotX_prev_close := nz(pivotX_prev_close[1])

get_pivot_resolution() =>
    resolution = "M"
    if pivot_time_frame == AUTO
        if timeframe.isintraday
            resolution := timeframe.multiplier <= 15 ? "D" : "W"
        else if timeframe.isweekly or timeframe.ismonthly
            resolution := "12M"
    else if pivot_time_frame == DAILY
        resolution := "D"
    else if pivot_time_frame == WEEKLY
        resolution := "W"
    else if pivot_time_frame == MONTHLY
        resolution := "M"
    else if pivot_time_frame == QUARTERLY
        resolution := "3M"
    else if pivot_time_frame == YEARLY or pivot_time_frame == BIYEARLY or pivot_time_frame == TRIYEARLY or pivot_time_frame == QUINQUENNIALLY or pivot_time_frame == DECENNIALLY
        resolution := "12M"
    resolution

var lines = array.new_line()
var labels = array.new_label()

draw_line(i, pivot, col) =>
    if array.size(arr_time) > 1
        array.push(lines, line.new(array.get(arr_time, i), array.get(pivot, i), array.get(arr_time, i + 1), array.get(pivot, i), color=col, xloc=xloc.bar_time))

draw_label(i, y, txt, txt_color) =>
    if show_labels
        offset = '‏  ‏  ‏  ‏  ‏'
        labels_align_str_left= position_labels == "Left" ? txt + offset : offset + txt 
        x = position_labels == "Left" ? array.get(arr_time, i) : array.get(arr_time, i + 1)
        array.push(labels, label.new(x = x, y=y, text=labels_align_str_left, textcolor=txt_color, style=label.style_label_center, color=#00000000, xloc=xloc.bar_time))
        
traditional() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close) / 3
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_Median * 2 - pivotX_prev_low)
    array.push(s1, pivotX_Median * 2 - pivotX_prev_high)
    array.push(r2, pivotX_Median + 1 * (pivotX_prev_high - pivotX_prev_low))
    array.push(s2, pivotX_Median - 1 * (pivotX_prev_high - pivotX_prev_low))
    array.push(r3, pivotX_Median * 2 + (pivotX_prev_high - 2 * pivotX_prev_low))
    array.push(s3, pivotX_Median * 2 - (2 * pivotX_prev_high - pivotX_prev_low))
    array.push(r4, pivotX_Median * 3 + (pivotX_prev_high - 3 * pivotX_prev_low))
    array.push(s4, pivotX_Median * 3 - (3 * pivotX_prev_high - pivotX_prev_low))
    array.push(r5, pivotX_Median * 4 + (pivotX_prev_high - 4 * pivotX_prev_low))
    array.push(s5, pivotX_Median * 4 - (4 * pivotX_prev_high - pivotX_prev_low))

fibonacci() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close) / 3
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_Median + 0.382 * pivot_range)
    array.push(s1, pivotX_Median - 0.382 * pivot_range)
    array.push(r2, pivotX_Median + 0.618 * pivot_range)
    array.push(s2, pivotX_Median - 0.618 * pivot_range)
    array.push(r3, pivotX_Median + 1 * pivot_range)
    array.push(s3, pivotX_Median - 1 * pivot_range)

woodie() =>
    pivotX_Woodie_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_open * 2)/4
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Woodie_Median)
    array.push(r1, pivotX_Woodie_Median * 2 - pivotX_prev_low)
    array.push(s1, pivotX_Woodie_Median * 2 - pivotX_prev_high)
    array.push(r2, pivotX_Woodie_Median + 1 * pivot_range)
    array.push(s2, pivotX_Woodie_Median - 1 * pivot_range)
    
    pivot_point_r3 = pivotX_prev_high + 2 * (pivotX_Woodie_Median - pivotX_prev_low)
    pivot_point_s3 = pivotX_prev_low - 2 * (pivotX_prev_high - pivotX_Woodie_Median)
    array.push(r3, pivot_point_r3)
    array.push(s3, pivot_point_s3)
    array.push(r4, pivot_point_r3 + pivot_range)
    array.push(s4, pivot_point_s3 - pivot_range)

classic() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close)/3
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_Median * 2 - pivotX_prev_low)
    array.push(s1, pivotX_Median * 2 - pivotX_prev_high)
    array.push(r2, pivotX_Median + 1 * pivot_range)
    array.push(s2, pivotX_Median - 1 * pivot_range)
    array.push(r3, pivotX_Median + 2 * pivot_range)
    array.push(s3, pivotX_Median - 2 * pivot_range)
    array.push(r4, pivotX_Median + 3 * pivot_range)
    array.push(s4, pivotX_Median - 3 * pivot_range)

demark() =>
    pivotX_Demark_X = pivotX_prev_high + pivotX_prev_low * 2 + pivotX_prev_close
    if pivotX_prev_close == pivotX_prev_open
        pivotX_Demark_X := pivotX_prev_high + pivotX_prev_low + pivotX_prev_close * 2
    if pivotX_prev_close > pivotX_prev_open
        pivotX_Demark_X := pivotX_prev_high * 2 + pivotX_prev_low + pivotX_prev_close
    array.push(p, pivotX_Demark_X / 4)
    array.push(r1, pivotX_Demark_X / 2 - pivotX_prev_low)
    array.push(s1, pivotX_Demark_X / 2 - pivotX_prev_high)
    
camarilla() =>
    pivotX_Median = (pivotX_prev_high + pivotX_prev_low + pivotX_prev_close) / 3
    pivot_range = pivotX_prev_high - pivotX_prev_low
    array.push(p, pivotX_Median)
    array.push(r1, pivotX_prev_close + pivot_range * 1.1 / 12.0)
    array.push(s1, pivotX_prev_close - pivot_range * 1.1 / 12.0)
    array.push(r2, pivotX_prev_close + pivot_range * 1.1 / 6.0)
    array.push(s2, pivotX_prev_close - pivot_range * 1.1 / 6.0)
    array.push(r3, pivotX_prev_close + pivot_range * 1.1 / 4.0)
    array.push(s3, pivotX_prev_close - pivot_range * 1.1 / 4.0)
    array.push(r4, pivotX_prev_close + pivot_range * 1.1 / 2.0)
    array.push(s4, pivotX_prev_close - pivot_range * 1.1 / 2.0)

resolution = get_pivot_resolution()

[sec_open, sec_high, sec_low, sec_close] = security(syminfo.tickerid, resolution, [open, high, low, close], lookahead = barmerge.lookahead_on)
sec_open_gaps_on = security(syminfo.tickerid, resolution, open, gaps = barmerge.gaps_on, lookahead = barmerge.lookahead_on)




var number_of_years = 0
is_change_years = false
var custom_years_resolution = pivot_time_frame == BIYEARLY or pivot_time_frame == TRIYEARLY or pivot_time_frame == QUINQUENNIALLY or pivot_time_frame == DECENNIALLY
if  custom_years_resolution and change(time(resolution))
    number_of_years += 1
    if pivot_time_frame == BIYEARLY and number_of_years % 2 == 0
        is_change_years := true
        number_of_years := 0
    else if pivot_time_frame == TRIYEARLY and number_of_years % 3 == 0
        is_change_years := true
        number_of_years := 0
    else if pivot_time_frame == QUINQUENNIALLY and number_of_years % 5 == 0
        is_change_years := true
        number_of_years := 0
    else if pivot_time_frame == DECENNIALLY and number_of_years % 10 == 0
        is_change_years := true
        number_of_years := 0

var is_change = false
var uses_current_bar = timeframe.isintraday and kind == WOODIE  
var change_time = int(na)
is_time_change = (change(time(resolution)) and not custom_years_resolution) or is_change_years
if is_time_change
    change_time := time


if (not uses_current_bar and is_time_change) or (uses_current_bar and not na(sec_open_gaps_on))
    if is_daily_based
        pivotX_prev_open := sec_open[1]
        pivotX_prev_high := sec_high[1]
        pivotX_prev_low := sec_low[1]
        pivotX_prev_close := sec_close[1]
        pivotX_open := sec_open
        pivotX_high := sec_high
        pivotX_low := sec_low
    else
        pivotX_prev_high := pivotX_high
        pivotX_prev_low := pivotX_low
        pivotX_prev_open := pivotX_open
        pivotX_open := open
        pivotX_high := high
        pivotX_low := low
        pivotX_prev_close := close[1]
    
    if barstate.islast and not is_change and  array.size(arr_time) > 0 
        array.set(arr_time, array.size(arr_time) - 1, change_time)
    else
        array.push(arr_time, change_time)
    
    if kind == TRADITIONAL
        traditional()
    else if kind == FIBONACCI
        fibonacci()
    else if kind == WOODIE
        woodie()
    else if kind == CLASSIC
        classic()
    else if kind == DEMARK
        demark()
    else if kind == CAMARILLA
        camarilla()
    
    if array.size(arr_time) > look_back
        if array.size(arr_time) > 0
            array.shift(arr_time)
        if array.size(p) > 0 and p_show
            array.shift(p)
        if array.size(r1) > 0 and s1r1_show
            array.shift(r1)
        if array.size(s1) > 0 and s1r1_show
            array.shift(s1)
        if array.size(r2) > 0 and s2r2_show
            array.shift(r2)
        if array.size(s2) > 0 and s2r2_show
            array.shift(s2)
        if array.size(r3) > 0 and s3r3_show
            array.shift(r3)
        if array.size(s3) > 0 and s3r3_show
            array.shift(s3)
        if array.size(r4) > 0 and s4r4_show
            array.shift(r4)
        if array.size(s4) > 0 and s4r4_show
            array.shift(s4)
        if array.size(r5) > 0 and s5r5_show
            array.shift(r5)
        if array.size(s5) > 0 and s5r5_show
            array.shift(s5)
    is_change := true
else
    if is_daily_based
        pivotX_high := max(pivotX_high, sec_high)
        pivotX_low := min(pivotX_low, sec_low)
    else
        pivotX_high := max(pivotX_high, high)
        pivotX_low := min(pivotX_low, low)

if barstate.islast and array.size(arr_time) > 0 and is_change
    is_change := false
    if array.size(arr_time) > 2 and custom_years_resolution
        last_pivot_time = array.get(arr_time, array.size(arr_time) - 1)
        prev_pivot_time = array.get(arr_time, array.size(arr_time) - 2)
        estimate_pivot_time = last_pivot_time - prev_pivot_time
        array.push(arr_time, last_pivot_time + estimate_pivot_time)
    else 
        array.push(arr_time, time_close(resolution))
        
    for i = 0 to array.size(lines) - 1
        if array.size(lines) > 0 
            line.delete(array.shift(lines))
        if array.size(lines) > 0
            label.delete(array.shift(labels))
    
    for i = 0 to array.size(arr_time) - 2
        if array.size(p) > 0 and p_show
            draw_line(i, p, p_color)
            draw_label(i, array.get(p, i), "P", p_color)
        if array.size(r1) > 0 and s1r1_show
            draw_line(i, r1, s1r1_color)
            draw_label(i, array.get(r1, i), "R1", s1r1_color)
        if array.size(s1) > 0 and s1r1_show
            draw_line(i, s1, s1r1_color)
            draw_label(i, array.get(s1, i), "S1", s1r1_color)
        if array.size(r2) > 0 and s2r2_show
            draw_line(i, r2, s2r2_color)
            draw_label(i, array.get(r2, i), "R2", s2r2_color)
        if array.size(s2) > 0 and s2r2_show
            draw_line(i, s2, s2r2_color)
            draw_label(i, array.get(s2, i), "S2", s2r2_color)
        if array.size(r3) > 0 and s3r3_show
            draw_line(i, r3, s3r3_color)
            draw_label(i, array.get(r3, i), "R3", s3r3_color)
        if array.size(s3) > 0 and s3r3_show
            draw_line(i, s3, s3r3_color)
            draw_label(i, array.get(s3, i), "S3", s3r3_color)
        if array.size(r4) > 0 and s4r4_show
            draw_line(i, r4, s4r4_color)
            draw_label(i, array.get(r4, i), "R4", s4r4_color)
        if array.size(s4) > 0 and s4r4_show
            draw_line(i, s4, s4r4_color)
            draw_label(i, array.get(s4, i), "S4", s4r4_color)
        if array.size(r5) > 0 and s5r5_show
            draw_line(i, r5, s5r5_color)
            draw_label(i, array.get(r5, i), "R5", s5r5_color)
        if array.size(s5) > 0 and s5r5_show
            draw_line(i, s5, s5r5_color)
            draw_label(i, array.get(s5, i), "S5", s5r5_color)


show_m_cam = input(title="Show M Camarilla", type=input.bool, defval=false, inline = "Camarilla")
res = input(title="Resolution", type=input.resolution, defval="12M")
width = input(1, minval=1)
xHigh  = security(syminfo.tickerid,res, high)
xLow   = security(syminfo.tickerid,res, low)
xClose = security(syminfo.tickerid,res, close)
H4 = (0.55*(xHigh-xLow)) + xClose
H3 = (0.275*(xHigh-xLow)) + xClose
H2 = (0.183*(xHigh-xLow)) + xClose
H1 = (0.0916*(xHigh-xLow)) + xClose
L1 = xClose - (0.0916*(xHigh-xLow))
L2 = xClose - (0.183*(xHigh-xLow))
L3 = xClose - (0.275*(xHigh-xLow))
L4 = xClose - (0.55*(xHigh-xLow))
plot(show_m_cam?H2[1]:na, color=#ff002a, title="H2", style = plot.style_circles, linewidth = width)
plot(show_m_cam?H3[1]:na, color=#ff014a, title="H3", style = plot.style_circles, linewidth = width)
plot(show_m_cam?H4[1]:na, color=#ff014a, title="H4", style = plot.style_circles, linewidth = width)
plot(show_m_cam?L2[1]:na, color=#006F00, title="L2", style = plot.style_circles, linewidth = width)
plot(show_m_cam?L3[1]:na, color=#004900, title="L3", style = plot.style_circles, linewidth = width)
plot(show_m_cam?L4[1]:na, color=#004900, title="L4", style = plot.style_circles, linewidth = width)


// study("Previous Days High & Low", shorttitle="PDHL", overlay=true)
days = input(1, "Days", minval=1, tooltip="Number of days previous to read from.")
lo_src = input(low, "Low", group="Sources", tooltip="The source of the low value.\nDefaults to the low of the bars but could be changed to close (for example).")
hi_src = input(high, "High", group="Sources", tooltip="The source of the high value.\nDefaults to the high of the bars but could be changed to close (for example).")
useClose = input(false, "Use close for alerts", group="Sources", tooltip="When true, will use the close value instead of the high / low values to trigger alerts.")

var los = array.new_float()
var his = array.new_float()
var datePrev = 0

lo = lo_src[0]
hi = hi_src[0]
var L_n = lo
var H_n = hi
var L_d = lo
var H_d = hi
var float L = na
var float H = na

date = time('D')
newDay = date!=datePrev

if(datePrev!=0 and newDay)
    if(array.size(los)==days)
        array.shift(los)
    if(array.size(his)==days)
        array.shift(his)
    array.push(los,L_d)
    array.push(his,H_d)
    L_n := lo
    H_n := hi
    los_s = array.size(los)
    if(los_s>1)
        for i = 1 to los_s-1
            v = array.get(los,i)
            if(v<L_n)
                L_n := v
    his_s = array.size(his)     
    if(his_s>1)
        for i = 1 to his_s-1
            v = array.get(his,i)
            if(v>H_n)
                H_n := v
    L_d := lo
    H_d := hi
    L := array.min(los)
    H := array.max(his)
else
    if(hi>H_d)
        H_d := hi
    if(lo<L_d)
        L_d := lo
    if(hi>H_n)
        H_n := hi
    if(lo<L_n)
        L_n := lo        

datePrev := date
    
plot(L, "Low", color=color.red, style=plot.style_circles)
plot(H, "High", color=color.lime, style=plot.style_circles)

//EMA
PlotEMA = input(title = "Plot EMA?", type=input.bool, defval=true)
EMALength = input(title="EMA Length", type=input.integer, defval=200)
EMASource = input(title="EMA Source", type=input.source, defval=close)
EMAvg = ema (EMASource, EMALength)
plot(PlotEMA ? EMAvg : na,  color= color.red, title="EMA")

PlotEMA2 = input(title = "Plot EMA?", type=input.bool, defval=true)
EMALength2 = input(title="EMA Length", type=input.integer, defval=50)
EMASource2 = input(title="EMA Source", type=input.source, defval=close)
EMAvg2 = ema (EMASource2, EMALength2)
plot(PlotEMA2 ? EMAvg2 : na,  color= color.red, title="EMA")

//EMA block ploting usind default 200 and 50
PlotBand = input(title = "Plot BAND?", type=input.bool, defval=true)
col = EMAvg > EMAvg2 ? color.red : EMAvg < EMAvg2 ? color.lime : color.yellow
p1 = plot(EMAvg, title="Slow MA", linewidth=2,  color=col)
p2 = plot(EMAvg2, title="Slow MA",  linewidth=2,color=col)
fill(p1, p2, color=color.silver, transp=50)


//Bollinger band 
mult = input(2.0, type=input.float, minval=0.001, maxval=50, title="StdDev")

EMALength11 = input(title="EMA Length", type=input.integer, defval=20)
EMASource11 = input(title="EMA Source", type=input.source, defval=close)
basis = ema(EMASource11, EMALength11)

dev = mult * stdev(EMASource11, EMALength11)
upper = basis + dev
lower = basis - dev

offset = input(title="Offset", type=input.integer, defval=0, minval=-500, maxval=500)
PlotBB = input(title = "Plot BB?", type=input.bool, defval=true)
plot(PlotBB?basis:na, title="Basis", color=color.blue, offset=offset)
bb1 = plot(PlotBB?upper:na , title="Upper", color=color.red, offset=offset)
bb2 = plot(PlotBB?lower:na, title="Lower", color=color.green, offset=offset)
fill(bb1,bb2, title="Background", color=color.rgb(33, 150, 243, 95))