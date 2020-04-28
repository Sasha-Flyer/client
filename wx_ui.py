import platform
import wx
from api import api
from wx.lib.plot import PlotCanvas, PlotGraphics, PolyLine, PolyMarker
import wx.lib.plot as plot
import sys
from copy import copy

zero_history = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)]

def append_history(history, new):
    for i in range(len(history)-1):
        history[i] = (i+1, history[i+1][1])
    history[i+1] = (i+2, new)
    print(history)

class PlotCanvasExample(plot.PlotCanvas):
    def __init__(self, parent, id, size, data = zero_history):
        ''' Initialization routine for the this panel.'''
        plot.PlotCanvas.__init__(self, parent, id, size=size)
        self.data = data
        line = plot.PolyLine(self.data)
        gc = plot.PlotGraphics([line], xLabel="время", yLabel="%")
        self.Draw(gc, )

    def draw(self, data):
        line = plot.PolyLine(data)
        gc = plot.PlotGraphics([line], xLabel="время", yLabel="%")
        self.Draw(gc, )


class Frame(wx.Frame):
    def __init__(self):

        """Constructor"""
        wx.Frame.__init__(
            self, None, size=(1200, 500), title='Server Info'
        )
        panel = wx.Panel(self, id=0)
        self.RAM = "Использовано памяти {0} из {1} ({2}%)"
        self.CPU = "Процессор занят на {0}%"
        self.SSD = "ssd занят на {0}%"
        root_sizer = wx.BoxSizer(wx.HORIZONTAL)
        RAM_sizer = wx.BoxSizer(wx.VERTICAL)
        CPU_sizer = wx.BoxSizer(wx.VERTICAL)
        SSD_sizer = wx.BoxSizer(wx.VERTICAL)
        root_sizer.AddSpacer(10)
        root_sizer.Add(RAM_sizer)
        root_sizer.AddSpacer(100)
        root_sizer.Add(CPU_sizer)
        root_sizer.AddSpacer(100)
        root_sizer.Add(SSD_sizer)
        self.RAM_text = wx.StaticText(panel, label= self.RAM)
        RAM_sizer.Add(self.RAM_text, 0, wx.ALL, 5)
        self.RAM_ui = wx.Gauge(panel, size=wx.Size(300, 20))
        RAM_sizer.Add(self.RAM_ui)
        self.RAM_graph = PlotCanvasExample(panel, 0, wx.Size(300, 186))
        RAM_sizer.Add(self.RAM_graph)
        self.RAM_history = copy(zero_history)

        self.CPU_text = wx.StaticText(panel, label=self.CPU)
        CPU_sizer.Add(self.CPU_text, 0, wx.ALL, 5)
        self.CPU_ui = wx.Gauge(panel, size=wx.Size(300, 20))
        CPU_sizer.Add(self.CPU_ui)
        self.CPU_graph = PlotCanvasExample(panel, 0, wx.Size(300, 186))
        CPU_sizer.Add(self.CPU_graph)
        self.CPU_history = copy(zero_history)

        self.SSD_text = wx.StaticText(panel, label=self.SSD)
        SSD_sizer.Add(self.SSD_text, 0, wx.ALL, 5)
        self.SSD_ui = wx.Gauge(panel, size=wx.Size(300, 20))
        SSD_sizer.Add(self.SSD_ui)
        self.SSD_graph = PlotCanvasExample(panel, 0, wx.Size(300, 186))
        SSD_sizer.Add(self.SSD_graph)
        self.SSD_history = copy(zero_history)

        panel.SetSizer(root_sizer)
        api.connect(self.slot)
        self.Show()

        self.RAM_graph.draw([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0)])
    def slot(self, args):
        print("new")
        used = args['used_memory']
        total = args['total_memory']
        percent = int(used * 100 / total)
        self.RAM_text.SetLabel(self.RAM.format(used, total, percent))
        self.RAM_ui.SetValue(percent)
        append_history(self.RAM_history, percent)
        self.RAM_graph.draw(self.RAM_history)

        percent = int(args['cpu_usage'])
        self.CPU_text.SetLabel(self.CPU.format(percent))
        self.CPU_ui.SetValue(percent)
        append_history(self.CPU_history, percent)
        self.CPU_graph.draw(self.CPU_history)

        percent = int(args['ssd_usage'])
        self.SSD_text.SetLabel(self.SSD.format(percent))
        self.SSD_ui.SetValue(percent)
        append_history(self.SSD_history, percent)
        self.SSD_graph.draw(self.SSD_history)


def main_wx():
    app = wx.App(False)
    frame = Frame()
    app.MainLoop()
    sys.exit()

if __name__ == "__main__":
    main_wx()