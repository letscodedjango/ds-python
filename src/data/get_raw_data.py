# To write the code from jupyter notebook to python file

import os
import kaggle
from dotenv import find_dotenv, load_dotenv
import sys
import logging


def extract_data(folder, filename=None, type=None):
    logger = logging.getLogger(__name__)
    logger.info("Getting raw data...")
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    dotenv_file = find_dotenv()
    load_dotenv(dotenv_file)
    os.environ['KAGGLE_USERNAME']=os.environ.get('KAGGLE_USERNAME')
    os.environ['KAGGLE_KEY']=os.environ.get('KAGGLE_KEY')
    print(os.environ.get('KAGGLE_USERNAME') + ' ' + os.environ.get('KAGGLE_KEY'))
    raw_dir = os.path.join(os.pardir, 'data', 'raw')
    command = "kaggle competitions download -c"
    print(command)
    if type=='file':
        logger.info("Downloading the dataset from kaggle ...")
        os.system(command + ' ' +folder+ ' -f ' + filename +' -p ' + raw_dir)   
    else:
        logger.info("Downloading the dataset from kaggle ...")
        os.system(command + ' '+folder +' -p ' + raw_dir)
        
if __name__ == '__main__':
    extract_data('titanic', 'train.csv', type='file')
    extract_data('titanic', 'test.csv', type='file')
    extract_data('titanic')
