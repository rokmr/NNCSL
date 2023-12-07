import yaml
import pprint
import logging
logging.basicConfig()
logger = logging.getLogger()
fname ="configs/nncsl/cifar10/cifar10_0.8%_buffer500_nncsl.yaml"
with open(fname, 'r') as y_file:
        params = yaml.load(y_file, Loader=yaml.FullLoader)
        logger.info('loaded params...')
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(params)