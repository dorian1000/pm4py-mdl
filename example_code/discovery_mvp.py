import custom_package_importer  
custom_package_importer.apply()

from pm4pymdl.objects.mdl.importer import importer as mdl_importer
from pm4pymdl.algo.mvp.discovery import algorithm as mvp_disc_factory
from pm4pymdl.visualization.mvp import visualizer as mvp_vis_factory

#df = mdl_importer.apply("example_logs/mdl/order_management.mdl")
#df = mdl_importer.apply("example_logs\mdl\log_createRefernce_WF_checkRequest.csv")
df = mdl_importer.apply("example_logs\mdl\log_createRefernce_WF_OfficeActions.csv")

model = mvp_disc_factory.apply(df)
gviz = mvp_vis_factory.apply(model, parameters={"format": "svg"})
mvp_vis_factory.view(gviz)
