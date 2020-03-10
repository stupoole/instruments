import instruments
import time

sb = instruments.SwitchBox()
pg = instruments.K2461()
sb.connect(4)
pg.connect()

# bb = instruments.BalanceBox()
# bb.connect(5)
# bb.enable_all()
# bb.reset_resistances()

ass1 = {"I+": "A", "I-": "E", "V1+": "B", "V1-": "D"}
ass2 = {"I+": "B", "I-": "F", "V1+": "C", "V1-": "E"}
ass3 = {"I+": "C", "I-": "G", "V1+": "D", "V1-": "F"}
ass4 = {"I+": "D", "I-": "H", "V1+": "E", "V1-": "G"}
ass5 = {"I+": "E", "I-": "A", "V1+": "F", "V1-": "H"}
ass6 = {"I+": "F", "I-": "B", "V1+": "G", "V1-": "A"}
ass7 = {"I+": "G", "I-": "C", "V1+": "H", "V1-": "B"}
ass8 = {"I+": "H", "I-": "D", "V1+": "A", "V1-": "C"}

R = [0, 0, 0, 0, 0, 0, 0, 0]

sb.switch(ass1)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[0] = v / c
pg.disable_probe_current()

sb.switch(ass2)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[1] = v / c
pg.disable_probe_current()

sb.switch(ass3)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[2] = v / c
pg.disable_probe_current()

sb.switch(ass4)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[3] = v / c
pg.disable_probe_current()

sb.switch(ass5)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[4] = v / c
pg.disable_probe_current()

sb.switch(ass6)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[5] = v / c
pg.disable_probe_current()

sb.switch(ass7)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[6] = v / c
pg.disable_probe_current()

sb.switch(ass8)
time.sleep(1)
pg.enable_4_wire_probe(1e-3)
time.sleep(1)
c, v = pg.read_one()
R[7] = v / c

print('Resistances: \n', R)
pg.disable_probe_current()
