
from obspy import read
from aaa_features.features import FeatureVector

data_mseed=read("./data_sample/EC.RETU..SHZ.2012.06.28.185423.mseed")
data = data_mseed[0].data
# Change if you want your screen to keep quiet
# 0 = quiet
# 1 = in between
# 2 = detailed information
verbatim = 2

config = {'features_file':'./config_sample/features_00.json', 'domains':'time spectral cepstral'}

# Feature extraction for each data
features = FeatureVector(config, verbatim=verbatim)

features.compute(data,100)
for i,f in enumerate(features.featuresValues):
    print(i,f)
            
            
