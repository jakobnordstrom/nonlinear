# Constructs SMT formula to check:
# (x|k)(z+1) >= kz + x
# Where k is ...101010, & is bitwise-AND and | is bitwise-OR.
import sys
import os

def writeINEQ10(numBits):
    smtFileName = "benchmarks/%dineq10.smt" % (numBits)
    f_smt = open(smtFileName,'w')
    f_smt.write("(set-logic QF_BV)\n\n")

    f_smt.write("(declare-const x (_ BitVec %d))\n" % (2*numBits))
    f_smt.write("(declare-const x_temp (_ BitVec %d))\n" % numBits)
    f_smt.write("(assert (= x ((_ zero_extend %d) x_temp)))\n\n" % numBits)

    f_smt.write("(declare-const z (_ BitVec %d))\n" % (2*numBits))
    f_smt.write("(declare-const z_temp (_ BitVec %d))\n" % numBits)
    f_smt.write("(assert (= z ((_ zero_extend %d) z_temp)))\n\n" % numBits)
    
    f_smt.write("(declare-const k (_ BitVec %d))\n" % (2*numBits))
    f_smt.write("(declare-const k_temp (_ BitVec %d))\n" % numBits)
    extra = ""
    if numBits % 2 == 1:
        extra = "0"
    k_temp = extra + "10" * (numBits / 2) 
    f_smt.write("(assert (= k_temp #b%s))\n" % (k_temp))
    f_smt.write("(assert (= k ((_ zero_extend %d) k_temp)))\n\n" % numBits)

    f_smt.write("(declare-const xok (_ BitVec %d))\n" % (2*numBits))
    f_smt.write("(assert (= xok (bvor x k)))\n\n")

    f_smt.write("(declare-const xok_zpl1 (_ BitVec %d))\n" % (2*numBits))
    f_smt.write("(assert (= xok_zpl1 (bvmul xok (bvadd z #b%s))))\n" % (("0" * (2*numBits - 1)) + "1"))

    f_smt.write("(declare-const kz (_ BitVec %d))\n" % (2*numBits))
    f_smt.write("(assert (= kz (bvmul k z)))\n\n")

    f_smt.write("(assert (bvult xok_zpl1 (bvadd kz x)))\n")
    f_smt.write("(check-sat)\n")

if not os.path.exists("benchmarks"):
    os.makedirs("benchmarks")


for i in range(9,37):
    writeINEQ10(i)








    
