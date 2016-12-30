class AnalysisWave:
    def __init__(self):
        self.storge = {}

    def analysis(self, serial_num, brain_wave):
        self.storge[serial_num] = brain_wave

    def get_wave(self, serial_num, index):
        brain_wave = self.storge[serial_num]

        wave_list = []
        for _, data in brain_wave.items():
            for _, wave in data.items():
                wave_list.append(float(wave[index]))

        return wave_list

    def get_times(self, serial_num):
        brain_wave = self.storge[serial_num]
        time = len(brain_wave['raw_data'].keys()) + 1
        return [t for t in range(1, time)]