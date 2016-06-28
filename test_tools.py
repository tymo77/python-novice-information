#tests the functionality of analyze_csv
import tools
assert(tools.analyze_csv('tests\\zeroes.csv')==[0.0,0.0,0.0])
assert(tools.analyze_csv('tests\\ones.csv')==[1.0,1.0,0.0])
