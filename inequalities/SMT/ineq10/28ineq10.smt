(set-logic QF_BV)

(declare-const x (_ BitVec 56))
(declare-const x_temp (_ BitVec 28))
(assert (= x ((_ zero_extend 28) x_temp)))

(declare-const z (_ BitVec 56))
(declare-const z_temp (_ BitVec 28))
(assert (= z ((_ zero_extend 28) z_temp)))

(declare-const k (_ BitVec 56))
(declare-const k_temp (_ BitVec 28))
(assert (= k_temp #b1010101010101010101010101010))
(assert (= k ((_ zero_extend 28) k_temp)))

(declare-const xok (_ BitVec 56))
(assert (= xok (bvor x k)))

(declare-const xok_zpl1 (_ BitVec 56))
(assert (= xok_zpl1 (bvmul xok (bvadd z #b00000000000000000000000000000000000000000000000000000001))))
(declare-const kz (_ BitVec 56))
(assert (= kz (bvmul k z)))

(assert (bvult xok_zpl1 (bvadd kz x)))
(check-sat)
