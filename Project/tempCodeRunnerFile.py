chart = ScatterChart()

xvalues = Reference(sheet, min_col = switch_for_chart(location_for_name), min_row = 2, max_row = (counter + 1))

yvalues = Reference(sheet, min_col = switch_for_chart(location_for_score), min_row = 2, max_row = (counter + 1))

series = Series(values = yvalues, xvalues = xvalues, title = "2019 중간고사 성적")

chart.series.append(series)

chart.title = "Number Theory 2019 Middle Term"

chart.x_axis.title = "학생 이름"

chart.y_axis.title = "학생 성적"

sheet.add_chart(chart, "E36")

num.save("num.xlsx")
