from circuits_pb import *
import sys
import os

def writeCOMM(numBits, greater_than=True, only_tvars=False, t_equals=True):
    # Map from columns to the constraints on those columns.
    # We will fill col_constraints with the full set of constraints.
    # Constraints in column -1 will always be included.
    col_constraints = {}
    for i in range(-1,2*numBits+2):
        col_constraints[i] = []

    # Choose filename based on settings
    keyFileName = "benchmarks/%darraycomm" % (numBits)
    opbFileName = "benchmarks/%darraycomm" % (numBits)
    if greater_than:
        keyFileName += "_greater"
        opbFileName += "_greater"
    else:
        keyFileName += "_less"
        opbFileName += "_less"
    if t_equals:
        keyFileName += "_teq"
        opbFileName += "_teq"
    if only_tvars:
        keyFileName += "_tvars"
        opbFileName += "_tvars"
    keyFileName += ".key"
    opbFileName += ".opb"

    f_key = open(keyFileName,'w')
    f_opb = open(opbFileName,'w')
        
    nextDIMACS = 1

    if not only_tvars:
        x, nextDIMACS = createBITVECTOR(nextDIMACS,f_key,'x',numBits)
        y, nextDIMACS = createBITVECTOR(nextDIMACS,f_key,'y',numBits)
        
    txy, nextDIMACS = createGRID_VARIABLES(nextDIMACS,f_key,"txy",numBits,numBits)
    tyx, nextDIMACS = createGRID_VARIABLES(nextDIMACS,f_key,"tyx",numBits,numBits)       
    cxy, nextDIMACS = createGRID_VARIABLES(nextDIMACS,f_key,"cxy",numBits,numBits)
    cyx, nextDIMACS = createGRID_VARIABLES(nextDIMACS,f_key,"cyx",numBits,numBits)
    dxy, nextDIMACS = createGRID_VARIABLES(nextDIMACS,f_key,"dxy",numBits,numBits)
    dyx, nextDIMACS = createGRID_VARIABLES(nextDIMACS,f_key,"dyx",numBits,numBits)

    oyx, nextDIMACS = createBITVECTOR(nextDIMACS,f_key,'oyx',2*numBits)
    oxy, nextDIMACS = createBITVECTOR(nextDIMACS,f_key,'oxy',2*numBits)

    if not only_tvars:
        writeARRAYMULT(col_constraints, x,y,cxy,dxy,txy,oxy,numBits)
        writeARRAYMULT(col_constraints, y,x,cyx,dyx,tyx,oyx,numBits)
    else:
        writeARRAYSUM(col_constraints,cxy,dxy,txy,oxy,numBits)
        writeARRAYSUM(col_constraints,cyx,dyx,tyx,oyx,numBits)

    # Write t-equalities
    if t_equals:
        for i in range(numBits):
            for j in range(numBits):
                writeEQUAL(col_constraints, i+j, txy[(i,j)], tyx[(j,i)])

    if greater_than:
        # inequality xy > yx
        writeBIGGER_NUMBER(col_constraints,0,oxy,oyx,2*numBits)
    else:
        # inequality xy < yx
        writeSMALLER_NUMBER(col_constraints,0,oxy,oyx,2*numBits)

    # Write all constraints to file
    writeHEADER(f_opb, nextDIMACS, col_constraints)
    for col in range(-1,2*numBits+2):
        for clause in col_constraints[col]:
            f_opb.write(clause)
    f_opb.close()

if __name__ == '__main__':
    if not os.path.exists("benchmarks"):
        os.makedirs("benchmarks")
    # Set only_tvars to True to remove xy-variables.
    only_tvars = False
    # Set t_equals to False to turn off preprocessing t-equalities.
    t_equals = True

    numBits = int(sys.argv[1])
    
    writeCOMM(numBits, True, only_tvars, t_equals)
    writeCOMM(numBits, False, only_tvars, t_equals)














    
