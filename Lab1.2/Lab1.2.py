
from matplotlib import pyplot
from openpyxl import load_workbook

def getvalue(x):
    return x.value
wb = load_workbook("data_analysis_lab.xlsx")
sheet = wb["Data"]


Years = list(map(getvalue,sheet['A'][1:]))
Temperature = list(map(getvalue,sheet['C'][1:]))
Activity = list(map(getvalue, sheet['D'][1:]))


pyplot.plot(Years,Temperature,label="Относит. Температура")
pyplot.plot(Years,Activity,label="Активность Солнца")
pyplot.show()