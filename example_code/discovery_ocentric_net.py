import os 
print("os: ",os.getcwd())

import sys
sys.path.append(os.getcwd())
print("sys:",r"\n".join(sys.path))


from pm4pymdl.objects.mdl.importer import importer as mdl_importer
from pm4pymdl.algo.mvp.get_logs_and_replay import algorithm as discovery_factory
from pm4pymdl.visualization.petrinet import visualizer as pn_vis_factory

import numpy as np


for i in np.arange(0,11,1):

    #df = mdl_importer.apply("example_logs/mdl/order_management.mdl")
    df = mdl_importer.apply("example_logs/mdl/log_createRefernce_custom_" + str(i) + ".csv")

    model = discovery_factory.apply(df)
    gviz = pn_vis_factory.apply(model, parameters={"format": "png"})
    pn_vis_factory.view(gviz)
    break
