from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication

import os
import sys
import requests
import json
from collections import defaultdict




ui_path = os.path.join(
    os.path.dirname(__file__),
    'meteo.ui'
)

FORM_CLASS, _ = uic.loadUiType(ui_path)


class meteoGui(QDialog, FORM_CLASS):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.manage_gui()
        self.station_combo.currentIndexChanged.connect(self.update_sensors)
        self.download_button.clicked.connect(self.download_data)


    
    def manage_gui(self):

        # per le stazioni
        url_stations = 'http://dati.retecivica.bz.it/services/meteo/v1/stations'
        data = requests.get(url_stations).text
        data = json.loads(data)

        self.places_dict = {}
        for i in data['features']:
            self.places_dict[i['properties']['NAME_I']] = i['properties']['SCODE']
        
        self.station_combo.clear()
        for k, v in self.places_dict.items():
            self.station_combo.addItem(k, v)
        
        # per i sensorsi
        url_sensors = 'http://dati.retecivica.bz.it/services/meteo/v1/sensors'
        sendata = requests.get(url_sensors).text
        sendata = json.loads(sendata)

        self.sensors_dict = defaultdict(list)
        for i in sendata:
            self.sensors_dict[i['SCODE']].append(i['TYPE'])


    def update_sensors(self):

        self.sensor_combo.clear()

        a = self.places_dict[self.station_combo.currentText()]
        self.sensor_combo.addItems(self.sensors_dict[a])
        

    def download_data(self):


        start_date = self.date_from.dateTime().toString('yyyyMMddhhmm')
        end_date = self.date_to.dateTime().toString('yyyyMMddhhmm')

        station_code = self.places_dict[self.station_combo.currentText()]
        sensor_code = self.sensor_combo.currentText()


        url = f'http://daten.buergernetz.bz.it/services/meteo/v1/timeseries?station_code={station_code}&output_format=CSV&sensor_code={sensor_code}&date_from={start_date}&date_to={end_date}'

        r = requests.get(url)

        out_file = 'meteo.csv'

        with open(out_file, 'wb') as f:
            f.write(r.content)
        




if __name__ == "__main__":

    app = QApplication(sys.argv)
    form = meteoGui()
    form.show()
    app.exec_()
