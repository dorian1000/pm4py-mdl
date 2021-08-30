
import custom_package_importer
custom_package_importer.apply()

from pm4pymdl.objects.mdl.importer import importer as mdl_importer
from pm4pymdl.algo.mvp.get_logs_and_replay import algorithm as discovery_factory
from pm4pymdl.visualization.petrinet import visualizer as pn_vis_factory

import numpy as np


format = "svg"

#df = mdl_importer.apply("example_logs/mdl/log_sample_cluster_0.csv")

#df = mdl_importer.apply("example_logs\mdl\old\log_sample_v3_C_short.mdl")
df = mdl_importer.apply("example_logs\mdl\log_createRefernce_WF_OfficeActions.csv")
#df = mdl_importer.apply("example_logs\mdl\log_sample_cluster_1.csv")

model = discovery_factory.apply(df)

gviz = pn_vis_factory.apply(model, parameters={"format": format})

# create filename with involved objectTypes
write_path = "output_nets"
suffix = '_'.join(list(model["nets"].keys())) 
suffix = suffix + '.gv' + "." + format
filename = write_path + "\\" + suffix

pn_vis_factory.save(gviz, filename)

pn_vis_factory.view(gviz)