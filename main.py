from Code import DataSetCreation as DataSet
from Code import ProcessingAndEmbedding as processData
from Code import TrainModel
from Code import RecognizeAndStoreFaces as rsf


def main():
    DataSet()
    processData()
    TrainModel()
    rsf()


if __name__ == '__main__':
    main()