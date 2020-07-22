import r2pipe
import sys

f = open(f'extracted_script{sys.argv[1]}.js', 'w')
r2 = r2pipe.open(sys.argv[1])
r2.cmd('aaa')
ref = r2.cmdj('axtj @ str.var_config')
func = ref[0]['fcn_addr']
data_refs = r2.cmdj(f'afxj @ {func}')
for data in data_refs:
    if data['type'] == 'data':
        loc = data['to']
        print(loc)
        try:
            string = r2.cmdj(f'pfjz @ {loc}')
            print(string[0]['value'])
            f.write(string[0]['value'])
        except:
            pass
