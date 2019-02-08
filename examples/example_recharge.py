"""
This test file is meant for developing purposes, providing an easy method to
test the functioning of Pastas recharge module during development.

Author: R.A. Collenteur, University of Graz.

"""
import pastas as ps
from pastas.stressmodels import Recharge

# read observations
obs = ps.read_dino('data/B58C0698001_1.csv')

# Create the time series model
ml = ps.Model(obs, name="groundwater head")

# read weather data
rain = ps.read_knmi('data/neerslaggeg_HEIBLOEM-L_967-2.txt', variables='RD')
evap = ps.read_knmi('data/etmgeg_380.txt', variables='EV24')

# Create stress
sm = Recharge(prec=rain, evap=evap, rfunc=ps.Exponential,
              recharge="Linear", name='recharge')
ml.add_stressmodel(sm)

## Solve
ml.solve()
ml.plot()