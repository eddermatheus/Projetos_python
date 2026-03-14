Siemens = ["S7-1500", "S7-300"]
AllenBradley = ["MicroLogix", "CompactLogix", "ControlLogix"]
SchneiderElectric = ["M221", "M241", "M340", "M580"]
CLPs = [Siemens, AllenBradley, SchneiderElectric]

if "S7-1200" not in CLPs[0]:
 CLPs[0].insert(1,"S7-1200")
 print(CLPs[0])
else:
 print(False)