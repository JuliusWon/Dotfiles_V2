syntax match rsFancyOperator "!=" conceal cchar=≠
syntax match rsFancyOperator "<=" conceal cchar=≤
syntax match rsFancyOperator ">=" conceal cchar=≥
syntax match rsFancyOperator "<<" conceal cchar=«
syntax match rsFancyOperator ">>" conceal cchar=»
syntax match rsFancyOperator "::" conceal cchar=∷
syntax match rsFancyOperator "->" conceal cchar=→
syntax match rsFancyOperator "=>" conceal cchar=⇒
syntax match rsFancyOperator "sqrt" conceal cchar=√
syntax match rsFancyOperator "pi" conceal cchar=π
syntax match rsFancyOperator "||" conceal cchar=∥


hi! link rsFancyOperator Operator
hi! link Conceal Operator

setlocal conceallevel=1
