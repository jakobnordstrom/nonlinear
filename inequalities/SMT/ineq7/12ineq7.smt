(set-logic QF_BV)

(declare-const x (_ BitVec 24))
(declare-const x_temp (_ BitVec 12))
(assert (= x ((_ zero_extend 12) x_temp)))

(declare-const k (_ BitVec 24))
(declare-const k_temp (_ BitVec 12))
(assert (= k_temp #b101010101010))
(assert (= k ((_ zero_extend 12) k_temp)))

(declare-const xok (_ BitVec 24))
(assert (= xok (bvor x k)))

(declare-const z (_ BitVec 24))
(declare-const z_temp (_ BitVec 12))
(assert (= z ((_ zero_extend 12) z_temp)))

(declare-const xok_z (_ BitVec 24))
(declare-const kz (_ BitVec 24))
(assert (= xok_z (bvmul xok z)))
(assert (= kz (bvmul k z)))

(assert (bvult xok_z kz))
(check-sat)
