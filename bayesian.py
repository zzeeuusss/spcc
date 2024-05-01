from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

model = BayesianModel([('Cloudy', 'Sprinkler'),
                       ('Cloudy', 'Rain'),
                       ('Sprinkler', 'WetGrass'),
                       ('Rain', 'WetGrass')])

cpd_cloudy = TabularCPD(variable='Cloudy', variable_card=2, values=[[0.5], [0.5]])
cpd_sprinkler = TabularCPD(variable='Sprinkler', variable_card=2,
                            values=[[0.1, 0.5], [0.9, 0.5]],
                            evidence=['Cloudy'], evidence_card=[2])
cpd_rain = TabularCPD(variable='Rain', variable_card=2,
                      values=[[0.8, 0.2], [0.2, 0.8]],
                      evidence=['Cloudy'], evidence_card=[2])
cpd_wetgrass = TabularCPD(variable='WetGrass', variable_card=2,
                          values=[[0.99, 0.9, 0.9, 0.01],
                                  [0.01, 0.1, 0.1, 0.99]],
                          evidence=['Sprinkler', 'Rain'],
                          evidence_card=[2, 2])

model.add_cpds(cpd_cloudy, cpd_sprinkler, cpd_rain, cpd_wetgrass)

assert model.check_model()

print("CPD for Cloudy:")
print(cpd_cloudy)
print("\nCPD for Sprinkler:")
print(cpd_sprinkler)
print("\nCPD for Rain:")
print(cpd_rain)
print("\nCPD for WetGrass:")
print(cpd_wetgrass)
