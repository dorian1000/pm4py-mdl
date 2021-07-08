import custom_package_importer  
custom_package_importer.apply()

from pm4pymdl.objects.mdl.importer import importer as mdl_importer
from pm4pymdl.algo.mvp.gen_framework3 import discovery, conformance
from pm4pymdl.visualization.mvp.gen_framework3 import visualizer as visualizer

#dataframe = mdl_importer.apply("example_logs/mdl/o2c_red.mdl")
dataframe = mdl_importer.apply("example_logs/mdl/log_createRefernce_custom_0.csv")
model = discovery.apply(dataframe, parameters={"epsilon": 0.1, "noise_threshold": 0.1})
conf_result = conformance.apply(dataframe, model)
fitness = len([x for x in conf_result if len(x) == 0]) / len(conf_result)
print(fitness)
gviz = visualizer.apply(model, parameters={"min_act_freq": 0, "min_edge_freq": 0})
visualizer.view(gviz)
for el in conf_result:
    if el:
        print(el)