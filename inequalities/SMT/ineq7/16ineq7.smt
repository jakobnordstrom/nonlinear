(set-logic QF_BV)

(declare-const x (_ BitVec 32))
(declare-const x_temp (_ BitVec 16))
(assert (= x ((_ zero_extend 16) x_temp)))

(declare-const k (_ BitVec 32))
(declare-const k_temp (_ BitVec 16))
(assert (= k_temp #b1010101010101010))
(assert (= k ((_ zero_extend 16) k_temp)))

(declare-const xok (_ BitVec 32))
(assert (= xok (bvor x k)))

(declare-const z (_ BitVec 32))
(declare-const z_temp (_ BitVec 16))
(assert (= z ((_ zero_extend 16) z_temp)))

(declare-const xok_z (_ BitVec 32))
(declare-const kz (_ BitVec 32))
(assert (= xok_z (bvmul xok z)))
(assert (= kz (bvmul k z)))

(assert (bvult xok_z kz))
(check-sat)
