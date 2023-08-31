import numpy as np
from vtk import vtkPolyDataReader, vtkPoints, vtkPolyDataWriter
import os
from vtk.numpy_interface import dataset_adapter as dsa




def convertVtk2Np_Poly(vtkFilePath):
    reader = vtkPolyDataReader()
    reader.SetFileName('ExampleDataDingrong/0124-LeftMob_0913-USPlane0/PreOperative/0124_bel_align.vtk')
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()

    PolyData = reader.GetOutput()

    npPoints = dsa.WrapDataObject(PolyData).Points

    points = npPoints

    return points