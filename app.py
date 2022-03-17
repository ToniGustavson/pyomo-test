import streamlit as st
import pyomo.environ as pyo
import pyomo.opt as opt

model = pyo.ConcreteModel()

model.x = pyo.Var([1,2], domain=pyo.NonNegativeReals)

model.OBJ = pyo.Objective(expr = 2*model.x[1] + 3*model.x[2])

model.Constraint1 = pyo.Constraint(expr = 3*model.x[1] + 4*model.x[2] >= 1)

st.write(type(model))


solver = "glpk"
optimizer = opt.SolverFactory(solver)
solver_info = optimizer.solve(model, tee=True)
st.write(type(solver_info))
