from paraview.simple import *

model_path = r'C:\Users\Abajinn1\opm-data\norne\NORNE_PORTFOLIO.e'
output_path = r'C:\Users\Abajinn1\Documents\GitHub\paraview-portfolio\assets\project1-norne\p1-test-poro.png'

reader = OpenDataFile(model_path)
view = GetActiveViewOrCreate('RenderView')
Show(reader, view)
ColorBy(GetDisplayProperties(reader, view), ('CELLS', 'poro'))
reader.UpdatePipeline()

view.ResetCamera()
Render()
SaveScreenshot(output_path, view, ImageResolution=[2200, 1200])
