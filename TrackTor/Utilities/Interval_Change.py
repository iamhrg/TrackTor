"""
**Module Overview:**

This module will implement the funtionality of showing Intervals for the Graphs

|- _Interval_Change
    - __init__: This function will initialize UI object and other class variables in all files
    - Uploads: This function will implement the functinality of showing interval for uploads
    - Downloads: This function will implement the functinality of showing interval for downloads
    - Inbound: This function will implement the functinality of showing interval for Inbound connections
    - Outbound: This function will implement the functinality of showing interval for Inbound connections

"""

Downloads_Interval = 1000
Uploads_Interval = 1000
Inbound_Interval = 1000
Outbound_Interval = 1000

class _Interval_Change():
    def __init__(self, ui):
        self.ui = ui

    #Function performing change in the Uploads_Interval
    def Uploads(self):
        str = "Refreshing every "
        global Uploads_Interval
        if (self.ui.Uploads_Interval.currentText() == "Secondly"):
            Uploads_Interval = 1000
            str = str + "Second"
        elif (self.ui.Uploads_Interval.currentText() == "5 Secs"):
            Uploads_Interval = 5000
            str = str + "5 Seconds"
        elif (self.ui.Uploads_Interval.currentText() == "10 Secs"):
            Uploads_Interval = 10000
            str = str + "10 Seconds"
        elif (self.ui.Uploads_Interval.currentText() == "30 Secs"):
            Uploads_Interval = 30000
            str = str + "30 Seconds"
        elif (self.ui.Uploads_Interval.currentText() == "Minutely"):
            Uploads_Interval = 60000
            str = str + "Minute"
        elif (self.ui.Uploads_Interval.currentText() == "5 Mins"):
            Uploads_Interval = 300000
            str = str + "5 Minutes"
        elif (self.ui.Uploads_Interval.currentText() == "10 Mins"):
            Uploads_Interval = 600000
            str = str + "10 Minutes"
        elif (self.ui.Uploads_Interval.currentText() == "30 Mins"):
            Uploads_Interval = 1800000
            str = str + "30 Minutes"
        elif (self.ui.Uploads_Interval.currentText() == "Hourly"):
            Uploads_Interval = 3600000
            str = "Refreshing Hourly"
        elif (self.ui.Uploads_Interval.currentText() == "Daily"):
            Uploads_Interval = 86400000
            str = "Refreshing Daily"
        self.ui.Uploads.setLabel('bottom', str)
        self.ui.uploads_timer.timeout.connect(self.ui.ds.Uploads)
        self.ui.uploads_timer.start(Uploads_Interval)

    #Function performing change in the Downloads_Interval
    def Downloads(self):
        global Downloads_Interval
        str = "Refreshing every "
        if (self.ui.Downloads_Interval.currentText() == "Secondly"):
            Downloads_Interval = 1000
            str = str + "Second"
        elif (self.ui.Downloads_Interval.currentText() == "5 Secs"):
            Downloads_Interval = 5000
            str = str + "5 Seconds"
        elif (self.ui.Downloads_Interval.currentText() == "10 Secs"):
            Downloads_Interval = 10000
            str = str + "10 Seconds"
        elif (self.ui.Downloads_Interval.currentText() == "30 Secs"):
            Downloads_Interval = 30000
            str = str + "30 Seconds"
        elif (self.ui.Downloads_Interval.currentText() == "Minutely"):
            Downloads_Interval = 60000
            str = str + "Minute"
        elif (self.ui.Downloads_Interval.currentText() == "5 Mins"):
            Downloads_Interval = 300000
            str = str + "5 Minutes"
        elif (self.ui.Downloads_Interval.currentText() == "10 Mins"):
            Downloads_Interval = 600000
            str = str + "10 Minutes"
        elif (self.ui.Downloads_Interval.currentText() == "30 Mins"):
            Downloads_Interval = 1800000
            str = str + "30 Minutes"
        elif (self.ui.Downloads_Interval.currentText() == "Hourly"):
            Downloads_Interval = 3600000
            str = "Refreshing Hourly"
        elif (self.ui.Downloads_Interval.currentText() == "Daily"):
            Downloads_Interval = 86400000
            str = "Refreshing Daily"
        self.ui.Downloads.setLabel('bottom', str)
        self.ui.downloads_timer.timeout.connect(self.ui.ds.Downloads)
        self.ui.downloads_timer.start(Downloads_Interval)

    #Function performing change in the Outbound_Interval
    def Outbound(self):
        str = "Refreshing every "
        global Outbound_Interval
        if (self.ui.Outbound_Interval.currentText() == "Secondly"):
            Outbound_Interval = 1000
            str = str + "Second"
        elif (self.ui.Outbound_Interval.currentText() == "5 Secs"):
            Outbound_Interval = 5000
            str = str + "5 Seconds"
        elif (self.ui.Outbound_Interval.currentText() == "10 Secs"):
            Outbound_Interval = 10000
            str = str + "10 Seconds"
        elif (self.ui.Outbound_Interval.currentText() == "30 Secs"):
            Outbound_Interval = 30000
            str = str + "30 Seconds"
        elif (self.ui.Outbound_Interval.currentText() == "Minutely"):
            Outbound_Interval = 60000
            str = str + "Minute"
        elif (self.ui.Outbound_Interval.currentText() == "5 Mins"):
            Outbound_Interval = 300000
            str = str + "5 Minutes"
        elif (self.ui.Outbound_Interval.currentText() == "10 Mins"):
            Outbound_Interval = 600000
            str = str + "10 Minutes"
        elif (self.ui.Outbound_Interval.currentText() == "30 Mins"):
            Outbound_Interval = 1800000
            str = str + "30 Minutes"
        elif (self.ui.Outbound_Interval.currentText() == "Hourly"):
            Outbound_Interval = 3600000
            str = "Refreshing Hourly"
        elif (self.ui.Outbound_Interval.currentText() == "Daily"):
            Outbound_Interval = 86400000
            str = "Refreshing Daily"
        self.ui.Outbound.setLabel('bottom', str)
        self.ui.outbound_timer.timeout.connect(self.ui.conn.Outbound)
        self.ui.outbound_timer.start(Outbound_Interval)

    #Function performing change in the Inbound_Interval
    def Inbound(self):
        str = "Refreshing every "
        global Inbound_Interval
        if (self.ui.Inbound_Interval.currentText() == "Secondly"):
            Inbound_Interval = 1000
            str = str + "Second"
        elif (self.ui.Inbound_Interval.currentText() == "5 Secs"):
            Inbound_Interval = 5000
            str = str + "5 Seconds"
        elif (self.ui.Inbound_Interval.currentText() == "10 Secs"):
            Inbound_Interval = 10000
            str = str + "10 Seconds"
        elif (self.ui.Inbound_Interval.currentText() == "30 Secs"):
            Inbound_Interval = 30000
            str = str + "30 Seconds"
        elif (self.ui.Inbound_Interval.currentText() == "Minutely"):
            Inbound_Interval = 60000
            str = str + "Minute"
        elif (self.ui.Inbound_Interval.currentText() == "5 Mins"):
            Inbound_Interval = 300000
            str = str + "5 Minutes"
        elif (self.ui.Inbound_Interval.currentText() == "10 Mins"):
            Inbound_Interval = 600000
            str = str + "10 Minutes"
        elif (self.ui.Inbound_Interval.currentText() == "30 Mins"):
            Inbound_Interval = 1800000
            str = str + "30 Minutes"
        elif (self.ui.Inbound_Interval.currentText() == "Hourly"):
            Inbound_Interval = 3600000
            str = "Refreshing Hourly"
        elif (self.ui.Inbound_Interval.currentText() == "Daily"):
            Inbound_Interval = 86400000
            str = "Refreshing Daily"
        self.ui.Inbound.setLabel('bottom', str)
        self.ui.inbound_timer.timeout.connect(self.ui.conn.Inbound)
        self.ui.inbound_timer.start(Inbound_Interval)
