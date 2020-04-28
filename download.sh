# Download GloVe
wget http://nlp.stanford.edu/data/glove.840B.300d.zip -O data/glove.840B.300d.zip
unzip data/glove.840B.300d.zip -d data
rm data/glove.840B.300d.zip

# Download CoVe
wget https://s3.amazonaws.com/research.metamind.io/cove/wmtlstm-b142a7f2.pth -O resource/MT-LSTM.pt

# Download ELMo
wget https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway_5.5B/elmo_2x4096_512_2048cnn_2xhighway_5.5B_weights.hdf5 -O data/elmo_2x4096_512_2048cnn_2xhighway_5.5B_weights.hdf5
wget https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway_5.5B/elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json -O data/elmo_2x4096_512_2048cnn_2xhighway_5.5B_options.json
