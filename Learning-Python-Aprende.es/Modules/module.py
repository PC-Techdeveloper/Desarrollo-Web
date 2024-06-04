# Importando un módulo completo
import stats

print(stats.mean(6, 3, 9, 5))

print(stats.std(6, 3, 9, 5))

# Importando un módulo por partes
from stats import mean

print(mean(7, 9, 3, 5, 6))

# Importando varios objetos en funciones, separados por coma en la misma línea
from stats import mean, std

# Importando usando un alias
from stats import mean as avg

print(avg(6, 3, 9, 5))
