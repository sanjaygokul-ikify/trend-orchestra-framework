import argparse
from services.orchestrator import Orchestrator
from packages.core.engine import Engine
from packages.utils.logging import configure_logging

parser = argparse.ArgumentParser(description='Orchestra Framework CLI')
parser.add_argument('--log-file', help='Log file path', default='orchestra.log')
args = parser.parse_args()

configure_logging(args.log_file)

engine = Engine(logger=logging.getLogger(__name__))
orchestrator = Orchestrator(engine)

orchestrator.start()
