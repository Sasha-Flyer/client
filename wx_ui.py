import platform
import wx
from api import api


class Frame(wx.Frame):
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(
            self, None, size=(400, 250), title='Server Info'
        )
        panel = wx.Panel(self)

        self.RAM = "Использовано памяти {0} из {1} ({2}%)"
        self.CPU = "Процессор занят на {0}%"
        self.SSD = "ssd занят на {0}%"
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        size = (20, -1)

        self.RAM_text = wx.StaticText(panel, label= self.RAM)
        main_sizer.Add(self.RAM_text, 0, wx.ALL, 5)
        self.RAM_ui = wx.Gauge(panel)
        main_sizer.Add(self.RAM_ui)
        self.CPU_text = wx.StaticText(panel, label=self.CPU)
        main_sizer.Add(self.CPU_text, 0, wx.ALL, 5)
        self.CPU_ui = wx.Gauge(panel)
        main_sizer.Add(self.CPU_ui)
        self.SSD_text = wx.StaticText(panel, label=self.SSD)
        main_sizer.Add(self.SSD_text, 0, wx.ALL, 5)
        self.SSD_ui = wx.Gauge(panel)
        main_sizer.Add(self.SSD_ui)
        panel.SetSizer(main_sizer)
        api.connect(self.slot)
        self.Show()

    def slot(self, args):
        used = args['used_memory']
        total = args['total_memory']
        percent = int(used * 100 / total)
        self.RAM_text.SetLabel(self.RAM.format(used, total, percent))
        self.RAM_ui.SetValue(percent)
        percent = int(args['cpu_usage'])
        self.CPU_text.SetLabel(self.CPU.format(percent))
        self.CPU_ui.SetValue(percent)
        percent = int(args['ssd_usage'])
        self.SSD_text.SetLabel(self.SSD.format(percent))
        self.SSD_ui.SetValue(percent)


def main_wx():
    app = wx.App(False)
    frame = Frame()
    app.MainLoop()